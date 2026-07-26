## ADDED Requirements

### Requirement: RBAC Permission Codename Reference

User and role administration pages SHALL document exact Django permission codenames required for each system module.

#### Scenario: Admin assigns module permissions to a user role

- **WHEN** an administrator configures permissions for a custom role
- **THEN** the documentation MUST list the precise codenames (e.g. `trade.add_invoice`, `employee.change_salary`).

### Requirement: Audit Log Inspection Procedures

The Audit Log documentation SHALL specify exact filter and inspection procedures for tracking user actions and security events.

#### Scenario: Security audit conducted on system actions

- **WHEN** an administrator inspects audit logs for suspicious account activity
- **THEN** the documentation MUST explain how to filter logs by user, action type, and date range.
