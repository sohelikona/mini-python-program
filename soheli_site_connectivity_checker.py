import urllib.request as urllib


def main(url):
    print("Checking connectivity   ")


    response = urllib.urlopen(url)
    print("Connected to ", url, "successfully.")
    print("\nThe response code was:   ", response.getcode())


print("This is a site connectivity checker")
input_url = input("\nInput the url if the site you want to check:       ")


main(input_url)