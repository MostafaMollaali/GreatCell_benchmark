import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv
import math

pi = math.pi
#angle = np.array([0, 22.5, 45, 67.5, 90]) * pi/180
#mock_sn = 7 * (np.cos(angle)**2) + 3 * (np.sin(angle)**2)

angle = np.array([0, 22.5, 45, 67.5, 90]) * pi/180
mock_sn = 7 * (np.cos(angle)**2) + 3 * (np.sin(angle)**2)


labels = [r'$F$', r'$E$', r'$D$', r'$C$',  r'$B$']

def get_fracture_k_and_s_at_the_center(root_directory):
    # Define the directories
    directories = [root_directory + 'B',
                   root_directory + 'C',
                   root_directory + 'D',
                   root_directory + 'E',
                   root_directory + 'F']

    k_f_all = []
    k_sn_all = []
    
    # Loop through the directories
    for directory in directories:
        # Find the pvd file
        for file in os.listdir(directory):
            if file.endswith('.pvd'):
                pvd_file = os.path.join(directory, file)
                break
    
        # Open the pvd file
        tree = ET.parse(pvd_file)
        root = tree.getroot()
    
        # Get the last DataSet tag
        last_dataset = root.findall('.//DataSet')[-1]
    
        # Get the 'file' attribute of the last DataSet tag
        file_attribute = last_dataset.attrib['file']
    
        print(f"The 'file' attribute of the last DataSet tag in {pvd_file} is {file_attribute}.")
    
        file_name = os.path.join(directory, file_attribute)
        mesh = pv.read(file_name)
        target_mat_id = 0
        matIDs = mesh.cell_data["MaterialIDs"]
        submesh = mesh.extract_cells(np.where(matIDs == target_mat_id)[0])
        center_p_id = submesh.find_closest_point((0.02, 0.0, 0.11))
        k_f = mesh.point_data["fracture_permeability"][center_p_id]
        k_f_all.append(k_f)
        print(f'The fracture permeability in the center is {k_f}')
        s_f = mesh.point_data["fracture_stress"][center_p_id]
        print(f'The normal stress on the fracture is {s_f[2]}')
        k_sn_all.append(s_f[2])

    return np.array(k_f_all) * 1.e+11, -np.array(k_sn_all) * 1.e-6


# high fracture stiffness
root_output_directory = '../output_new_load/high_kn/'
k, sn = get_fracture_k_and_s_at_the_center(root_output_directory)
   
root_output_directory = '../output_new_load/low_kn/'
k_l, sn_l = get_fracture_k_and_s_at_the_center(root_output_directory)
    
# Plotting
plt.rcParams['figure.figsize'] = [12, 12]
plt.plot(mock_sn, k, marker='o', linestyle = 'dashed', label=r'$k_{nn}=k_{tt}=100$ GPa/m')
plt.plot(mock_sn, k_l, marker='*', linestyle = 'dashed', label=r'$k_{nn}$=10 GPa/m, $k_{tt}=4$ GPa/m')
for label, x, y in zip(labels, mock_sn, k):
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(10,-20), ha='center')

#plt.title('Your Data Plot')
plt.xlabel('Normal fracture stress from the far stress state [MPa]')
plt.ylabel(r'Fracture permeabilty [$10^{-11}$ m$^2$]')
plt.legend()

plt.show()


plt.plot(mock_sn, sn, marker='o', linestyle = 'dashed', label=r'$k_{nn}=k_{tt}=100$ GPa/m')
plt.plot(mock_sn, sn_l, marker='*', linestyle = 'dashed', label=r'$k_{nn}$=10 GPa/m, $k_{tt}=4$ GPa/m')
for label, x, y in zip(labels, mock_sn, sn):
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center')

print(sn)    
print(sn_l)
print(mock_sn)

plt.xlabel('Normal fracture stress from the far stress state [MPa]')
plt.ylabel(r'Calculated normal fracture stress [MPa]')
plt.legend()
plt.show()

