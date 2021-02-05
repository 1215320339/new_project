import re

s="""i love you not because of who 234 you are, 234 but 3234ser because of who i am when i am with you"""

r = re.search(r"(\d+)[a-z]+", s)
print(r.group())