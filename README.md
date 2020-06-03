# ytdownload

ytdownload is an async library to download youtube videos.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ytdownload.

```bash
pip install ytdownload
```

## Usage

```python
import ytdownload
youtube = ytdownload.Youtube()

print(youtube.search(type="url", search="search your video here", download="yes", downloadformat="mp4"))

```

## License
[MIT](https://github.com/Miguel-cyber/ytdownload/blob/master/LICENSE)
