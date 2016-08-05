#!/usr/bin/env python

 ###			   					   ###
### Finding the ccd_id from file header ###
 ###			   					   ###

 def ccd_id_finder(obsID):

	for obs in obsID:
		inter = int(obs)
		if 1000 <= inter < 10000: # Note that obsID's with #### have a (0) in front of the _repro
			ccd = dmkeypar("%s/repro/acisf0%s_repro_evt2.fits" % (obs, obs), keyword='CCD_ID', echo='True') # Get value of keyword 'CCD_ID', the ccd_id of the observation from broad_flux.fits
		elif 0 < inter < 1000:
			ccd = dmkeypar("%s/repro/acisf00%s_repro_evt2.fits" % (obs, obs), keyword='CCD_ID', echo='True')
		else:
			ccd = dmkeypar("%s/repro/acisf%s_repro_evt2.fits" % (obs, obs), keyword='CCD_ID', echo='True')
		ID = int(ccd) # Make the number an integer instead of a ciao.string
		ccd_id.append(ID) # stick to list for later

# Finding the start and stop times from dmlist #

def time_finder(obsid, ccd):

	ccd_count = 0
	for obs in obsid:
		the_list = subprocess.check_output(['dmlist', "reprojected_data/%s_background.fits[GTI%s]" % (obs, ccd[ccd_count]), 'data']) # Captures the time list output of dmlist
		ccd_count += 1 # Adds the next ccd_id index
		start = the_list[234:254] # Gets the start time from the first row
		stop = the_list[-21:-1] # Gets the stop time from the last row and deletes the /newline
		times.append(start)
		times.append(stop)