# mineways-importer

The mineways-importer is a Python script designed to run in Blender 2.91 after importing a 3D Minecraft world from [Mineways](https://github.com/erich666/Mineways "Mineways on Github") and fix all the materials and textures automatically. When running the script Blender will
* fix blurry textures
* set default specular for all materials
* set default roughness for all materials
* create a bump node for every material (optional)

## How to use

__Step 1__<br />
Import the .obj file of your Mineways export in a new blend file.
<!-- ![Screenshot of object import in Blender](screenshots/object_import.PNG?raw=true "Object Import") -->
<br />

__Step 2__<br />
Switch to the scripting tab of Blender.
<!-- ![Screenshot of scripting tab in Blender](screenshots/scripting_tab.PNG?raw=true "Switch to Scripting Tab") -->
<br />

__Step 3__<br />
Open the [mineways_importer.py](mineways_importer.py) script or create a new text file and paste the contents of the script inside it.
<br />

__Step 4__<br />
Run the script
Press run to execute the program and fix the materials automatically. Done!
<!-- ![Screenshot of executing the script in Blender](screenshots/run_script.PNG?raw=true "Run the script") -->
<br />

_Info: Toggle the system console to see the output._
