import re

# email="james@email.com"
# email="john@email.com"

#create a pattern
# pattern = re.compile(r"com$")
# pattern = re.compile(r"\w{2,}@\w{4,}\.com")
# pattern = re.compile(r"\w+@\w+\.\w+")

email = "chris@gmail.com"
pattern = re.compile(r"\w+@(gmail.com|yahoo.com)")
pattern = re.compile(r"\w+@[.&_]com")


result = pattern.search(email)

print(result)