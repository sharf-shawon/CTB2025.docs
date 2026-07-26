## ADDED Requirements

### Requirement: Task documentation SHALL include verified role permissions and prerequisites

Every task-oriented documentation page SHALL explicitly document the required Django permission codenames, user role prerequisites, and record state preconditions under `Prerequisites & Role Permissions`.

#### Scenario: Reviewing task prerequisites

- **WHEN** a user reads `docs/user-guide/03-trade/invoices/create-invoice.md` or `docs/user-guide/04-employee/salary/generate-salary.md`
- **THEN** the `Prerequisites & Role Permissions` section lists the exact required roles, permission codenames (e.g. `trade.add_invoice`), and active prerequisite records required to execute the task.

### Requirement: Task documentation SHALL specify explicit verification criteria

Every procedural task page SHALL include a `Verification & Definition of Done` section detailing how the user verifies that an operation succeeded.

#### Scenario: Verifying task completion

- **WHEN** a user completes a procedure described on a task page
- **THEN** the `Verification & Definition of Done` section lists specific observable outcomes such as status pill updates, generated voucher entries, financial ledger adjustments, or stock movements.

### Requirement: Field references SHALL document all validation rules and default values

Every `Field reference` table SHALL detail visible UI field labels, required flags (`*`), allowed format constraints, default values, and backend Django validation rules verified against `github-mcp-server` and `ctb-staging-mcp-server`.

#### Scenario: Inspecting field reference table

- **WHEN** a user reviews a field in a documentation table
- **THEN** the entry specifies whether the field is required, auto-generated, or restricted by balance limits/roles.
