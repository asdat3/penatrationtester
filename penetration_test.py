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

def proxies():
    with open('proxies.txt','r') as proxyIn:
        proxyInput = proxyIn.read().splitlines()

    proxyList = [i for i in proxyInput]
    p = random.choice(proxyList)
    p = p.split(':')
    try:
        proxies = {
            'http':f'http://{p[2]}:{p[3]}@{p[0]}:{p[1]}',
            'https':f'https://{p[2]}:{p[3]}@{p[0]}:{p[1]}'
        }
    except:
        proxies = {
            'http':f'http://{p[0]}:{p[1]}',
            'https':f'https://{p[0]}:{p[1]}'
        }
    return proxies

#  input settings

print(Fore.RED + "AsdatIndustries Penetration Test")
print(Fore.WHITE + "")
url_t_request = input("URL: ")
time_in_s_delay = int(input("DELAY (s): "))

#  starting and logging

date_i_want_now = f'{datetime.datetime.now().strftime("%H")}:{datetime.datetime.now().strftime("%M")} - '
tag = str(datetime.datetime.now().strftime("%d-%m-%Y"))

print(Fore.GREEN + f'{tag} - {date_i_want_now}Started')
write_log(log_print_text=f'{tag} - {date_i_want_now}Started')
write_log(log_print_text=f'URL: {url_t_request}')
write_log(log_print_text=f'DELAY: {time_in_s_delay}')

#  MAIN
start_total = timer()
while banned == False:
    tmain_counter = tmain_counter + 1

    date_i_want_now = f'{datetime.datetime.now().strftime("%H")}:{datetime.datetime.now().strftime("%M")} - '
    print(Fore.BLUE + f'{date_i_want_now}requesting... {str(tmain_counter)}')
    write_log(log_print_text=f'{date_i_want_now}requesting... {str(tmain_counter)}')

    start = timer()

    #scraper = cloudscraper.create_scraper()
    #r = scraper.get(url_t_request)
    r = requests.get(url_t_request)

    end = timer()
    print(Fore.WHITE + f'{str(end - start)} - request done... {str(tmain_counter)}')
    write_log(log_print_text=f'{str(end - start)} - request done... {str(tmain_counter)}')

    if "unauthorized" in r.text or "Unauthorized" in r.text or "refused" in r.text or "Refused" in r.text or "REFUSED" in r.text or "rate limit" in r.text or "Rate Limit" in r.text or "rate Limit" in r.text:
        banned = True
    if "Jordan" in r.text or "Nike" in r.text or "Apple iPhone" in r.text or "PlayStation" in r.text:
        banned = False
    else:
        banned = True

    bsdosefofseiusfefs = str(r.text)
    with open("quick_safe.html","w") as f:
        f.write(str(bsdosefofseiusfefs.encode("utf-8")))

    if banned == True:
        print(Fore.RED + f'{str(end - start_total)} - BANNED {str(tmain_counter)}')
        write_log(log_print_text=f'{str(end - start_total)} - BANNED {str(tmain_counter)}')
    else:
        print(Fore.GREEN + f'{str(end - start_total)} - NOT BANNED {str(tmain_counter)}')
        write_log(log_print_text=f'{str(end - start_total)} - NOT BANNED {str(tmain_counter)}')

    time.sleep(time_in_s_delay)

#  end print
date_i_want_now = f'{datetime.datetime.now().strftime("%H")}:{datetime.datetime.now().strftime("%M")} - '
print(Fore.GREEN + "See you :)")
write_log(log_print_text=f'{date_i_want_now}Program closed')

print("\n\n")
wait_for_space_eh_enter_to_close_the_script_sdiuwefuhewfhuew = input("press 'enter' to close the program    ")

