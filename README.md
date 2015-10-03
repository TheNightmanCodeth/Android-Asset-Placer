# Android Asset Placer
A python script to move images from archives made with Android Asset Studio into their correct directories.

# Usage (Not ubuntu)
>python assetplacer.py -a '/path/to/ic_archive.zip' -p '/path/to/project' -o

* -a path to zip
* -p path to project
* -o use for everything except launcher icons
* -i use instead of -o for launcher icons
* -w use to move the web-hi-res image (If you chose to generate one) to your home (~/) folder
* -d use to delete the archive when done 

# Installation (Ubuntu)
> sudo add-apt-repository ppa:joyod3/androidassetplacer

> sudo apt-get update

> sudo apt-get install assetplacer

# Usage (Ubuntu)
> assetplacer -a '/path/to/ic_archive.zip' -p '/path/to/project/' -o

* -a path to zip
* -p path to project
* -o use for everything except launcher icons
* -i use instead of -o for launcher icons
* -w use to move the web-hi-res image (If you chose to generate one) to your home (~/) folder
* -d use to delete the archive when done

For example, If you had a zip called ic_launcher.zip in your home directory, your project path is ~/AndroidStudioProjects/Highdeas/, you generated the web-hi-res version of your icon, and you want to delete the archive (ic_launcher.zip) when finished, this is what you would run:
> assetplacer -a '~/ic_launcher.zip' -p '~/AndroidStudioProjects/Highdeas/' -i -w -d
