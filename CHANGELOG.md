# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] — 2026-08-23

### Added
- **Camera2D** — a new system for following the player or any target object.
  - Supports hard follow mode.
  - Works with `world.draw_layer()` and `sprite.draw()` when the camera is passed as an argument.
- **Animation system** — a lightweight frame-based animation system.
  - `get_frame()` method in `Sprite` handles frame switching with delta time and custom delay.
- **Vector2** — an optional class for vector math.
  - Includes addition, subtraction, multiplication, division, length, normalisation, and distance.
  - Not required for basic use; users can choose to adopt it.
- **Documentation** — updated `README.md` and `DOCS.md` with examples for new features.

### Changed
- **Project structure** — moved to a more modular architecture.
- **Tests** — updated `test.py` to demonstrate all new features.

### Fixed
- Collision handling now works correctly when moving separately along the X and Y axes.
- Animation frame switching no longer depends on FPS.

---

## [0.1.0] — 2026-08-19

### Added
- Initial release.
- `Keyboard` input handler.
- `Sprite` class with creation, movement, and drawing.
- `World` class with JSON map loading and tile rendering.
- `Transform` class for scaling and rotation.
- `Collision` system with `can_move_to()`.
- PyPI and GitHub publication.
- Basic documentation.