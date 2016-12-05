#!/usr/bin/env python3

import os
import re
import shutil

'''
date-rename
 - renames files with American-style dates (MM-DD-YYYY) to European-Style Dates (DD-MM-YYYY)

'''

# construct a regex to match American-style dates (MM-DD-YYYY)
date_regex = re.compile(r"""
                         (?P<before_date>^(.*?))                    # match all text before the date
                         (?P<month>(0|1)?\d)-                       # month
                         (?P<day>(0|1|2|3)?\d)-                     # date
                         (?P<year>(19|20)\d\d)                      # year
                         (?P<after_date>(.*?)$)""", re.VERBOSE)     # everything else


def is_amercian_style_date(match):
    if match:
        # check that the month is valid
        if int(match.group('month')) > 12:
            return False
        else:
            return True
    return False


if __name__ == '__main__':
    # searches for all files in the current working directory with American-style dates
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print("CWD: %s" % cwd)
    print("Files: %s" % ' '.join(files))

    for filename in files:
        match = date_regex.match(filename)
        if match:
            print(match.group('before_date'), match.group('day'), match.group('month'), match.group('year'), match.group('after_date'))
        if is_amercian_style_date(match):
            print('filename %s matched' % filename)
            new_filename = match.group('before_date') + match.group('day') + '-' + match.group('month') + '-' + \
                           match.group('year') + match.group('after_date')
            print('renaming to %s' % new_filename)
            shutil.move(filename, new_filename)
        else:
            print('filename %s did not match' % filename)

    # when one is found, the file is renamed such that the month and day are swapped to make it
    # European-style

