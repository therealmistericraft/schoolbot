import json

def read(message, list):
    file = open(f".../data/usr/courselists/{message.guild.id}.json", "w+")
    content = json.load(list)
    json.dump(content, file, indent=4)
