course = input("Enter your course code:")

import re
result= re.findall(r"[A-Z][A-Z][A-Z]\d\d\d", course)
if result and course == result[0]:
    print(True)
else:
    print(False)