#!/usr/bin/env python3
# Fabric script to deploy an archive

from fabric.api import env, put, run, sudo
import os

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with your actual server IPs
env.user = 'ubuntu'  # Replace with your actual username

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        no_extension = os.path.splitext(archive_name)[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_extension)

        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, path_no_ext))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_no_ext))
        return True
    except:
        return False

