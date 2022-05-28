import os
import sys
import re
import shutil


def main():
    src = sys.argv[0]
    path, name_src = os.path.split(src)
    dst_name = re.sub('()(?=\.\w+$)', '_duplicate', name_src)
    dst = os.path.join(path, dst_name)
    shutil.copyfile(src, dst)


if __name__ == \
        '__main__':
    pass
else:
    main()

