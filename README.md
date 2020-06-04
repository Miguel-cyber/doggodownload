# hoversearch

hoversearch is a Python Module to download youtube videos.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install hoversearch.

```bash
pip install hoversearch
```

## Usage

```python
import hoversearch
youtube = hoversearch.Youtube()

print(youtube.search(type="url", search="search your video here", download="True", downloadformat="mp4"))

```

## License
[MIT](https://github.com/Miguel-cyber/hoversearch/blob/master/LICENSE)
