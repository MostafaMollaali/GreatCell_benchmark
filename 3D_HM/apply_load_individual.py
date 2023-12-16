from ogs6py import ogs
import os
import ogs6py
import numpy as np
import sys
from types import MethodType

# define method to be assigned to model, to replace a specific curve, given by name 
# (analogue to replace_parameter method)
def replace_curve(self, name=None, value=None, coords=None, parametertype=None, valuetag="values", coordstag="coords"):
    root = self._get_root()
    parameterpath = "./curves/curve"
    parameterpointer = self._get_parameter_pointer(root, name, parameterpath)
    self._set_type_value(parameterpointer, value, parametertype, valuetag=valuetag)
    self._set_type_value(parameterpointer, coords, parametertype, valuetag=coordstag)

def apply_load_curves(model, curve_name, coords, values):
    values2string = ' '.join(map(str, values))
    print(curve_name)
    model.replace_curve(name= curve_name, value=values2string, coords=coords)

def apply_top_load(model, F_top, coords, n_time_steps):
    F_top = [F_top] * n_time_steps
    values_F_top = ' '.join(map(str, F_top))
    model.replace_curve(name="TOP_SURFACE_DZ_CURVE",value=values_F_top, coords=coords)

def apply_all_load(input_file, output_file,  times_string, bag_load_values, column_swap = False):
    # swap columns 4 and 7, columns 5 and 6, respective.
    if column_swap == True:
        bag_load_values[:, [4, 7]] = bag_load_values[:, [7, 4]]
        bag_load_values[:, [5, 6]] = bag_load_values[:, [6, 5]]

    strip_load_values = bag_load_values.copy()

    ncols = strip_load_values.shape[1]
    for i in range(ncols):
        j = (i+1) % ncols
        strip_load_values[:, i] = 0.5 * (strip_load_values[:, i]
                                    + strip_load_values[:, j])  

    #print(bag_load_values)
    #print(strip_load_values)

    model = ogs.OGS(INPUT_FILE=input_file, PROJECT_FILE=output_file, MKL=True)
    model.replace_curve = MethodType(replace_curve, model)

    # Apply load curve
    for i in range(ncols):
       curve_name = "PEE_" + str(i+1) + "_SURFACE_CURVE"
       values = bag_load_values[:, i].tolist()
       print(values)
       apply_load_curves(model, curve_name, times_string, values) 
       curve_name = "DSS_" + str(i+1) + "_SURFACE_CURVE"
       values = strip_load_values[:, i].tolist()
       print(values)
       apply_load_curves(model, curve_name, times_string, values) 

    ntimes = strip_load_values.shape[0]
    apply_top_load(model, -12.e6, times_string, ntimes)
    model.write_input()

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

        times = "0.0 500"

        bag_load_values = -1.0e+6 * np.array(
                      [[3.0, 4.3, 5.6, 7.0, 7.0, 5.6, 4.3, 3.0],
                       [3.0, 4.3, 5.6, 7.0, 7.0, 5.6, 4.3, 3.0]])

        output_file = "great_cell_HM2_new_load_B.prj"
        apply_all_load(input_file, output_file, times, bag_load_values)

        bag_load_values = -1.0e+6 * np.array(
                      [[4.3, 5.6, 7.0, 7.0, 5.6, 4.3, 3.0, 3.0],
                       [4.3, 5.6, 7.0, 7.0, 5.6, 4.3, 3.0, 3.0]])
        output_file = "great_cell_HM2_new_load_C.prj"
        apply_all_load(input_file, output_file, times, bag_load_values)

        bag_load_values = -1.0e+6 * np.array(
                      [[5.6, 7.0, 7.0, 5.6, 4.3, 3.0, 3.0, 4.3],
                       [5.6, 7.0, 7.0, 5.6, 4.3, 3.0, 3.0, 4.3]])
        output_file = "great_cell_HM2_new_load_D.prj"
        apply_all_load(input_file, output_file, times, bag_load_values)

        bag_load_values = -1.0e+6 * np.array(
                      [[7.0, 7.0, 5.6, 4.3, 3.0, 3.0, 4.3, 5.6],
                       [7.0, 7.0, 5.6, 4.3, 3.0, 3.0, 4.3, 5.6]])
        output_file = "great_cell_HM2_new_load_E.prj"
        apply_all_load(input_file, output_file, times, bag_load_values)

        bag_load_values = -1.0e+6 * np.array(
                      [[7.0, 5.6, 4.3, 3.0, 3.0, 4.3, 5.6, 7.0],
                       [7.0, 5.6, 4.3, 3.0, 3.0, 4.3, 5.6, 7.0]])
        output_file = "great_cell_HM2_new_load_F.prj"
        apply_all_load(input_file, output_file, times, bag_load_values)

        print('The loads are applied successfully!')
    except FileNotFoundError:
        print("Error: file %s is not found" % input_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()






        
