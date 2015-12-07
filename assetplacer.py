#!/usr/bin/env python
import sys
import os
import argparse

def main(argv):
	dirName = "drawable"
	zipdir = None
	extractTo = "app"

	#handle arguments and set variables
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--icon', action='store_true', help='for use with launcher icons. If you selected Launcher icons in asset studio, use -i. This is used for archives that contain /res/mipmap-xxxxx',required=False)
	parser.add_argument('-o', '--other', action='store_true', help='for use with generic images. If you selected generic icons in asset studio, use -o. This is used for archives that contain /res/drawable-xxxxx', required=False)
	parser.add_argument('-p', '--project', help='your project directory. ie. assetplacer -p ~/AndroidStudioProjects/app_name/', required=True)
	parser.add_argument('-a', '--archive', help='the path to your archive. ie. assetplacer -a ~/ic_image.zip', required=True)
	parser.add_argument('-w', '--web', action='store_true', help='If you generated the web hi-res version of your image, this flag will move it to the specified directory', required=False)
	parser.add_argument('-d', '--delete', action='store_true', help='If you want the archive deleted at the end, use -d')
	args = vars(parser.parse_args())

	#Set directory variables
	zipdir = args['archive']
	projDir = args['project']

	#Set variables for directories. Icons are placed in ~/project/(mobile, app, or wear)/src/main/res/mipmap-xxxxx, and other would be placed in ~/project/mobile/src/main/res/drawable-xxxxx
	if args['icon']:
		dirName = 'mipmap'
	elif args['other']:
		dirName = 'drawable'
	else:
		print 'Missing -i or -o argument. Use -h for usage'
		sys.exit()

	#If zip directory or project directory is missing we can't do anything
	if zipdir is None:
		print "ERROR: Required argumnent -a missing"
		usage()

	if projDir is None:
		print "ERROR: Required argument -p missing"
		usage()

	if os.path.exists("%s/mobile/" %(projDir)):
		print "mobile"
		extractTo = 'mobile'

	#Make a temporary directory to extract the zip. Will be deleted later
	print 'Making temporary directory...'
	os.system('mkdir ~/assetplacer_temp/')
	os.system('unzip %s -d ~/assetplacer_temp/' %(zipdir))

	#Make sure the path exists. Sometimes a project directory won't have a drawable-xxxxx folder. I'm pretty sure they all have the mipmap dirs but we'll check for those too just in case
	print 'Making sure directories exist...'
	if os.path.exists("%s/%s/src/main/res/%s-hdpi/" %(projDir, extractTo, dirName)):
		print 'Moving hdpi...'
		os.system('cp ~/assetplacer_temp/res/%s-hdpi/* %s/%s/src/main/res/%s-hdpi/' %(dirName, projDir, extractTo, dirName))
	else:
		#The directory isn't there, so we have to create it before we move anything
		print 'Making drawable-hdpi directory and moving files...'
		os.system('mkdir %s/%s/src/main/res/%s-hdpi/' %(projDir, extractTo, dirName))
		os.system('cp ~/assetplacer_temp/res/%s-hdpi/* %s/%s/src/main/res/%s-hdpi/' %(dirName, projDir, extractTo, dirName))

	if os.path.exists("%s/%s/src/main/res/%s-mdpi/" %(projDir, extractTo, dirName)):
		print 'Moving mdpi...'
		os.system('cp ~/assetplacer_temp/res/%s-mdpi/* %s/%s/src/main/res/%s-mdpi/' %(dirName, projDir, extractTo, dirName))
	else:
		#The directory isn't there, so we have to create it before we move anything
		print 'Making drawable-mdpi directory and moving files...'
		os.system('mkdir %s/%s/src/main/res/%s-mdpi/' %(projDir, extractTo, dirName))
		os.system('cp ~/assetplacer_temp/res/%s-mdpi/* %s/%s/src/main/res/%s-mdpi/' %(dirName, projDir, extractTo, dirName))

	if os.path.exists("%s/%s/src/main/res/%s-xhdpi/" %(projDir, extractTo, dirName)):
		print 'Moving xhdpi...'
		os.system('cp ~/assetplacer_temp/res/%s-xhdpi/* %s/%s/src/main/res/%s-xhdpi/' %(dirName, projDir, extractTo, dirName))
	else:
		#The directory isn't there, so we have to create it before we move anything
		print 'Making drawable-xhdpi directory and moving files...'
		os.system('mkdir %s/%s/src/main/res/%s-xhdpi/' %(projDir, extractTo, dirName))
		os.system('cp ~/assetplacer_temp/res/%s-xhdpi/* %s/%s/src/main/res/%s-xhdpi/' %(dirName, projDir, extractTo, dirName))

	if os.path.exists("%s/%s/src/main/res/%s-xxhdpi/" %(projDir, extractTo, dirName)):
		print 'Moving xxhdpi...'
		os.system('cp ~/assetplacer_temp/res/%s-xxhdpi/* %s/%s/src/main/res/%s-xxhdpi/' %(dirName, projDir, extractTo, dirName))
	else:
		#The directory isn't there, so we have to create it before we move anything
		print 'Making drawable-xxhdpi directory and moving files...'
		os.system('mkdir %s/%s/src/main/res/%s-xxhdpi/' %(projDir, extractTo, dirName))
		os.system('cp ~/assetplacer_temp/res/%s-xxhdpi/* %s/%s/src/main/res/%s-xxhdpi/' %(dirName, projDir, extractTo, dirName))

	if os.path.exists("%s/%s/src/main/res/%s-xxxhdpi/" %(projDir, extractTo, dirName)):
		print 'Moving xxxhdpi...'
		os.system('cp ~/assetplacer_temp/res/%s-xxxhdpi/* %s/%s/src/main/res/%s-xxxhdpi/' %(dirName, projDir, extractTo, dirName))
	else:
		#The directory isn't there, so we have to create it before we move anything
		print 'Making drawable-xxxhdpi directory and moving files...'
		os.system('mkdir %s/%s/src/main/res/%s-xxxhdpi/' %(projDir, extractTo, dirName))
		os.system('cp ~/assetplacer_temp/res/%s-xxxhdpi/* %s/%s/src/main/res/%s-xxxhdpi/' %(dirName, projDir, extractTo, dirName))

	#If the -w argument was passed we need to move the web-hi-res version into the project root
	if args['web']:
		print 'Moving web-hi-res to home directory...'
		os.system('cp ~/assetplacer_temp/*.png %s' %(projDir))

	#Delete the temporary directory
	print 'Deleting temporary directory...'
	os.system('rm -rf ~/assetplacer_temp')

	#If the -d argument was passed, we want to delete the archive now.
	if args['delete']:
		print 'Deleting archive...'
		os.system('rm %s' %(zipdir))
	pass

if __name__ == "__main__":
    main(sys.argv)
