#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    djangoPath = os.path.split(os.path.realpath(__file__))[0] + '/mapthing'
    sys.path.insert(0, djangoPath)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mapthing.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
