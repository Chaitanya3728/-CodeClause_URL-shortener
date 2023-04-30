import pyshorteners

# get the long URL from user input
long_url = input("Enter the long URL to shorten: ")

# create an instance of the pyshorteners.Shortener class
shortener = pyshorteners.Shortener()

# shorten the URL using the TinyURL service
short_url = shortener.tinyurl.short(long_url)

# print the shortened URL
print("\nShortened URL:", short_url,"\n")
