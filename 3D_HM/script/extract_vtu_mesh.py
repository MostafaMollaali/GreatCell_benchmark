from ogs6py import ogs
import os
import ogs6py
import numpy as np
import sys
import pyvista as pv

from types import MethodType

def main():
    if "--help" in sys.argv:
        print("This script applies the specified loads to the HM2 test")
        print("Usage: apply_load.py <input_file>")
        return

    if len(sys.argv) != 2:
        print("Usage: apply_load.py <input_file>")
        return

    input_file = sys.argv[1]

    try:

        mesh = pv.read(input_file)

        # Specify the target cell ID value for extraction
        target_mat_id = 0
        matIDs = mesh.cell_data["MaterialIDs"]
        submesh = mesh.extract_cells(np.where(matIDs == target_mat_id)[0])
        #submesh.plot(show_edges=True)
        submesh.save("test.vtu")

        print('The frature mesh is extracted successfully!')
    except FileNotFoundError:
        print("Error: file %s is not found" % input_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()






        
