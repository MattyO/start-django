from os import listdir
import fnmatch
from jinja2 import Template
from optparse import OptionParser
import json

parser = OptionParser()
parser.add_option('-j', dest="template_data")

(options, args) = parser.parse_args()

template_data = json.loads(args.template_data)

for file in listdir("."):
    if fnmatch.fnmatch("{{app_name}}"):
        print file
        #os.rename(file, template_data['app_name"])




