import requests, os, json, utils, re





# curr_dir = os.path.dirname(os.path.abspath(__file__))
curr_dir = utils.DIRECTORY


requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass


url = "https://shakespeare.mit.edu/"
page = requests.get(url, verify=False)
html = page.text
html_list = html.split("\n")


# plays = open(os.path.join(curr_dir, "plays.txt"), "w")
plays_raw = []
plays_dict = {}

for line in html_list:
    if "index.html" in line:
        if line[len(line)-4:] == "</a>":
            # print(line, file=plays)
            plays_raw.append(line)
        else:
            # print(f"{line}{html_list[(html_list.index(line))+1]}", file=plays)
            plays_raw.append(f"{line}{html_list[(html_list.index(line))+1]}")
        # print(html_list[(html_list.index(line))+1], file=plays)
        # print(file=plays)

# print(plays_raw[0])

# result = re.search('<a href=\"(.*)\">', plays_raw[0])
# print(result.group(1))

# start = plays_raw[0].find("index.html\">") + len("index.html\">")
# end = plays_raw[0].find("</a>")

# print(plays_raw[0][start:end])


for play in plays_raw:
    
    result = re.search('<a href=\"(.*)\">', play)
    start = play.find("index.html\">") + len("index.html\">")
    end = play.find("</a>")

    key = play[start:end]
    val = str(url + result.group(1).replace("index", "full"))

    plays_dict[key] = val

with open(os.path.join(curr_dir, "plays.json"), "w") as file:
    json.dump(plays_dict, file, indent=2)
# plays.close()
