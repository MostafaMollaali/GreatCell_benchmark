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

def apply_F_to_BAG(model,F,n,coords='0 1200.0', value_mult = [1,1]):
    F_v = [-x*F for x in value_mult]
    values_F_v = ' '.join(map(str, F_v))
    model.replace_curve(name="BAG_"+str(n)+"_SURFACE_CURVE",value=values_F_v, coords=coords)
    
def apply_F_to_STRIP(model,F_a, F_b,n,coords='0 1200.0', value_mult = [1,1]):
    F = 0.5*(F_a+F_b)
    F_v = [-x*F for x in value_mult]
    values_F_v = ' '.join(map(str, F_v))
    model.replace_curve(name="STRIP_"+str(n)+"_SURFACE_CURVE",value=values_F_v, coords=coords)
    
def apply_F_to_TOP(model,F_top,coords='0 1200.0', value_mult = [1,1]):
    F_top = [x*F_top for x in value_mult]
    values_F_top = ' '.join(map(str, F_top))
    model.replace_curve(name="TOP_SURFACE_DZ_CURVE",value=values_F_top, coords=coords)
    
def apply_F_to_all(model,F_values,t_coords='0 1200.0', value_mult = [1,1]):
    # apply given F_values as BC on BAG and mean values on STRIP in between, 
    # with given time coordinates t_coords in given loading steps value_mult
    # F_values for example: [10e6,0,0,0,5e6,0,0,0,10e6,0,0,0,5e6,0,0,0]
    for i in range(1,17):
        apply_F_to_BAG(model,F_values[i-1],i,t_coords,value_mult)
        apply_F_to_STRIP(model,F_values[i-1], F_values[i%16],i,t_coords,value_mult)

# load_values: PEE1, PEE2, PEE3, PEE4, PEE5, PEE6, PEE7, PEE8,
def apply_load(input_file, output_file, load_values):
    model11_ = ogs.OGS(INPUT_FILE=input_file, PROJECT_FILE=output_file, MKL=True)
    model11_.replace_curve = MethodType(replace_curve, model11_)

    size = 16
    loads = [0] * size
    #apply_F_to_all(model11_, loads)        

    for i in range(8):
        loads[i] = load_values[i]
        loads[8+i] = load_values[i]
        
    # PEE1 PEE2, PEE3, PEE4, PEE5, PEE6, PEE7, PEE8, PEE1a, PEE2a PEE3a, PEE4a, PEE5a, PEE6a, PEE7a, PEE8a
    apply_F_to_all(model11_, loads)
    apply_F_to_TOP(model11_,-10.e6)
    model11_.write_input()

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
        load_values = [0] * 8
        output_file_name_base = "great_cell_HM2_test"
        # Case B
        load_values[0] = 8.8e6
        load_values[1] = 8.8e6
        load_values[2] = 9.2e6
        load_values[3] = 9.0e6
        load_values[4] = 8.9e6
        load_values[5] = 8.7e6
        load_values[6] = 9.3e6
        load_values[7] = 8.7e6
        apply_load(input_file, output_file_name_base + "_B.prj", load_values)

        # Case C
        load_values[0] =  7.1e6
        load_values[1] =  6.3e6
        load_values[2] =  6.3e6
        load_values[3] =  6.9e6
        load_values[4] =  7.9e6
        load_values[5] =  8.7e6
        load_values[6] =  8.8e6
        load_values[7] =  7.8e6
        apply_load(input_file, output_file_name_base + "_C.prj", load_values)

        # Case D
        load_values[0] = 7.7e6
        load_values[1] = 8.7e6
        load_values[2] = 8.7e6
        load_values[3] = 7.7e6
        load_values[4] = 7.3e6
        load_values[5] = 6.3e6
        load_values[6] = 6.3e6
        load_values[7] = 6.6e6
        apply_load(input_file, output_file_name_base + "_D.prj", load_values)

        # Case E
        load_values[0] = 7.2e6
        load_values[1] = 8.2e6
        load_values[2] = 8.7e6
        load_values[3] = 8.7e6
        load_values[4] = 7.8e6
        load_values[5] = 6.8e6
        load_values[6] = 6.3e6
        load_values[7] = 6.2e6
        apply_load(input_file, output_file_name_base + "_E.prj", load_values)

        # Case F
        load_values[0] = 6.2e6
        load_values[1] = 7.2e6
        load_values[2] = 8.3e6
        load_values[3] = 8.7e6
        load_values[4] = 8.7e6
        load_values[5] = 7.7e6
        load_values[6] = 6.9e6
        load_values[7] = 6.3e6
        apply_load(input_file, output_file_name_base + "_F.prj", load_values)

        # Case G
        load_values[0] = 6.2e6
        load_values[1] = 6.2e6
        load_values[2] = 7.3e6
        load_values[3] = 8.1e6
        load_values[4] = 8.7e6
        load_values[5] = 8.7e6
        load_values[6] = 7.8e6
        load_values[7] = 6.7e6
        apply_load(input_file, output_file_name_base + "_G.prj", load_values)

        # Case H
        load_values[0] = 6.8e6
        load_values[1] = 6.4e6
        load_values[2] = 6.9e6
        load_values[3] = 7.5e6
        load_values[4] = 8.2e6
        load_values[5] = 8.7e6
        load_values[6] = 8.3e6
        load_values[7] = 7.2e6
        apply_load(input_file, output_file_name_base + "_H.prj", load_values)

        print('The loads are applied successfully!')
    except FileNotFoundError:
        print("Error: file %s is not found" % input_file)
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()






        
