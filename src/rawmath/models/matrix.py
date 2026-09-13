from __future__ import annotations
from operator import mul, truediv
from typing import Never, Literal

from ..types.functions import OrderedPair
from ..types.matrix import MatrixData
from ..types.number import Number

OPERATIONS = {
    'mul': mul,
    'truediv': truediv
}


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
        self, key: tuple[int, int], value: Number
    ) -> None:
        i, j = key

        if not isinstance(value, (int, float)):
            raise TypeError('matrix elements must be numeric')

        self._matrix[i][j] = value

    def __getitem__(self, key: int) -> list[Number]:
        return self._matrix[key]

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Matrix):
            return NotImplemented

        return self._matrix == value._matrix

    def __ne__(self, value: object) -> bool:
        if not isinstance(value, Matrix):
            return NotImplemented

        return self._matrix != value._matrix

    def __neg__(self) -> Matrix:
        result = [
            [-element for element in row] for row in self._matrix
        ]

        return Matrix(result)

    def __abs__(self) -> Number:
        return max(
            max(abs(element) for element in row)
            for row in self._matrix
        )

    def __add__(self, other: Matrix) -> Matrix:
        if not isinstance(other, Matrix):
            raise TypeError('matrix operand must be a Matrix')

        if self.m != other.m or self.n != other.n:
            raise ValueError('matrices must have the same dimensions')

        result = [
            [x + y for x, y in zip(row_a, row_b)]
            for row_a, row_b in zip(self._matrix, other._matrix)
        ]

        return Matrix(result)

    def __sub__(self, other: Matrix) -> Matrix:
        return self + (-other)

    def __mul__(self, other: Number) -> Matrix:
        result = self._calculate_scaling(other, _type='mul')

        return result

    def __rmul__(self, other: Number) -> Matrix:
        return self*other

    def __truediv__(self, other: Number) -> Matrix:
        result = self._calculate_scaling(other, _type='truediv')

        return result

    def __rtruediv__(self, other: Number) -> Never:
        raise TypeError('division of a scalar by a Matrix is not defined')

    def _ignite(self, data: MatrixData | OrderedPair) -> None:
        if isinstance(data, tuple):
            self.m, self.n = data

            if not isinstance(self.m, int) or not isinstance(self.n, int):
                raise TypeError('matrix dimensions must be integers')

            if self.m < 1 or self.n < 1:
                raise ValueError('matrix dimensions must be positive')

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

        self._matrix = [
            [element for element in row] for row in data
        ]
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

        visible_rows: list[list[Number | str]] = []
        for row in rows:
            visible_row: list[Number | str]

            if summarize:
                visible_row = [
                    *row[:self.edgeitems],
                    '...',
                    *row[-self.edgeitems:]
                ]
            else:
                visible_row = [element for element in row]

            visible_rows.append(visible_row)

        widths = [0]*len(visible_rows[0])
        for visible_row in visible_rows:
            for column, value in enumerate(visible_row):
                value_width = len(str(value))

                if value_width > widths[column]:
                    widths[column] = value_width

        formatted_rows = []
        for index, visible_row in enumerate(visible_rows):
            formatted_values = []

            for column, value in enumerate(visible_row):
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

    def _calculate_scaling(
        self, other: Number, /, _type: Literal['mul', 'truediv']
    ) -> Matrix:
        if not isinstance(other, (int, float)):
            raise TypeError('matrix scalar must be an int or float')

        result = [
            [OPERATIONS[_type](element, other) for element in row]
            for row in self._matrix
        ]

        return Matrix(result)

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
    def main_diagonal(self) -> list[Number] | None:
        result = None

        order = self.order
        if self.is_square and order is not None:
            result = [
                self._matrix[n][n] for n in range(order)
            ]

        return result

    @property
    def anti_diagonal(self) -> list[Number] | None:
        result = None

        order = self.order
        if self.is_square and order is not None:
            result = [
                self._matrix[order - n][n - 1]
                for n in range(order, 0, -1)
            ]

        return result

    @property
    def secondary_diagonal(self) -> list[Number] | None:
        return self.anti_diagonal

    @property
    def counter_diagonal(self) -> list[Number] | None:
        return self.anti_diagonal

    @property
    def reverse_diagonal(self) -> list[Number] | None:
        return self.anti_diagonal

    @property
    def is_diagonal(self) -> bool:
        if not self.is_square:
            return False

        return all(
            element == 0
            for i, row in enumerate(self._matrix)
            for j, element in enumerate(row)
            if i != j
        )

    @property
    def is_identity(self) -> bool:
        result = False

        if self.is_square and self.is_diagonal:
            main_diagonal, order, _count = (
                self.main_diagonal, self.order, 0
            )

            if main_diagonal is None or order is None:
                return result

            for element in main_diagonal:
                if element == 1:
                    _count += 1

            result = _count == order

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
        return all(
            element == 0
            for row in self._matrix
            for element in row
        )

    def is_opposite(self, target: Matrix) -> bool:
        return (self + target).is_null
