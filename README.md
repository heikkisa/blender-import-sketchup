Blender Google SketchUp importer
================================

This is an unofficial addon to [Blender](http://www.blender.org/) (2.70 and up) which imports .dae and .kmz files created by [Google SketchUp](http://www.sketchup.com/) and is also designed to be used with models from [3D Warehouse](https://3dwarehouse.sketchup.com/). Because both of those formats are basically Collada (.dae) files this addon uses the default Blender Collada importer under the hood, but does some useful additional processing to the imported objects.

If you are having problems that are not mentioned in the *Troubleshooting*-section or in the [existing issues](https://github.com/heikkisa/blender-import-sketchup/issues) feel free to open a new issue. Remember to provide any files etc. that you are having problems with and your Blender version.

Download
--------

Use the "Download ZIP"-button on the GitHub. You can also directly copy and paste the actual [import script](src/import_sketchup.py) to your machine.

Installation
------------

Unzip the downloaded archive and install the importer in Blender by selecting

 - User Preferences... -> Addons -> Install from File...

Select the *import_sketchup.py* file you have downloaded. The importer should then be listed in the **Import-Export** section. Remember to enable it and also save the settings if you want to keep it enabled after restarting Blender.

After enabling it you should see an entry "File -> Import -> SketchUp (.kmz/.dae)" in the Blender menu.

If you are having trouble check the Blender documentation about [installing addons](http://wiki.blender.org/index.php/Doc:2.6/Manual/Extensions/Python/Add-Ons).

Importer Options
----------------

**Fix duplicate faces**

Attempts to remove duplicate faces. This is important because otherwise it can lead to some pretty nasty z-fighting which usually causes black shadow "acne" or artifacts when rendering the scene with lights. Most of the time this should be left enabled. This option is not very optimized so it might take a while when importing large or complex models.

**Fix duplicate vertices**

Attempts to remove duplicate vertices. This tries to find faces that don't actually share vertices but still form duplicated geometry. This can be extremely slow on large models. You can open the Blender System Console before running the import script and see some progress feedback while the import is running.

**Add a parent object**

When importing objects they will be added as children to a new root object. This makes the Outliner-view much more usable after importing models that might contain hundreds of separate objects. It also makes manipulating the imported objects easier because you only have to select one object when you want to translate or manipulate the imported model.

**Pack images**

Packs imported images inside the .blend-file instead of loading them from the file system. Increases the saved file size, but makes the .blend-files more "robust" (you can move and share them without worrying about the file references going invalid etc.).

Troubleshooting
---------------

The grim fact is that 3D model exporters and importers can be quite unreliable when working together and SketchUp and Blender are not exceptions in this. Here are listed some of the problems you might encounter when importing models.

**1. Some objects are missing from the imported scene**

When you export models from SketchUp you should usually select them all (Edit -> Select All) and *Explode* (Edit -> Component -> Explode) them before exporting. Importantly some objects might have to be exploded multimple times before they are exported in a reasonable way. I usually explode everything once, then export and import the results into Blender. If I see that something important is missing I explode those missing objects again in the SketchUp and do a new export. Then I repeat that until everything looks good enough or something goes horribly wrong. Try not to explode objects any more than you have to, otherwise the scene triangle count can increase a lot without any visible benefits. 

**2. Some faces have lost their textures**

Happens occasionally, try to enable "Fix duplicate vertices". One workaround is to select all faces that should be textured and texture map them again. If the surface is large and texture is not very complex it is sometimes enough to unwrap them all and scale the texture coordinates until it looks reasonable.

**3. Some faces have wrong material**

Happens occasionally, try to enable "Fix duplicate vertices". Usually it is easiest to use the face selection mode, select invalid faces and assign the correct material by hand. This might have messed up the face texture coordinates in which case you might have to remap those faces. If you are feeling lazy you could select all faces and then apply the same solution as to problem 2 (unwrap all).

**4. Some models import correctly, some look terrible**

Depending from SketchUp version and objects some models might import without a problem while some will not look that good or don't import anything at all. There are many moving parts involved so it can be quite hard to figure out what causes the issues. Sometimes older models downloaded from the 3D Warehouse work better after loading them into a new version of SketchUp and exporting them from there, so pay attention to the SketchUp version that was used to export the model.

**5. Importing is slooooow**

The option to fix duplicate faces can take some time, it is not very optimized (feel free to contribute improvements). Also importing into a scene that has a lot of existing stuff in it is slower. One good way is to import big models into a new, empty .blend-file. You can save this to a new .blend-file and use Blender "File -> Append" functionality in your other files to link to that object. I tend to have a collection of "component" .blend-files which contain common models which I then append into the actual scenes that I want to render.
