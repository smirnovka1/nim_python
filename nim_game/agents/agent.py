from random import choice, randint

from nim_game.common.enumerations import AgentLevels
from nim_game.common.models import NimStateChange


class Agent:
    """
    В этом классе реализованы стратегии игры для уровней сложности
    """

    _level: AgentLevels         # уровень сложности

    def __init__(self, level: str) -> None:
        level = AgentLevels(level)
        self._level = level

    def easy(self, state_curr: list[int]):
        heap_id = choice([
            i for i in range(len(state_curr)) if state_curr[i] != 0
        ])
        decrease = randint(1, state_curr[heap_id])
        return NimStateChange(heap_id, decrease)

    def dificult(self, state_curr: list[int]):
        nim_sum = 0

        for rocks_count in state_curr:
            nim_sum ^= rocks_count

        if nim_sum == 0:
            return self.easy(self, state_curr)

        else:
            for heap_id in range(len(state_curr)):
                if state_curr[heap_id] != 0:
                    for decrease in range(1, state_curr[heap_id] + 1):
                        if (nim_sum ^ decrease == 0):
                            return NimStateChange(heap_id, decrease)

            return NimStateChange(heap_id, decrease)

    def make_step(self, state_curr: list[int]) -> NimStateChange:
        """
        Сделать шаг, соотвутствующий уровню сложности

        :param state_curr: список целых чисел - состояние кучек
        :return: стуктуру NimStateChange - описание хода
        """
        if self._level == AgentLevels.EASY:
            return self.easy(state_curr)

        if self._level == AgentLevels.HARD:
            return self.dificult(state_curr)

        if self._level == AgentLevels.NORMAL:
            return choice([self.easy(state_curr), self.dificult(state_curr)])
