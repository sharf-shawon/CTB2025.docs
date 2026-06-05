# User Management

Use this page to create a new user account in CTB Admin. A user account provides login credentials and permission controls that determine what modules and actions each staff member can access.

## Summary

Create a complete user profile with valid credentials and appropriate permissions before the user can access CTB Admin. Proper setup ensures each staff member can only perform approved tasks.

## When to use this page

- Onboarding a new employee who needs CTB Admin access
- Creating admin accounts with elevated permissions
- Setting up department-specific user accounts with limited access

## How to access this page

From the sidebar, go to **Settings and Admin → User Management**. On the Users list page, click the **purple (+) icon** in the top-right corner.

The system opens the **Add User Page**.

## Account Information

![Add User Form](add-user.png)

Fill in the following fields:

| Field                         | What to Do             | Description                                               |
| ----------------------------- | ---------------------- | --------------------------------------------------------- |
| Username                      | Enter a unique name    | Used for login; must be unique across the system          |
| Is Active                     | Toggle ON/OFF          | Controls whether the account is immediately usable        |
| Password-based authentication | Enable or disable      | Determines if the user logs in with username and password |
| Password                      | Enter a valid password | See password requirements below                           |
| Password confirmation         | Re-enter the password  | Must match the password field exactly                     |

!!! warning "Required Fields"
Fields marked with a **red star (\*)** are mandatory.

______________________________________________________________________

## Password Requirements

When creating a password, the system enforces the following rules:

- **Minimum 8 characters** — Password must be at least 8 characters long
- **Cannot match username** — Password cannot be identical to the username
- **Cannot be all numeric** — Password must contain at least one letter or special character

!!! tip "Password Best Practices"
Use a mix of uppercase, lowercase, numbers, and special characters for stronger security.

______________________________________________________________________

## Permissions Section

After clicking **Save and continue editing**, the system displays the **Permissions** section where you can control access levels.

![Permissions Section](user-permission-page.png)

| Option                      | Description                                                                             |
| --------------------------- | --------------------------------------------------------------------------------------- |
| Staff status                | Grants access to the CTB Admin interface (must be enabled for most users)               |
| Superuser / is_superuser    | Admin-level access to all modules and settings (use carefully)                          |
| Module-specific permissions | Fine-grained controls for individual modules (Business, Factory, Trade, Employee, etc.) |
| Action-level permissions    | Controls specific actions like Add, Change, Delete within each module                   |

Assign the minimum required permissions for the user's role.

______________________________________________________________________

## Saving the User

After completing account information:

- Click **Save** to create the user account
- Click **Save and continue editing** to save and assign permissions on the same page

______________________________________________________________________

## Tips and common issues

- **Password rejected?** Ensure it is 8+ characters, differs from the username, and includes at least one non-numeric character.
- **Grant minimum required access first** — expand permissions only if the user needs additional tasks.
- **User cannot log in after creation?** Verify that **Is Active** and **Staff status** are both enabled.
- **Permissions not taking effect?** Ask the user to sign out completely and sign back in.
- [App Settings](app-settings.md)
- [Maintenance Mode](maintenance-mode.md)
