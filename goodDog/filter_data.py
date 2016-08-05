#!/usr/bin/env python

 ###																														  ###
### Filtering the reprojected files in energy space and extracting background only lightcurve by excluding cluster and sources ###
 ###																														  ###

# Filtering the files in energy space based on user input energies #

def espace_filt(obsid, ccd):

	nrgy1 = raw_input("Input minimum energy filter value: ") # Allows specification of energy filter values
	nrgy2 = raw_input("Input maximum energy filter value: ")
	ccd_count = 0
	for obs in obsid:
		print "Performing dmcopy step for obsID %s to make efilter.fits file" % obs
		dmcopy(infile='reprojected_data/%s_reproj_evt.fits[energy=%s:%s, ccd_id=%s]' % (obs, nrgy1, nrgy2, ccd[ccd_count]), outfile='reprojected_data/%s_efilter.fits' % obs, opt='all', clobber='yes') # dmcopy step to make efilter files
		ccd_count += 1

# Excluding cluster from the background #

def bkg_lightcurve(obsid):

	for obs in obsid:
		print "Performing dmcopy step for obsID %s to make background.fits file" % obs
		dmcopy(infile='reprojected_data/%s_efilter.fits[exclude sky=region(cluster.reg)]' % obs, outfile='reprojected_data/%s_background.fits' % obs, opt='all', clobber='yes') # make background.fits files