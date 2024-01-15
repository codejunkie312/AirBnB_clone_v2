#!/usr/bin/python3
"""a Fabric script that generates a '.tgz' archive
from the contents of the 'web_static' folder
of your AirBnB Clone repo, using the function 'do_pack'"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Function to compress files"""
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        file = 'versions/web_static_{}.tgz'.format(date)
        local('tar -cvzf {} web_static'.format(file))
        return file
    except Exception:
        return None
