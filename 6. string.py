s = "Hello, World!"

print(f"Length of the string: {len(s)}")

print(f"Occurrences of 'l': {s.count('l')}")

print(f"Uppercase string: {s.upper()}")

print(f"Lowercase string: {s.lower()}")

print(f"Capitalized string: {s.capitalize()}")

print(f"Titlecased string: {s.title()}")

substring = "World"
print(f"Index of 'World': {s.find('World')}")

ss1 = "World"
ss2 = "Python"
ns = s.replace(ss1, ss2)
print(f"Replaced string: {ns}")

words = s.split(", ")
print(f"Split string: {words}")

joined_string = ", ".join(words)
print(f"Joined string: {joined_string}")

string_with_spaces = "   Hello, World!   "
print(f"Stripped string: '{string_with_spaces.strip()}'")

print(f"Is 'Hello' alphabetic? {'Hello'.isalpha()}")

print(f"Is '123' numeric? {'123'.isdigit()}")

print(f"Does string start with 'Hello'? {s.startswith('Hello')}")

print(f"Does string end with 'World!'? {s.endswith('World!')}")