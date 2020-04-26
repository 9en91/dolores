import logging
import threading
import time

import requests
import six
from vk_api import ApiHttpError, ApiError, Captcha, CAPTCHA_ERROR_CODE, NEED_VALIDATION_CODE, TOO_MANY_RPS_CODE, \
    TWOFACTOR_CODE



class VkApi(object):


    RPS_DELAY = 0.34  # ~3 requests per second

    def __init__(self, token=None,
                 api_version='5.92', app_id=6222115,
                 client_secret=None, session=None):


        self.token = {'access_token': token}

        self.api_version = api_version
        self.app_id = app_id

        self.client_secret = client_secret


        self.http = requests.Session()

        self.http.headers.update({
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0'
        })

        self.last_request = 0.0

        self.error_handlers = {
            NEED_VALIDATION_CODE: self.need_validation_handler,
            CAPTCHA_ERROR_CODE: captcha_handler or self.captcha_handler,
            TOO_MANY_RPS_CODE: self.too_many_rps_handler,
            TWOFACTOR_CODE: auth_handler or self.auth_handler
        }

        self.lock = threading.Lock()

        self.logger = logging.getLogger('vk_api')



    def get_api(self):
        return VkApiMethod(self)

    def http_handler(self, error: Exception):
        pass

    def method(self,
               method,
               values=None,
               captcha_sid=None,
               captcha_key=None,
               raw=False):

        values = values.copy() if values else {}

        if 'v' not in values:
            values['v'] = self.api_version

        if self.token:
            values['access_token'] = self.token['access_token']

        if captcha_sid and captcha_key:
            values['captcha_sid'] = captcha_sid
            values['captcha_key'] = captcha_key

        with self.lock:
            # Ограничение 3 запроса в секунду
            delay = self.RPS_DELAY - (time.time() - self.last_request)

            if delay > 0:
                time.sleep(delay)

            response = self.http.post('https://api.vk.com/method/' + method,
                                      values)
            self.last_request = time.time()

        if response.ok:
            response = response.json()
        else:
            error = ApiHttpError(self, method, values, raw, response)
            response = self.http_handler(error)
            if response is not None:
                return response

            raise error

        if 'error' in response:
            error = ApiError(self, method, values, raw, response['error'])

            if error.code in self.error_handlers:
                if error.code == CAPTCHA_ERROR_CODE:
                    error = Captcha(
                        self,
                        error.error['captcha_sid'],
                        self.method,
                        (method,),
                        {'values': values, 'raw': raw},
                        error.error['captcha_img']
                    )

                response = self.error_handlers[error.code](error)

                if response is not None:
                    return response

            raise error

        return response if raw else response['response']


class VkApiMethod(object):

    __slots__ = ('_vk', '_method')

    def __init__(self, vk, method=None):
        self._vk = vk
        self._method = method

    def __getattr__(self, method):
        if '_' in method:
            m = method.split('_')
            method = m[0] + ''.join(i.title() for i in m[1:])

        return VkApiMethod(
            self._vk,
            (self._method + '.' if self._method else '') + method
        )

    def __call__(self, **kwargs):
        for k, v in six.iteritems(kwargs):
            if isinstance(v, (list, tuple)):
                kwargs[k] = ','.join(str(x) for x in v)

        return self._vk.method(self._method, kwargs)