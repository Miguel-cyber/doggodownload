import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ytdownload", 
    version="0.0.1",
    author="Miguel_2020",
    author_email="michaeljamesrose@outlook.com",
    description="An async youtube Video Downloader for Discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Miguel-cyber/ytdownload",
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
