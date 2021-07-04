# pykindler
Command line tool that automatically detects and converts downloaded e-books to mobi format (and auto-uploads to Kindle, on a schedule)

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/VivekBits2210/pykindler

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)] (<insert_package_name_here>)

```sh
pip3 install pykindler
```

## Dependencies
- UNIX based system needed (Linux, MacOS)
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
Please feel free to mail ideas to the maintainer: [viveknayak2210@gmail.com]
