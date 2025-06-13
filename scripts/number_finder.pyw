import pyperclip
import re

message = pyperclip.paste()

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # Creates the search tool
result = phoneNumRegex.findall(message) # Uses the tool to search


if result:
    listed_numbers = '\n'.join(result)  # Join numbers with newlines
    pyperclip.copy(listed_numbers)      # Copy to clipboard

