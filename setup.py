from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in manageasset/__init__.py
from manageasset import __version__ as version

setup(
	name="manageasset",
	version=version,
	description="Mangement of Company Assets",
	author="Rajnish Yadav",
	author_email="rajnish.yadav@datamann.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
