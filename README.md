# Manga-Downloader

## Supported resources

see https://yuru-yuri.github.io/Manga-Downloader/#resources-list


## How to use

### Installation

```bash
git clone --progress --prune --recurse-submodules=no origin  https://github.com/yuru-yuri/Manga-Downloader.git
cd Manga-Downloader
git submodule init
git submodule update --recursive --remote
# install requirements
pip3 install -r requirements.txt
cd helpers/cloudflare_scrape
python setup.py install
```

_If you use Windows, see 'https://github.com/sfbahr/PyCrypto-Wheels'_

####If you using windows, require http://landinghub.visualstudio.com/visual-cpp-build-tools

### Downloading

___:info:For sites with cloudflare protect need installed Node.js___


___:warning:Notice! The name of the manga is always added to the path!___

___To change this behavior, add the key --no-name___

```bash
# download to ./manga directory
./manga.py -i -p -u http://manga-url-here/manga-name
# or download to /manga/destination/path/ directory
./manga.py -i -p -u http://manga-url-here/manga-name -d /manga/destination/path/
# or interactive mode
./manga.py -i -p
# skip 3 volumes
./manga.py --skip-volumes 3 -u http://manga-url-here/manga-name
# reverse volumes downloading (24 -> 1)
./manga.py --reverse-downloading -u http://manga-url-here/manga-name
```

### Help

```bash
./manga.py -h
# or
./manga.py --help
```
