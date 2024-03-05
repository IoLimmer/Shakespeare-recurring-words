import requests


requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass


url = "https://shakespeare.mit.edu/macbeth/full.html"
page = requests.get(url, verify=False)
html = page.text

# print(type(html))
# print(len(html))

with open("macbeth.txt", "w") as file:
    file.write(html)

# for x in range(2000):
#     print(html[x], end="")