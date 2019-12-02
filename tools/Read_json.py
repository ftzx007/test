import json
def read_json(filename):
        with open("../data/"+filename, "r", encoding="utf-8")as f:
            return json.load(f)

if __name__ == '__main__':
    data = read_json('addbill.json')
    print(data)