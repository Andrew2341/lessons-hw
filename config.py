import json

data = {
    "name": "app1",
    "version": "0,01"
}
data_json = json.dumps(data)

with open('config.json', 'w') as file:
    file.write(data_json)
with open ("config.json", "r") as file:
    # data_json = file.read()
    data = json.load(file)
# data = json.loads(data_json)
print(data["name"])
