
# Changelog

All notable changes to AIMS-mini will be documented in this file.

This changelog follows the Keep a Changelog format and Semantic Versioning.

## [Unreleased]

### Added
- No unreleased changes yet.

## [1.0.1] - 2026-11-07

### Fixed
- Reject discount percentages outside the valid 0–100 range, including NaN.

## [1.0.0] - 2026-11-07

### Added
- `Cart.print_cart()` to display DVD titles, prices, and total cost.
- `search_by_title()` to search DVDs by title.
- `Cart.total_cost_with_discount()` to calculate discounted cart totals.
- Unit tests for cart capacity and discount calculation.

### Changed
- Updated DVD added confirmation messages to Vietnamese.
- Added application version information.

### Fixed
- Fixed the cart capacity bug that allowed the 21st DVD to be added (#6).
- Corrected the discount calculation formula.
- Added validation for discount percentages outside the range 0–100.
