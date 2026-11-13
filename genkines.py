def calculate_salary():
  basic_salary = 50000
  hra = basic_salary * 0.20
  da = basic_salary * 0.10
  gross_salary = basic_salary + hra + da

  print("-- Employee Salary Details --")
  print(f"Basic Salary : Rs {basic_salary}")
  print(f"HRA (20%)    : Rs {hra}")
  print(f"DA (10%)     : Rs {da}")
  print(f"Gross Salary : Rs {gross_salary}")


if __name__ == "__main__":
  calculate_salary()
