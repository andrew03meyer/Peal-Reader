import requests
import lxml.etree as etree

# Step 1: Make the API request
def fetch_bellboard_data():
    url = "https://bellboard.uk/view.php?id=110081&fmt=xml" #https://bellboard.uk/search.php?changed_since=2025-06-29&format=xml
    response = requests.get(url)
    
    # Step 2: Check if the request was successful
    if response.status_code == 200:
        # Step 3: Parse the XML content
        xml_data = response.content
        return xml_data
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

def print_child_values(xml_tree_root_node):
    xml_tree_root_node = etree.fromstring(xml_tree_root_node)
    # print(etree.tostring(xml_data, pretty_print="True"))
    print(xml_tree_root_node.attrib)
    print("\n")

    #Prints tag, attribute and text of the root's child
    for child in xml_tree_root_node:
        print(child.tag, child.attrib, child.text)


def main():
    xml_data = ""
    try:
        xml_data = fetch_bellboard_data()
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print_child_values(xml_data)
    
if __name__ == "__main__":
    main()