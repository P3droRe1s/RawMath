# RawMath

A from-scratch mathematics library for Python.

RawMath implements mathematical structures and operations directly from their
definitions, with a focus on clarity, independence, and understanding the
mathematics behind the implementation.

## Requirements

- Python 3.10+

## Installation

RawMath is currently under development.

For local development:

    python -m pip install -e .

## Quick Start

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

## Status

RawMath is currently in pre-alpha development. The API may change between
versions.

## License

RawMath is licensed under the MIT License.