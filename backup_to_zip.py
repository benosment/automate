#!/usr/bin/env python3

import sys
import os
import zipfile


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
    # determine filename based on any other zip archives with same name
    version = 1
    while True:
        zip_filename = "%s_%d.zip" % (zip_name, version)
        if not os.path.exists(zip_filename):
            break
        version += 1
    print("Creating %s..." % zip_filename)
    # create a zip archive
    archive = zipfile.ZipFile(zip_filename, 'w')
    for this_dir, sub_dirs, filenames in os.walk(dirname):
        print('Adding files in %s...' % this_dir)
        archive.write(this_dir)
        for filename in filenames:
            if filename.endswith('.zip'):
                continue
            archive.write(os.path.join(this_dir, filename), compress_type=zipfile.ZIP_DEFLATED)
    archive.close()
    print('Done')

