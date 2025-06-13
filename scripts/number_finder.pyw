import pyperclip
import re

message = pyperclip.paste()

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # Creates the search tool
result = phoneNumRegex.findall(message) # Uses the tool to search


if result:
    for num in result:
        print(num)
        pyperclip.copy()
else:
    print("No phone number found")

