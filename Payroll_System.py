def calculate_bonus(base_salary, performance_rating):

    if performance_rating == 5:
        bonus = 0.20
    elif performance_rating in (3, 4):
        bonus = 0.10
    elif performance_rating in (1, 2):
        bonus = 0.0

    return base_salary * bonus


def calculate_tax(gross_salary):
    if gross_salary > 7000:
        tax_percentage = 0.15
    elif 3000 <= gross_salary <= 7000:
        tax_percentage = 0.10
    elif gross_salary < 3000:
        tax_percentage = 0.0

    return gross_salary * tax_percentage


def main_hr_app():
    name = input("Please Enter your name :")
    department = input("Please Enter Your Department :")
    base_salary = float(input("Please Enter your salary :"))
    performance_rating = int(input("Please Enter your rating (1-5) :"))

    if performance_rating > 5 or performance_rating < 1 or base_salary < 0:
        print(" Invalid input , Please restart the program and try again.")
        return

    bonus = calculate_bonus(base_salary, performance_rating)
    gross_salary = base_salary + bonus
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax

    print("=" * 25)
    print(f"Payroll System for: {name}")
    print("=" * 25)
    print(f"=>Department: {department}")
    print(f"=>Base Salary: {base_salary:.2f} EGP")
    print(f"=>Earned Bonus: {bonus:.2f} EGP")
    print(f"=>Tax Deduction: {tax:.2f} EGP")
    print("=" * 25)
    print(f"Net Payable Cash: {net_salary:.2f} EGP")
    print(f"Thanks For Using Eng {name}")


main_hr_app()
