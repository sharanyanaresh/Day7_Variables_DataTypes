"""
Personal Finance Calculator
Day 7 - Variables & Data Types Assignment
"""


def get_employee_data():
    """
    Collect employee financial details from user input.
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
    Validate financial inputs.
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
    Perform financial calculations.
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


def format_indian_currency(amount):
    """
    Format number into Indian numbering system (lakhs/crores).
    Example: 2000000 -> 20,00,000.00
    """
    amount_str = f"{amount:.2f}"
    integer_part, decimal_part = amount_str.split(".")

    if len(integer_part) <= 3:
        return f"{integer_part}.{decimal_part}"

    last_three = integer_part[-3:]
    remaining = integer_part[:-3]

    parts = []
    while len(remaining) > 2:
        parts.insert(0, remaining[-2:])
        remaining = remaining[:-2]

    if remaining:
        parts.insert(0, remaining)

    indian_number = ",".join(parts) + "," + last_three
    return f"{indian_number}.{decimal_part}"


def calculate_health_score(data):
    """
    Calculate financial health score (0-100).
    """
    score = 0

    rent_ratio = data["rent_ratio"]
    savings_rate = (data["savings_amount"] / data["net_salary"]) * 100
    disposable_rate = (data["disposable"] / data["net_salary"]) * 100

    if rent_ratio < 30:
        score += 30

    if savings_rate >= 20:
        score += 30

    if disposable_rate >= 20:
        score += 40

    return score


def generate_report(name, annual_salary, data, health_score):
    """
    Generate formatted financial summary report.
    """
    line = "═" * 44
    sub_line = "─" * 44

    report = f"""
{line}
EMPLOYEE FINANCIAL SUMMARY
{line}
Employee : {name}
Annual Salary : ₹{format_indian_currency(annual_salary)}
{sub_line}
Monthly Breakdown:
Gross Salary : ₹ {format_indian_currency(data["monthly_salary"])}
Tax ({data["monthly_tax"] / data["monthly_salary"] * 100:.1f}%) : ₹ {format_indian_currency(data["monthly_tax"])}
Net Salary : ₹ {format_indian_currency(data["net_salary"])}
Rent : ₹ {format_indian_currency(data["total_rent"] / 12)} ({data["rent_ratio"]:.1f}% of net)
Savings ({data["savings_amount"] / data["net_salary"] * 100:.1f}%) : ₹ {format_indian_currency(data["savings_amount"])}
Disposable : ₹ {format_indian_currency(data["disposable"])}
{sub_line}
Annual Projection:
Total Tax : ₹ {format_indian_currency(data["total_tax"])}
Total Savings : ₹ {format_indian_currency(data["total_savings"])}
Total Rent : ₹ {format_indian_currency(data["total_rent"])}
{sub_line}
Financial Health Score : {health_score}/100
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

        health_score = calculate_health_score(financial_data)

        report = generate_report(
            name, annual_salary, financial_data, health_score
        )

        print(report)

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()