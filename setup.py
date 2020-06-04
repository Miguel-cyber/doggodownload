import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hoversearch", 
    version="0.0.1",
    author="Miguel_Rose",
    author_email="michaeljamesrose@outlook.com",
    description="An Youtube Video Downloader for Discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Miguel-cyber/hoversearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["aiohttp","pafy","Pillow","discord","beautifulsoup4","requests", "youtube_dl"],
    include_package_data=True
)
