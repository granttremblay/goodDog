#!/usr/bin/env python

 ###			   ###
### Contour Binning ###
 ###			   ###

# Creating directory for work #

def contbin_dir():

	os.system("cp reprojected_data/merged_evt.fits contbin/") # Copies merged-evt.fits over from reprojected_data to contbin folder
	print "Make a box region around the target to obtain the x and y coordinates to input (physical coordinates in ds9)..."
	print "For now, write these coordinates down. Make sure to save the region as contbin_mask.reg (ciao format) in the contbin folder in this project's parent directory"
	os.system("ds9 merged_evt.fits") # Opens merged_evt.fits in ds9
	
# Define coordinate boundaries #

def coordinate_inp():

	xmin = raw_input("Input the minimum x coordinate (physical): ")
	xmax = raw_input("Input the maximum x coordinate (physical): ")
	ymin = raw_input("Input the minimum y coordinate (physical): ")
	ymax = raw_input("Input the maximum y coordinate (physical): ")
	coor_values.extend([xmin, xmax, ymin, ymax]) # Adds all of the entered values to the list
	minmax_check(coor_values)
	return coor_values

# Check the min / max values #

def minmax_check(value):

	for val in value:
		if value[0] < value[1]: # Checks if the max / min values have been correctly entered (that the max is not smaller than the min)
			pass
		else:
			print "The min / max values were entered incorrectly, please enter them again"
			del coor_values[:]
			coordinate_inp()
			break
		if value[2] < value[3]:
			pass
		else:
			print "The min / max physical coordinate values were entered incorrectly, please enter them again"
			del coor_values[:]
			coordinate_inp()
			break

# Define energy boundaries #

def energy_inp():

	nrgy1 = raw_input("Input minimum energy filter value: ")
	nrgy2 = raw_input("Input maximum energy filter value: ")
	energy_li.extend([nrgy1, nrgy2])
	nrgy_check(energy_li)
	return energy_li

# Checks the energy input values #

def nrgy_check(value):

	for val in value:
		if value[0] < value[1]:
			pass
		else:
			print "The min / max energy filter values were entered incorrectly, please enter them again"
			del energy_li[:]
			energy_inp()
			break

# Creating the region for contbinning work #

def reg_creator(energy, coor_values): # DS9 closes before this step ??

	raw = energy + coor_values
	minmaxnrgy_check(energy_li, coor_values)
	os.system("dmcopy 'contbin/merged_evt.fits[energy=%s:%s][bin x=%s:%s:1, y=%s:%s:1]' contbin/contbin_input.fits clobber=yes" % tuple(raw))

# Asks if inputs are good #

def minmaxnrgy_check(energy, coor_values):

	raw = energy + coor_values
	print "min_energy:%s max_energy:%s min_x:%s max_x:%s min_y:%s max_y:%s" % tuple(raw)
	choice = raw_input("Are these the values you wanted? (yes/no): ")
	for decision in choice:
		if choice == "yes":
			break
		elif choice == "no":
			del coor_values[:]
			del energy_li[:]
			coordinate_inp() # Goes back to coordinate_inp() function
			energy_inp() # Goes back to function
			reg_creator(energy_li, coor_values)
			break
		else:
			choice = raw_input("Enter yes or no: ")

# Checks for contbin_mask.reg #

def contbinmask_file_check(): # Checks for the .reg files, only runs twice as of now

	if os.path.exists("contbin_mask.reg") == True:
		print "The file has been found"
	else:
		print "Please create contbin_mask.reg in DS9 (save as ciao file to the contbin folder in the project directory)"
		raw_input("Press enter once the file has been made...")
		contbinmask_file_check()

# Farith step and preparation to make region files #

def farith():

	###### Need heasoft - maybe something to check that it is installed and need a way to call the program, also need it for contbin ?? ######
	os.system("farith contbin_input.fits 0 temp.fits MUL")
	os.system("farith temp.fits 1 allones.fits ADD")
	os.system("rm temp.fits")
	dmcopy(infile='allones.fits[sky=region(contbin_mask.reg)][opt full]' outfile='mask.fits')
	os.system("rm allones.fits")
	sn = raw_input("Input signal to noise (sn): ")
	const_val = raw_input("Input constrainval value (e.g. 2.0): ")
	os.system("contbin --mask=mask.fits --sn=%s --smoothsn=3 --constrainfill --constrainval=%s contbin_input.fits" % (sn, const_val))
