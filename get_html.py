import urllib

url_n = input("url: ")
urllib.urlretrieve(url_n, "safe.html")