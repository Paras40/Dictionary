import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()


    if word in data:

        return data[word]


    elif len(get_close_matches(word, data.keys()))>0:

        yn = input("Did you mean %s instead? Enter Y if yes, or N if No : " % get_close_matches(word,data.keys())[0])
        yn = yn.upper()

        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            word = word.title()
            return f"{word} dosen't exist. Please double check it."
        else:
            return "We didn't understand your query."


    else:

        return "This word dosen't exist."
        

word = input("Enter word : ").strip()

output = (meaning(word))

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)
