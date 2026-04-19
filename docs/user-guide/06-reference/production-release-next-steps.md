# Production Release Next Steps

Use this checklist to complete final production release actions.

## Final validation checklist

- [ ] Run `uv run mkdocs build --strict` and confirm zero warnings
- [ ] Run `uv run pre-commit run --all-files` and confirm all checks pass
- [ ] Run `uv run mkdocs serve` and manually verify key pages in browser
- [ ] Verify all sidebar links resolve correctly across modules
- [ ] Verify screenshots load correctly on critical pages

## Content and navigation verification

- [ ] Confirm all module overview pages are current
- [ ] Confirm naming is consistent for files, headings, and nav labels
- [ ] Confirm new pages are included in `mkdocs.yml` nav
- [ ] Confirm no orphaned docs that should be discoverable via nav

## Release operations

- [ ] Confirm required environment variables are configured for deployment
- [ ] Merge release PR to `main`
- [ ] Verify docs deploy workflow succeeds
- [ ] Smoke test published site URLs

## Post-release follow-up

- [ ] Record any audit findings in issue tracker
- [ ] Prioritize documentation gaps for next iteration
- [ ] Update this checklist based on lessons learned
