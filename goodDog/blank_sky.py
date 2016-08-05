#!/usr/bin/env python

 ###					 ###
### Blank Sky Backgrounds ###
 ###					 ###

# Organise blank sky work #

def bsky_organiser():

	os.system('cp reprojected_data/*reproj_clean.fits blank_sky') # This will copy all of the ####_reproj_clean.fits files to the blank sky folder

	# Get the background file #

def get_evt2():

	ID = obdsID_li[0]
	loca = subprocess.check_output(['acis_bkgrnd_lookup', '%s_reproj_clean.fits' % ID]) # This is a subprocess command, which captures the terminal output from the ciao background lookup and sets it = loca
	location = loca[:-1] # There is a newline at the end of loca variable, have to remove it before passing to os.system
	os.system("cp %s blank_sky/bkgevt2.fits" % location) # Copies the file to current directory and renames it
	os.system("dmcopy 'blank_sky/bkgevt2.fits[status=0]' blank_sky/bkgevt2_clean.fits")

# Add pointing header keywords to the background file #

def evt2_pointer(obsid):

	for obs in obsid:
		os.system("dmmakepar blank_sky/%s_reproj_clean.fits blank_sky/%s_event_header.par" % (obs, obs))
		os.system("grep _pnt blank_sky/%s_event_header.par > blank_sky/%s_event_pnt.par" % (obs, obs))
		os.system("cp blank_sky/bkgevt2_clean.fits blank_sky/%s_bkgevt2_notproj.fits" % obs) # Clone the clean background file into separate versions, one for each ObsID
	os.system("chmod +w blank_sky/*_bkgevt2_notproj.fits") # Make the clones writable
	for obs in obsid:
		os.system("dmreadpar blank_sky/%s_event_pnt.par 'blank_sky/%s_bkgevt2_notproj.fits[events]' clobber+" % (obs, obs)) # Migrate the pointing header keywords to the new clones

# While still in blank_sky, finding and copying aspect solution files over for reproject_events #

def aspect_sol(obsid):

	for obs in ID:
		os.system("punlearn reproject_events")
		asp_file = [os.path.basename(x) for x in glob.glob('%s/repro/*pcad*asol*' % obs)] # Captures only the basename of the file in the path and adds it in a list
		aspect = asp_file[0] # Assigns the file to a variable
		os.system("cp %s/repro/*asol*.fits blank_sky" % obs)
		os.system("reproject_events infile=blank_sky/%s_bkgevt2_notproj.fits outfile=blank_sky/%s_bkg_reproj_clean.fits aspect=blank_sky/%s match=blank_sky/%s_reproj_clean.fits random=0 verbose=5 clobber=yes" % (obs, obs, aspect, obs))
		del asp_file
		del aspect