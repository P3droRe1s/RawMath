# RawMath

A from-scratch mathematics library for Python.

RawMath implements mathematical structures and operations directly from their
definitions, with a focus on clarity, independence, and understanding the
mathematics behind the implementation.

> **Status:** RawMath is currently in pre-alpha development. The API may change
> between versions.

## Installation

Install RawMath from PyPI:

```bash
pip install rawmath
```

For local development:

```bash
git clone https://github.com/P3droRe1s/RawMath.git
cd RawMath
python -m pip install -e .
```

## Requirements

- Python 3.10+

## Quick Start

```python
from rawmath import Matrix

A = Matrix([
    [1, 2],
    [3, 4],
])

B = Matrix([
    [5, 6],
    [7, 8],
])

print(A + B)
```

Output:

```text
Matrix([  6   8 ]
       [ 10  12 ])
```

## Matrix

RawMath currently provides the `Matrix` class for working with matrices
directly from their mathematical definitions.

```python
from rawmath import Matrix

A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
])

print(A.shape)
print(A.elements)
```

```text
(2, 3)
6
```

A null matrix can also be created directly from its dimensions:

```python
A = Matrix((2, 3))

print(A)
```

```text
Matrix([ 0.0  0.0  0.0 ]
       [ 0.0  0.0  0.0 ])
```

### Matrix properties

RawMath currently supports properties including:

- shape and number of elements;
- square matrices and order;
- row and column matrices;
- null matrices;
- diagonal matrices;
- identity matrices;
- main and anti-diagonals.

Example:

```python
A = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])

print(A.is_square)
print(A.is_diagonal)
print(A.is_identity)
print(A.main_diagonal)
```

```text
True
True
True
[1, 1, 1]
```

### Matrix operations

RawMath currently supports matrix equality, opposite matrices, addition and
subtraction.

```python
A = Matrix([
    [1, 2],
    [3, 4],
])

B = Matrix([
    [5, 6],
    [7, 8],
])

print(A + B)
print(A - B)
print(-A)
```

## Documentation

More detailed documentation is available in
[`docs/matrices.md`](docs/matrices.md).

## Development

Clone the repository:

```bash
git clone https://github.com/P3droRe1s/RawMath.git
cd RawMath
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install RawMath in editable mode:

```bash
python -m pip install -e .
```

Install pytest and run the test suite:

```bash
python -m pip install pytest
pytest
```

## Project Status

RawMath is currently in **pre-alpha** development.

The project is being expanded alongside the study and implementation of
mathematical concepts. Features and public APIs may change between versions.

Current release:

```text
0.1.0
```

## Links

- PyPI: https://pypi.org/project/rawmath/
- GitHub: https://github.com/P3droRe1s/RawMath

## License

RawMath is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.
