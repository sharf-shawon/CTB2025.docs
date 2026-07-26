## ADDED Requirements

### Requirement: Documentation build SHALL support automated browser screenshot capture

The system SHALL provide an automated browser workflow utilizing `ctb-staging-mcp-server` to capture staging UI screens and store optimized image files alongside referencing documentation pages.

#### Scenario: Capturing a missing workflow screenshot

- **WHEN** a documentation page contains a `<!-- TODO: screenshot <filename>.png -->` comment
- **THEN** the automated screenshot workflow navigates to the staging screen, captures the image, and saves it as `<filename>.png` in the page directory.

### Requirement: Screenshot graphics SHALL adhere to kebab-case naming and image gallery categorization

All captured UI graphics SHALL use lowercase kebab-case file names and automatically register in `gallery.md` categories (`admin.md`, `dashboard.md`, `mobile.md`, `reports.md`).

#### Scenario: Registering screenshot in image gallery

- **WHEN** a new screenshot graphic is added to `docs/user-guide/`
- **THEN** `mkdocs.yml` `image-gallery` plugin registers the file into the corresponding category gallery.
