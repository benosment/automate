#!/usr/bin/env python3

import sys
import logging
import requests
import bs4
import re
import time

'''
xkcd.py
 - downloads all xkcd comics
'''

BASE_URL = 'https://www.xkcd.com'

comic_number_regex = re.compile(r'''Permanent link to this comic: https://xkcd.com/(\d+)/''')


def get_comic_number(result):
    return int(comic_number_regex.findall(result.text)[0])


def download_image(result):
    try:
        bs = bs4.BeautifulSoup(result.text, "html.parser")
        img_tag = bs.select('#comic img')[0]
        logging.debug("img_tag: %s", img_tag)
        img_url = "https:" + img_tag.get('src')
        logging.debug("img_url: %s", img_url)
        # download the image
        image = requests.get(img_url)
        image.raise_for_status()

        number = get_comic_number(result)

        filename = img_tag.get('src').split('/')[-1]
        image_filename = "xkcd-%d-%s" % (number, filename)
        image_file = open(image_filename, 'wb')
        for chunk in image.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        logging.debug("Wrote %s", image_filename)
    except:
        logging.error("Was not able to download")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
    logging.debug('Starting %s...' % sys.argv[0])
    logging.debug('sys.argv: %s' % ' '.join(sys.argv))

    url = BASE_URL
    prev_exists = True

    while prev_exists:
        result = requests.get(url)
        result.raise_for_status()
        download_image(result)
        current_comic = get_comic_number(result)
        if current_comic == 1:
            prev_exists = False
        else:
            if current_comic == 405:
                current_comic = 404
            url = "https://xkcd.com/%d/" % (current_comic - 1)
        time.sleep(1)
    logging.debug("all done")



