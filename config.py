import json


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, "w") as file:
        json.dump(data, file, indent = 4)

def read(filename):
    with open(filename, "r") as file:
        return json.load(file)

print(read("config.json"))
input()
