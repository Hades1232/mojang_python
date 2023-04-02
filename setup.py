from setuptools import setup
import setuptools

setup(
   name='mojang_python',
   version='1.2.0',
   description='Easy Mojang API Wrapper',
   license = 'Apache',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   url = "https://github.com/Hades1232/mojang_python",
   author='Hades_',
   packages=setuptools.find_packages(), 
   install_requires=['requests', 'typing'],
   python_requires='>=3.10'
)
