#!/usr/bin/env python3

import sys
import os
import zipfile
import re
import shutil

'''
backup_to_zip
 - given a directory, creates a zip archive of the content
 - increments file name to provide different snapshots

'''

if __name__ == '__main__':
    # check if there are exactly two arguments
    if len(sys.argv) != 2:
        print("Error: usage is %s <directory>" % sys.argv[0])
        exit(-1)

    # check if the specified directory exists
    dirname = sys.argv[1]
    if os.path.exists(dirname):
        print('%s is a valid directory' % dirname)
    else:
        print("Error: directory %s not found" % dirname)
        exit(-1)

    zip_name = os.path.basename(dirname)
    print("Zip name: %s" % zip_name)
    # determine filename based on any other zip archives with same name
    highest_version = 0
    for f in os.listdir():
        if zip_name in f and '.zip' in f:
            print(f)
            zip_version = int(f.split('_')[-1][:-4])
            if zip_version > highest_version:
                highest_version = zip_version
    this_version = highest_version + 1
    print(this_version)
    zip_filename = "%s_%d.zip" % (zip_name, this_version)
    archive = zipfile.ZipFile(zip_filename, 'w')
    for (this_dir, sub_dirs, files) in os.walk(dirname):
        for f in files:
            archive.write(os.path.join(this_dir, f), compress_type=zipfile.ZIP_DEFLATED)
    archive.close()
    # create a zip archive

