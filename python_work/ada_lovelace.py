name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # f-string is a formatted string literal
print(full_name)
print(full_name.title())

message = f"Hello, {full_name.title()}!"
print(message)