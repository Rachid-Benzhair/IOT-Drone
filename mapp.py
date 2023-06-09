import os

# Define the desired folder structure
folder_structure = {
    "K:\\IOT-Drone\\IOT-Drone": [
        "Arduino_Code\\drone_control",
        "Arduino_Code\\libraries\\Blynk",
        "Arduino_Code\\libraries\\ESP8266",
        "Blynk_App",
        "Hardware_Design\\Components_List.md",
        "Hardware_Design\\Drone_Frame_Design\\CAD_Files",
        "Hardware_Design\\Drone_Frame_Design\\Images",
        "Hardware_Design\\Wiring_Diagram",
        "Documentation\\Project_Presentation",
        "Documentation\\Project_Report",
        "LICENSE",
        "README.md"
    ]
}

for root, subdirs in folder_structure.items():
    # Create the root directory if it doesn't exist
    if not os.path.exists(root):
        os.makedirs(root)
    # Iterate through the subdirectories
    for subdir in subdirs:
        path = os.path.join(root, subdir)
        dir_path = os.path.dirname(path)
        # Create the parent directory of the file or folder if it doesn't exist
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        # Create the subdirectory or file if it doesn't exist
        if not os.path.exists(path):
            if path.endswith(".md"):
                with open(path, "w") as f:
                    pass
            else:
                os.makedirs(path)
                # Create a .gitkeep file in each folder
                with open(os.path.join(path, ".gitkeep"), "w") as f:
                    pass
