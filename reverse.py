import fnmatch
import os
import json
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("template_data")

args = parser.parse_args()

template_data = json.loads(args.template_data)
folder = template_data['app_name']

template_data = json.loads(args.template_data)

for (dirpath, dirnames, filenames) in os.walk('./' + folder, topdown=False):

    for dirname in dirnames:
        if fnmatch.fnmatch(dirname, template_data['app_name'] ):
            os.rename(dirpath+"/"+dirname, dirpath+"/"+"{{app_name}}")

    for filename in filenames:
        if filename.endswith(".pyc"):
            continue

        new_file_contents = ""
        with open(dirpath + "/" + filename, 'r') as f:
            for line in f.readline():
                line, times = re.subn(template_data['app_name'], '{{app_name}}', line)
                new_file_contents += line
        with open(dirpath + "/" + filename, 'w') as f:
            f.write(new_file_contents)


if fnmatch.fnmatch(folder, template_data['app_name']):
    os.rename(folder, "{{app_name}}")
