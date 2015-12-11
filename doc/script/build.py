# -*- coding: UTF-8 -*-

import os
import shutil, errno


def copy_anything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:  # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise

if __name__ == "__main__":

    base_path = os.path.abspath('..') + "/"
    src_path = base_path + "src/"
    doc_path = base_path + "doc/"
    paths_need_copy = [src_path + "resources",
                       src_path + "image",
                       src_path + "logs",]
    dest = src_path + "dist/main/"

    for path in paths_need_copy:
        file_name = dest + os.path.basename(path)
        os.removedirs(file_name)
        copy_anything(path, file_name)
        print "copy files {0} -> {1}".format(path, file_name)
