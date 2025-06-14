import pyperclip
import re

emailRegex = re.compile('''

[a-zA-Z0-9_.+-~$%#^/.&='+]   # name part
@   # @ symbol
[a-zA-Z0-9_.+-~$%#^/.&=']+   # domain part      
                                          
''', re.VERBOSE)

text = pyperclip.paste()

results = emailRegex.findall(text)

if results:
    pyperclip.copy(results)