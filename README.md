# mineways-importer

The mineways-importer is a Python script designed to run in Blender after importing a 3D Minecraft world from [Mineways](https://github.com/erich666/Mineways "Mineways on Github") and fix all the materials and textures automatically. When running the script Blender will
* fix blurry textures
* set default specular for all materials
* set default roughness for all materials
* create a bump node for every material (optional)

## How to use

You simply need to import the .obj of your Mineways export in a fresh blend file and load (or copy and paste) the script to your Blender scripting tab and press run. When toggling the system console you can see the output.
