import os
import fnmatch
from jinja2 import Template
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("template_data")

args = parser.parse_args()

template_data = json.loads(args.template_data)

for (dirpath, dirnames, filenames) in os.walk('.', topdown=False):
    for dirname in dirnames:
        if fnmatch.fnmatch(dirname, "{{app_name}}"):
            os.rename(dirpath+"/"+dirname, dirpath+"/"+template_data['app_name'])

    print '---------'
    print dirpath
    print dirnames
    print filenames


