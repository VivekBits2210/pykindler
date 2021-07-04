# pykindler
Command line tool that automatically detects and converts downloaded e-books to mobi format (and auto-uploads to Kindle, on a schedule)

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/VivekBits2210/pykindler

Package is deployed at [Python Package Index (PyPI)](https://pypi.org/project/pykindler/)

```sh
pip3 install pykindler
```

Make sure to install Calibre first ([Guide](https://calibre-ebook.com/download_linux))
```sh
sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin
```

## Dependencies
- UNIX based system needed (Linux, MacOS)
- Calibre
- [pyenchant - Offers an English Dictionary, helpful in detecting if a file is a book](https://pypi.org/project/pyenchant/)
- [python-crontab - Allows scheduling of pykindler jobs that auto-convert and email your books in the background](https://pypi.org/project/python-crontab/)
- [pgi - Auto-detects your downloads folder](https://pypi.org/project/pgi/)

## Usage
- In default mode, pykindler will auto-detect your downloads folder and populate 'Converted_Books' and 'Processed_Books' folders
```sh
pykindler-run
```
- In custom mode, specify your downloads folder and setup a twice-a-day conversion job
```sh
pykindler-run -d /home/some-user/Desktop -c Y
```

- If you just want to convert one file, specify it after -f
```sh
pykindler-run -f /home/some-user/Desktop/my-book.epub
```
- If you want to not convert to mobi, choose your own extension with -x
```sh
pykindler-run -f /home/some-user/Desktop/my-book.mobi -x epub
```

- For more help
```sh
pykindler-run -h
```

## License
[MIT](LICENSE)

## Getting Help

For usage questions, the best place to go to is [StackOverflow](https://stackoverflow.com/questions/).

## Contributing to pykindler

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.
Here is what I [plan to do next](https://docs.google.com/document/d/1ZjnNMVRCZE592LtXDs4G56BMRfQ9DBM9hKjtFrYV2w8/edit?usp=sharing) 
Please feel free to mail ideas to the maintainer: [viveknayak2210@gmail.com]
