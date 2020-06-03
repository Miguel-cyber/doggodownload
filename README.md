# doggodownload

doggodownload is an async library to download youtube videos.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install doggodownload.

```bash
pip install doggodownload
```

## Usage

```python
import doggodownload
youtube = doggodownload.Youtube()

print(youtube.search(type="url", search="search your video here", download="yes", downloadformat="mp4"))

```

## License
[MIT](https://github.com/Miguel-cyber/ytdownloader/blob/master/LICENSE)
