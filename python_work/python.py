print("Python")

print("\tPython") # \t is a tab

print("Languages:\nPython\nC\nJaveScript") # \n is a newline character

print("Languages:\n\tPython\n\tC\n\tJaveScript") # \n\t is a newline character followed by a tab character

favorite_language = ' python '


favorite_language.rstrip() # rstrip() removes whitespace from the right side of a string
print(favorite_language.rstrip())
favorite_language.lstrip() # lstrip() removes whitespace from the left side of a string
print(favorite_language.lstrip())
favorite_language.strip() # strip() removes whitespace from both sides of a string
print(favorite_language.strip())

nostarch_url = "https://nostarch.com"
print(nostarch_url)

nostarch_url.removeprefix("https://") # removeprefix() removes a prefix from a string
print(nostarch_url.removeprefix("https://"))

simple_url = nostarch_url.removeprefix("https://")
print(simple_url)