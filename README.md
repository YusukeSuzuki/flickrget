flickrget
=========

Command line utility program for searching flickr photos

Requirements
============
Python 2.7.x
flickrapi

Usage
=====
At first, you should save flickr API key to config file.

```bash
flickrget.py --set_api_key YOUR_API_KEY
```

API key saved to ~/.flickrget.cfg .
To get API key, see http://www.flickr.com/services/apps/create/ for detail.

Querying photo URL tagged with 'cat'. This usage try to output all of querying result.

```bash
flickrget.py --tags cat
```

You can limit output count with --max option.

```bash
flickrget.py --tags cat --max 15
```

You can search with text search mode.

```bash
flickrget.py --text "happy birthday to you" --max 15
```

You can select output image size with --url_mode option.
Valid values are 'sq', 't', 'q', 'm', 'n', 'z', 'c', 'l', 'o'.

```bash
flickrget.py --tags cat --url_mode o --max 15
```

See also http://www.flickr.com/services/api/misc.urls.html .

Install
=======
```bash
sudo bash install.sh
```

This command simply do pip installation for depending modules, and put files on /usr/local/bin
