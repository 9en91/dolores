from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List

from dolores.exceptions import ContentException
from enum import Enum
from collections import namedtuple

class VkContent(Enum):

    text = "text"
    photo = "photo"
    audio = "audio"
    video = "video"
    doc = "doc"
    wall = "wall"





