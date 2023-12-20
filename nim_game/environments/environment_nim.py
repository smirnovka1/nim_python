from random import randint

from nim_game.common.models import NimStateChange


STONE_AMOUNT_MIN = 1        # минимальное начальное число камней в кучке
STONE_AMOUNT_MAX = 10       # максимальное начальное число камней в кучке


class EnvironmentNim:
    """
    Класс для хранения и взаимодействия с кучками
    """

    _heaps: list[int]       # кучки

    def __init__(self, heaps_amount: int) -> None:
        if not (2 <= heaps_amount <= 10):
            raise ValueError(
                "Количество кучек должно быть "
                "не меньше 2 и не больше 10"
            )

        self._heaps = [
            randint(STONE_AMOUNT_MIN, STONE_AMOUNT_MAX)
            for _ in range(heaps_amount)
        ]

    def get_state(self) -> list[int]:
        """
        Получение текущего состояния кучек
        :return: копия списка с кучек
        """
        heap_state = self._heaps[:]
        return heap_state

    def change_state(self, state_change: NimStateChange) -> None:
        """
        Изменения текущего состояния кучек

        :param state_change: структура описывающая изменение состояния
        """
        heap_id = state_change.heap_id
        decrease = state_change.decrease

        if not (1 <= heap_id <= len(self._heaps)):
            raise ValueError("Индекс кучки вне допустимого диапазона")

        if not (1 <= decrease <= self._heaps[heap_id - 1]):
            raise ValueError("Недопустимое изменение состояния кучки")

        self._heaps[heap_id - 1] -= decrease
