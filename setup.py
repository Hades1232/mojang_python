from setuptools import setup

setup(
   name='mojang_python',
   version='1.1.0',
   description='Easy Mojang API Wrapper',
   licence = 'Apache',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   url = "https://github.com/Hades1232/mojang_python",
   author='Hades_',
   packages=['mojang_python'], 
   install_requires=['requests', 'typing'],
   python_requires='>=3.10'
)
