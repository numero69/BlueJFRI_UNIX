#!/usr/bin/python3

import shutil
import requests
import subprocess as sp


URL = "https://www.bluej.org/download/files/BlueJ-linux-422.deb"
response = requests.get(URL)
open("bluejdeb.deb", "wb").write(response.content)
sp.call(["sudo","dpkg","-i", "bluejdeb.deb"])

print('=== copying checkstyle extension')

shutil.copyfile('src/default_checks.xml', '/usr/share/bluej/extensions/default_checks.xml')
shutil.copyfile('src/checkstyle-extension-5.4.1.jar', '/usr/share/bluej/extensions/checkstyle-extension-5.4.1.jar')