import json

# takes array and writes to JSON file
def create_json(result):
    date = result[0]
    performance = result[1]
    society = result[2]
    ringers = result[3]
    footnote = result[4]

    json_text = {
        "date" : date,
        "performance" : performance,
        "society" : society,
        "ringers" : ringers,
        "footnote" : footnote
    }

    json_file = json.dumps(json_text)
    # needs to create a unique key for storing the file
    export_path = "./output-json/" + date + "-" + performance + ".json"
    export_file = open(export_path, "w")
    export_file.write(json_file)
    export_file.close()


def check_society(result):
    file_path = './bellboard-data.json'
    file_json = open(file_path)
    societies = json.load(file_json)
    print(societies['Bow'])

def main():
    # check_society("hi")
    create_json(["hi", "hello", "yes", "hee", "yoyo"])

if __name__ == "__main__":
    main()