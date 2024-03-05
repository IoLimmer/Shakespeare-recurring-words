import re

with open("macbeth.txt", "r") as file:
    html_str = file.read()
with open("macbeth.txt", "r") as file:
    html_list = file.readlines()


with open("macbeth2.txt", "w") as file:
    pattern = "<(.|\n)*?>"
    html_str = re.sub(pattern, "", html_str)
    file.write(html_str)
