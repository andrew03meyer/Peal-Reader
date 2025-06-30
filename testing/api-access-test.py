import requests

# Step 1: Make the API request
def fetch_bellboard_data():
    url = "https://bellboard.uk/search.php?changed_since=2025-06-29&format=xml"
    response = requests.get(url)
    
    # Step 2: Check if the request was successful
    if response.status_code == 200:
        # Step 3: Parse the XML content
        xml_data = response.content
        return xml_data
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

# Step 4: Extract the <p> data from the XML
def pull_div_data(data):
    split_data = data.split("div")
    for line in split_data:
        print(line.split("</div>", 1))
        print("\n")

def main():
    try:
        xml_data = str(fetch_bellboard_data())
        print("Data fetched successfully.")
        print(xml_data)
        # print(pull_div_data(xml_data))
    except Exception as e:
        print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    main()