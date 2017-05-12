from distutils.core import setup
import os

# Extract requirements from requirements.txt
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requirements.txt')) as requirements_file:
	requirements = [r.strip() for r in requirements_file if not r.startswith('#') and len(r.strip()) > 0]


setup(
    name='emulambda',
    version='0.1',
    packages=['emulambda'],
    scripts=['bin/emulambda'],
    url='http://www.fugue.co',
    license='Apache 2.0',
    author='dominiczippilli',
    author_email='dom@fugue.co',
    description='Python emulator for AWS Lambda.',
    install_requires=requirements
)
