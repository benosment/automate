#!/usr/bin/env python3

import sys
import pyperclip
import logging
import webbrowser

'''
map_it.py
 - opens a browser to Google Maps based on command line arguments or clipboard

'''

BASE_URL = 'https://www.google.com/maps/place/'

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
    logging.debug('Starting %s...' % sys.argv[0])
    logging.debug('sys.argv: %s' % ' '.join(sys.argv))
    logging.debug('clipboard: %s' %pyperclip.paste())
    # grab the street address from CLI if there are more than two arguments
    # if there is only one argument, grab street address from clipboard
    address = ''
    if len(sys.argv) >= 2:
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    if address == '':
        print('Address is empty')
        exit(-1)

    logging.debug("Address is %s" % address)
    url = BASE_URL + address
    logging.debug("URL is %s" % url)
    webbrowser.open(url)
    logging.debug("done.")
