# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- Documentation system (`docs/`) with architecture, quickstart, and data model guides
- `LICENSE` file (MIT)
- `CONTRIBUTING.md` contribution guide
- `CHANGELOG.md` this file

### Changed
- Removed Tencent AI chat integration (permanently deprecated)
- Moved all hardcoded secrets to environment variables
- Comments and replies now use separate RESTful API endpoints (`/api/comments/`, `/api/comments/<id>/replies/`)
- Comment deletion requires authentication and ownership verification
- Logout changed from GET to POST for CSRF safety
- JSON response structure unified to `{"success": bool, "error": str}`
- User profile private fields (email, birthday, signature) now visible only to the profile owner
- Image uploads validated server-side (type: JPG/PNG/GIF/WebP, max size: 2MB)
- Registration wrapped in database transaction to handle concurrent username conflicts
- Account deletion wrapped in database transaction
- Comment list queries optimized with `Prefetch` to eliminate N+1 issues

### Fixed
- Reply delete button now checks reply author instead of parent comment author
- Comment creation now uses `cleaned_data` instead of raw `request.POST`

## [0.1.0] - 2025-01-01

### Added
- Initial release
- Homepage with Swiper image carousel
- User registration and login system
- User profile with avatar upload
- Discussion area with comments and replies
- Comment moderation system
- FAQ page
- About page
- Docker Compose deployment setup
