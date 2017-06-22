#!/usr/bin/env python2
# Yu Liu @ ETRO VUB

import argparse
import os
import random
import re
import ConfigParser
import sys
import argparse

Config = ConfigParser.ConfigParser()
# Configure here to set the data config files
Config.read("./setting_data.ini")
data_root = Config.get('Data_basic', 'DataRoot')
ind_file = Config.get('Data_basic', 'TagIndex')
image_root = data_root + 'JPEG/'

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="indicate the output index file")
args = parser.parse_args()

def xh_test():
	tag_list = []
	f = open(ind_file)
	for line in f.readlines():
		line = line.strip()
		if not line:
			continue
		path = None
		# might contain a numerical label at the end
		match = re.match(r'(.*\d)\s+(.*\S)$', line)
		if match:
			tag_id = int(match.group(1))
			tag_str = match.group(2)
			tag_list.append([tag_id, tag_str])

	f_ind = open(args.file, 'w')
	for root, dirs, files in os.walk(image_root):
		for onefile in files:
			s_write = image_root + onefile
			for each_tag in tag_list:
				tag_str = each_tag[1]
				if tag_str in s_write:
					s_write = s_write + ' ' + str(each_tag[0]) + '\n'
			f_ind.write(s_write)

	for each_tag in tag_list:
		print each_tag


if __name__ == '__main__':
    xh_test()
