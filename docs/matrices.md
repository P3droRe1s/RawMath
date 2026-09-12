# Matrices

The `Matrix` class represents a rectangular arrangement of numeric elements
organized into rows and columns.

A matrix with `m` rows and `n` columns has shape `(m, n)`.

## Creating a Matrix

A matrix can be created by providing its elements as nested lists:

```python
from rawmath import Matrix

A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
])
```

In this example, `A` has 2 rows and 3 columns, therefore its shape is `(2, 3)`.

A null matrix can also be created by providing its dimensions as an ordered
pair:

```python
A = Matrix((2, 3))
```

This creates:

```text
Matrix([ 0.0  0.0  0.0 ]
       [ 0.0  0.0  0.0 ])
```

Matrix elements must be numeric, and all rows must have the same number of
elements.

## Shape

The `shape` property returns the dimensions of the matrix as the ordered pair
`(m, n)`, where `m` is the number of rows and `n` is the number of columns.

```python
A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
])

A.shape
# (2, 3)
```

## Number of Elements

The `elements` property returns the total number of elements in the matrix.

For a matrix of shape `(m, n)`, the number of elements is:

```text
m*n
```

Example:

```python
A.elements
# 6
```

## Square Matrices

A matrix is square when it has the same number of rows and columns.

The `is_square` property checks this condition:

```python
A = Matrix([
    [1, 2],
    [3, 4],
])

A.is_square
# True
```

For a square matrix, `order` returns its order:

```python
A.order
# 2
```

For a non-square matrix, `order` returns `None`.

## Row Matrices

A row matrix contains exactly one row.

```python
A = Matrix([
    [1, 2, 3],
])

A.is_row
# True
```

The `is_row` property returns whether a matrix is a row matrix.

## Column Matrices

A column matrix contains exactly one column.

```python
A = Matrix([
    [1],
    [2],
    [3],
])

A.is_column
# True
```

The `is_column` property returns whether a matrix is a column matrix.

A `1 x 1` matrix is both a row matrix and a column matrix.

## Null Matrices

A null matrix is a matrix whose elements are all zero.

```python
A = Matrix([
    [0, 0],
    [0, 0],
])

A.is_null
# True
```

## Diagonals

### Main Diagonal

For a square matrix, the main diagonal contains the elements whose row and
column indices are equal.

```python
A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

A.main_diagonal
# [1, 5, 9]
```

For a non-square matrix, `main_diagonal` returns `None`.

### Anti-Diagonal

The anti-diagonal runs from the upper-right element to the lower-left element.

```python
A.anti_diagonal
# [3, 5, 7]
```

The following properties are aliases for `anti_diagonal`:

```python
A.secondary_diagonal
A.counter_diagonal
A.reverse_diagonal
```

For a non-square matrix, these properties return `None`.

## Diagonal Matrices

A diagonal matrix is a square matrix whose elements outside the main diagonal
are all zero.

```python
A = Matrix([
    [2, 0, 0],
    [0, 5, 0],
    [0, 0, 8],
])

A.is_diagonal
# True
```

The elements on the main diagonal do not need to be equal.

## Identity Matrices

An identity matrix is a diagonal matrix whose elements on the main diagonal
are all equal to `1`.

```python
I = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])

I.is_identity
# True
```

`is_unit` is an alias for `is_identity`:

```python
I.is_unit
# True
```

## Equality

Two matrices are equal when their elements are equal.

```python
A = Matrix([
    [1, 2],
    [3, 4],
])

B = Matrix([
    [1, 2],
    [3, 4],
])

A == B
# True

A != B
# False
```

## Opposite Matrix

The opposite of a matrix `A`, written `-A`, is obtained by replacing every
element with its additive inverse.

```python
A = Matrix([
    [1, -2],
    [3, 4],
])

-A
```

produces:

```text
Matrix([ -1   2 ]
       [ -3  -4 ])
```

Two matrices are opposite when their sum is a null matrix.

```python
B = -A

A.is_opposite(B)
# True
```

## Addition

Matrices can be added only when they have the same dimensions.

If:

```text
A = (a_ij)
B = (b_ij)
```

then:

```text
A + B = (a_ij + b_ij)
```

In RawMath:

```python
A = Matrix([
    [1, 2],
    [3, 4],
])

B = Matrix([
    [5, 6],
    [7, 8],
])

A + B
```

produces:

```text
Matrix([  6   8 ]
       [ 10  12 ])
```

Attempting to add matrices with different dimensions raises a `ValueError`.

## Subtraction

Matrix subtraction is defined using the opposite matrix:

```text
A - B = A + (-B)
```

Example:

```python
A = Matrix([
    [10, -4, 7],
    [3, 8, -2],
])

B = Matrix([
    [6, 2, -3],
    [-5, 1, 4],
])

A - B
```

produces:

```text
Matrix([ 4  -6  10 ]
       [ 8   7  -6 ])
```

## Accessing Elements

A row can be accessed using its index:

```python
A[0]
```

Python indices start at `0`.

Matrix elements can currently be assigned using a pair of indices:

```python
A[0, 1] = 5
```

## Errors

RawMath rejects invalid matrix data.

A `TypeError` is raised when a matrix contains a non-numeric element.

A `ValueError` is raised when:

- matrix rows have different lengths;
- matrix data is empty;
- matrices with different dimensions are added or subtracted.

## Development Status

Matrix support is currently under active development. Additional operations
and properties will be introduced as RawMath evolves.