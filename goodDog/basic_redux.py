#!/usr/bin/env python

 ###			   				###
### Basic Chandra data reduction ###
 ###			   				###

# Reduce data to lvl 2 #

def lvl2_data(obsid):

	for obs in obsid: # For every obsID in the list, do the chandra_repro step below
		print "Performing chandra_repro step for obsID %s" % obs
		chandra_repro(indir='%s' % obs, outdir='%s/repro' % obs, verbose=5, cleanup='no') # Need to have the % variables next to where they appear, all words must be in quotations, and all elements must be comma separated

# Align observations to the same WCS space.  Create directories and open broad_flux.fits #

def WCS():

	os.system('mkdir reprojected_data')
	print "Performing reproject_obs step"
	reproject_obs(infiles='*/repro/*evt2.fits', outroot='reprojected_data/', verbose=5) # Reprojects the evt2.fits files of all obsIDs
	os.system('mkdir exposure_corrected_mosaic')
	print "Performing flux_obs step (may take some time...)"
	flux_obs(infiles='reprojected_data/*reproj_evt.fits', outroot='exposure_corrected_mosaic/', bands='broad,csc', bin=1, verbose=5) # Flux_obs step
	os.system('cp exposure_corrected_mosaic/broad_flux.img exposure_corrected_mosaic/broad_flux.fits') # Copies broad_flux.img to broad_flux.fits so I can view it in my DS9
	print "Create circular regions around the target and around a background portion of the image in DS9.  Save the target region as cluster.reg and the background region as background.reg.  Save both in /reprojected_data/.  Make sure to save the regions in ciao format."
	raw_input("Press enter to open DS9, then close DS9 once you have fininshed making the files...")
	os.system('ds9 broad_flux.fits')  # Opens broad_flux.fits in DS9 for making regions

# Waiting for the .region files to be saved #

def deep_space_9():
	
	raw_input("Press Enter to continue when the files have been saved...") # Allows a pause while the user creates the files
	reg_file_check()
	
# Checks reprojected_data/ for the .region files #

def reg_file_check(): # Checks with os.path.exists command

	if os.path.exists("reprojected_data/cluster.reg") == True:
		print "The file cluster.reg has been found"
	else:
		print "Please create cluster.reg in DS9 (save as ciao file) and save it to reprojected_data/"
		deep_space_9()
	if os.path.exists("reprojected_data/background.reg") == True:
		print "The file background.reg has been found"
	else:
		print "Please create background.reg in DS9 (save as ciao file) and save it to reprojected_data/"
		deep_space_9()
