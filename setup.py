from setuptools import setup, find_packages
import os
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='seaborn-logger',
    version='0.0.1',
    description='SeabornLogger enables the streaming of the '
                'data relevant ot a program\'s to a logging file',
    long_description='',
    author='Ben Christenson',
    author_email='Python@BenChristenson.com',
    url='https://github.com/SeabornGames/Logger',
    download_url='https://github.com/SeabornGames/Logger'
                 '/tarball/download',
    keywords=['logging'],
    install_requires=[],
    extras_require={
    },
    packages=['seaborn'] + ['seaborn.' + i
                            for i in find_packages(where='./seaborn')],
    license='MIT License',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
)
