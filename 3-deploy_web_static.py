#!/usr/bin/python3
# A script that creates and distributes an archive
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ['52.91.152.149', '52.91.117.216']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Function that distributes an archive to a web server
    """
    if not os.path.exists(archive_path):
        return False

    try:
        release_folder = "/data/web_static/releases/"

    # Upload the archive to /tmp/
        put(archive_path, "/tmp/")

        # Extract the archive to a new release folder
        run(f"sudo tar -xzf /tmp/{archive_path} -C {release_folder}")

        # Delete archived file from tmp
        run(f"sudo rm /tmp/{archive_path}")

        # Delete old symlink
        run("sudo rm /data/web_static/current")

        # Create new symlink
        run("sudo ln -s {} /data/web_static/current".format(
            release_folder + "web_static"))
        print("New version deployed!")
        return True

    except Exception as deployError:
        print("Something went wrong because:", deployError)
        return False


def deploy():
    """This function creates and distributes an archive to a web server"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
