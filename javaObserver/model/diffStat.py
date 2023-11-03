from typing import List
import json


class Position:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Code:
    def __init__(self, code: str, position: Position):
        self.position = position
        self.content = code

    @property
    def color(self):
        """
        :return: red, green, black
        """
        if self.content.startswith('-'):
            return 'red'
        elif self.content.startswith('+'):
            return 'green'
        else:
            return 'black'


class DiffStat:
    def __init__(self, filePath: str, codes: List[Code]):
        self.filePath = filePath
        self.codes = codes


if __name__ == '__main__':
    print({'a': Position(2, 3).__dict__})
