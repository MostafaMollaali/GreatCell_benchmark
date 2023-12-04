import pyvista as pv
import numpy as np
import sys

def main():
    if "--help" in sys.argv:
        print("This script removes line cell vtu data.")
        print("Usage: python remove_line_cell_of_vtu.py <input_file>"
              " <output_file>\n"
              "If <output_file> is not given, the input file will be overriden."
              )
        return

    if len(sys.argv) < 2:
        print("Usage: python remove_line_cell_of_vtu.py <input_file>"
              " <output_file>\n"
              "If <output_file> is not given, the input file will be overriden."
              )
        return

    input_file_name = sys.argv[1]

    output_file_name = input_file_name if len(sys.argv) == 2 else sys.argv[2] 

    try:
        mesh = pv.UnstructuredGrid(input_file_name)

        print(mesh, mesh.array_names)

        if ("Material_Group" not in mesh.array_names):
            print("Not found Material_Group array. Do nothing.")
            return
        else:
            mesh.rename_array("Material_Group", "MaterialIDs")
            if ("X" in mesh.array_names):
                del mesh.point_data["X"]
            if ("Y" in mesh.array_names):
                del mesh.point_data["Y"]
            if ("Z" in mesh.array_names):
                del mesh.point_data["Z"]

            # Get the cell types using get_cell_type method
            cell_types = mesh.celltypes

            #print(cell_types)

            # Find the indices of the line cells (VTK_LINE)
            line_cell_indices = np.where(cell_types == 3)[0]

            if len(line_cell_indices) > 0:
                mat_IDs = mesh.cell_data["MaterialIDs"]
                moved_cell_mat_id = mat_IDs[line_cell_indices[0]]

                # Remove line cells
                mesh_cleaned = mesh.remove_cells(line_cell_indices)

                # Optionally clean up the mesh
                mesh_cleaned_cleaned = mesh_cleaned.clean()
                mat_IDs = mesh_cleaned_cleaned.cell_data["MaterialIDs"]
                for i, mat_id in enumerate(mat_IDs):
                    if mat_id > moved_cell_mat_id:
                        mat_IDs[i] = mat_id - 1

                mesh_cleaned_cleaned.cell_data["MaterialIDs"] = mat_IDs
                mesh_cleaned_cleaned.save(output_file_name)

    except FileNotFoundError:
        print("Error: file %s is not found" % input_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()
