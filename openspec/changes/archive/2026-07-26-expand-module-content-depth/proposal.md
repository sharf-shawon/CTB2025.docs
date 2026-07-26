## Why

The current documentation for CTB Admin covers basic page structures and nav entries across all 10 modules, but key operational sections suffer from shallow step-by-step procedures, missing form field constraints, and inadequate error recovery guidance.

Expanding the module content depth addresses critical operational friction for users by providing comprehensive step-by-step guides, explicit field validations, permissions context, and concrete error recovery protocols for complex workflows in Trade, Business, Factory, and Employee modules.

## What Changes

- **Step-by-Step UI Procedure Expansion**: Update task pages across `01-business`, `02-factory`, `03-trade`, and `04-employee` to include complete click-by-click instructions, required vs. optional fields, and UI feedback states.
- **Form Field & Validation Catalog**: Document mandatory field formats, character limits, date ranges, and system constraints for complex entries (e.g. Invoice creation, Voucher posting, Salary generation).
- **Domain Error Recovery & Failure Modes**: Add dedicated "Common Errors & Troubleshooting" sections to key operational workflows with specific error messages, causes, and step-by-step resolution paths.
- **Role & Permission Callouts**: Annotate each major task with required User/Group permissions (e.g. `Can add payment`, `Can approve salary`).

## Capabilities

### New Capabilities

- `module-operational-procedures`: Detailed step-by-step UI workflows, field validation constraints, and role permissions across core CTB Admin modules.
- `domain-error-recovery-reference`: Comprehensive mapping of domain operational failure modes, diagnostic symptoms, and step-by-step recovery protocols.

### Modified Capabilities

*(None)*

## Impact

- **Documentation Files**: Enhances markdown pages in `docs/user-guide/01-business/`, `02-factory/`, `03-trade/`, `04-employee/`, and `09-reference/`.
- **Search & Usability**: Improves MkDocs search discovery for error messages, field labels, and workflow terms.
- **Verification Pipeline**: Leverages `style_lint.py` to ensure all expanded pages maintain strict `STYLE_SPEC.md` structural compliance.
