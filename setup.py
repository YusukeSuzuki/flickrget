from setuptools import setup

setup(
	name = 'flickrget',
	version = '0.1',
	description = 'search image url from flickr',
	url = 'https://github.com/YusukeSuzuki/flickrget',
	author = 'Yusuke Suzuki',
	author_email = '@trinity_site',
	license = 'MIT',
	packages = ['flickrget'],
	entry_points = {
		'console_scripts' : ['flickrget=flickrget.flickrget_command:main'],
		},
	install_requires = [
		'flickrapi'
		],
	zip_safe = False)

