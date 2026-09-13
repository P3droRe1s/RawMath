# Changelog

All notable changes to RawMath will be documented in this file.

## [0.2.0] - 2026-09-13

### Added

- Added scalar multiplication with `A * n` and `n * A`.
- Added scalar division with `A / n`.
- Added the maximum-entry matrix norm with `abs(A)`.
- Added support for calculating matrix distance naturally with `abs(A - B)`.
- Defined `from rawmath import Matrix` as the intended public API.

### Validation & Safety

- `__setitem__` now only accepts numeric values.
- Matrix dimensions provided through `Matrix((m, n))` are now validated.
- Matrix dimensions must be positive integers.
- Zero and negative dimensions are rejected.
- Scalar operations now validate their operands.
- Scalar-by-matrix division is explicitly rejected.
- Matrix addition and subtraction now validate operand types.
- `__eq__` and `__ne__` now behave correctly with non-`Matrix` objects.
- Matrix input data is copied instead of sharing mutable row references with the original input.

### Internals & Typing

- Added the `Number` type and removed unnecessary uses of `Any`.
- Improved type narrowing for `order` and diagonal properties.
- Refactored `is_diagonal` and `is_null` using `all()`.
- Improved internal matrix formatting types for static type checking.

### Tests

- Expanded test coverage for matrix construction and validation.
- Added tests for scalar multiplication and division.
- Added tests for the maximum-entry norm.
- Added tests for matrix distance.
- Added tests for invalid operands and scalar operations.
- Added tests for comparisons with non-`Matrix` objects.
- Added tests to ensure matrix input data is copied independently.
