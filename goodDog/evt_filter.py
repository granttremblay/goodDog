#!/usr/bin/env python

 ###											 ###
### Filter the event lists for all of the obsID's ###
 ###											 ###

# If deflare was run #

def evt_list_filt(data):

	for obs in data:
		dmcopy(infile='reprojected_data/%s_efilter.fits[@%s_bkg_deflare.gti]' % (obs, obs), outfile='reprojected_data/%s_reproj_clean.fits' % obs, clobber='yes')

# In case deflare is skipped #

def evt_list_filt_nodeflare(data):

	for obs in data:
		dmcopy(infile='reprojected_data/%s_efilter.fits' % obs, outfile='reprojected_data/%s_reproj_clean.fits' % obs, clobber='yes')
