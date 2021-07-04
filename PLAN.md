# pykindler
Command line tool that automatically detects and converts downloaded e-books to mobi format (and auto-uploads to Kindle, on a schedule)

## Work Left
### Critical
- **Fix SMTP calls**: Commented out the e-mailing code for now, would be sweet to have a working auto-email-to-Kindle feature
### Testing
- **CI/CD pipeline**: Automating testing and releases
- **Coverage**: Add a code coverage tool
- **Modularizing and unit-testing**: The bash client code and convertor scripts are not testable, need to modularize and then write unit tests
- **Better unit-testing for utils**: A couple of util functions don't have unit tests, I don't know how to write them. Some of them run slowly, can they be sped up?
### Expansion
- **Convert to any**: Allow conversions to any format, not just .mobi
- **Get rid of dependence**: The conversion and metadata calls depend on Calibre. If we can write our own, the tool would be self-contained.
- **Windows support**

## License
[MIT](LICENSE)

## Contributing to pykindler

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.
Please feel free to mail ideas to the maintainer: [viveknayak2210@gmail.com]
