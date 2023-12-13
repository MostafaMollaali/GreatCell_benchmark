import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('G3_v3.gml')
root = tree.getroot()

# Remove 'name' attribute from 'point' elements
for point_element in root.findall('.//point'):
    if 'name' in point_element.attrib:
        del point_element.attrib['name']

# Remove 'name' attribute from 'polyline' elements
for polyline_element in root.findall('.//polyline'):
    if 'name' in polyline_element.attrib:
        attr_name = polyline_element.get("name")
        if attr_name == "MIDDLE_BAG1":
            continue
        if attr_name == "MIDDLE_BAG5":
            continue
        if attr_name == "MIDDLE_BAG9":
            continue
        if attr_name == "MIDDLE_BAG13":
            continue
        print(attr_name)
        del polyline_element.attrib['name']

# Save the modified XML to a new file or overwrite the existing one
tree.write('G3_v3_named_required_entities.gml')
