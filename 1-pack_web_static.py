#!/usr/bin/env python3
# Fabric script to generate a .tgz archive
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """A function that creates a tgz archive of the directory web_static."""
    dt = datetime.utcnow()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)

    # set conditions if versions directory could not be created
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -cvzf {} web_static".format(archive_path)).failed is True:
        return None

    return archive_path
