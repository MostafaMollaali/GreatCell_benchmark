import sys
import os
import xml.etree.ElementTree as ET

def main():
    if "--help" in sys.argv:
        print("This script convert the compenent wise traction boundary conditions (assigned with Neumann)."
               "to normal traction boundary conditions")
        print("Usage: python neumann2normal_traction.py <input_file> <output_file>")
        return

    if len(sys.argv) != 3:
        print("Usage: python neumann2normal_traction.py <input_file> <output_file>")
        return

    input_file = sys.argv[1]
    infile_name = os.path.basename(input_file)
    output_file = sys.argv[2]
    outfile_name = os.path.basename(output_file)

    try:
        # Parse the XML file
        tree = ET.parse(infile_name)
        root = tree.getroot()

        def change_tags(elements, sub_tag_name, sub_sub_tag_name1, sub_sub_tag_name2=""):
            for element in elements.findall(sub_tag_name):
                name_element = element.find(sub_sub_tag_name1)
                if name_element is not None:
                    name_text = name_element.text
                    if 'FY' in name_text:
                        print('Removed element %s' % name_text)
                        elements.remove(element)
                    elif 'FX' in name_text:
                        # Remove the 'FX' prefix from the name
                        name_element.text = name_text.replace('_FX', '')
                        curve_element = element.find(sub_sub_tag_name2)
                        if curve_element is not None:
                            curve_element.text = curve_element.text.replace('_FX', '')

        elements = root.find("parameters")
        change_tags(elements, "parameter", "name", "curve")

        elements = root.find("curves")
        change_tags(elements, "curve", "name")

        elements = root.find("process_variables")
        processes = elements.findall("process_variable")
        for process in processes:
            bcs = process.findall("boundary_conditions")
            for bc in bcs:
                for element in bc.findall("boundary_condition"):
                    name_element = element.find("parameter")

                    if name_element is not None:
                        name_text = name_element.text
                        if 'FY' in name_text:
                            print('Removed element %s' % name_text)
                            bc.remove(element)
                        elif 'FX' in name_text:
                            # Remove the 'FX' prefix from the name
                            name_element.text = name_text.replace('_FX', '')
                            type_element = element.find("type")
                            if type_element is not None:
                                type_element.text = type_element.text.replace('Neumann', 'NormalTraction')
                            comp_element = element.find("component")
                            if comp_element is not None:
                                print('Removed component element %s' % comp_element.text)
                                element.remove(comp_element)

        # Save the modified XML to a new file or overwrite the existing one
        tree.write(outfile_name, encoding='ISO-8859-1', xml_declaration=True)
    except FileNotFoundError:
        print("Error: file %s is not found" % input_file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
   
