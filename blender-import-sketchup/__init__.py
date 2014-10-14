
bl_info = {
    "name": "SketchUp Collada and KMZ format",
    "author": "Heikki Salo",
    "version": (1, 0, 0),
    "blender": (2, 70, 0),
    "location": "File > Import-Export",
    "description": "Import SketchUp .dae and .kmz files",
    "category": "Import-Export"
}

import imp
import bpy

from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper

class ImportSketchUp(bpy.types.Operator, ImportHelper):
    """Load a Google SketchUp .dae or .kmz file"""
    bl_idname = "import_scene.sketchup"
    bl_label = "Import"
    bl_options = {"PRESET", "UNDO"}

    filename_ext = ".kmz"
    filter_glob = StringProperty(
            default="*.kmz;*.dae",
            options={"HIDDEN"})

    fix_duplicate_faces = BoolProperty(
            name="Fix duplicate faces",
            description="Remove duplicate faces from imported objects. Can be slow.",
            default=True)

    tris_to_quads = BoolProperty(
            name="Triangles to quads",
            description="Convert triangles to quads.",
            default=False)

    add_parent = BoolProperty(
            name="Add a parent object",
            description="Add a parent root object for imported objects.",
            default=True)

    pack_images = BoolProperty(
            name="Pack images",
            description="Pack imported images into the .blend file.",
            default=True)

    def execute(self, context):
        from . import import_sketchup
        imp.reload(import_sketchup)

        keywords = self.as_keywords()
        return import_sketchup.load(self, context, **keywords)

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.prop(self, "fix_duplicate_faces")

        row = col.row()
        row.enabled = self.fix_duplicate_faces
        row.prop(self, "tris_to_quads")

        col.prop(self, "add_parent")
        col.prop(self, "pack_images")

def menu_func_import(self, context):
    self.layout.operator(ImportSketchUp.bl_idname, text="SketchUp (.kmz/.dae)")

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()
