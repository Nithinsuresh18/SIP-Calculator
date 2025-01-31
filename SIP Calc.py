# sip calculator
premium=float(input("Enter sip amount : "))
Years=int(input("Enter no of Years : "))
month=int(Years*12)
Expreturn=float(input("Enter the expected return : "))
monthly_return=float(Expreturn/12)
x=premium+(premium*(monthly_return/100))
for y in range(month-1):
    x=premium+x+((premium+x)*(monthly_return/100))
print(f"The expected return is {round(x)}")