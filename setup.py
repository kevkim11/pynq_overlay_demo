from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import overlays

setup(
    name = "new_overlay",
    version = overlays.__version__,
    url = 'https://github.com/kevkim11/pynq_overlay_demo',
    license = 'All rights reserved.',
    author = "Kevin Kim",
    author_email = "kevkim11@email.com",
    packages = ['new_overlay'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so'],
    },
    install_requires = ['pynq',],
    dependency_links=['http://github.com/xilinx/PYNQ'],
    description = "New custom overlay for PYNQ-Z1"
)