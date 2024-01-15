#!/usr/bin/python3
"""a Fabric script that distributes an archive to your web servers"""
from fabric.api import env, run, put
from os.path import exists


env.hosts = ["428581-web-01", "428581-web-02"]


def do_deploy(archive_path):
    """Function to deploy"""
    if not exists(archive_path):
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
