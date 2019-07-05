a = int(input("investment amount: "))
b = int(input("interest rate in percentage: "))
c = int(input("number of years to invest: "))

print("future value:", round(a * (1 + b / 100) ** c, 3))
