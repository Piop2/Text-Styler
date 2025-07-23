from __future__ import annotations

from typing import Self
from enum import IntEnum


class _Color(IntEnum):
    BLACK = 30
    RED = 31
    GREEN = 32
    # YELLOW = 33
    # BLUE = 34
    # MAGENTA = 35
    # CYAN = 36
    # WHITE = 37

class _Style(IntEnum):
    NONE = 0
    BOLD = 1
    DIM = 2
    # ITALIC = 3
    # UNDERLINE = 4
    # BLINK = 5
    # REVERSE = 7
    # STRIKETHROUGH = 9


class __Styler:
    def __init__(self) -> None:
        self.__color_code: _Color = _Color.BLACK
        self.__style: _Style = _Style.NONE
        return

    def __call__(self, text: str) -> str:
        styled_text: str = (
            f"\033[{self.__style};{self.__color_code}m"
            f"{text}"
            f"\033[0m"
        )

        # reset
        self.__color_code = _Color.BLACK
        self.__style = _Style.NONE

        return styled_text

    @property
    def bold(self) -> Self:
        self.__style = _Style.BOLD
        return self

    @property
    def dim(self) -> Self:
        self.__style = _Style.DIM
        return self

    @property
    def red(self) -> Self:
        self.__color_code = _Color.RED
        return self

    @property
    def green(self) -> Self:
        self.__color_code = _Color.GREEN
        return self


STYLER = __Styler()
