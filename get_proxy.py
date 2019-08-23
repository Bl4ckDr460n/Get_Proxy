# copyright (c) 2019-2020 BL4CK DR460N
# Codded By BL4CK DR460N
# Please Contact BL4CK DR460N To Recoded This Tools, Thank You :)
import requests,os,time,sys
from bs4 import BeautifulSoup as bs

s = requests.Session()
def proxy_daily():
	print "\033[31m[!] Gettings Proxy -> https://proxy-daily.com"
	r = s.get("https://proxy-daily.com")
	soup = bs(r.content, "html.parser")
	f = soup.find("div",{"class":"centeredProxyList freeProxyStyle"})
	rp = str(f).replace('<div class="centeredProxyList freeProxyStyle">','').replace('</div>','')
	print "\033[32m[+] Success To Get Proxy"
	time.sleep(3)
	print "\033[33m[!] Saving Proxy -> proxy.txt"
	with open("proxy.txt","a") as sv:
		sv.write(rp)
	print "\033[32m[+] Success To Saving Proxy -> proxy.txt"

def proxy_cz():
	print "\033[31m[!] Gettings Proxy -> http://multiproxy.org"
	r = s.get("http://multiproxy.org/txt_all/proxy.txt")
	print "\033[32m[+] Success To Get Proxy"
        time.sleep(3)
        print "\033[33m[!] Saving Proxy -> proxy.txt"
        with open("proxy.txt","a") as sv:
                sv.write(r.text)
        print "\033[32m[+] Success To Saving Proxy -> proxy.txt"

def spys_me():
	print "\033[31m[!] Gettings Proxy -> http://spys.me"
	r = s.get("http://spys.me/proxy.txt").text
	rp = str(r).replace("Free HTTP/HTTPS(SSL) proxy list only. Text format. Updated hourly.","").replace("Proxy list updated at Thu, 22 Aug 19 14:55:09 +0300\nMirrors=http://spys.me/proxy.txt https://twitter.com/spys_one https://t.me/spys_one\nSupport by donations:\nBTC 1H1ZH7WJVzU7GMDSwsAQrqvGrbLY49wdae\nETC 0xd1Cf57E35003aD846524a7778D99e8856B96C241\nBCH 19o72EjQw3mEYNciZ4JxvpDmUbjjtXghBb\nLTC LMrLZNWGYK3kMHvyioBqZdXYWE3pKj7xZX\nIP address:Port Country-Anonymity(Noa/Anm/Hia)-SSL_support(S)-Google_passed(+)","")
	print rp

os.system('clear')
print "\033[36m     ===========GET PROXY==========="
print "\033[34m          CODDED BY BL4CK DR460N"
print "\033[34m  Thanks To All Members Woll Cyber Team"
print "\033[36m     ==============================="
proxy_daily()
proxy_cz()
sys.exit()
