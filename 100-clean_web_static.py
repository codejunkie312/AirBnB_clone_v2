#!/usr/bin/python3
"""a Fabric script that distributes an archive to your web servers"""
from fabric.api import env, run, put, local
from datetime import datetime
import os


env.hosts = ["100.26.178.240", "54.146.86.217"]


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


def do_deploy(archive_path):
    """Function to deploy"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split('/')[-1]
        name = file_name.split('.')[0]
        put(archive_path, '/tmp/{}'.format(file_name))
        run('mkdir -p /data/web_static/releases/{}/'.format(name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_name, name))
        run('rm /tmp/{}'.format(file_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(name, name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(name))

        return True
    except Exception:
        return False


def deploy():
    """Function to deploy"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
