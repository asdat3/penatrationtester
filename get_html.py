from email import header
import urllib.request

url_n = input("url: ")
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(url_n, "safe.html")