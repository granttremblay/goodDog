#!/usr/bin/env python

import glob
import os
from ciao_contrib.runtool import specextract

def extract_spec(obsid_list):

	regions = glob.glob('xaf_*.reg') # get regions
	for reg in regions:
		for obs in obsid_list:
			print('Extracting spectra for region: %s, obsid: %s ...' % (reg, obs))
			root = reg[:-4] + '_' + obs
			evt2_file = glob.glob('../../reprojected_data/' + str(obs) + '_reproj_evt.fits') # file for obsid
			evt2_filter = evt2_file[0] + '[sky=region(%s)]' % reg # add xaf.reg filter
			#bkg_file = '../../' + 'reprojected_data/' + obs + '_background.fits'
			#bkg_filter = bkg_file + '[sky=region(%s)]' % reg # add xaf.reg filter
			asp_file = glob.glob('../../reprojected_data/' + str(obs) + '.asol')
			asp_file = asp_file[0] # Turn into string from glob list
			bpix_file = glob.glob('../../reprojected_data/' + str(obs) + '.bpix')
			bpix_file = bpix_file[0]
			msk_file = glob.glob('../../reprojected_data/' + str(obs) + '.mask')
			msk_file = msk_file[0]
			os.system("punlearn specextract") # Reset specextract
			specextract(infile=evt2_filter, outroot=root, asp=asp_file, badpixfile=bpix_file, mskfile=msk_file, weight='yes')

obsids = ['17218', '18689']
extract_spec(obsids)

