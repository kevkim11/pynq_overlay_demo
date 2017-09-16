from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import new_overlay

setup(
    name = "new_overlay",
    version = new_overlay.__version__,
    url = 'https://github.com/kevkim11/pynq_overlay_demo',
    license = 'All rights reserved.',
    author = "Kevin Kim",
    author_email = "kevkim11@email.com",
    packages = ['new_overlay'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so'],
    },
    description = "New custom overlay for PYNQ-Z1"
)