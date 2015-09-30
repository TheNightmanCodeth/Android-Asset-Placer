#Android Asset Placer
A python script to move images from archives made with Android Asset Studio into their correct directories.

#Usage
python assetplacer.py -a '/path/to/ic_archive.zip' -p '/path/to/project' -o

* -a path to zip
* -p path to project
* -o use for everything except launcher icons
* -i use instead of -o for launcher icons
* -w use to move the web-hi-res image (If you chose to generate one) to your home (~/) folder
* -d use to delete the archive when done 