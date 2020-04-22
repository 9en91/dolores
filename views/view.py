from core.base import bot
from core.view import View
from utils.state import State


@bot.view(state=State.START)
class First(View):

    @bot.message(regex="Начать")
    def func(self, event):

        self.api.send_message(self.user.id, "Начать")

    @bot.message(regex="Назад")
    def func(self, event):
        self.api.send_message(self.user.id, "Назад")

