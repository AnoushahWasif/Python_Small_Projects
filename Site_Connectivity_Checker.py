import urllib.request as urllib


def main(url):
    print("Checking the connectivity of the site...")

    response = urllib.urlopen(input_url)
    print("Connected to", input_url, "successfully!")
    print("Response code:", response.getcode())

print("Welcome to Site Connectivity Checker!")
input_url = input("Enter the URL of the site you want to check: ")

while True:
    main(input_url)
    print("")
    repeat = input("Would you like to check another site? (Y/N): ")
    if repeat.lower() != "y":
        print("Program terminated")
        quit()
    print("")