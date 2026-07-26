# Generate Salary

Use this page to create a salary record for an employee in CTB Admin. A salary record calculates the payable amount for a specific employee and month based on their salary rate, work units, overtime, bonuses, and deductions. Salary records are used to manage monthly or periodic compensation and maintain a complete payroll history.

## When to use Generate Salary page

- Generating a monthly salary entry for an employee
- Recording salary payments with bonuses or deductions
- Logging overtime hours for compensation calculation
- Marking a salary as paid and recording the payment date
- Tracking outstanding salary balances before processing payroll

## How to access Generate Salary page

From the sidebar, go to **Employee Management → Salaries**. On the Salaries List page, click the **purple (+) icon** in the top-right corner.

The system opens the **Generate Salary** page.

______________________________________________________________________

## General Information

![Generate Salary General Information](generate-salary-general-info.png)

Fill in the following fields:

| Step | Field    | What to Do           | Description                                            |
| ---- | -------- | -------------------- | ------------------------------------------------------ |
| 1    | Employee | Select from dropdown | The employee this salary record is being generated for |
| 2    | Month    | Select date          | The month and year this salary record covers           |

!!! warning "Required Fields"

    Fields marked with a **red star (\*)** are mandatory. Employee and Month must be filled before saving.

______________________________________________________________________

## Salary Components

![Salary Components Section](generate-salary-componant-section.png)

Enter the salary calculation fields:

| Step | Field            | What to Do      | Description                                                                    |
| ---- | ---------------- | --------------- | ------------------------------------------------------------------------------ |
| 1    | SKU              | Auto-generated  | Unique identifier for this salary record (read-only)                           |
| 2    | Salary           | Enter amount    | Salary rate for this period; enter 0 to use the employee's default salary rate |
| 3    | Salary Units     | Enter number    | Number of workdays or work hours to calculate salary against                   |
| 4    | Overtime (hours) | Enter hours     | Number of overtime hours worked during this period                             |
| 5    | Bonus            | Enter amount    | Bonus amount in Tk to add to the base salary                                   |
| 6    | Deductions       | Enter amount    | Deduction amount in Tk to subtract from the base salary                        |
| 7    | Net Salary       | Auto-calculated | Final payable amount (Salary × Units + Overtime + Bonus - Deductions)          |

!!! note "Net Salary Calculation"

    Net Salary is calculated automatically based on Salary, Salary Units, Overtime, Bonus, and Deductions. You do not need to enter it manually.

!!! tip

    Set **Salary** to **0** to apply the default salary rate configured on the employee's profile.

______________________________________________________________________

## Payment Details

![Payment Details Section](generate-salary-payment-detail.png)

Record whether this salary has been paid:

| Step | Field         | What to Do    | Description                                                    |
| ---- | ------------- | ------------- | -------------------------------------------------------------- |
| 1    | Is Paid       | Toggle ON/OFF | Mark the salary record as paid or unpaid                       |
| 2    | Payment Date  | Select date   | The date the payment was made (required if Is Paid is ON)      |
| 3    | Payment Notes | Enter text    | Optional notes about the payment method, reference, or remarks |

!!! note "Payment Date Visibility"

    Payment Date and Payment Notes fields are active when **Is Paid** is toggled on. Leave Is Paid off if the salary is still outstanding.

______________________________________________________________________

## Related Records

The **Related Records** section at the bottom is a collapsible section that displays any linked records associated with this salary entry, such as attendance record

!!! info

    Click the **Related Records** header to expand and review linked data for this salary record.

______________________________________________________________________

## Saving the Salary Record

After completing all sections:

- Click **Save** to create the salary record
- Click **Save and continue editing** to save and stay on the page
- Click **Save and add another** to save and immediately generate another salary record

______________________________________________________________________

## Deleting a Salary Record

A **Delete Salary** button is available at the bottom-left of the page.

!!! warning "Restricted Action"

    Deleting a salary record is permanent. Only delete records that were created in error and have not been linked to any payout or financial transaction. Contact your system administrator if a linked salary record needs to be removed.

______________________________________________________________________

## Tips and common issues

- **Employee is required** — You must select an employee before saving
- **Month is required** — Select the correct month to ensure the record appears in the right payroll period
- **Default salary applies when Salary is 0** — If no salary is entered, the system uses the rate set on the employee's profile
- **Net Salary updates automatically** — It recalculates whenever Salary, Salary Units, Overtime, Bonus, or Deductions are changed
- **Salary Units represent workdays or hours** — Enter the correct number based on the employee's salary type (e.g., Monthly or Hourly)
- **Toggle Is Paid only when payment is confirmed** — Setting Is Paid without a Payment Date may cause payroll reporting inconsistencies
- **Deductions reduce Net Salary** — Enter deductions carefully as they directly reduce the employee's final payable amount
- **History button** — Use the **History** button in the top-right corner to review all changes made to this salary record

______________________________________________________________________

## Related Pages

- **Salaries Overview** — View and manage all salary records
- **Employees** — Manage employee profiles and default salary rates
- **Wages** — Record production-based wage entries for employees
- **Payouts** — Process and track salary disbursements
- **Attendance** — Review attendance records used for salary unit calculation
