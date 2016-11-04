#!/usr/bin/env python

import glob
import numpy
import os

def paint_spectra_to_map(obsids):

	regions = glob.glob('xaf_*.reg')
	data_filename = 'spectra_wabs_mekal.dat'
	dtype = {'names': ('reg_id', 'kT', 'kT_loerr', 'kT_hierr', 'Z', 'Z_loerr', 'Z_hierr', 'norm', 'norm_loerr', 'norm_hierr', 'nH', 'nH_loerr', 'nH_hierr', 'chi2', 'totcnts', 'nbins'), 'formats': ('i4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'i4')}
	data1 = numpy.loadtxt(data_filename, dtype=dtype) # get the .dat file data as a dictionary
	region_filename = 'region_list.txt' # make region_list.txt which will be used by paint_output_images
	reg_file = open(region_filename, "w")
	for i in range(len(regions)):
		root = regions[i][:-4] # xaf_##
		output_filename = root + '_fit_out.txt' # the file that paint_output_images will read
		data_file = open(output_filename, "w") # write a new file each time which will be used to paint the values on

		# Write kT, kT_loerr, kT_hierr
		ktemp = data1['kT'][i]
		kT_loerr = data1['kT_loerr'][i]
		kT_hierr = data1['kT_hierr'][i]
		data_file.write('kT ' + str(ktemp) + '\n')
		data_file.write('kT_loerr ' + str(kT_loerr) + '\n')
		data_file.write('kT_hierr ' + str(kT_hierr) + '\n')

		# Write Z, Z_loerr, Z_hierr
		zval = data1['Z'][i]
		Z_loerr = data1['Z_loerr'][i]
		Z_hierr = data1['Z_hierr'][i]
		data_file.write('Z ' + str(zval) + '\n')
		data_file.write('Z_loerr ' + str(Z_loerr) + '\n')
		data_file.write('Z_hierr ' + str(Z_hierr) + '\n')

		# Close
		data_file.close()

		# Region list
		reg_file.write(root + ' ' + root + '_group.pi\n') # the second part is a dud file

	reg_file.close()

	# Paint the values onto the regions
	os.system('paint_output_images --binmap=contbin_binmap.fits')


obsid_list = ['17218', '18689']

paint_spectra_to_map(obsid_list)
