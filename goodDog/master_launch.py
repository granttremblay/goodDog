#!/usr/bin/env python

 ###			   						  ###
### By Dominic Eggerman and Grant Tremblay ###
 ###			   						  ###

### Imports ###

import make_dirs
import obsID_select #1
import basic_redux #2
import info_finder #3
import filter_data #4
import deflare #5
import evt_filter #6
import blank_sky #7
import make_binmap #8

### Lists ###

#directory
obsID_li = [] #1
ccd_id = [] #3
times = [] #3
coor_values = [] #8
energy_li = [] #8

### Functions ###

mkdir()

obsID_select #1

lvl2_data(obsID_li) #2
WCS() #2
deep_space_9() #2

ccd_id_finder(obsID_li) #3

espace_filt(obsID_li, ccd_id) #4
bkg_lightcurve(obsID_li) #4

time_finder(obsID_li, ccd_id) #3

for decision in choice:
		if choice == "yes":
			extract_flare(obsID_li, times) #5
			evt_list_filt(obsID_li) #6
			break
		elif choice == "no":
			evt_list_filt_nodeflare(ordered_list) #6
			break
		else:
			choice = raw_input("Enter yes or no: ")

bsky_organiser() #7
get_evt2() #7
evt2_pointer(obsID_li) #7
aspect_sol(obsID_li) #7

contbin_dir() #8
coordinate_inp() #8
energy_inp() #8
reg_creator(energy_li, coor_values) #8
contbinmask_file_check() #8
farith() #8

