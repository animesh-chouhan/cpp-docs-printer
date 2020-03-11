# cpp-docs-printer
![.](https://img.shields.io/badge/platforms-linux--64-lightgrey.svg)
![license](https://img.shields.io/github/license/animesh-chouhan/youtube-playman)

Generates PDF documents from the HTML C++ documentation

## Setup

### Linux:

Cloning the repository:
```sh
#clone the repo
$git clone https://github.com/animesh-chouhan/cpp-docs-printer.git
$cd cpp-docs-printer
```
Installing the dependencies:

```sh
#run the script directly
$chmod +x ./download.sh
$./download.sh


#directly running the script
$download

```
Add Jobs To cron:

```sh
#creating a cron job that will update the playlists automatically
$crontab -e

#this will open a editor and add this entry to the file
#don't forget the newline after the last entry

PATH="/usr/local/bin:/usr/bin:/bin:/home/<YOUR-USERNAME>/.local/bin"
@daily printf "update-all" | download

```

## Usage example

<a href="https://asciinema.org/a/bQgrwQfcFLtcuJpKMGEuq0Til?speed=2&preload=1&autoplay=1">
  <img src="https://asciinema.org/a/bQgrwQfcFLtcuJpKMGEuq0Til.png" max-width="1000px"/>
</a>

_For more examples and usage, please refer to the [Wiki][wiki]._


## Built with

* [requests](https://requests.readthedocs.io/en/master/) - Requests is an elegant and simple HTTP library for Python, built for human beings.
* [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/) - Beautiful Soup is a library that makes it easy to scrape information from web pages.
* [weasyprint](https://weasyprint.org/) - WeasyPrint is a smart solution helping web developers to create PDF documents.



## Contributing

1. Fork the repo (<https://github.com/animesh-chouhan/cpp-docs-printer/>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[wiki]: https://github.com/animesh-chouhan/youtube-playman/wiki

## License
MIT License
copyright (c) 2020 [Animesh Singh Chouhan](https://github.com/animesh-chouhan). Please have a look at the [license](LICENSE) for more details.
