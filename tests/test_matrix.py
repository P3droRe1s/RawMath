import pytest

from rawmath import Matrix


def test_create_matrix_shape() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert matrix.shape == (2, 2)


def test_create_matrix_elements() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert matrix.elements == 4


def test_create_null_matrix_from_dimensions_shape() -> None:
    matrix = Matrix((2, 3))

    assert matrix.shape == (2, 3)


def test_create_null_matrix_from_dimensions_is_null() -> None:
    matrix = Matrix((2, 3))

    assert matrix.is_null


def test_reject_non_numeric_element() -> None:
    with pytest.raises(TypeError):
        Matrix([
            [1, 2],
            [3, 'hello'],
        ])


def test_reject_irregular_rows() -> None:
    with pytest.raises(ValueError):
        Matrix([
            [1, 2],
            [3],
        ])


def test_reject_empty_matrix() -> None:
    with pytest.raises(ValueError):
        Matrix([])


def test_reject_single_empty_row() -> None:
    with pytest.raises(ValueError):
        Matrix([
            [],
        ])


def test_reject_multiple_empty_rows() -> None:
    with pytest.raises(ValueError):
        Matrix([
            [],
            [],
        ])


def test_shape_rectangular_matrix() -> None:
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    assert matrix.shape == (2, 3)


def test_elements_rectangular_matrix() -> None:
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    assert matrix.elements == 6


def test_square_matrix() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert matrix.is_square


def test_non_square_matrix() -> None:
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    assert not matrix.is_square


def test_square_matrix_order() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert matrix.order == 2


def test_non_square_matrix_order() -> None:
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    assert matrix.order is None


def test_row_matrix() -> None:
    matrix = Matrix([
        [1, 2, 3],
    ])

    assert matrix.is_row


def test_non_row_matrix() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert not matrix.is_row


def test_column_matrix() -> None:
    matrix = Matrix([
        [1],
        [2],
        [3],
    ])

    assert matrix.is_column


def test_non_column_matrix() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert not matrix.is_column


def test_one_by_one_is_row() -> None:
    matrix = Matrix([
        [7],
    ])

    assert matrix.is_row


def test_one_by_one_is_column() -> None:
    matrix = Matrix([
        [7],
    ])

    assert matrix.is_column


def test_one_by_one_is_square() -> None:
    matrix = Matrix([
        [7],
    ])

    assert matrix.is_square


def test_one_by_one_order() -> None:
    matrix = Matrix([
        [7],
    ])

    assert matrix.order == 1


def test_main_diagonal() -> None:
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    assert matrix.main_diagonal == [1, 5, 9]


def test_main_diagonal_one_by_one() -> None:
    matrix = Matrix([
        [7],
    ])

    assert matrix.main_diagonal == [7]


def test_main_diagonal_non_square() -> None:
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    assert matrix.main_diagonal is None


def test_anti_diagonal() -> None:
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    assert matrix.anti_diagonal == [3, 5, 7]


def test_anti_diagonal_one_by_one() -> None:
    matrix = Matrix([
        [7],
    ])

    assert matrix.anti_diagonal == [7]


def test_anti_diagonal_non_square() -> None:
    matrix = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    assert matrix.anti_diagonal is None


def test_secondary_diagonal_alias() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert matrix.secondary_diagonal == matrix.anti_diagonal


def test_counter_diagonal_alias() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert matrix.counter_diagonal == matrix.anti_diagonal


def test_reverse_diagonal_alias() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert matrix.reverse_diagonal == matrix.anti_diagonal


def test_diagonal_matrix() -> None:
    matrix = Matrix([
        [2, 0, 0],
        [0, 5, 0],
        [0, 0, -3],
    ])

    assert matrix.is_diagonal


def test_zero_diagonal_matrix() -> None:
    matrix = Matrix([
        [0, 0],
        [0, 0],
    ])

    assert matrix.is_diagonal


def test_non_diagonal_matrix() -> None:
    matrix = Matrix([
        [1, 2],
        [0, 1],
    ])

    assert not matrix.is_diagonal


def test_non_square_is_not_diagonal() -> None:
    matrix = Matrix([
        [1, 0, 0],
        [0, 1, 0],
    ])

    assert not matrix.is_diagonal


def test_identity_matrix() -> None:
    matrix = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ])

    assert matrix.is_identity


def test_non_identity_diagonal_matrix() -> None:
    matrix = Matrix([
        [2, 0],
        [0, 2],
    ])

    assert not matrix.is_identity


def test_non_diagonal_is_not_identity() -> None:
    matrix = Matrix([
        [1, 1],
        [0, 1],
    ])

    assert not matrix.is_identity


def test_non_square_is_not_identity() -> None:
    matrix = Matrix([
        [1, 0, 0],
        [0, 1, 0],
    ])

    assert not matrix.is_identity


def test_one_by_one_identity() -> None:
    matrix = Matrix([
        [1],
    ])

    assert matrix.is_identity


def test_unit_alias() -> None:
    matrix = Matrix([
        [1, 0],
        [0, 1],
    ])

    assert matrix.is_unit


def test_null_matrix() -> None:
    matrix = Matrix([
        [0, 0],
        [0, 0],
    ])

    assert matrix.is_null


def test_non_null_matrix() -> None:
    matrix = Matrix([
        [0, 0],
        [0, 1],
    ])

    assert not matrix.is_null


def test_negative_matrix_is_not_null() -> None:
    matrix = Matrix([
        [0, -1],
        [0, 0],
    ])

    assert not matrix.is_null


def test_get_first_row() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert matrix[0] == [1, 2]


def test_get_second_row() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert matrix[1] == [3, 4]


def test_setitem() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    matrix[0, 1] = 10

    assert matrix[0][1] == 10


def test_setitem_negative_value() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    matrix[1, 0] = -20

    assert matrix[1][0] == -20


def test_setitem_float() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    matrix[0, 0] = 1.5

    assert matrix[0][0] == 1.5


def test_equal_matrices() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert a == b


def test_different_matrices_are_not_equal() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [1, 2],
        [3, 5],
    ])

    assert not (a == b)


def test_different_matrices() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [1, 2],
        [3, 5],
    ])

    assert a != b


def test_equal_matrices_are_not_different() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert not (a != b)


def test_negative_matrix() -> None:
    matrix = Matrix([
        [1, -2],
        [3, 4],
    ])

    assert -matrix == Matrix([
        [-1, 2],
        [-3, -4],
    ])


def test_double_negative_matrix() -> None:
    matrix = Matrix([
        [1, -2],
        [3, 4],
    ])

    assert -(-matrix) == matrix


def test_negative_null_matrix() -> None:
    matrix = Matrix([
        [0, 0],
        [0, 0],
    ])

    assert -matrix == matrix


def test_opposite_matrices() -> None:
    a = Matrix([
        [1, -2],
        [3, 4],
    ])

    b = Matrix([
        [-1, 2],
        [-3, -4],
    ])

    assert a.is_opposite(b)


def test_non_opposite_matrices() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [-1, -2],
        [-3, -5],
    ])

    assert not a.is_opposite(b)


def test_null_matrix_is_opposite_to_itself() -> None:
    matrix = Matrix([
        [0, 0],
        [0, 0],
    ])

    assert matrix.is_opposite(matrix)


def test_matrix_addition() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [5, 6],
        [7, 8],
    ])

    assert a + b == Matrix([
        [6, 8],
        [10, 12],
    ])


def test_matrix_addition_with_negative_values() -> None:
    a = Matrix([
        [-1, 2],
        [3, -4],
    ])

    b = Matrix([
        [5, -6],
        [-7, 8],
    ])

    assert a + b == Matrix([
        [4, -4],
        [-4, 4],
    ])


def test_matrix_addition_with_null_matrix() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    null = Matrix((2, 2))

    assert a + null == a


def test_matrix_addition_commutative() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [5, 6],
        [7, 8],
    ])

    assert a + b == b + a


def test_addition_different_row_count() -> None:
    a = Matrix([
        [1, 2],
    ])

    b = Matrix([
        [1, 2],
        [3, 4],
    ])

    with pytest.raises(ValueError):
        a + b


def test_addition_different_column_count() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    with pytest.raises(ValueError):
        a + b


def test_matrix_subtraction() -> None:
    a = Matrix([
        [10, -4, 7],
        [3, 8, -2],
    ])

    b = Matrix([
        [6, 2, -3],
        [-5, 1, 4],
    ])

    assert a - b == Matrix([
        [4, -6, 10],
        [8, 7, -6],
    ])


def test_matrix_subtraction_from_itself() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert (matrix - matrix).is_null


def test_matrix_subtraction_null_matrix() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    null = Matrix((2, 2))

    assert matrix - null == matrix


def test_subtraction_different_row_count() -> None:
    a = Matrix([
        [1, 2],
    ])

    b = Matrix([
        [1, 2],
        [3, 4],
    ])

    with pytest.raises(ValueError):
        a - b


def test_subtraction_different_column_count() -> None:
    a = Matrix([
        [1, 2],
        [3, 4],
    ])

    b = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    with pytest.raises(ValueError):
        a - b


def test_str_matrix() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert str(matrix) == (
        'Matrix([ 1  2 ]\n'
        '       [ 3  4 ])'
    )


def test_repr_contains_shape() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert 'shape=(2, 2)' in repr(matrix)


def test_str_does_not_contain_shape() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert 'shape=' not in str(matrix)


def test_large_matrix_is_summarized() -> None:
    matrix = Matrix(
        [[0 for _ in range(40)] for _ in range(40)]
    )

    assert '...' in str(matrix)


def test_small_matrix_is_not_summarized() -> None:
    matrix = Matrix([
        [1, 2],
        [3, 4],
    ])

    assert '...' not in str(matrix)
