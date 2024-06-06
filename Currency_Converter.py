def main():
    print("Welcome to the Currency Converter!")
    print("We currently support the following currencies:")
    print("1. USD - United States Dollar")
    print("2. EUR - Euro")
    print("3. JPY - Japanese Yen")
    print("4. GBP - British Pound")
    print("5. AUD - Australian Dollar")
    print("6. CAD - Canadian Dollar")
    print("7. CHF - Swiss Franc")
    print("8. CNY - Chinese Yuan")
    print("9. SEK - Swedish Krona")
    print("10. NZD - New Zealand Dollar")
    print("11. KRW - South Korean Won")
    print("12. SGD - Singapore Dollar")
    print("13. NOK - Norwegian Krone")
    print("14. MXN - Mexican Peso")
    print("15. INR - Indian Rupee")
    print("16. RUB - Russian Ruble")
    print("17. ZAR - South African Rand")
    print("18. TRY - Turkish Lira")
    print("19. BRL - Brazilian Real")
    print("20. HUF - Hungarian Forint")
    print("21. PLN - Polish Zloty")
    print("22. IDR - Indonesian Rupiah")
    print("23. DKK - Danish Krone")
    print("24. SAR - Saudi Riyal")
    print("25. AED - United Arab Emirates Dirham")
    print("26. MYR - Malaysian Ringgit")
    print("27. HKD - Hong Kong Dollar")
    print("28. THB - Thai Baht")
    print("29. COP - Colombian Peso")
    print("30. PHP - Philippine Peso")
    print("31. ILS - Israeli Shekel")
    print("32. EGP - Egyptian Pound")
    print("33. ARS - Argentine Peso")
    print("34. CLP - Chilean Peso")
    print("35. PKR - Pakistani Rupee")

    currency_dict = {
        "USD": 1.0,
        "EUR": 0.85,
        "JPY": 113.61,
        "GBP": 0.76,
        "AUD": 1.36,
        "CAD": 1.29,
        "CHF": 0.92,
        "CNY": 6.47,
        "SEK": 8.48,
        "NZD": 1.43,
        "KRW": 1131.58,
        "SGD": 1.35,
        "NOK": 8.55,
        "MXN": 20.47,
        "INR": 73.57,
        "RUB": 74.47,
        "ZAR": 14.74,
        "TRY": 8.44,
        "BRL": 5.33,
        "HUF": 309.85,
        "PLN": 3.92,
        "IDR": 14497.5,
        "DKK": 6.35,
        "SAR": 3.75,
        "AED": 3.67,
        "MYR": 4.14,
        "HKD": 7.77,
        "THB": 33.07,
        "COP": 3875.0,
        "PHP": 50.46,
        "ILS": 3.22,
        "EGP": 15.69,
        "ARS": 97.85,
        "CLP": 758.0,
        "PKR": 175.0
    }

    while True:
        try:
            amount = float(input("Enter the amount you want to convert: "))
            from_currency = input("Enter the currency you want to convert from: ").upper()
            to_currency = input("Enter the currency you want to convert to: ").upper()

            converted_amount = amount * currency_dict[to_currency] / currency_dict[from_currency]
            print("Converted amount:", converted_amount)
        except KeyError:
            print("Invalid currency. Please enter a valid currency.")
        except ValueError:
            print("Invalid amount. Please enter a valid amount.")
        except ZeroDivisionError:
            print("You cannot convert to the same currency. Please enter different currencies.")
        except Exception as e:
            print("An error occurred:", e)

        print("")
        repeat = input("Would you like to convert another currency? (Y/N): ")
        if repeat.lower() != "y":
            print("Program terminated")
            quit()
        print("")
main()
