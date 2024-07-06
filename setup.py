from setuptools import setup, find_packages

setup(
    name='github_downloader',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'github_downloader=github_downloader:main',
        ],
    },
    author='Sufiyaan Usmani',
    author_email='usmanisufiyaan@gmail.com',
    description='A simple tool to download GitHub repositories or folders.',
    url='https://github.com/sufiyaanusmani/github-repo-downloader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
