from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import overlays

setup(
    name = "pynq_overlay_demo",
    version = overlays.__version__,
    url = 'https://github.com/kevkim11/pynq_overlay_demo',
    license = 'All rights reserved.',
    author = "Kevin Kim",
    author_email = "kevkim11@email.com",
    packages = ['overlays'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so'],
    },
    install_requires = ['pynq',],
    dependency_links=['http://github.com/xilinx/PYNQ'],
    description = "New simple custom overlay for PYNQ-Z1"
)