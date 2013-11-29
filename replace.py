import os
import fnmatch
from jinja2 import Template
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("template_data")

args = parser.parse_args()

template_data = json.loads(args.template_data)

os.renames("**/{{app_name}}", template_data['app_name'])

for (dirpath, dirnames, filenames) in os.walk('.', topdown=False):
    print '---------'
    print dirpath
    print dirnames
    print filenames


