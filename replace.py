import os
import fnmatch
from jinja2 import Template
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("template_data")
parser.add_argument("folder")

args = parser.parse_args()

template_data = json.loads(args.template_data)

exten_to_ignore = ['pyc', 'eot', 'ttf', 'woff', 'zip', 'sqlite3']
jinga_config = {
            'block_start_string' : "<%",
            'block_end_string' : "%>",
            'variable_start_string' : "<%=",
            'variable_end_string' : "%>",
        }

for (dirpath, dirnames, filenames) in os.walk('./' + args.folder, topdown=False):

    for dirname in dirnames:
        if fnmatch.fnmatch(dirname, "{{app_name}}"):
            os.rename(dirpath+"/"+dirname, dirpath+"/"+template_data['app_name'])


    for filename in filenames:
        print dirpath
        print filename
        if filename.split('.')[-1] in exten_to_ignore:
            continue

        fileobj = open(dirpath + "/" + filename, 'r')
        file_contents = fileobj.read()
        fileobj.close()
        template = Template(file_contents, **jinga_config )
        with open(dirpath + "/" + filename, 'w') as f:
            f.write(template.render(template_data))


if fnmatch.fnmatch(args.folder, "{{app_name}}"):
    os.rename(args.folder, template_data['app_name'])


