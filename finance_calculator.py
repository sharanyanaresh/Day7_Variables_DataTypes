"""
Personal Finance Calculator
Day 7 - Variables & Data Types Assignment
"""


def get_employee_data():
    """
    Collect employee financial details from user input.

    Returns:
        tuple: (name, annual_salary, tax_percentage,
                monthly_rent, savings_percentage)
    """
    try:
        name = input("Enter employee name: ")

        annual_salary = float(input("Enter annual salary: "))
        tax_percentage = float(input("Enter tax percentage (0-50): "))
        monthly_rent = float(input("Enter monthly rent: "))
        savings_percentage = float(
            input("Enter savings goal percentage (0-100): ")
        )

        return (
            name,
            annual_salary,
            tax_percentage,
            monthly_rent,
            savings_percentage,
        )

    except ValueError as exc:
        raise ValueError(
            "Invalid input. Please enter numeric values correctly."
        ) from exc


def validate_inputs(
    annual_salary, tax_percentage, monthly_rent, savings_percentage
):
    """
    Validate all financial inputs.

    Raises:
        ValueError: If any input is invalid.
    """
    if annual_salary <= 0:
        raise ValueError("Annual salary must be greater than 0.")

    if not 0 <= tax_percentage <= 50:
        raise ValueError("Tax percentage must be between 0 and 50.")

    if monthly_rent <= 0:
        raise ValueError("Monthly rent must be greater than 0.")

    if not 0 <= savings_percentage <= 100:
        raise ValueError("Savings percentage must be between 0 and 100.")


def calculate_financials(
    annual_salary, tax_percentage, monthly_rent, savings_percentage
):
    """
    Perform all financial calculations.

    Returns:
        dict: Dictionary containing calculated values.
    """
    monthly_salary = annual_salary / 12
    monthly_tax = monthly_salary * tax_percentage / 100
    net_salary = monthly_salary - monthly_tax

    savings_amount = net_salary * savings_percentage / 100
    disposable = net_salary - savings_amount - monthly_rent
    rent_ratio = (monthly_rent / net_salary) * 100

    total_tax = monthly_tax * 12
    total_savings = savings_amount * 12
    total_rent = monthly_rent * 12

    return {
        "monthly_salary": monthly_salary,
        "monthly_tax": monthly_tax,
        "net_salary": net_salary,
        "savings_amount": savings_amount,
        "disposable": disposable,
        "rent_ratio": rent_ratio,
        "total_tax": total_tax,
        "total_savings": total_savings,
        "total_rent": total_rent,
    }


def generate_report(name, annual_salary, data):
    """
    Generate formatted financial summary report.

    Returns:
        str: Formatted financial report.
    """
    line = "═" * 44
    sub_line = "─" * 44

    report = f"""
{line}
EMPLOYEE FINANCIAL SUMMARY
{line}
Employee : {name}
Annual Salary : ₹{annual_salary:,.2f}
{sub_line}
Monthly Breakdown:
Gross Salary : ₹ {data["monthly_salary"]:,.2f}
Tax ({data["monthly_tax"] / data["monthly_salary"] * 100:.1f}%) : ₹ {data["monthly_tax"]:,.2f}
Net Salary : ₹ {data["net_salary"]:,.2f}
Rent : ₹ {data["total_rent"] / 12:,.2f} ({data["rent_ratio"]:.1f}% of net)
Savings ({data["savings_amount"] / data["net_salary"] * 100:.1f}%) : ₹ {data["savings_amount"]:,.2f}
Disposable : ₹ {data["disposable"]:,.2f}
{sub_line}
Annual Projection:
Total Tax : ₹ {data["total_tax"]:,.2f}
Total Savings : ₹ {data["total_savings"]:,.2f}
Total Rent : ₹ {data["total_rent"]:,.2f}
{line}
"""
    return report


def main():
    """
    Main execution function.
    """
    try:
        (
            name,
            annual_salary,
            tax_percentage,
            monthly_rent,
            savings_percentage,
        ) = get_employee_data()

        validate_inputs(
            annual_salary,
            tax_percentage,
            monthly_rent,
            savings_percentage,
        )

        financial_data = calculate_financials(
            annual_salary,
            tax_percentage,
            monthly_rent,
            savings_percentage,
        )

        report = generate_report(name, annual_salary, financial_data)
        print(report)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()