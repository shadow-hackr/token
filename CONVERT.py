#!/usr/bin/env python3
import requests, time, os, re
# Warna
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
P = ('\x1b[1;97m')
# Logo
__logo__ = (f'''{M}╔═╗┌─┐
{M}║ s │ h│a│d│o│w└
{P}╚═╝└─┘┘└┘ └┘ └─
      {H}({P}Cookies{H}){P}
''')
# Menu Convert Token
def __main__():
  try:
    os.system('clear')
    print(f"""{__logo__}
{P}1{M}.{P} Get token EAAB
{P}2{M}.{P} My Facebook
{P}2{M}.{P} Back (exit)
    """)
    masuk = input(f"{P}?{H}.{P}  :{K} ")
    if masuk in ['1','01']:
      cookie = input(f"{P}?{H}.{P} Cookies :{K} ")
      if len(cookie) == 0:
        exit(f"{M}!{P}.{M} Don't be empty")
      else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Cookie': cookie
        }
        with requests.Session() as r:
          req = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
          cari_id = re.findall('act=(.*?)&nav_source', req.text)
          for z in cari_id:
            rex = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={z}&nav_source=no_referrer', headers = headers)
            token = re.search('(EAAB\w+)', rex.text).group(1)
            print(f"\n{M}#{P} Your token :{H} {token}")
    elif masuk in ['2','02']:
      print(f"{P}!{K}.{P} You will be directed to  Facebook...");time.sleep(2);os.system('xdg-open https://www.facebook.com/profile.php?id=100006455309918 ');exit()
    elif masuk in ['3','03']:
      exit()
    else:
      exit(f"{M}!{P}.{M} Wrong input")
  except Exception as e:
    exit(f"{M}!{P}.{M} {e}")

if __name__=='__main__':
  os.system('git pull');__main__()