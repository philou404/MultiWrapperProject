from setuptools import setup, find_packages


VERSION = '1.0.6'
DESCRIPTION = 'E621 wrapper'
LONG_DESCRIPTION = 'E621 wrapper with download and search with tags on e621 API'

# Setting up
setup(
    name="E621Project",
    version=VERSION,
    author="philou404",
    author_email="<philouerror404@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests >= 2.27.0'],
    keywords=['python', 'wrapper', 'e621', 'furry', 'yiff'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)