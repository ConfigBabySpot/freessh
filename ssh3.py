#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as DELtaXN 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
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
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def DeltaXN_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	cetak(panel(f"""[bold red]               ╔═══╦═══╦╗──╔╗───╔═╗╔═╦═╗─╔╗
               [bold yellow]╚╗╔╗║╔══╣║─╔╝╚╗──╚╗╚╝╔╣║╚╗║║
               [bold green]─║║║║╚══╣║─╚╗╔╬══╗╚╗╔╝║╔╗╚╝║
               [bold blue]─║║║║╔══╣║─╔╣║║╔╗║╔╝╚╗║║╚╗║║
               [bold purple]╔╝╚╝║╚══╣╚═╝║╚╣╔╗╠╝╔╗╚╣║─║║║
               [bold orange]╚═══╩═══╩═══╩═╩╝╚╩═╝╚═╩╝─╚═╝
             """,width=90,style=f"bold red"))
#------------------[ SSH-WEBSOCKET ]---------------#
def sshws():
	clear()
	banner()
	cetak(panel(f"\t[yellow]>>> KALAU LAG WAJAR DIGB BERARTI",style=f"bold red"))
	cetak(panel(f"\t[yellow]>>> DONATE BANG : 081342791377",style=f"bold red"))
	print('')
	print(f"{asu}sg-ssh.sshmax.xyz:80@sshmax-wedusgem:123456")
	print(f"{asu}sg03-7.sshsrv.com:80@garudassh.com-aauuwbf:15exp15")
	print(f"{asu}sg03.sshsrv.com:80@createssh.net-ajaib0:11223343")
	print('')
	print(f">>> Ketik python ssh3.py kalau ingin kembali kemenu")
#------------------[ SSH-UDP ]---------------#
def udp():
	clear()
	banner()
	cetak(nel(f"\t[yellow]>>> KALAU LAG WAJAR DIGB BERARTI",style=f"bold red"))
	cetak(nel(f"\t[yellow]>>> DONATE BANG : 081342791377",style=f"bold red"))
	print('')
	print(f"{asu}sg1udp.ipservers.xyz:1-7299@roamsaberrrr:220022993399")
	print(f"{asu}sg4udp.sshsrv.com:1-65535@premiumssh.com-juddah:jentiuy")
	print(f"{asu}idvvip.mytun.cloud:1-65535@bundaamah:041019")
	print('')
	print(f">>> Ketik python ssh3.py kalau ingin kembali kemenu")
#------------------[ SSH-PREMIUM ]---------------#
def prem():
	clear()
	banner()
	cetak(nel(f"\t[yellow]>>> KALAU LAG WAJAR DIGB BERARTI",style=f"bold red"))
	cetak(nel(f"\t[yellow]>>> DONATE BANG : 081342791377",style=f"bold red"))
	print('')
	print(f"{asu}ox.steven-vip.my.id:80@yuechan:vip")
	print(f"{asu}fahrul.rmblvpn.xyz:80@pakai:saja")
	print(f"{asu}idvvip.mytun.cloud:80@Bundaamah:041019")
	print('')
	print(f">>> Ketik python ssh3.py kalau ingin kembali kemenu")
#------------------[ SSH-MENU ]---------------#
clear()
banner()
print('')
print(f"{m}Author : {k}DELtaXN")
print(f"{m}Script : {k}SSH GRATIS")
print(f"{m}Github : {k}https://github.com/DELtaXN")
print('')
print(f"{m}Pesan : {k}Kalau SSH Expired Ketik Perintah git pull biar keupdate")
print(f"{m}Pesan : {k}Bilang KeAuthor Kalau SC Error")
print('')
prints(panel(f"[yellow]>>> 1.SSH WEBSOCKET \n[yellow]>>> 2.SSH UDP \n[yellow]>>> 3.SSH PREMIUM",width=43,padding=(0,3),title=f"[red]MENU SSH",style=f"bold red"))
delta = input(f"{m}>>> Pilih : {k}")
if delta in ["1"]:
	sshws()
elif delta in ["2"]:
	udp()
elif delta in ["3"]:
	prem()
else:
	print(f"{m}Pilih Yang Benar Mas")
	exit()