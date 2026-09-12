from __future__ import annotations
from typing import Any

from ..types.functions import OrderedPair
from ..types.matrix import MatrixData


class Matrix:
    def __init__(
        self,
        data: MatrixData | OrderedPair,
        edgeitems: int = 3,
        threshold: int = 1000
    ) -> None:
        self.edgeitems = edgeitems
        self.threshold = threshold

        self._ignite(data=data)
        self._class_name = type(self).__name__

    def __str__(self) -> str:
        return self._format_matrix()

    def __repr__(self) -> str:
        return self._format_matrix(debug=True)

    def __setitem__(
        self, key: tuple[int, int], value: Any
    ) -> None:
        i, j = key

        self._matrix[i][j] = value

    def __getitem__(self, key: int) -> list[Any]:
        return self._matrix[key]

    def __eq__(self, value: Matrix) -> bool:
        return self._matrix == value._matrix

    def __ne__(self, value: Matrix) -> bool:
        return self._matrix != value._matrix

    def __neg__(self) -> Matrix:
        result = [
            [-element for element in row] for row in self._matrix
        ]

        return Matrix(result)

    def __add__(self, other: Matrix) -> Matrix:
        if self.m != other.m or self.n != other.n:
            raise ValueError('matrices must have the same dimensions')

        result = [
            [x + y for x, y in zip(row_a, row_b)]
            for row_a, row_b in zip(self._matrix, other._matrix)
        ]

        return Matrix(result)

    def __sub__(self, other: Matrix) -> Matrix:
        return self + (-other)

    def _ignite(self, data: MatrixData | OrderedPair) -> None:
        if isinstance(data, tuple):
            self.m, self.n = data

            self._matrix = [
                [0.0 for _ in range(self.n)]
                for _ in range(self.m)
            ]

            return

        rows_length = []
        for row in data:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError('matrix elements must be numeric')

            rows_length.append(len(row))

        if len(set(rows_length)) > 1:
            raise ValueError('all matrix rows must have the same length')

        if len(rows_length) == 0 or rows_length[0] == 0:
            raise ValueError('matrix data cannot be empty')

        self._matrix = data
        self.m = len(self._matrix)
        self.n = rows_length[0]

    def _format_matrix(self, debug: bool = False) -> str:
        name = self._class_name
        padding = '\n' + ' '*(len(name) + 1)

        summarize = self.elements >= self.threshold
        rows = self._matrix

        if summarize:
            rows = (
                rows[:self.edgeitems] + rows[-self.edgeitems:]
            )

        visible_rows = []
        for row in rows:
            if summarize:
                row = (
                    row[:self.edgeitems] + ['...'] + row[-self.edgeitems:]
                )

            visible_rows.append(row)

        widths = [0]*len(visible_rows[0])
        for row in visible_rows:
            for column, value in enumerate(row):
                value_width = len(str(value))

                if value_width > widths[column]:
                    widths[column] = value_width

        formatted_rows = []
        for index, row in enumerate(visible_rows):
            formatted_values = []

            for column, value in enumerate(row):
                formatted_values.append(
                    f'{value:>{widths[column]}}'
                )

            clean_row = '  '.join(formatted_values)
            clean_row = '[ ' + clean_row + ' ]'

            formatted_rows.append(clean_row)

            if summarize and index == self.edgeitems - 1:
                formatted_rows.append('...'.center(len(clean_row)))

        final_str = padding.join(formatted_rows)
        shape = f', shape={self.shape}' if debug else ''

        return f'{name}({final_str}{shape})'

    @property
    def shape(self) -> OrderedPair:
        return self.m, self.n

    @property
    def elements(self) -> int:
        return self.m*self.n

    @property
    def is_square(self) -> bool:
        return self.shape[0] == self.shape[1]

    @property
    def order(self) -> int | None:
        return self.shape[0] if self.is_square else None

    @property
    def main_diagonal(self) -> list[Any] | None:
        result = None

        if self.is_square:
            result = [
                self._matrix[n][n] for n in range(self.order)
            ]

        return result

    @property
    def anti_diagonal(self) -> list[Any] | None:
        result = None

        if self.is_square:
            order = self.order

            result = [
                self._matrix[order - n][n - 1]
                for n in range(order, 0, -1)
            ]

        return result

    @property
    def secondary_diagonal(self) -> list[Any] | None:
        return self.anti_diagonal

    @property
    def counter_diagonal(self) -> list[Any] | None:
        return self.anti_diagonal

    @property
    def reverse_diagonal(self) -> list[Any] | None:
        return self.anti_diagonal

    @property
    def is_diagonal(self) -> bool:
        result = False

        if self.is_square:
            _sum = 0

            for i_index, row in enumerate(self._matrix):
                for j_index, element in enumerate(row):
                    if i_index != j_index:
                        _sum += abs(element)

            result = not bool(_sum)

        return result

    @property
    def is_identity(self) -> bool:
        result = False

        if self.is_square and self.is_diagonal:
            _count = 0

            for element in self.main_diagonal:
                if element == 1:
                    _count += 1

            result = _count == self.order

        return result

    @property
    def is_unit(self) -> bool:
        return self.is_identity

    @property
    def is_row(self) -> bool:
        return self.shape[0] == 1

    @property
    def is_column(self) -> bool:
        return self.shape[1] == 1

    @property
    def is_null(self) -> bool:
        _sum = 0

        for row in self._matrix:
            for element in row:
                _sum += abs(element)

        return not bool(_sum)

    def is_opposite(self, target: Matrix) -> bool:
        return (self + target).is_null
