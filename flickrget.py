#!/usr/bin/python
# coding:utf-8

import flickrapi

import ConfigParser

import getopt
import os
import sys
import xml

#print(len(sys.argv))
#print(sys.argv)

api_key = ''
config_file_name = '.flickrget.cfg'

def get_config_file_path():
	return os.path.join(os.path.expanduser('~'), config_file_name)
	#if( os.path.exists( config_file_path ) ):

def print_help():
	print('no help')

def set_api_key(key):
	config = ConfigParser.SafeConfigParser()
	config.read( get_config_file_path() )
	if not config.has_section('Global'):
		config.add_section('Global')
	config.set('Global', 'api_key', key)

	with open( get_config_file_path(), 'wb' ) as config_file:
		config.write( config_file )

def get_env():
	config = ConfigParser.SafeConfigParser()
	config.read( get_config_file_path() )

	if config.has_option('Global', 'api_key'):
		global api_key
		api_key = config.get('Global', 'api_key')
		#print(api_key)
	else:
		print('there is no config about api_key')
		print('use: %(command)s --set_api_key key'% {'command': sys.argv[0]})
		exit(0)

def main():
	try:
		options, args = getopt.getopt(sys.argv[1:], 'h',
			['help', 'set_api_key='])
	except getopt.GetoptError:
		print('arg error')
		sys.exit(2)

	for option, arg in options:
		if option in ("--set_api_key"):
			set_api_key(arg)
			exit(0)
		elif option in ('-h', '--help'):
			print_help()

	get_env()

	flickr = flickrapi.FlickrAPI(api_key)

	page = 0
	pages = 1

	while page < pages:
		photos = flickr.photos_search(
			tags="日本",per_page='100',media='photos', page=str(page),
			extras='url_m,url_n,url_c,url_l,url_o')

		if not photos.attrib['stat'] == 'ok':
			print('not ok')
			break

		pages = int(photos.find('photos').attrib['pages'],10)
		page = int(photos.find('photos').attrib['page'], 10)
		#print( 'page = %(page)d, pages = %(pages)d' % {'page' : page, 'pages' : pages} )

		page += 1

		if True:
			for photo in photos.iter('photo'):
				#print( xml.etree.ElementTree.dump(photo) )
				print( photo.attrib['url_m'] )

main()
