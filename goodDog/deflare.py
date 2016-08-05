#!/usr/bin/env python

 ###		 ###
### Deflaring ###
 ###		 ###

def extract_flare(obsid, time):

	count = 1
	for obs in obsid: # Cycles through obsID's
		bin = raw_input("Input bin length (usually 200): ") # Gets bin length input each time a new obsID is used
		index1 = (count*2)-2 # Gets the start time index of the obsID
		index2 = (count*2)-1 # Gets the stop time index of the obsID
		start = time[index1] # Selects the start and stop times for the obsID being run
		stop = time[index2]
		count += 1 # Adds 1 to the count to continue formula ie. obsID number 3 will have count = 3, index1=4, and index2=5 which are its start and stop times in the times list
		print "Performing dmextract step for obsID %s" % obs
		dmextract(infile="reprojected_data/%s_background.fits[bin time=%s:%s:%s]" % (obs, start, stop, bin), outfile='reprojected_data/%s_background.lc' % obs, opt='ltc1', clobber='yes')
		deflare(infile='reprojected_data/%s_background.lc' % obs, outfile='reprojected_data/%s_bkg_deflare.gti' % obs, method='clean', plot='no', save='reprojected_data/%s_plot' % obs)
	flare_checker() # Passes to the checker

# Checks with user to confirm the binning amount #

def flare_checker():
	choice = raw_input("Is the binning what you wanted? (yes/no): ")
	for decision in choice:
		if choice == "yes":
			break
		elif choice == "no": # Loops infinitly if you keep hitting "no" until a desired bin is found.
			os.system('rm reprojected_data/*_bkg_deflare.gti')
			os.system('rm reprojected_data/*_background.lc')
			extract_flare(ordered_list, times)
			break
		else:
			choice = raw_input("Enter yes or no: ")