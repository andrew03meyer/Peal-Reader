import json

# takes array and writes to JSON file
def create_json(result):
    association = result[0]
    place = result[1]
    date = result[2]
    duration = result[3]
    title = result[4]
    timestamp = 0
    source = ""
    rwref = ""

    json_text = {
        "association" : association,
        "place" : place,
        "date" : date,
        "duration" : duration,
        "title" : title,
        "timestamp" : timestamp,
        "source" : source,
        "rwref" : rwref
    }

    json_file = json.dumps(json_text)
    # needs to create a unique key for storing the file
    export_path = "./output-json/" + place + "-" + str(timestamp) + ".json"
    export_file = open(export_path, "w")
    export_file.write(json_file)
    export_file.close()


def check_society(result):
    file_path = './bellboard-data.json'
    file_json = open(file_path)
    societies = json.load(file_json)
    return result.lower() in societies['societies']


def main():
    print(check_society("St Martin's Guild"))
    # create_json(["St Martin's Guild", "7450", "2009-12-02", "5h 21", "None", "2017-01-05T15:06:19", "None", "5149.11"])

if __name__ == "__main__":
    main()

# date id = date_rung
# association id =  association
# place id = place
# county id = region
# dedication id = address
# length id = changes
# method id = title
# duration id = duration
# tenor id = tenor_size
# details id = details
# composer id = composer
# ringers id 1-16 = ringers.x
# footnotes id = footnotes
# submit id = formsubmit