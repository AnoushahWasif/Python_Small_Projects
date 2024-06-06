def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a leap year.") 
            else:
                print("This is not a leap year.")
        else:
            print("This is a leap year.")
    else:
        print("This is not a leap year.")

def main():
    print("Welcome to Leap Year Checker!")
    year = int(input("Enter the year you want to check: "))
    is_leap_year(year)

    repeat = input("Would you like to check another year? (Y/N): ")
    if repeat.lower() != "y":
        print("Program terminated")
        quit()
    print("")

main()
        