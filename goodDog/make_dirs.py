#!/usr/bin/env python

 ###			   			 ###
### Make directories for work ###
 ###			   			 ###

def mkdir(directory):

	os.chdir(directory)
	os.system('mkdir reprojected_data')
	os.system('mkdir exposure_corrected_mosaic')
	os.system('mkdir blank_sky')
	os.system('mkdir contbin')