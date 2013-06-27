#!/usr/bin/python
# coding:utf-8

import flickrapi

import ConfigParser

import getopt
import os
import sys
import xml

class UrlMode:
	sq = 0
	t = 1
	s = 2
	q = 3
	m = 4
	n = 5
	z = 6
	c = 7
	l = 8
	o = 9

	str = {
		sq : "url_sq",
		t : "url_t",
		s : "url_s",
		q : "url_q",
		m : "url_m",
		n : "url_n",
		z : "url_z",
		c : "url_c",
		l : "url_l",
		o : "url_o"}

api_key = ''
config_file_name = '.flickrget.cfg'
url_mode = UrlMode.m

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

def show_api_key():
	get_env()
	print(api_key)

def main():
	try:
		options, args = getopt.getopt(sys.argv[1:], 'h',
			['help', 'set_api_key=', 'api_key'])
	except getopt.GetoptError:
		print('arg error')
		sys.exit(2)

	for option, arg in options:
		if option in ("--api_key"):
			show_api_key()
			exit(0)
		elif option in ("--set_api_key"):
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
			extras='%(url_mode)s' %
				{'url_mode' : UrlMode.str[url_mode]} )

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
				print( photo.attrib[UrlMode.str[url_mode]] )

main()

