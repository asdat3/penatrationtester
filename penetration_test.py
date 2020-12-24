import requests, random, os, sys, time, datetime, json, filecmp, cloudscraper
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from colorama import init, Fore, Back, Style
from timeit import default_timer as timer
#  inits

init() #init of colorama
banned = False
tmain_counter = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

#  setting log file name:

log_file_name = f'logs_{datetime.datetime.now().strftime("%d-%m-%Y")}_{datetime.datetime.now().strftime("%M")}:{datetime.datetime.now().strftime("%H")}.txt'
with open(f'request_ban_penetration_log/{log_file_name}',"w") as f:
    f.write("created file\n")

def write_log(log_print_text):
    with open(f'request_ban_penetration_log/{log_file_name}',"a") as f:
        f.write(log_print_text + "\n")
