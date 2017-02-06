#!/usr/bin/env python3

import sys
import logging
import webbrowser
import requests
import bs4

'''
lucky.py
 - opens tabs in a browser with the top ten results

'''

BASE_URL = 'https://www.google.com/search?q='
# example https://www.google.com/webhp#q=hats+for+men

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
    logging.debug('Starting %s...' % sys.argv[0])
    logging.debug('sys.argv: %s' % ' '.join(sys.argv))

    # grab the query from CLI
    query = '+'.join(sys.argv[1:])
    query_url = BASE_URL + query
    logging.debug('query URL : %s' % query_url)

    result = requests.get(query_url)
    result.raise_for_status()

    results_html = open('results.html', 'wb')
    for chunk in result.iter_content(100000):
        results_html.write(chunk)
    results_html.close()

    bs = bs4.BeautifulSoup(result.text, "html.parser")
    links = bs.select('.r a')
    for i in range(len(links)):
        logging.debug("%d: %s" % (i, links[i]))
        webbrowser.open('http://google.com' + links[i].get('href'))
