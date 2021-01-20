from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='lndcvr_unet',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='Working through the landcover UNet example.',
    long_description=long_description,
    author='Esri Advanced Analytics Team',
    license='Apache 2.0',
)
