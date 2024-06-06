def main():
    print("This program calculates the interest on your savings account")
    print("")

    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the number of years: "))

    monthly_interest_rate = rate / 12 / 100
    amount_of_months = time * 12
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** amount_of_months) / ((1 + monthly_interest_rate) ** amount_of_months - 1)
    total_payment = monthly_payment * amount_of_months
    print("The total amount you will have after " + str(time) + " years is: " + str(total_payment))

while True:
    main()
    print("")
    repeat = input("Would you like to calculate another interest? (Y/N): ")
    if repeat.lower() != "y":
        print("Program terminated")
        quit()
    print("")