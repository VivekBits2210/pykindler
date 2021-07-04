# pykindler
Command line tool that automatically detects and converts downloaded e-books to mobi format (and auto-uploads to Kindle, on a schedule)

## Work Left
I'll be updating the plan [here](https://docs.google.com/document/d/1ZjnNMVRCZE592LtXDs4G56BMRfQ9DBM9hKjtFrYV2w8/edit?usp=sharing) instead

### Deprecated
- **Fix SMTP calls**: Commented out the e-mailing code for now, would be sweet to have a working auto-email-to-Kindle feature
- **CI/CD pipeline**: Failing Test cases, need to deal with that jazz
- **Modularizing and unit-testing**: The bash client code and convertor scripts are not testable, need to modularize and then write unit tests
- **Better unit-testing for utils**: A couple of util functions don't have unit tests, I dunno how to write them
- **Calibre dependency**: The conversion and metadata calls depend on Calibre. If we can write our own, the tool would be self-contained.
- **Windows support**

## License
[MIT](LICENSE)

## Contributing to pykindler

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.
Please feel free to mail ideas to the maintainer: [viveknayak2210@gmail.com]
