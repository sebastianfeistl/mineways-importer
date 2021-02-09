import bpy

######################################### CONFIGURATION ##############################################

SHARP_TEXTURES = True # fix image texture interpolation
GENERATE_BUMP_NODES = False # create bump nodes for every material

DEFAULT_BUMP_STRENGTH = 0.1
DEFAULT_SPECULAR = 0.5
DEFAULT_ROUGHNESS = 0.4
WATER_ROUGHNESS = 0.02

######################################################################################################
        
def fix_all_materials():
    """
        Loops through all materials and changes their nodes automatically.
    """
    
    for i in range(0, len(bpy.data.materials)):
        
        mat = bpy.data.materials[i]
        
        # make sure it uses nodes
        if mat.use_nodes == False:
            print("[{}] {} does not use nodes.".format(i, bpy.data.materials[i].name))
            continue
        
        # define aliases
        tree = mat.node_tree
        nodes = tree.nodes
        
        # fix image textures
        if SHARP_TEXTURES:
            fix_interpolation(nodes)
        
        principled = nodes["Principled BSDF"]
        
        # set default principled
        principled.inputs['Specular'].default_value = DEFAULT_SPECULAR
        principled.inputs['Roughness'].default_value = DEFAULT_ROUGHNESS
        
        # set custom materials
        if mat.name == 'Stationary_Water':
                principled.inputs['Roughness'].default_value = WATER_ROUGHNESS
        elif mat.name == 'Glass':
                print(".")
        
        # generate bump nodes
        if GENERATE_BUMP_NODES:
            create_bump_node(tree)
        
        print("[{}] {} has been fixed.".format(i, bpy.data.materials[i].name))
    

def fix_interpolation(nodes):
    """
        Sets the interpolation of all image texture nodes to Closest.
        
        :param tree: The nodes.
    """
    
    for node in nodes:
        if node.bl_rna.identifier == 'ShaderNodeTexImage':
            node.interpolation = 'Closest'
    

def create_bump_node(tree):
    """
        Create a new bump node (if it does not exist yet) and add it to the material.
        
        :param tree: The node tree.
    """
    
    # define aliases
    nodes = tree.nodes
    bump = nodes.get("Bump", None)
    
    # replace old bump node
    if bump is not None:
        nodes.remove(bump)
    
    # get other nodes
    image = nodes.get("Image Texture", None)
    principled = nodes["Principled BSDF"]
    
    if image is None:
        return
    
    # add bump node
    bump = nodes.new('ShaderNodeBump')
    link_bump_to_image_node(tree, bump, image, principled)
    

def link_bump_to_image_node(tree, bump, image, principled):
    """
        Link the specified nodes together.
        
        :param tree: The node tree.
        :param bump: The bump node.
        :param image: The image texture node.
        :param principled: The principled node.
    """
    
    # set default strength
    bump.inputs[0].default_value = DEFAULT_BUMP_STRENGTH
    
    # link the nodes
    tree.links.new(bump.inputs[2], image.outputs[0])
    tree.links.new(bump.outputs[0], principled.inputs[20])


def print_all_node_names():
    """
        Prints all shader node names to the console.
    """
    
    nodes = [node.bl_rna.identifier for node in bpy.types.ShaderNode.__subclasses__()]
    for node in nodes:
        print(node)

# run
fix_all_materials()
print("\nPatching completed.")