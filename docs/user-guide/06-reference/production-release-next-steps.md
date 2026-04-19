# Production Release Next Steps

Use this checklist to complete final production release actions.

## Summary

Use this page to finish the final checks before publishing the docs site.

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

## Tips and common issues

- Keep the final validation close to the publish step so the content does not drift.
- Smoke test the most visited pages first after deployment.
- Capture any missing screenshot or content gaps as follow-up work instead of blocking the release when they are non-critical.

## Related pages

- [Consolidated Release Checklist](release-checklist.md)
- [Production Release Summary](production-release-summary.md)
