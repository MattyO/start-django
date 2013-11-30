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

for (dirpath, dirnames, filenames) in os.walk('./' + args.folder, topdown=False):
    for dirname in dirnames:
        print "doing thing in dir " + dirname
        if fnmatch.fnmatch(dirname, "{{app_name}}"):
            os.rename(dirpath+"/"+dirname, dirpath+"/"+template_data['app_name'])

        print "should be running though files"
        print filenames

        for filename in filenames:
            print "running " + filename + " though jinja"
            print "opening " + dirpath + "/" + filename
            fileobj = open(dirpath + "/" + filename, 'r')
            file_contents = fileobj.read()
            fileobj.close()
            template = Template(file_contents)
            with open(dirpath + "/" + filename, 'w') as f:
                f.write(template.render(template_data))



