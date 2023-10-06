#!/usr/bin/python3
# Distributes an archive to a web server.
import os.path
from fabric.api import run, put, env

env.hosts = ["52.91.152.149", "52.91.117.216"]

def do_deploy(archive_path):
    """Function that distributes an archive to a web server.
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
        run("sudo ln -s {} /data/web_static/current".format(release_folder + "web_static"))
        print("New version deployed!")
        return True

    except Exception as deployError:
        print("Something went wrong because:", deployError)
        return False
