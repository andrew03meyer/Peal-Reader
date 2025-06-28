import json

def create_json(result):
    date = ""
    performance = "" #e.g. Bristol Suprise Maximus
    society = ""
    ringers = []
    footnote = ""

def check_society(result):
    file_path = './bellboard-data.json'
    file_json = open(file_path)
    societies = json.load(file_json)
    print(societies['Bow'])

def main():
    check_society("hi")

if __name__ == "__main__":
    main()