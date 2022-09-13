import json
numbers_json = {"number":[
    "279(8757)730-45-03",
    "31(7818)853-36-16",
    "13(99)373-42-84",
    "47(4565)248-58-57",
    "99(2882)656-84-04",
    "813(797)455-21-27",
    "1(3066)229-06-05",
    "86(2499)350-66-24",
    "411(777)060-66-53",
    "22(7262)122-85-66"
]
}
data_json = json.dumps(numbers_json)
with open("number.json", "w") as file:
    file.write(data_json)
with open ("number.json", "r") as file:
    data_json = file.read()
numbers_json = json.loads(data_json)
