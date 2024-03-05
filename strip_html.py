import re, os

import utils


with open(os.path.join(utils.DIRECTORY, "macbeth.txt"), "r") as file:
    html_str = file.read()
with open(os.path.join(utils.DIRECTORY, "macbeth.txt"), "r") as file:
    html_list = file.readlines()


with open(os.path.join(utils.DIRECTORY, "macbeth2.txt"), "w") as file:

    ### Anything marked in italics is a stage direction, so not important to this
    pattern = "<i>.*?</i>"
    html_str = re.sub(pattern, "", html_str)

    ### Upper case words are assumed to be the names of characters
    pattern = "\n<A NAME=speech.*?/a>"
    html_str = re.sub(pattern, "", html_str)

    ### Anything marked which h3 is text reading the act and scene number
    pattern = "\n<[Hh]3.*?/[Hh]3>"
    html_str = re.sub(pattern, "", html_str)


    pattern = "<(.|\n)*?>"
    html_str = re.sub(pattern, "", html_str) ### remove html artifacts
    html_str = re.sub("\n+", " ", html_str) ### replace newlines with spaces



    ### Remove all punctuation except apostrophes 
    html_str = re.sub(r"[^a-zA-Z0-9\'\s]",'',html_str)


    ### remove everything before "Entire play"
    start_index = html_str.find("Entire play") + len("Entire play") + 1
    # print(start_index)
    html_str = html_str[start_index:]

    # html_str = re.sub(r"\b[A-Z]{2,}\b",'',html_str) ### Remove anything in block capitals
    html_str = re.sub(" +", " ", html_str) ### replace excessive spaces with just one

    file.write(html_str)

