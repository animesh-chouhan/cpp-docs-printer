import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from weasyprint import HTML, CSS

#URL = "http://www.cplusplus.com/reference/cstdio/printf/"


def get_html(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    tag = soup.find(id="I_main")

    if tag == None:
        print("Something went wrong.")
        return None
    else:
        body = tag.wrap(soup.new_tag("body")).prettify()

        head = """ 
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>C++ Reference</title>
            <link rel="canonical" href="http://www.cplusplus.com/reference/cstdio/printf/">
            <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
            <link rel="stylesheet" type="text/css" href="../css/main.css">
        </head>
        """

        html = "<html>" + head + body + "</html>"
        # print(html)

        filename = urlparse(url)[2][1:-1].replace("/", "-")
        # print(filename)

        with open("./html/{}.html".format(filename), "w") as f:
            f.write(html)

        return filename


def get_pdf(filename):
    html_file = "./html/{}.html".format(filename)
    pdf_file = "./pdf/{}.pdf".format(filename)
    HTML(html_file).write_pdf(pdf_file)


if __name__ == "__main__":
    filename = get_html(sys.argv[1])
    if filename != None:
        get_pdf(filename)
