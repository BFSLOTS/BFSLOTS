# -*- coding: utf-8 -*-
from TEAM_TERMUX import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from googletrans import Translator
from threading import Thread,Event
import wikipedia as wiki
from subprocess import check_output
from Naked.toolshed.shell import execute_js
import sys,traceback
import json, requests, LineService
from thrift.transport import THttpClient
from zalgo_text import zalgo
requests.packages.urllib3.disable_warnings()

_session = requests.session()
botStart = time.time()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
bot1 = LINE("hujj488@gmail.com","Aa1234")    
cl = LINE("Aryounoi100web@hotmail.com","Za0868726084") #ganti imel line mu di sini
cl.log("Auth Token : " + str(cl.authToken))

#bot1 = LINE("gijeno4122@jmpant.com","Aa1234") #ganti imel line mu di sini
bot1.log("Auth Token : " + str(bot1.authToken))
#==========SB_TEMPLATE========
print ("\nSukses Bro..BY BF SLOT เข้าใจวัยรุ่น")
oepoll = OEPoll(cl)
call = cl
creator = ["ue8d4c133178ae5a305354ddc71b1e577"]
owner = ["u917ee831e5df87145bf880d30f8d5cb3","ue8d4c133178ae5a305354ddc71b1e577"]
admin = ["u917ee831e5df87145bf880d30f8d5cb3","ue8d4c133178ae5a305354ddc71b1e577"]
staff = ["ue8d4c133178ae5a305354ddc71b1e577"]

api = {"kw":{}}
lineProfile = cl.getProfile()
mid = cl.getProfile().mid
Amid = bot1.getProfile().mid
KAC = [cl]
Bots = [mid,Amid]
Saints = admin + owner + staff
admin = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

welcome = []
targets = []
protectname = []
prohibitedWords = ['บาย', 'เหี้ย', 'ควย', 'เตะ', 'หี', 'บิน']
userTemp = {}
userKicked = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
offbot = []
#============
web168 = {"type": "flex",
 "altText": "ฟรี 188 สมาชิกใหม่ ฝากครั้งแรก",
 "contents":
 {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/kupromo1.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:26.8",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://lin.ee/QY4peth"
        }
      }
    },
    {
      "type": "bubble",
      "size": "mega",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/kupromo2.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:26.8",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://lin.ee/9FX1chx"
        }
      }
    }
  ]
}
     }
     
web = {  
 "type": "flex",
 "altText": "้โปรผีบอก....",
 "contents":
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/kk.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:23.6",
        "animated": true
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "สมัครกดตรงนี้",
            "weight": "bold",
            "align": "center",
            "color": "#ffdd00",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://game.evo168.com/register?channel=1676466361728&affiliatecode=1349"
            }
          }
        ],
        "backgroundColor": "#000000",
        "justifyContent": "space-evenly",
        "borderColor": "#ffdd00",
        "background": {
          "type": "linearGradient",
          "angle": "70deg",
          "startColor": "#00000050",
          "endColor": "#000000",
          "centerColor": "#ffffff50"
        }
      }
    },
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/pros.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:23.6",
        "animated": true
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ติดต่อโปรโมทเว็บคลิ๊ก",
            "weight": "bold",
            "align": "center",
            "color": "#ffdd00",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://lin.ee/9FX1chx"
            }
          }
        ],
        "backgroundColor": "#000000",
        "justifyContent": "space-evenly",
        "borderColor": "#ffdd00",
        "background": {
          "type": "linearGradient",
          "angle": "70deg",
          "startColor": "#00000050",
          "endColor": "#000000",
          "centerColor": "#ffffff50"
        }
      }
    }
  ]
}
 
  }
  
web188 = {  
 "type": "flex",
 "altText": "้โปรผีบอก....",
 "contents":
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/kk.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:23.6",
        "animated": true
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "สมัครกดตรงนี้",
            "weight": "bold",
            "align": "center",
            "color": "#ffdd00",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://game.evo168.com/register?channel=1676466361728&affiliatecode=1349"
            }
          }
        ],
        "backgroundColor": "#000000",
        "justifyContent": "space-evenly",
        "borderColor": "#ffdd00",
        "background": {
          "type": "linearGradient",
          "angle": "70deg",
          "startColor": "#00000050",
          "endColor": "#000000",
          "centerColor": "#ffffff50"
        }
      }
    },
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/pros.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:23.6",
        "animated": true
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ติดต่อโปรโมทเว็บคลิ๊ก",
            "weight": "bold",
            "align": "center",
            "color": "#ffdd00",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://lin.ee/9FX1chx"
            }
          }
        ],
        "backgroundColor": "#000000",
        "justifyContent": "space-evenly",
        "borderColor": "#ffdd00",
        "background": {
          "type": "linearGradient",
          "angle": "70deg",
          "startColor": "#00000050",
          "endColor": "#000000",
          "centerColor": "#ffffff50"
        }
      }
    }
  ]
}
 
  }
#===
settings = {
    "welcome": True,
    "leave": False,
    "mid": False,
    "size": "micro",
    "keyCommand": "dent",
    "commentPost": "BF SLOTS\nรับโปรโมทเว็บพนัน ออนไลน์\nสนใจติดต่อ\nLine: guzaja24",
    "Aip": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": {},
    "postingan":{},
    "checkPost": False,
    "autoRead": False,
    "autoJoinTicket": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changevp": False,
    "changeCover":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "delFriend":False,
    "addadmin":False,
    "delladmin":False,
    "checkmid": False,
    "getMid": False,
    "invite":False,
    "Invi":False,
    "staff":{},
    "Timeline": False,
    "likePost": False,
    "likeOn": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "readPoint":{},
    "readMember":{},
    "lang":False,
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "tumbal":True,
    "proJS":True,
    "backup":True,
    "contact":False,
    "autoRead": False,
    "autoBlock": False,
    "autoJoin":True,
    "autoAdd":False,
    'autoCancel':{"on":True, "members":1},
    "autoReject":False,
    "autoLeave":False,
    "detectMention":False,
    "detectMention2":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "Unsend":False,
    "responsmule":True,
    "ytube":True,
    "tiktok":True,
    "nCall":True,
    "sticker":False,
    "selfbot":True,
    "clear":"santet",
    "tagall":"all",
    "mention":"ɴɢɪɴɪᴘ ᴍᴜʟᴜ ᴄᴏʟᴏᴋ ɴɪʜ",
    "Respontag":"🛡ʜᴀᴅɪʀ ᴋᴀɴɢᴇɴ ʏᴀ ᴛᴀɢ ᴍᴜʟᴜ",
    "Respontag2":"🛡ᴛᴀɢ ʟᴀɢɪ ᴋᴇᴘʟᴇᴛ ɴɪʜ",
    "welcome":"🛡sᴀʟᴋᴇɴ sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ᴋᴀ",
    "autoLeave":"🛡sᴇʟᴀᴍᴀᴛ ᴊᴀʟᴀɴ ᴋᴀ ᴛᴛᴅᴊ ʏᴀ",
    "comment":"ʜᴀᴅɪʀ ɴʏɪᴍᴀᴋ☺☺ʟɪᴋᴇ ʟɪᴋᴇ ʙʏ:ɴᴜʀᴄʜ",
    "message1":"ᴛʜᴀɴᴋᴢ ғᴏʀᴅ ᴀᴅᴅ ᴍᴇ\nCreator:http://line.me/ti/p/~guzaja24",
}
protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[]
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

try:
    with open('api.json', 'r') as f:
        api = json.load(f)
except:
    print("Couldn't read Log data")

f = codecs.open('api.json','w','utf-8')
json.dump(api, f, sort_keys=True, indent=4, ensure_ascii=False)  

clProfile = cl.getProfile()
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
bot1Profile = bot1.getProfile()
myProfile["displayName"] = bot1Profile.displayName
myProfile["statusMessage"] = bot1Profile.statusMessage
myProfile["pictureStatus"] = bot1Profile.pictureStatus
contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
imagesOpen = codecs.open("image.json","r","utf-8")
images = json.load(imagesOpen)
videosOpen = codecs.open("video.json","r","utf-8")
videos = json.load(videosOpen)
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers = json.load(stickersOpen)
audiosOpen = codecs.open("audio.json","r","utf-8")
audios = json.load(audiosOpen)
mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
           
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def picFinder(name):    
        try:
            rgram = requests.get('http://www.instagram.com/{}'.format(name))
            rgram.raise_for_status()
            selenaSoup=BeautifulSoup(rgram.text,'html.parser')
            pageJS = selenaSoup.select('script')
            for i, j in enumerate(pageJS):
                pageJS[i]=str(j)
            picInfo = sorted(pageJS,key=len, reverse=True)[0]
            allPics = json.loads(str(picInfo)[52:-10])['entry_data']['ProfilePage'][0]
            return allPics
        except requests.exceptions.HTTPError:
            return '\t \t ### ACCOUNT MISSING ###'
def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == True:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postid'],wait["comment"])
          print ("✪[]► Like Success")
        except:
          pass
      else:
          print ("Already Liked")
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items

def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        cl.updateProfilePicture(path_p, 'vp')
                     
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'GEGE.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
def NoteCreate(to,cmd,msg):
	h = []
	s = []
	if cmd == 'tagnote':
		sakui = cl.getProfile()
		group = cl.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
		data = nama
		k = len(data)//20
		for aa in range(k+1):
			nos = 0
			if aa == 0:dd = '╭─[ Mention Note ]';no=aa
			else:dd = '';no=aa*20
			msgas = dd
			for i in data[aa*20 : (aa+1)*20]:
				no+=1
				if no == len(data):msgas+='\n│{}. @  \n╰─[ Mention Note ]'.format(no)
				else:msgas+='\n│{}. @'.format(no)
			msgas = msgas
			for i in data[aa*20 : (aa+1)*20]:
				gg = []
				dd = ''
				for ss in msgas:
					if ss == '@':
						dd += str(ss)
						gg.append(dd.index('@'))
						dd = dd.replace('@',' ')
					else:
						dd += str(ss)
				s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
				nos +=1
			h = cl.createPostGroup(msgas,msg.to,holdingTime=None,textMeta=s)
#=====
def RmentionMembers(to, mid):
    try:
        arrData = ""
        textx = "     [Total {} Butir]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "╚══[Ternak {} aman]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error) 
def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╔═════[ Sider Members ]═══════\n║ Sini Gabung Chat ka 😊..\n╠☛ 1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠☛  {}. ".format(str(no))
            else:
                textx += "╚══════════════════\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = (str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
       # cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
    #    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error)) 

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :「Gaje Bots」  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)                     
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost


#=====DEF HELP MENU =======
def sendTextTemplatelike(to, text): #autolike
    data = {
                                "type": "flex",
                                "altText": "BF SLOTS",
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#800000"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "80px",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "4px",
        "offsetStart": "4px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xs",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "offsetTop": "3px",
            "offsetStart": "0px",
            "color": "#0000ff"
          }
        ],
        "position": "absolute",
        "width": "150px",
        "height": "23px",
        "backgroundColor": "#ff7f00",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "87px",
        "offsetStart": "2px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(timeNow.strftime('%A')),
            "size": "xs",
            "color": "#ffd700",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "0px",
            "offsetBottom": "0px"
          }
        ],
        "position": "absolute",
        "width": "53px",
        "height": "20px",
        "backgroundColor": "#ff0000",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "offsetTop": "4px",
        "offsetStart": "97px",
        "cornerRadius": "8px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(datetime.strftime(timeNow,'%H:%M:%S')),
            "size": "xxs",
            "color": "#ffd700",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "2px",
            "offsetBottom": "0px"
          }
        ],
        "position": "absolute",
        "width": "53px",
        "height": "20px",
        "backgroundColor": "#ff0000",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "24px",
        "offsetStart": "97px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(datetime.strftime(timeNow,'%d-%m-%Y')),
            "size": "xxs",
            "color": "#ffd700",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "0px"
          }
        ],
        "position": "absolute",
        "width": "53px",
        "height": "20px",
        "backgroundColor": "#ff0000",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "45px",
        "offsetStart": "97px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "ᴄʜᴅ-ʙᴏᴛs",
            "size": "xxs",
            "color": "#ffd700",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "3px"
          }
        ],
        "position": "absolute",
        "width": "53px",
        "height": "20px",
        "backgroundColor": "#ff0000",
        "borderWidth": "1px",
        "borderColor": "#0000ff",
        "cornerRadius": "8px",
        "offsetTop": "65px",
        "offsetStart": "97px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(mid).displayName),
            "size": "xxs",
            "weight": "bold",
            "style": "normal",
            "align": "start",
            "offsetTop": "5px",
            "offsetStart": "2px",
            "color": "#ffd700",
            "wrap": True
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "20px",
        "offsetTop": "61px",
        "offsetStart": "9px"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "3px",
    "borderColor": "#0000ff",
    "cornerRadius": "10px",
    "position": "relative"
  },
  "action": {
    "type": "uri",
    "label": "action",
    "uri": "http://line.me/ti/p/~guzaja24"
  },
  "styles": {
    "body": {
      "backgroundColor": "#800000"
    }
  }
}
}
    cl.postTemplate(to, data)                                      
def sendTextTemplate233(to, text):
    data = {
                                       "type": "flex",
                                       "altText": "BF SLOTS",
                                       "contents": 
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#000000",
"type": "box",
"layout": "vertical",
"contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#ffffff"            
      },
      {
        "type": "separator",
        "color": "#ffffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#ffffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ⁴",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#ffffff"
          },
          {
          "type": "image",
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"size": "xxs",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24",
            },
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#ffffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🚹{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#33ffff",
#"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#ffffff"
},{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ffffff",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#ffffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#ffffff"
            },
           {
            "contents": [
              {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#ccffff",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#ffffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://www.youtube.com/channel/UC2dxt9FfRfijNyHyGeQHhdQ?view_as=subscriber"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/___nurch__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate25(to, text):
    data = {
                                       "type": "flex",
                                       "altText": "BF SLOTS",
                                       "contents": 
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#000000",
"type": "box",
"layout": "vertical",
"contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#ffffff"            
      },
      {
        "type": "separator",
        "color": "#ffffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#ffffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ⁴",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#ffffff"
          },
          {
          "type": "image",
          "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
"size": "xxs",
      "aspectMode": "cover",
           "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24",
            },
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#ffffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": "🚹{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#33ffff",
#"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#ffffff"
},{
"type": "text",
"text": "📆 "+ datetime.strftime(timeNow,'%Y-%m-%d'),
"weight": "bold",
"color": "#ffffff",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#ffffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#ffffff"
            },
           {
            "contents": [
              {
          "text": text,
           "size": "xxs",
          # "align": "center",
           "color": "#ccffff",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
         },
         {          
        "contents": [
          {
            "type": "separator",
            "color": "#ffffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com/@bfslots?view_as=subscriber"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/__H__",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
#=========DEF
def sendTextTemplate(to, text):
    data = {
                                       "type": "flex",
                                       "altText": "BF SLOTS",
                                       "contents": 
{
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
             #   "type": "text",
             #   "text": ".",
              #  "color": "#ffffff"
                  "type": "image",
                 "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                 "size": "full",
                 "aspectRatio": "1:3",
                 "aspectMode": "cover"
              }
            ],
            "cornerRadius": "10px",
            "height": "68px",
            "borderColor": "#9900cc",
            "borderWidth": "2px",
            "offsetTop": "-20px",
            "offsetStart": "10px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px",
        "height": "114px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "xxs",
            "color": "#ffffff",
            "wrap": True,
            "offsetTop": "-1px",
            "offsetStart": "15px"
          }
        ],
        "position": "absolute",
        "borderColor": "#9900cc",
        "borderWidth": "2px",
        "cornerRadius": "8px",
        "backgroundColor": "#3300CC",
        "offsetTop": "10px",
        "offsetStart": "40px",
        "width": "114px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
            "size": "xs",
            "color": "#ffffff",
            "wrap": True,
            "offsetStart": "10px"
          }
        ],
        "position": "absolute",
        "backgroundColor": "#336600",
        "borderWidth": "2px",
        "borderColor": "#9900cc",
        "cornerRadius": "8px",
        "offsetTop": "35px",
        "offsetStart": "40px",
        "width": "114px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "gravity": "top",
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "line://nv/profilePopup/mid=uadef1340887c690dfad8b5307adcecf1",
            }
          }
        ],
        "position": "absolute",
        "borderWidth": "4px",
        "borderColor": "#9900cc",
        "cornerRadius": "100px",
        "height": "55px",
        "width": "55px",
        "offsetTop": "6px"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": "#9900cc",
    "cornerRadius": "20px",
    "height": "72px",
    "backgroundColor": "#000000"
  },
  "styles": {
    "body": {
      "backgroundColor": "#cc00ff"
    }
    },
  }
}
    cl.postTemplate(to, data)
def sendTextTemplate23(to, text):
                data = {
                                        "type": "flex",
                                        "altText": "BF SLOTS",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": text,
            "color": "#ffffff",
            "align": "start",
            "size": "xxs",
            "gravity": "center",
            "weight": "bold",
            "style": "normal",
            "wrap": True,
            "offsetTop": "-15px",
            "offsetStart": "-5px"
          }
        ],
        "backgroundColor": "#000000",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://line.me/ti/p/~guzaja24"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#000000",
                "size": "xxs",
                "wrap": True,
                "weight": "regular",
                "style": "italic",
                "align": "center"
              }
            ],
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "30px",
            "height": "30px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "100px",
            "offsetStart": "2px",
            "offsetTop": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "width": "30px",
            "height": "30px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "100px",
            "offsetStart": "122px",
            "offsetTop": "5px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xxs",
                "color": "#ffffff",
                "weight": "regular",
                "style": "normal",
                "align": "center",
                "offsetTop": "5px",
                "offsetStart": "0px"
              }
            ],
            "width": "90px",
            "height": "30px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "backgroundColor": "#ff0000",
            "cornerRadius": "5px",
            "offsetTop": "5px",
            "offsetStart": "32px"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://line.me/ti/p/~guzaja24"
        }
      },
      "styles": {
        "header": {
          "backgroundColor": "#000000"
        },
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "separator": False
        }
      }
    }
  ]
}
}
                cl.postTemplate(to, data)
def sendTextTemplate2(to, text):
    data = {
                                       "type": "flex",
                                       "altText": "BF SLOTS",
                                       "contents": 
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#000000",
"type": "box",
"layout": "vertical",
"contents": [
{
"contents": [
{
"type": "separator",
"color": "#ffffff"
},{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
{
"text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
"size": "xxs",
"align": "center",
"color": "#ccff00",
"wrap": True,
"weight": "bold",
"type": "text"
}],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},{
"type": "separator",
"color": "#ffffff"
}],
"type": "box",
"layout": "horizontal"
},{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
{
"text": text,
"size": "xxs",
#"align": "center",
"color": "#ccffff",
"wrap": True,
"weight": "bold",
"type": "text"
}],
"type": "box",
"spacing": "xs",
"layout": "vertical"
},{
"type": "separator",
"color": "#ffffff"
}],
"type": "box",
"layout": "horizontal"
},{
"type": "separator",
"color": "#ffffff"
},{
"contents": [
          {
            "type": "separator",
            "color": "#ffffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/___H___",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ffffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ffffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplate1(to, text):
                data = {
                                        "type": "flex",
                                        "altText": "BF SLOTS",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": text,
            "color": "#ffffff",
            "align": "center",
            "size": "xxs",
            "gravity": "center",
            "weight": "bold",
            "style": "italic",
            "wrap": True,
            "offsetTop": "-15px",
            "offsetStart": "-5px"
          }
        ],
        "backgroundColor": "#000000",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://line.me/ti/p/~guzaja24"
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#000000",
                "size": "xxs",
                "wrap": True,
                "weight": "regular",
                "style": "italic",
                "align": "center"
              }
            ],
            "flex": 1
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "30px",
            "height": "30px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "100px",
            "offsetStart": "2px",
            "offsetTop": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "width": "30px",
            "height": "30px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "100px",
            "offsetStart": "122px",
            "offsetTop": "5px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xxs",
                "color": "#ffffff",
                "weight": "regular",
                "style": "normal",
                "align": "center",
                "offsetTop": "5px",
                "offsetStart": "0px"
              }
            ],
            "width": "90px",
            "height": "30px",
            "position": "absolute",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "backgroundColor": "#ff0000",
            "cornerRadius": "5px",
            "offsetTop": "5px",
            "offsetStart": "32px"
          }
        ],
        "spacing": "md",
        "paddingAll": "12px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "http://line.me/ti/p/~guzaja24"
        }
      },
      "styles": {
        "header": {
          "backgroundColor": "#000000"
        },
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "separator": False
        }
      }
    }
  ]
}
}
                cl.postTemplate(to, data)                           
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd 

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMessage(op.param1,"ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴏɴ \nᴄᴏᴍᴇɴ ᴅɪ ᴛʟ ᴋʟᴏ ᴀᴅᴀ ᴘᴇʀʟᴜ")
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate1(op.param1,"ɴʏᴜʟɪᴋ ɴᴊɪʀʀʀʀ" +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplate1(op.param1,"ᴛʜᴀɴᴋs" + str(ginfo.name))

        if op.type == 13:
            if wait["autoJoin"] and mid in op.param3:
                group = cl.getGroup(op.param1)
                group.notificationDisabled = False
                cl.acceptGroupInvitation(op.param1)
                cl.updateGroup(group)
                ginfo = cl.getGroup(op.param1)
                data = {
                        "type": "flex",
                        "altText": "BF SLOTS",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getGroup(op.param1).pictureStatus),
            "aspectMode": "cover",
            "aspectRatio": "4:5",
            "size": "full"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "102px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "198px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "align": "center",
            "size": "full",
            "aspectRatio": "1:3",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "283px",
        "height": "75px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "offsetTop": "113px",
        "offsetStart": "5px",
        "cornerRadius": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "makasih udah diinvite dimari salken kk smua.",
            "size": "xxs",
            "weight": "regular",
            "style": "normal",
            "align": "center",
            "color": "#ffffff",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "0px"
          }
        ],
        "position": "absolute",
        "width": "270px",
        "height": "60px",
        "offsetTop": "119px",
        "offsetStart": "13px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "150px",
        "height": "20px",
        "backgroundColor": "#Ff0000",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "174px",
        "offsetStart": "75px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "GROUP",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center",
            "style": "normal"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "117px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "color": "#ffffff",
            "style": "normal",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "213px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "xxs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "10px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(ginfo.name),
            "size": "xxs",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "107px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(mid).displayName),
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "4px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "20px",
        "offsetTop": "82px",
        "offsetStart": "203px"
      }
    ],
    "paddingAll": "0px",
    "width": "300px",
    "height": "200px",
    "borderWidth": "3px",
    "borderColor": "#3300cc",
    "cornerRadius": "15px",
    "backgroundColor": "#000000"
  }
}
}
                cl.postTemplate(op.param1, data)

        if op.type == 0:
            return
        if op.type == 26:
            msg = op.message
            if msg.text is None:
                return
            try:
                if keyword["kw"][msg.text]:
                    kwts = keyword["kw"][str(msg.text)]
                    tn = cl.getContact(msg._from)
                    kwts = kwts.replace("{NAME}",tn.displayName)
                    try:
                        cl.sendMessage(msg.to,str(kwts))
                    except:
                        cl.sendMessage(msg._from,str(kwts))
            except Exception as Error:
                pass
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message1"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message1"])

        if op.type == 13:
            if mid in op.param3:
               if wait["autoReject"] == True:
                   if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                       cl.rejectGroupInvitation(op.param1)

        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                try:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            cl.cancelGroupInvitation(op.param1,[_dn])
                    except:
                        cl.cancelGroupInvitation(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        
            if op.param3 in wait["blacklist"]:
                try:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            cl.cancelGroupInvitation(op.param1,[_dn])
                    except:
                        cl.cancelGroupInvitation(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
               try:
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.sendMessage(op.param1,"そ、[ʙʟᴀᴄᴋʟɪsᴛ]そうですか(｀・ω・´)")
               except:
                   pass

        if op.type == 32:
            if wait["backup"] == True:
              if op.param3 in Bots:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                    	pass
                return

        if op.type == 19 or op.type == 32:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in creator:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.acceptGroupInvitation(op.param1)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                    	pass
                return

        if op.type == 19 or op.type == 32:
            if op.param3 in creator:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                cl.findAndAddContactsByMid(op.param3)
                cl.inviteIntoGroup(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 19 or op.type == 32:
            if op.param3 in admin:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                cl.findAndAddContactsByMid(op.param3)
                cl.inviteIntoGroup(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
                
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
               try:
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.sendMessage(op.param1,"そ、[ʙʟᴀᴄᴋʟɪsᴛ]そうですか(｀・ω・´)")
               except:
                   pass

        if op.type == 65:
            if wait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'ɢᴀᴍʙᴀʀʏᴀ ɪʟᴀɴɢ':
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs\nᴘᴇɴɢɪʀɪᴍ: "
                                ret_ = "ɴᴀᴍᴀ ɢʀᴜᴘ: {}".format(str(ginfo.name))
                                ret_ += "\nᴊᴀᴍ sʜᴀʀᴇ: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ik = str(ika.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ika.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                           else:
                                ginfo = cl.getGroup(at)
                                ika = cl.getContact(msg_dict[msg_id]["from"])
                                ika1 = "🚹{}".format(str(ika.displayName))
                                ika2 = "🏠:{}".format(str(ginfo.name))
                                ika3 = "🕙{}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                seber = "═══「 ᴘᴇsᴀɴ ᴅɪʜᴀᴘᴜs 」═══\n{}".format(str(msg_dict[msg_id]["text"]))
                                data = {
                                        "type": "flex",
                                        "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#2f2f4f"
    }
  },
  "type": "bubble",
 "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"  
      },
      {         
         "contents": [
          {
          "type": "separator",
          "color": "#33ffff"   
      },
      {
            "contents": [
              {
              "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          },{
 "type": "text",
"text": "sᴇʟғʙᴏᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴍᴘʟᴀᴛᴇ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴠᴇʀsɪ³",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
     "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
       "contents": [
          {
           "type": "separator",
           "color": "#33ffff"
          },
          {
          "url": "https://obs.line-scdn.net/{}".format(str(ika.pictureStatus)),
            "type": "image",
            "size": "xxs",
            "flex": 0
          },
          {
        "type": "separator",
        "color": "#33ffff"
      },
      {      
       "contents": [              
          {
"type": "text",
"text": ika1,
"weight": "bold",
"color": "#33ffff",
"align": "center",
"size": "xxs",
"flex": 0
},{
"type": "separator",
"color": "#33ffff"
},{
"type": "text",
"text": ika3, #"🕙"+ datetime.strftime(timeNow,'%H:%M:%S'+"🕙"),
"weight": "bold",
"color": "#ccffff",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
         "color": "#33ffff"
       },
       {     
       "contents": [           
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "type": "text",
"text": ika2, #"{}".format(cl.getContact(mid).displayName),
"weight": "bold",
"color": "#ffff00",
#"align": "center",
"size": "xxs",
"flex": 0
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {          
         "contents": [
         { 
           "type": "separator",
           "color": "#33ffff"
            },
           {
            "contents": [
              {
              "type": "separator",
           "color": "#33ffff"
            },
           {
          "text": seber,
           "size": "xxs",
       #   "align": "center",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "🖼️🖼️🖼️",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"
            },{
            "type": "separator",
            "color": "#33ffff"
           },
             {
            "text": "📧📧📧",
            "size": "xxs",
            "color": "#FF9900",
            "align": "center",
            "wrap": True,
            "weight": "bold",
            "type": "text"   
          },
         {
        "type": "separator",
        "color": "#33ffff"
         }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         },
         {
      "contents": [
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com",
           }, 
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24",             
           }, 
            "flex": 1            
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/ZHtFDts/20190427-185307.png", #chathttps://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/chat" #"http://line.me/ti/p/~guzaja24",
            },         
            "flex": 1          
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/kilua",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24"
          },
            "flex": 1           
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
        },{
        "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
            },
             {          
            "contents": [
               {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
    },{
 "type": "text",
"text": "ᴛʜᴀɴᴋᴢ ғᴏʀ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "sᴜᴘᴏʀᴛ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
},{
"type": "text",
"text": "ᴛᴇᴀᴍ",
"weight": "bold",
"color": "#ccff00",
"size": "xxs",
"flex": 0
      },
      {
    "type": "image",
    "url": "https://media.tenor.com/images/3cfcb167ed18a35f3a52f70e44fdf6c0/tenor.gif",
    "size": "xxs"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator", #batas APK
        "color": "#33ffff"     
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(at, data)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╔══「✯sᴛɪᴄᴋᴇʀ ɪɴғᴏ✯」\n"
                                ret_ += "┣[]►🚹: {}".format(str(ryan.displayName))
                                ret_ += "\n┣[]►🏠: {}".format(str(ginfo.name))
                                ret_ += "\n┣[]►🕘: {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\n╚══「✯ᴜɴsᴇɴᴅ ғɪɴɪsʜ✯」"
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                sendTextTemplate2(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'ɢᴀᴍʙᴀʀʏᴀ ᴅɪʙᴀᴡᴀʜ',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n╔══「✯sᴛɪᴄᴋᴇʀ ɪɴғᴏ✯]"
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ ɪᴅ: {}".format(stk_id)
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ: {}".format(stk_ver)
                   ret_ += "\n┣[]►sᴛɪᴄᴋᴇʀ: {}".format(pkg_id)
                   ret_ += "\n┣[]►ᴜʀʟ:{}".format(pkg_id)
                   ret_ += "\n╚══「✯ᴜɴsᴇɴᴅ ғɪɴɪsʜ✯」"
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
                if msg.contentType == 6:
                  if wait["nCall"] == True:
                    if msg._from not in Bots:
                        try:
                            contact = cl.getContact(sender)
                            group = cl.getGroup(msg.to)
                            cover = cl.getProfileCoverURL(sender)
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            if msg.toType == 2:                
                                b = msg.contentMetadata['GC_EVT_TYPE']
                                c = msg.contentMetadata["GC_MEDIA_TYPE"]
                                if c == "VIDEO" and b == "S":
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    arg = "ɢʀᴏᴜᴘ {} call".format(c)
                                    a1 = "{}".format(str(contact.displayName))
                                    a2 = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    a3 = "{}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    data = {
                                        "type": "flex",
                                        "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            "borderColor": "#FFD700",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            "backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "50px",
            "height": "45px",
            "borderWidth": "2px",
            "borderColor": "#0000CD",
            "cornerRadius": "2px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CALL VIDEO",
                "size": "xxs",
                "color": "#0000FFcc",
                "offsetTop": "3px",
                "offsetStart": "3px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            "backgroundColor": "#6699cccc",
            "offsetTop": "8px",
            "offsetStart": "55px",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": a1,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#FF0000",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "23px",
            "backgroundColor": "#6699cccc",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px",
            "offsetTop": "30px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "142px",
            "height": "60px",
            "backgroundColor": "#6699cc",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ʏᴀʜ ɴᴀɪᴋ ᴍᴀᴜ ᴍᴏᴅᴜs",
                "size": "xxs",
                "color": "#FFFF00cc",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "140px",
            "height": "20px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "7px",
            "backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "107px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": a2,
                "size": "xxs",
                "color": "#00ff00",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            "backgroundColor": "#F08080cc",
            "offsetTop": "185px",
            "offsetStart": "49px",
            "borderColor": "#DC143C"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": a3,
                "size": "xxs",
                "color": "#ff0000",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "55px",
            "height": "17px",
            "backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "204px",
            "offsetStart": "49px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#DC143C",
            "cornerRadius": "10px",
            "offsetTop": "55px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#00ff00",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
                                    cl.postTemplate(msg.to, data)
                                if c == 'AUDIO' and b == "S":
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    arg = "ɢʀᴏᴜᴘ {} call".format(c)
                                    satu = "{}".format(str(contact.displayName))
                                    dua = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    tiga = "{}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    data = {
                                        "type": "flex",
                                        "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            "borderColor": "#FFD700",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            "backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "50px",
            "height": "45px",
            "borderWidth": "2px",
            "borderColor": "#0000CD",
            "cornerRadius": "2px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CALL AUDIO",
                "size": "xxs",
                "color": "#0000FFcc",
                "offsetTop": "3px",
                "offsetStart": "3px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            "backgroundColor": "#6699cccc",
            "offsetTop": "8px",
            "offsetStart": "55px",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": satu,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#FF0000",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "23px",
            "backgroundColor": "#6699cccc",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px",
            "offsetTop": "30px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "142px",
            "height": "60px",
            "backgroundColor": "#6699cc",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ʏᴀʜ ɴᴀɪᴋ ᴍᴀᴜ ᴍᴏᴅᴜs",
                "size": "xxs",
                "color": "#FFFF00cc",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "140px",
            "height": "20px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "7px",
            "backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "107px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": dua,
                "size": "xxs",
                "color": "#00ff00",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            "backgroundColor": "#F08080cc",
            "offsetTop": "185px",
            "offsetStart": "49px",
            "borderColor": "#DC143C"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": tiga,
                "size": "xxs",
                "color": "#ff0000",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "55px",
            "height": "17px",
            "backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "204px",
            "offsetStart": "49px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#DC143C",
            "cornerRadius": "10px",
            "offsetTop": "55px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#00ff00",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
                                    cl.postTemplate(msg.to, data)
                                if c == 'LIVE' and b == 'S':
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    arg = "ɢʀᴏᴜᴘ {} call".format(c)
                                    c1 = "{}".format(str(contact.displayName))
                                    c2 = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                    c3 = "{}".format(datetime.strftime(timeNow,'%d-%m-%Y'))
                                    data = {
                                        "type": "flex",
                                        "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                                        "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            "borderColor": "#FFD700",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            "backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "50px",
            "height": "45px",
            "borderWidth": "2px",
            "borderColor": "#0000CD",
            "cornerRadius": "2px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CALL VIDEO",
                "size": "xxs",
                "color": "#0000FFcc",
                "offsetTop": "3px",
                "offsetStart": "3px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            "backgroundColor": "#6699cccc",
            "offsetTop": "8px",
            "offsetStart": "55px",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": c1,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#FF0000",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "23px",
            "backgroundColor": "#6699cccc",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px",
            "offsetTop": "30px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "142px",
            "height": "60px",
            "backgroundColor": "#6699cc",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴀsʏɪᴋ ᴀʀᴛɪs ʟɪᴠᴇ",
                "size": "xxs",
                "color": "#FFFF00cc",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "140px",
            "height": "20px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "7px",
            "backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "107px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": c2,
                "size": "xxs",
                "color": "#00ff00",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            "backgroundColor": "#F08080cc",
            "offsetTop": "185px",
            "offsetStart": "49px",
            "borderColor": "#DC143C"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": c3,
                "size": "xxs",
                "color": "#ff0000",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "55px",
            "height": "17px",
            "backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "204px",
            "offsetStart": "49px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#DC143C",
            "cornerRadius": "10px",
            "offsetTop": "55px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#00ff00",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
                                    cl.postTemplate(msg.to, data)
                                else:
                                    mills = int(msg.contentMetadata["DURATION"])
                                    seconds = (mills/1000)%60
                                    if c == "VIDEO" and b == "E":
                                   # 	tz = pytz.timezone("Asia/Jakarta")
                                  #      timeNow = datetime.now(tz=tz)
                                        arg ="ɢʀᴏᴜᴘ {} call".format(c)
                                        b1 = "{}".format(str(contact.displayName))
                                        b2 = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        b3 = "{}".format(seconds)
                                        data = {
                                            "type": "flex",
                                            "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                                            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            "borderColor": "#FFD700",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            "backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "50px",
            "height": "45px",
            "borderWidth": "2px",
            "borderColor": "#0000CD",
            "cornerRadius": "2px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CALL VIDEO",
                "size": "xxs",
                "color": "#0000FFcc",
                "offsetTop": "3px",
                "offsetStart": "3px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            "backgroundColor": "#6699cccc",
            "offsetTop": "8px",
            "offsetStart": "55px",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": b1,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#FF0000",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "23px",
            "backgroundColor": "#6699cccc",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px",
            "offsetTop": "30px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "142px",
            "height": "60px",
            "backgroundColor": "#6699cc",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴛᴜᴋᴀɴɢ ɴɪᴋᴜɴɢ ᴛᴜʀᴜɴ",
                "size": "xxs",
                "color": "#FFFF00cc",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "140px",
            "height": "20px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "7px",
            "backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "107px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": b2,
                "size": "xxs",
                "color": "#00ff00",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            "backgroundColor": "#F08080cc",
            "offsetTop": "185px",
            "offsetStart": "49px",
            "borderColor": "#DC143C"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": b3,
                "size": "xxs",
                "color": "#ff0000",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "55px",
            "height": "17px",
            "backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "204px",
            "offsetStart": "49px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#DC143C",
            "cornerRadius": "10px",
            "offsetTop": "55px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#00ff00",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
                                        cl.postTemplate(msg.to, data)
                                    if c == "AUDIO" and b == "E":
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        arg ="ɢʀᴏᴜᴘ {} call".format(c)
                                        empat = "{}".format(str(contact.displayName))
                                        lima = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        enam = "{}".format(seconds)
                                        data = {
                                            "type": "flex",
                                            "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                                            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            "borderColor": "#FFD700",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            "backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "50px",
            "height": "45px",
            "borderWidth": "2px",
            "borderColor": "#0000CD",
            "cornerRadius": "2px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "CALL AUDIO",
                "size": "xxs",
                "color": "#0000FFcc",
                "offsetTop": "3px",
                "offsetStart": "3px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            "backgroundColor": "#6699cccc",
            "offsetTop": "8px",
            "offsetStart": "55px",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": empat,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#FF0000",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "23px",
            "backgroundColor": "#6699cccc",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px",
            "offsetTop": "30px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "142px",
            "height": "60px",
            "backgroundColor": "#6699cc",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴛᴜᴋᴀɴɢ ɴɪᴋᴜɴɢ ᴛᴜʀᴜɴ",
                "size": "xxs",
                "color": "#FFFF00cc",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "140px",
            "height": "20px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "7px",
            "backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "107px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": lima,
                "size": "xxs",
                "color": "#00ff00",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            "backgroundColor": "#F08080cc",
            "offsetTop": "185px",
            "offsetStart": "49px",
            "borderColor": "#DC143C"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": enam,
                "size": "xxs",
                "color": "#ff0000",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "55px",
            "height": "17px",
            "backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "204px",
            "offsetStart": "49px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#DC143C",
            "cornerRadius": "10px",
            "offsetTop": "55px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#00ff00",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
                                        cl.postTemplate(msg.to, data)
                                    if c == "LIVE" and b == "E":
                                        tz = pytz.timezone("Asia/Jakarta")
                                        timeNow = datetime.now(tz=tz)
                                        arg ="ɢʀᴏᴜᴘ {} call".format(c)
                                        d1 = "{}".format(str(contact.displayName))
                                        d2 = "{}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                                        d3 = "{}".format(seconds)
                                        data = {
                                            "type": "flex",
                                            "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                                            "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#000000"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "221px",
            "borderWidth": "2px",
            "borderColor": "#FFD700",
            "cornerRadius": "3px",
            "offsetTop": "5px",
            "offsetStart": "3px",
            "backgroundColor": "#B0C4DEcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "50px",
            "height": "45px",
            "borderWidth": "2px",
            "borderColor": "#0000CD",
            "cornerRadius": "2px",
            "offsetTop": "8px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "     LIVE",
                "size": "xxs",
                "color": "#0000FFcc",
                "offsetTop": "3px",
                "offsetStart": "3px",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "25px",
            "backgroundColor": "#6699cccc",
            "offsetTop": "8px",
            "offsetStart": "55px",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": d1,
                "size": "xxs",
                "offsetTop": "2px",
                "offsetStart": "3px",
                "color": "#FF0000",
                "weight": "bold",
                "style": "italic"
              }
            ],
            "position": "absolute",
            "width": "93px",
            "height": "23px",
            "backgroundColor": "#6699cccc",
            "borderWidth": "2px",
            "borderColor": "#FF6347",
            "cornerRadius": "2px",
            "offsetTop": "30px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xxs",
                "color": "#6699cc"
              }
            ],
            "position": "absolute",
            "width": "142px",
            "height": "60px",
            "backgroundColor": "#6699cc",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ʏᴀʜ ʟɢɪ ᴀsɪᴋ ᴜᴅᴀʜᴀɴ",
                "size": "xxs",
                "color": "#FFFF00cc",
                "wrap": True,
                "weight": "bold",
                "style": "italic",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "140px",
            "height": "20px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "163px",
            "offsetStart": "7px",
            "backgroundColor": "#2F4F4Fcc"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "6px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "2:3",
                "aspectMode": "cover"
              }
            ],
            "width": "40px",
            "height": "42px",
            "borderWidth": "2px",
            "borderColor": "#0000FF",
            "cornerRadius": "2px",
            "offsetTop": "181px",
            "offsetStart": "107px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": d2,
                "size": "xxs",
                "color": "#00ff00",
                "offsetTop": "2px"
              }
            ],
            "position": "absolute",
            "width": "55px",
            "height": "20px",
            "backgroundColor": "#F08080cc",
            "offsetTop": "185px",
            "offsetStart": "49px",
            "borderColor": "#DC143C"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": d3,
                "size": "xxs",
                "color": "#ff0000",
                "offsetTop": "0px",
                "offsetStart": "2px"
              }
            ],
            "width": "55px",
            "height": "17px",
            "backgroundColor": "#ffffff",
            "position": "absolute",
            "offsetTop": "204px",
            "offsetStart": "49px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "4:4",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "135px",
            "height": "105px",
            "borderWidth": "2px",
            "borderColor": "#DC143C",
            "cornerRadius": "10px",
            "offsetTop": "55px",
            "offsetStart": "9px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#00ff00",
        "cornerRadius": "10px"
      }
    }
  ]
}
}
                                        cl.postTemplate(msg.to, data)
                        except Exception as error:
                            print (error)                
#____________________________
#____________________________________________________________________
        if op.type == 17:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
             #   cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                welcomeMembers(op.param1, [op.param2])
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = {
                        "type": "flex",
                        "altText": "BF SLOTS",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getGroup(op.param1).pictureStatus),
            "aspectMode": "cover",
            "aspectRatio": "4:5",
            "size": "full"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "102px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "198px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "align": "center",
            "size": "full",
            "aspectRatio": "1:3",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "283px",
        "height": "75px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "offsetTop": "113px",
        "offsetStart": "5px",
        "cornerRadius": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": wait["welcome"],
            "size": "xxs",
            "weight": "regular",
            "style": "normal",
            "align": "center",
            "color": "#ffffff",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "0px"
          }
        ],
        "position": "absolute",
        "width": "270px",
        "height": "60px",
        "offsetTop": "119px",
        "offsetStart": "13px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "150px",
        "height": "20px",
        "backgroundColor": "#Ff0000",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "174px",
        "offsetStart": "75px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "GROUP",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center",
            "style": "normal"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "117px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "color": "#ffffff",
            "style": "normal",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "213px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "xxs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "10px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(ginfo.name),
            "size": "xxs",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "107px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(mid).displayName),
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "4px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "20px",
        "offsetTop": "82px",
        "offsetStart": "203px"
      }
    ],
    "paddingAll": "0px",
    "width": "300px",
    "height": "200px",
    "borderWidth": "3px",
    "borderColor": "#3300cc",
    "cornerRadius": "15px",
    "backgroundColor": "#000000"
  }
}
}
                cl.postTemplate(op.param1, data)
        if op.type == 15:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
              #  cl.updateGroup(group)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                leaveMembers(op.param1, [op.param2])
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = {
                        "type": "flex",
                        "altText": "BF SLOTS",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getGroup(op.param1).pictureStatus),
            "aspectMode": "cover",
            "aspectRatio": "4:5",
            "size": "full"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "102px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": cover,
            "size": "full",
            "aspectRatio": "4:5",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "90px",
        "height": "100px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "5px",
        "offsetStart": "198px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "align": "center",
            "size": "full",
            "aspectRatio": "1:3",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "283px",
        "height": "75px",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "offsetTop": "113px",
        "offsetStart": "5px",
        "cornerRadius": "5px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": wait["autoLeave"],
            "size": "xxs",
            "weight": "regular",
            "style": "normal",
            "align": "center",
            "color": "#ffffff",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "0px"
          }
        ],
        "position": "absolute",
        "width": "270px",
        "height": "60px",
        "offsetTop": "119px",
        "offsetStart": "13px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "150px",
        "height": "20px",
        "backgroundColor": "#Ff0000",
        "borderWidth": "2px",
        "borderColor": "#3300cc",
        "cornerRadius": "5px",
        "offsetTop": "174px",
        "offsetStart": "75px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "20px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "GROUP",
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "align": "center",
            "style": "normal"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "117px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "PROFILE",
            "size": "xs",
            "weight": "bold",
            "color": "#ffffff",
            "style": "normal",
            "align": "center"
          }
        ],
        "position": "absolute",
        "width": "60px",
        "height": "20px",
        "offsetTop": "6px",
        "offsetStart": "213px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "xxs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "10px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(ginfo.name),
            "size": "xxs",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "10px",
            "offsetStart": "1px",
            "color": "#ffffff"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "30px",
        "offsetTop": "75px",
        "offsetStart": "107px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "xs",
            "color": "#ffffff",
            "weight": "bold",
            "style": "italic",
            "align": "start",
            "wrap": True,
            "offsetTop": "4px",
            "offsetStart": "1px"
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "20px",
        "offsetTop": "82px",
        "offsetStart": "203px"
      }
    ],
    "paddingAll": "0px",
    "width": "300px",
    "height": "200px",
    "borderWidth": "3px",
    "borderColor": "#3300cc",
    "cornerRadius": "15px",
    "backgroundColor": "#000000"
  }
}
}
                cl.postTemplate(op.param1, data)

        #===cctv
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        cover = cl.getProfileCoverURL(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        data = {
                                "type": "flex",
                                "altText": "asalamualaiku",
                                "contents": {
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "{} ".format(cl.getContact(op.param2).displayName),
            "size": "xs",
            "color": "#3300cc",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True,
            "offsetTop": "2px",
            "offsetStart": "15px"
          }
        ],
        "position": "absolute",
        "width": "140px",
        "height": "25px",
        "borderWidth": "2px",
        "cornerRadius": "10px",
        "offsetTop": "67px",
        "offsetStart": "14px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "50px",
        "height": "50px",
        "borderWidth": "3px",
        "borderColor": "#3300cc",
        "cornerRadius": "100px",
        "offsetTop": "42px",
        "offsetStart": "3px"
 #     },
    #  {
    #    "type": "box",
   #     "layout": "vertical",
  #      "contents": [
      #    {
        #    "type": "image",
          #  "url": "https://i.imgur.com/UeHKURR.png",
       #     "size": "full",
       #     "aspectRatio": "1:1",
        #    "aspectMode": "cover",
       #     "align": "center",
      #      "margin": "md"
       #   }
      #  ],
      #  "width": "95px",
       # "height": "30px",
      #  "borderWidth": "2px",
      #  "cornerRadius": "0px",
      #  "offsetTop": "3px",
        #"position": "absolute",
        #"offsetStart": "60px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": wait["mention"],
            "size": "xxs",
            "color": "#33cc00",
            "weight": "bold",
            "style": "normal",
            "align": "center",
            "wrap": True
          }
        ],
        "position": "absolute",
        "width": "84px",
        "height": "20px",
        "borderWidth": "2px",
        "cornerRadius": "5px",
        "offsetTop": "8px",
        "offsetStart": "65px"
      }
    ],
    "paddingAll": "0px",
    "width": "160px",
    "height": "100px",
    "borderWidth": "3px",
    "borderColor": "#3300cc",
    "cornerRadius": "15px",
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "http://line.me/ti/p/~guzaja24"
    }
  },
  "styles": {
    "body": {
      "backgroundColor": "#0066FF"
    }
  }
}
}
                        cl.postTemplate(op.param1, data)
  
#========={{{{{MENTION}}}}}===========
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if settings ["Aip"] == True:
                if msg.text in ["clearall","Ratakan!","!bumm",".tes","@zona","!otong","!curut","Cleanse","!cleanse",".cleanse","#jembut","!kickall",".kickall","mayhem","Ratakan","bubarkan","Nuke","nuke",".nuke","Bypass","bypass",".bypass","#bypass","#jancok","hancurkan","!malam","winebot",".malam","bubar",".bubar","86"]:
                    cl.kickoutFromGroup(receiver,[sender])
            if wait["selfbot"] == True:
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  cl.kickoutFromGroup(msg.to, [msg._from])
                              except:
                                  try:
                                  	cl.kickoutFromGroup(msg.to, [msg._from])
                                  except:
                                      pass
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data = {
                                       "type": "flex",
                                       "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "25px",
            "backgroundColor": "#556788",
            "borderWidth": "2px",
            "offsetTop": "5px",
            "offsetStart": "8px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "25px",
            "backgroundColor": "#566788",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "."
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "168px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "31px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": wait["Respontag"],
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "5px"
              }
            ],
            "position": "absolute",
            "width": "137px",
            "height": "30px",
            "backgroundColor": "#ff0000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "32px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": cover,
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~guzaja24"
                }
              }
            ],
            "position": "absolute",
            "width": "122px",
            "height": "122px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "100px",
            "offsetTop": "69px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "TAG 100C",
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "offsetTop": "1px",
                "offsetStart": "26px"
              }
            ],
            "position": "absolute",
            "backgroundColor": "#ff0000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "20px",
            "width": "95px",
            "offsetTop": "154px",
            "offsetStart": "55px",
            "height": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{} ".format(contact.displayName),
                "size": "xxs",
                "color": "#ffffff",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "25px"
              }
            ],
            "position": "absolute",
            "width": "100px",
            "height": "20px",
            "backgroundColor": "#ff0000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "20px",
            "offsetTop": "132px",
            "offsetStart": "55px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~guzaja24"
                }
              }
            ],
            "position": "absolute",
            "width": "72px",
            "height": "72px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "100px",
            "offsetTop": "101px",
            "offsetStart": "10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "5px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": " RESPONTAG ",
                "size": "xs",
                "offsetTop": "3px",
                "offsetStart": "1px",
                "color": "#ffffff"
              }
            ],
            "width": "114px",
            "height": "25px",
            "backgroundColor": "#ff0000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "5px",
            "offsetStart": "31px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "5px",
            "offsetStart": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "backgroundColor": "#556788",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "8px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "25px",
            "height": "25px",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "119px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "🅑🅨: BF SLOTS",
                "size": "xs",
                "color": "#ffffff",
                "offsetTop": "1px",
                "offsetStart": "0px"
              }
            ],
            "width": "92px",
            "height": "25px",
            "backgroundColor": "#000000",
            "borderWidth": "2px",
            "borderColor": "#ffffff",
            "cornerRadius": "0px",
            "offsetTop": "200px",
            "offsetStart": "31px",
            "position": "absolute"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/b53ztTR/20190427-191019.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~guzaja24"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "64px",
            "offsetStart": "12px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
                "aspectRatio": "1:1",
                "size": "full",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~guzaja24"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "64px",
            "offsetStart": "121px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~guzaja24"
                }
              }
            ],
            "width": "20px",
            "cornerRadius": "100px",
            "offsetTop": "175px",
            "position": "absolute",
            "offsetStart": "13px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "http://line.me/ti/p/~guzaja24"
                }
              }
            ],
            "position": "absolute",
            "width": "20px",
            "height": "20px",
            "cornerRadius": "100px",
            "offsetTop": "175px",
            "offsetStart": "121px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#330033",
        "cornerRadius": "10px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        }
      }
    },
  ]
}
}
                           cl.postTemplate(to, data)
                        #   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"155808605","STKPKGID":"6700627","STKVER":"1"}, contentType=7)
                           break
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplate1(msg.to,"j̸͟͞a̸͟͞n̸͟͞g̸͟͞a̸͟͞n̸͟͞ t̸͟͞a̸͟͞g̸͟͞ g̸͟͞u̸͟͞a̸͟͞ n̸͟͞a̸͟͞n̸͟͞t̸͟͞i̸͟͞ k̸͟͞e̸͟͞j̸͟͞i̸͟͞t̸͟͞a̸͟͞k̸͟͞")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                 if wait["detectMention2"] == True:
                   contact = cl.getContact(msg._from)
                   tz = pytz.timezone("Asia/Jakarta")
                   timeNow = datetime.now(tz=tz)
                   cover = cl.getProfileCoverURL(sender)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           data = {
                                       "type": "flex",
                                       "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                                       "contents": {
"type": "carousel",
"contents": [
{
"type": "bubble",
"size": "micro",
"body": {
"backgroundColor": "#00ff00",
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSlAYhp6Fav-3Oh35aW19Aq1DCBA7ulrrZnE6hHar-UMit1G8eT",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "4:5",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uadef1340887c690dfad8b5307adcecf1",
"type": "uri",
}
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://www.jimphicdesigns.com/downloads/imgs-mockup/bouncy-ball-change-colors-animation.gif",
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uadef1340887c690dfad8b5307adcecf1",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "5px",
"offsetStart": "5px",
"height": "189px",
"width": "149px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
"gravity": "bottom",
"size": "full",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uadef1340887c690dfad8b5307adcecf1",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "10px",
"offsetStart": "10px",
"height": "179px",
"width": "139px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": cover, #"https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uadef1340887c690dfad8b5307adcecf1",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "image",
"url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
"gravity": "bottom",
"size": "xxl",
"aspectMode": "cover",
"aspectRatio": "2:3",
"offsetTop": "0px",
"action": {
"uri": "line://nv/profilePopup/mid=uadef1340887c690dfad8b5307adcecf1",
"type": "uri",
}}],
"position": "absolute",
"cornerRadius": "10px",
"offsetTop": "16px",
"offsetStart": "16px",
"height": "167px",
"width": "127px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "ʀᴇsᴘᴏɴ²", 
"align": "center",
"color": "#000000",
"size": "xxs",
"weight": "bold",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "19px",
"backgroundColor": "#ffd700",
"offsetStart": "20px",
"height": "14px",
"width": "45px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.gifer.com/THMv.gif", #https://thumbs.gfycat.com/RawThirstyJanenschia-size_restricted.gif",
"size": "full",
"action": {
"type": "uri",
"uri": "https://wa.me/08585921409",
},         
"flex": 0
}
],
"position": "absolute",
"offsetTop": "13px",
"offsetStart": "115px",
"height": "43px",
"width": "25px"
},
{
"type": "box",
"layout": "vertical",
"contents": [ #dsini
{
"type": "image",
"url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
"size": "xl",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~guzaja24",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
"size": "full",
"action": {
"type": "uri",
"uri": "http://line.me/ti/p/~guzaja24",
},
"flex": 0
},{
"type": "image",
"url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
"size": "xl",
"action": {
"type": "uri",
"uri": "Https://smule.com/kilua",
},
"flex": 0
}
],
"position": "absolute",
"offsetTop": "37px",
"offsetStart": "14px",
"height": "180px",
"width": "32px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "⏰"+ datetime.strftime(timeNow,'%H:%M:%S'),
"weight": "bold",
"color": "#ccffff",
#"align": "center",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "131px",
"backgroundColor": "#4b4b4b",
"offsetStart": "80px",
"height": "16px",
"width": "61px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": wait["Respontag2"],
"weight": "bold",
"color": "#93ff00",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "148px",
"backgroundColor": "#ff0000",
"offsetStart": "20px",
"height": "16px",
"width": "121px"
},
{
"type": "box",
"layout": "vertical",
"contents": [
{
"type": "text",
"text": "🚹{} ".format(contact.displayName),
"weight": "bold",
"color": "#ccffff",
"size": "xxs",
"offsetTop": "0px"
}
],
"position": "absolute",
"cornerRadius": "4px",
"offsetTop": "165px",
"backgroundColor": "#ac00c8",
"offsetStart": "20px",
"height": "16px",
"width": "121px"
}
],
#"backgroundColor": "#",
"paddingAll": "0px"
}
},
]
}
}
                           cl.postTemplate(to, data)
                           break

               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n°❂° STKID : " + msg.contentMetadata["STKID"] + "\n°❂° STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n°❂° STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"°❂° Nama : " + msg.contentMetadata["displayName"] + "\n°❂° MID : " + msg.contentMetadata["mid"] + "\n°❂° Status Msg : " + contact.statusMessage + "\n°❂° Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
        #
        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != cl.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "╔══[ Details Post ]"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = client.getContact(sender)
                                        auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n╠❂🇮🇩➢ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n╠❂🇮🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n╠❂🇮🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n╠❂🇮🇩➢ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n╠❂🇮🇩➢ Tulisan :\n╠❂🇮🇩➢ {}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n╚══[ Finish ]"
                                    sendpostTemplate(to, data)
                                except:
                                    sendTextTemplate(to, "❂🇮🇩➢ Done Like")
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                adws = cl.createComment(purl[0], purl[1], settings["commentPost"])
                                sendTextTemplatelike(to, "❂🇮🇩➢ Done Like")
            except Exception as error:
                logError(error)   

            if msg.contentType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            sendTextTemplate1(msg.to, "ʟɪsᴛ ʙʟ")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 sᴜᴋsᴇs ɪɴᴠɪᴛᴇ 」\nɴᴀᴍᴀ"
                                  ret_ = "ᴋᴇᴛɪᴋ ɪɴᴠɪᴛᴇ ᴏғғ ᴊɪᴋᴀ sᴜᴅᴀʜ ᴅᴏɴᴇ"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  sendTextTemplate1(msg.to,"ᴀɴᴅᴀ ᴛᴇʀᴋᴇɴᴀ sᴛʀᴜᴋ")
                                  wait["invite"] = False
                                  break
                                  
               if msg.contentType == 13:
                 if wait["Invi"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                cl.sendMessage(msg.to,"-> " + _name + " was here")
                                wait["Invi"] = False
                                break         
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(msg.to,[target])
                                sendTextTemplate1(msg.to,"ᴅᴏɴᴇ ᴊᴇᴘɪᴛ ᴊᴏᴍʙʟᴏ\n➡" + _name)
                                wait["Invi"] = False
                                break
#=============MEDIA FOTOBOT=============

               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            sendTextTemplate1(msg.to,"Send gambarnya...")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            sendTextTemplate1(msg.to,"ᴠɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ ᴅᴏɴᴇ")
               if msg.contentType == 1:
                  if msg._from in admin:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "ᴅᴏɴᴇ ɢᴀᴍʙᴀʀ {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in admin:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in admin:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "ᴅᴏɴᴇ sᴛɪᴄᴋᴇʀ {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in admin:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         sendTextTemplate1(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate1(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate1(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate1(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in admin:
                  if wait["delFriend"] == True:
                      cl.deleteContact(msg.contentMetadata["mid"])
                      cl.sendReplyMention(msg_id, to, "Udh Euyyy @!", [sender])

                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        sendTextTemplate1(msg.to,"ᴡᴇs ᴊᴀᴅɪ sᴛᴀғғ")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sendTextTemplate1(msg.to,"ᴅᴏɴᴇ ᴀᴅᴅsᴛᴀғғ")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"✅sᴛᴀғғ ᴅɪʜᴀᴘᴜs")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sendTextTemplate1(msg.to,"❎Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate1(msg.to,"✅Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate1(msg.to,"ᴅᴏɴᴇ ᴀᴅᴅᴀᴅᴍɪɴ")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"✅ᴀᴅᴍɪɴ ᴅɪʜᴀᴘᴜs")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate1(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate1(msg.to,"❎Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate1(msg.to,"✅Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate1(msg.to,"✅Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate1(msg.to,"❎Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate1(msg.to,"✅Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate2(msg.to,"✅Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate2(msg.to,"✅Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate1(msg.to,"❎Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate1(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False
               if msg.contentType == 2:
               	if settings["changevp"] == True:
               		contact = cl.getProfile()
               		path = cl.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		path1 = cl.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		sendTextTemplate1(to, "ᴅᴏɴᴇ vɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ")
               if msg.contentType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     sendTextTemplate1(msg.to, "ᴅᴏɴᴇ ᴘɪᴄᴛ ɢʀᴜᴘ")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if mid in Setmain["RAfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            cl.updateProfilePicture(path)
                            sendTextTemplate1(msg.to,"ғᴏᴛᴏ ʙᴇʀʜᴀsɪʟ")
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path5 = cl.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     cl.updateProfilePicture(path)
                     cl.sendMessage(msg.to, "Sukses..")
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "keybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = keybot()
                               sendTextTemplate25(msg.to, str(helpMessage))
                        if cmd == "bot on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate1(msg.to, "ʙᴏᴛ ᴡᴇs ᴏɴ")
                        elif cmd == "bot off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate25(msg.to, "ʙᴏᴛ ᴡᴇs ᴍᴏᴅᴀʀ")
                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	settings["changevp"] = True
                            	sendTextTemplate1(to, "sʜᴀʀᴇ ᴠɪᴅᴇᴏɴʏᴀ")
                        elif cmd == "แจ้งปัญหา":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage1 = helpcreator()
                               sendTextTemplate25(msg.to, str(helpMessage1))
                        elif cmd == "เมนูตั้งค่า":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage2 = helpsetting()
                               sendTextTemplate25(msg.to, str(helpMessage2))
                        elif cmd == "เมนูมีเดีย":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage3 = media()
                               sendTextTemplate25(msg.to, str(helpMessage3))
                        elif cmd == "เมนูกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage4 = helpgroup()       
                               sendTextTemplate25(msg.to, str(helpMessage4))
                        elif cmd == "เมนูแอดมิน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               helpMessage5 = helpadmin()
                               sendTextTemplate25(msg.to, str(helpMessage5))
                        elif cmd == "เมนู":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕 ",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴍᴇ\n◯ ᴠᴘ\n◯ sᴇᴛᴛɪɴɢ\n◯ ʀᴜɴᴛɪᴍᴇ\n◯ sᴘᴇᴇᴅ\n◯ sᴘ\n◯ sᴀɴᴛᴇᴛ ᴍᴀɴᴛᴀɴ\n◯ ʙʏᴇᴍᴇ\n◯ ʀᴇᴊᴇᴄᴛ\n◯ ғʀɪᴇɴᴅʟɪsᴛ", #1
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ʙᴏᴛᴀᴅᴅ\n◯ ʙᴏᴛᴅᴇʟʟ\n◯ sᴛᴀғғ\n◯ sᴛᴀғᴅᴇʟʟ\n◯ ᴀᴅᴍɪɴᴅᴇʟʟ\n◯ ᴀᴅᴍɪɴ\n◯ ʀᴇʙᴏᴏᴛ\n◯ ʙᴀɴ\n◯ ʙʟᴄ\n◯ ʙᴀɴ:", #2
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ɢᴍɪᴅ\n◯ ɢᴇᴛ ɪᴅ\n◯ ɢᴇᴛᴍɪᴅ\n◯ ɢᴇᴛʙɪᴏ\n◯ ɢᴇᴛɪɴғᴏ\n◯ ɢᴇᴛᴘʀᴏғɪʟᴇ\n◯ ɢᴇᴛᴘɪᴄᴛᴜʀᴇ\n◯ ɪɴғᴏ\n◯ ᴋᴇᴘᴏ\n◯ ᴘᴘᴠɪᴅᴇᴏ", #3
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴄᴇᴋ sɪᴅᴇʀ\n◯ ᴄᴇᴋ ʟᴇᴀᴠᴇ\n◯ ᴄᴇᴋ ᴘᴇsᴀɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ²\n◯ sᴇᴛ sɪᴅᴇʀ:\n◯ sᴇᴛ ᴘᴇsᴀɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ²:\n◯ sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ:", #4
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ Addsticker\n◯ Addmp3\n◯ Addaudio\n◯ Addimg\n◯ Dellsticker\n◯ Dellaudio\n◯ Dellmp3\n◯ Dellvideo\n◯ Dellimg\n◯ Liststicker", #5
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴀᴊsɴᴀᴍᴇ:\n◯ ᴀᴊsғᴏᴛᴏ\n◯ ᴀᴊs ᴄᴀɴᴄᴇʟ\n◯ ᴀᴊs ᴋɪᴄᴋᴀʟ\n◯ ᴀᴊs ᴀʙsᴇɴ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴄᴀɴᴄᴇʟᴀʟʟ\n◯ ᴄʀᴏᴛ\n◯ ɢᴋɪᴄᴋ", #6
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋᴏɴᴛᴀᴋ\n◯ ᴄᴏɴᴛᴀᴄᴛ:\n◯ ɢɴᴀᴍᴇ\n◯ ᴍʏᴍɪᴅ\n◯ ᴍʏʙɪᴏ\n◯ ᴍʏғᴏᴛᴏ\n◯ ᴍʏɴᴀᴍᴇ\n◯ ᴍʏᴘʀᴏғɪʟᴇ\n◯ ᴍʏᴘɪᴄᴛᴜʀᴇ\n◯ ᴍʏᴄᴏᴠᴇʀ", #7
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ sᴇᴛ ʟᴇᴀᴠᴇ:\n◯ ʟɪᴋᴇ\n◯ ᴘᴏsᴛ\n◯ sᴛɪᴄᴋᴇʀ\n◯ ɪɴᴠɪᴛᴇ\n◯ ᴜɴsᴇɴᴅ\n◯ ʀᴇsᴘᴏɴ\n◯ ʀᴇsᴘᴏɴ²\n◯ ᴀᴜᴛᴏᴀᴅᴅ\n◯ ᴡᴇʟᴄᴏᴍᴇ", #8
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ Listimage\n◯ Listvideo\n◯ Listaudio\n◯ Listmp3\n◯ Lihat\n◯ Cctv metro\n◯ Ocmp4\n◯ Joox\n◯ mp4\n◯ mp3", #9
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋɪᴄᴋ\n◯ sᴛᴀʏ\n◯ ᴊs ɪɴ-ᴏᴜᴛ\n◯ ɢʟɪsᴛᴊs\n◯ ᴋ1-ɪɴᴠɪᴛ\n◯ ᴀᴅᴅᴀsɪs\n◯ ʙʀᴏᴀᴅᴄᴀsᴛ:\n◯ ɢʀᴜᴘᴘɪᴄᴛ\n◯ ɪɴғᴏɢʀᴏᴜᴘ ɴᴏ\n◯ ɪɴғᴏᴍᴇᴍ ɴᴏ", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)
                        elif cmd == "เมนูเจเอส":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕 ",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ #habisin\n◯ #bantai\n◯ #geboy\n◯ tanpasisa", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)

                        elif cmd == "เมนูบีเอฟ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               contact = cl.getProfile()
                               mids = [contact.mid]
                               cover = cl.getProfileCoverURL(sender)
                               listTimeLiking = time.time()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {
                                       "type": "flex",
                                       "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕 ",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ Ginfo: no\n◯ Open: no\n◯ Close: no\n◯ Ticket: no\n◯ member: no\n◯ pendingan: no\n◯ Cancel: no\n◯ Zul no\n◯ js: no\n◯ jiran no", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                               cl.postTemplate(to, data)
                        elif cmd.startswith("เมนูบอท"):
                           if msg._from in admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                ky = key["MENTIONEES"][0]["M"]                
                                m = cl.getContact(ky)                                
                                data = {
                                       "type": "flex",
                                       "altText": "〔 BF SLOT เข้าใจวัยรุ่น 〕 ",
                                       "contents": {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴍᴇ\n◯ ᴠᴘ\n◯ sᴇᴛᴛɪɴɢ\n◯ ʀᴜɴᴛɪᴍᴇ\n◯ sᴘᴇᴇᴅ\n◯ sᴘ\n◯ sᴀɴᴛᴇᴛ ᴍᴀɴᴛᴀɴ\n◯ ʙʏᴇᴍᴇ\n◯ ʀᴇᴊᴇᴄᴛ\n◯ ғʀɪᴇɴᴅʟɪsᴛ", #1
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ʙᴏᴛᴀᴅᴅ\n◯ ʙᴏᴛᴅᴇʟʟ\n◯ sᴛᴀғғ\n◯ sᴛᴀғᴅᴇʟʟ\n◯ ᴀᴅᴍɪɴᴅᴇʟʟ\n◯ ᴀᴅᴍɪɴ\n◯ ʀᴇʙᴏᴏᴛ\n◯ ʙᴀɴ\n◯ ʙʟᴄ\n◯ ʙᴀɴ:", #2
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
          "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ɢᴍɪᴅ\n◯ ɢᴇᴛ ɪᴅ\n◯ ɢᴇᴛᴍɪᴅ\n◯ ɢᴇᴛʙɪᴏ\n◯ ɢᴇᴛɪɴғᴏ\n◯ ɢᴇᴛᴘʀᴏғɪʟᴇ\n◯ ɢᴇᴛᴘɪᴄᴛᴜʀᴇ\n◯ ɪɴғᴏ\n◯ ᴋᴇᴘᴏ\n◯ ᴘᴘᴠɪᴅᴇᴏ", #3
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44"
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴄᴇᴋ sɪᴅᴇʀ\n◯ ᴄᴇᴋ ʟᴇᴀᴠᴇ\n◯ ᴄᴇᴋ ᴘᴇsᴀɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ\n◯ ᴄᴇᴋ ʀᴇsᴘᴏɴ²\n◯ sᴇᴛ sɪᴅᴇʀ:\n◯ sᴇᴛ ᴘᴇsᴀɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ:\n◯ sᴇᴛ ʀᴇsᴘᴏɴ²:\n◯ sᴇᴛ ᴡᴇʟᴄᴏᴍᴇ:", #4
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ Addsticker\n◯ Addmp3\n◯ Addaudio\n◯ Addimg\n◯ Dellsticker\n◯ Dellaudio\n◯ Dellmp3\n◯ Dellvideo\n◯ Dellimg\n◯ Liststicker", #5
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴀᴊsɴᴀᴍᴇ:\n◯ ᴀᴊsғᴏᴛᴏ\n◯ ᴀᴊs ᴄᴀɴᴄᴇʟ\n◯ ᴀᴊs ᴋɪᴄᴋᴀʟ\n◯ ᴀᴊs ᴀʙsᴇɴ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴘᴀs ʙᴀɴᴅ\n◯ ᴄᴀɴᴄᴇʟᴀʟʟ\n◯ ᴄʀᴏᴛ\n◯ ɢᴋɪᴄᴋ", #6
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋᴏɴᴛᴀᴋ\n◯ ᴄᴏɴᴛᴀᴄᴛ:\n◯ ɢɴᴀᴍᴇ\n◯ ᴍʏᴍɪᴅ\n◯ ᴍʏʙɪᴏ\n◯ ᴍʏғᴏᴛᴏ\n◯ ᴍʏɴᴀᴍᴇ\n◯ ᴍʏᴘʀᴏғɪʟᴇ\n◯ ᴍʏᴘɪᴄᴛᴜʀᴇ\n◯ ᴍʏᴄᴏᴠᴇʀ", #7
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ sᴇᴛ ʟᴇᴀᴠᴇ:\n◯ ʟɪᴋᴇ\n◯ ᴘᴏsᴛ\n◯ sᴛɪᴄᴋᴇʀ\n◯ ɪɴᴠɪᴛᴇ\n◯ ᴜɴsᴇɴᴅ\n◯ ʀᴇsᴘᴏɴ\n◯ ʀᴇsᴘᴏɴ²\n◯ ᴀᴜᴛᴏᴀᴅᴅ\n◯ ᴡᴇʟᴄᴏᴍᴇ", #8
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ Listimage\n◯ Listvideo\n◯ Listaudio\n◯ Listmp3\n◯ Lihat\n◯ Cctv metro\n◯ Ocmp4\n◯ Joox\n◯ mp4\n◯ mp3", #9
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {
         "backgroundColor": "#5eff7e"
        }
      }
    },
    {                                      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(m.pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "size": "xs",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "25px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "MENU HELP",
                "size": "xs",
                "color": "#2bff44",
                "weight": "bold",
                "style": "normal",
                "align": "center"
              }
            ],
            "position": "absolute",
            "width": "105px",
            "height": "15px",
            "offsetTop": "5px",
            "offsetStart": "20px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": ".",
                "color": "#2bff44",
                "size": "xxs"
              }
            ],
            "position": "absolute",
            "width": "125px",
            "height": "1px",
            "backgroundColor": "#5eff7e",
            "offsetTop": "200px",
            "offsetStart": "15px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xs",
                "style": "normal",
                "weight": "bold",
                "align": "center",
                "color": "#2bff44",
              }
            ],
            "position": "absolute",
            "width": "148px",
            "height": "25px",
            "offsetTop": "205px",
            "offsetStart": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "\n◯ ᴋɪᴄᴋ\n◯ sᴛᴀʏ\n◯ ᴊs ɪɴ-ᴏᴜᴛ\n◯ ɢʟɪsᴛᴊs\n◯ ᴋ1-ɪɴᴠɪᴛ\n◯ ᴀᴅᴅᴀsɪs\n◯ ʙʀᴏᴀᴅᴄᴀsᴛ:\n◯ ɢʀᴜᴘᴘɪᴄᴛ\n◯ ɪɴғᴏɢʀᴏᴜᴘ ɴᴏ\n◯ ɪɴғᴏᴍᴇᴍ ɴᴏ", #10
                "size": "xxs",
                "weight": "bold",
                "color": "#2bff44",
                "style": "normal",
                "wrap": True,
                "offsetTop": "0px",
                "offsetStart": "0px"
              }
            ],
            "position": "absolute",
            "offsetTop": "28px",
            "offsetStart": "15px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "3px",
        "borderColor": "#5eff7e",
        "cornerRadius": "15px"
      },
      "styles": {
        "body": {         
         "backgroundColor": "#5eff7e"
        }
      }
    }
  ]
}
}
                                cl.postTemplate(to, data)                                                                
                      
                        elif cmd.startswith("ชื่อ "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cl.renameContact(ls,sep[1])
                                        cl.sendReplyMention(msg_id, to, "Succes change @! display name to {}".format(sep[1]), [ls])

                        elif cmd == "ตั้งค่า":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                cover = cl.getProfileCoverURL(sender)
                                listTimeLiking = time.time()
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = ""
                                if settings["checkPost"] == True: md+="║║⏹️ Post : ✅\n"
                                else: md+="║║⏹️ Post : ❌\n"
                                if wait["likeOn"] == True: md+="║║⏹️ Like : ✅\n"
                                else: md+="║║⏹️ Like ❌\n"
                                if wait["contact"] == True: md+="║║⏹️ Contact : ✅\n"
                                else: md+="║║⏹️ Contact : ❌\n"
                                if wait["Mentionkick"] == True: md+="║║⏹️ Notag : ✅\n"
                                else: md+="║║⏹️ Notag : ❌\n"
                                if wait["detectMention"] == True: md+="║║⏹️ Respontag : ✅\n"
                                else: md+="║║⏹️ Respontag : ❌\n"
                                if wait["detectMention2"] == True: md+="║║⏹️ Respontag2 : ✅\n"
                                else: md+="║║⏹️ Respontag2 : ❌\n"
                                if wait["Unsend"] == True: md+="║║⏹️ Unsend : ✅\n"
                                else: md+="║║⏹️ Unsend : ❌\n"
                                if wait["autoAdd"] == True: md+="║║⏹️ Autoadd : ✅\n"
                                else: md+="║║⏹️ Autoadd : ❌\n"
                                if wait["autoLeave"] == True: md+="║║⏹️ Autoleave : ✅\n"
                                else: md+="║║⏹️ Autoleave : ❌\n"
                                if wait["autoJoin"] == True: md+="║║⏹️ Autojoin : ✅\n"
                                else: md+="║║⏹️ Autojoin : ❌\n"
                                if wait["sticker"] == True: md+="║║⏹️ Sticker : ✅\n"
                                else: md+="║║⏹️ Sticker ❌\n"
                                if settings["autoJoinTicket"] == True: md+="║║⏹️ Jointicket : ✅\n"
                                else: md+="║║⏹️ Jointicket : ❌\n"
                                if wait["autoReject"] == True: md+="║║⏹️ Autoreject : ✅\n"
                                else: md+="║║⏹️ Autoreject : ❌\n"
                                if wait["autoBlock"] == True: md+="║║⏹️ Autoblock : ✅\n"
                                else: md+="║║⏹️ Autoblock : ❌\n"
                                if settings["welcome"] == True: md+="║║⏹️ Welcome : ✅\n"
                                else: md+="║║⏹️ Welcome : ❌\n"
                                sendTextTemplate23(msg.to, "╔════════════════\n"+ md +"╚════════════════")

                        elif text.lower() == "มิด":
                          if wait["selfbot"] == True:
                               middd = "Name : " +cl.getContact(msg._from).displayName + "\nMid : " +msg._from
                               cl.sendMessage(msg.to,middd)

                        elif ("ชื่อกลุ่ม: " in msg.text):
                          if msg._from in admin:
                              X = cl.getGroup(msg.to)
                              X.name = msg.text.replace("ชื่อกลุ่ม ","")
                              cl.updateGroup(X)

                        elif "รูปกลุ่ม" in msg.text:
                          if msg._from in admin:
                                group = cl.getGroup(msg.to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                cl.sendImageWithURL(msg.to,path)

                        elif "ก็อปโปร " in msg.text:
                          if msg._from in admin:
                            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        profile = cl.getContact(mention['M'])
                                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                                    except Exception as e:
                                        pass

                        elif "ก็อปข้อมูล " in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = cl.getContact(key1)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            try:
                                sendTextTemplate1(msg.to,"Nama:\n" + contact.displayName)
                                sendTextTemplate1(msg.to,"Bio:\n" + contact.statusMessage)
                                cl.sendImageWithURL(msg.to,image)
                            except:
                                pass

                        elif cmd == 'แบล็คลิส':
                          if msg._from in admin:
                            blockedlist = cl.getBlockedContactIds()
                            kontak = cl.getContacts(blockedlist)
                            num=1
                            msgs="รายชื่อบันชีดำ"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nบล็อคทั้งหมด : %i" % len(kontak)
                            sendTextTemplate2(to, msgs)

                        elif "สเตตัส " in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = cl.getContact(key1)
                            try:
                                sendTextTemplate1(msg.to,contact.statusMessage)
                            except:
                                sendTextTemplate1(msg.to,"⟦ʙɪᴏ ᴇᴍᴘᴛʏ⟧")

                        elif text.lower() == 'kalender':
                          if msg._from in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                            sendTextTemplate2(msg.to, readTime)

                        elif cmd == "บอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                               bot1.sendMessage(msg.to, "ครับ")

                        elif cmd == "ชื่อ":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            sendTextTemplate1(to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))

                        elif cmd == "สเตตัส":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            sendTextTemplate1(to, "[ sᴛᴀᴛᴜs ʟɪɴᴇ ]\n{}".format(contact.statusMessage))

                        elif cmd == "รูป":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                        elif cmd == "วีดีโอ":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            cl.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                        elif cmd == "โปรโมท":
                          if msg._from in admin:
                              data = {  
 "type": "flex",
 "altText": "้โปรผีบอก....",
 "contents":
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/kk.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:23.6",
        "animated": true
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "สมัครกดตรงนี้",
            "weight": "bold",
            "align": "center",
            "color": "#ffdd00",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://https://bit.ly/3FAGjJN"
            }
          }
        ],
        "backgroundColor": "#000000",
        "justifyContent": "space-evenly",
        "borderColor": "#ffdd00",
        "background": {
          "type": "linearGradient",
          "angle": "70deg",
          "startColor": "#00000050",
          "endColor": "#000000",
          "centerColor": "#ffffff50"
        }
      }
    },
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/pros.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:23.6",
        "animated": true
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ติดต่อโปรโมทเว็บคลิ๊ก",
            "weight": "bold",
            "align": "center",
            "color": "#ffdd00",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://lin.ee/9FX1chx"
            }
          }
        ],
        "backgroundColor": "#000000",
        "justifyContent": "space-evenly",
        "borderColor": "#ffdd00",
        "background": {
          "type": "linearGradient",
          "angle": "70deg",
          "startColor": "#00000050",
          "endColor": "#000000",
          "centerColor": "#ffffff50"
        }
      }
    }
  ]
}
 
  }

                              gb = cl.getGroupIdsJoined()
                              for gp in gb:
                                  cl.postTemplate(gp, data)

                        elif cmd.startswith("nasa"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               data = {  
 "type": "flex",
 "altText": "้โปรผีบอก....",
 "contents":
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/kk.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:23.6",
        "animated": true
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "สมัครกดตรงนี้",
            "weight": "bold",
            "align": "center",
            "color": "#ffdd00",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://https://bit.ly/3FAGjJN"
            }
          }
        ],
        "backgroundColor": "#000000",
        "justifyContent": "space-evenly",
        "borderColor": "#ffdd00",
        "background": {
          "type": "linearGradient",
          "angle": "70deg",
          "startColor": "#00000050",
          "endColor": "#000000",
          "centerColor": "#ffffff50"
        }
      }
    },
    {
      "type": "bubble",
      "size": "giga",
      "hero": {
        "type": "image",
        "url": "https://slotthai.ml/img/pros.png",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:23.6",
        "animated": true
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ติดต่อโปรโมทเว็บคลิ๊ก",
            "weight": "bold",
            "align": "center",
            "color": "#ffdd00",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://lin.ee/9FX1chx"
            }
          }
        ],
        "backgroundColor": "#000000",
        "justifyContent": "space-evenly",
        "borderColor": "#ffdd00",
        "background": {
          "type": "linearGradient",
          "angle": "70deg",
          "startColor": "#00000050",
          "endColor": "#000000",
          "centerColor": "#ffffff50"
        }
      }
    }
  ]
}
 
  }                              
                               
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.postTemplate(group, data)
                                 #"""
                        elif cmd.startswith("แชร์"):
                            if msg._from in creator or msg._from in admin:
                                groups = cl.getGroupIdsJoined()
                                groupb = bot1.getGroupIdsJoined()
                                
                                for group1 in groupb:
                                    try:
                                        time.sleep(0/200)
                                        
                                        bot1.postTemplatework(group1, web188)
                                    except:pass 

                                for group in groups:
                                    try:
                                        time.sleep(0/200)
                        
                                        
                                        cl.postTemplateworks(group, web168)
                                    except:pass  
#broadcast
                        elif cmd.startswith("เพื่อน"):
                          if msg._from in admin:
                              contacts = cl.getAllContactIds()
                              for contact in contacts:
                                  try:
                                    time.sleep(20)
                                    
                                    cl.postTemplatework(contact, web168)
                                    bot1.postTemplateworks(contact, web188)
                                  except:pass  

                        elif cmd == "โปรไฟล์":
                          if msg._from in admin:
                            text = "~ Profile ~"
                            contact = cl.getContact(sender)
                            cover = cl.getProfileCoverURL(sender)
                            result = "╔══[ Details Profile ]"
                            result += "\n├≽ Display Name : @!"
                            result += "\n├≽ Mid : {}".format(contact.mid)
                            result += "\n├≽ Status Message : {}".format(contact.statusMessage)
                            result += "\n├≽ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n├≽ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            cl.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            cl.sendMentionWithFooter(to, text, result, [sender])

                        elif cmd.startswith("บล็อค"):
                          if msg._from in admin:
                            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.blockContact(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, "sᴜᴋsᴇs ʙʟᴏᴄᴋ ᴋᴏɴᴛᴀᴋ" + str(contact.displayName) + "ᴍᴀsᴜᴋ ᴅᴀғᴛᴀʀ ʙʟᴏᴄᴋʟɪsᴛ")

                        elif cmd.startswith("คท "):
                          if msg._from in admin:
                            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.findAndAddContactsByMid(ls)
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, "ʙᴇʀʜᴀsɪʟ ᴀᴅᴅ" + str(contact.displayName) + "ᴋᴜʀɪɴᴇᴍ ᴅᴜʟᴜ ʏᴀᴄʜ")

                        elif "Getmid " in msg.text:
                            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', msg.text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    try:
                                        cl.sendMessage(msg.to,str(mention['M']))
                                    except Exception as e:
                                        pass

                        elif "ข้อมูล " in msg.text:
                           if msg._from in admin:
                              mmid = msg.text.replace("ข้อมูล ","")
                              msg.contentType = 13
                              msg.contentMetadata = {"mid":mmid}
                              cl.sendMessage(msg.to, None, contentMetadata={'mid': mmid}, contentType=13)
                              path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                              image = 'http://dl.profile.line.naver.jp'+path
                              cl.sendImageWithURL(msg.to, image)

                        elif cmd.startswith("คท"):
                          if msg._from in admin:
                            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.sendContact(to,str(ls))

                        elif cmd.startswith("ppvideo"):
                          if msg._from in admin:
                            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                    cl.sendVideoWithURL(to, str(path))

                        elif text.lower() == wait["clear"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   sendTextTemplate(msg.to,"mantan berhasil disantet")
                               except:
                                   pass

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate1(msg.to, "☛ Nama : "+str(mi.displayName)+"\n☛ Mid : " +key1+"\n☛ Status Msg"+str(mi.statusMessage))
                               sendTextTemplate1(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "รีสตาร์ท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate23(msg.to, "ʀᴇsᴛᴀʀᴛ ʙᴏᴛ")
                               wait["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate1(msg.to, "ᴅᴏɴᴇ ʙᴏs")
#============================ABOUT====================================
                        elif cmd == "about":
                                groups = cl.getGroupIdsJoined()
                                contacts = cl.getAllContactIds()
                                blockeds = cl.getBlockedContactIds()
                                crt = "uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1"
                                supp = "uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1","uadef1340887c690dfad8b5307adcecf1"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nâ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "ᴀʙᴏᴜᴛ",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "size": "micro",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "TEAM\nTERMUX",
            "size": "xxs",
            "color": "#FFFF00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": " {}".format(cl.getProfile().displayName),
                "size": "xxs",
                "margin": "none",
                "color": "#ADFF2F",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "text": "ɢʀᴏᴜᴘ: {}".format(str(len(groups))),
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "ғʀɪᴇɴᴅ: {}".format(str(len(contacts))),
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "ʙʟᴏᴄᴋ: {}".format(str(len(blockeds))),
                "size": "xxs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "BF SLOTS เข้าใจวัยรุ่น",
        "size": "xxs",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "https://slotthai.gq"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "WEB BF SLOTS",
        "size": "xxs",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "httpS://slotthai.ml"
        },
        "align": "center"
      }
    ]
  }
}
}
                                cl.postTemplate(to, data)
                        
                        elif text.lower() == 'ไป':
                                                      	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)
                                data = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": ",〔 BF SLOT เข้าใจวัยรุ่น 〕",
            "size": "lg",
            "color": "#000000",
            "align": "center",
            "weight": "bold",
            "offsetTop": "5px"
          }
        ],
        "position": "absolute",
        "offsetBottom": "248px",
        "offsetStart": "7px",
        "offsetEnd": "0px",
        "borderColor": "#ff0000",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "282px",
        "height": "40px",
        "backgroundColor": "#00fdff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "List Bot",
            "size": "lg",
            "color": "#00fdff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "5px"
          }
        ],
        "position": "absolute",
        "offsetBottom": "198px",
        "offsetStart": "7px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "140px",
        "height": "45px",
        "backgroundColor": "#000000aa"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Harga Bots",
            "size": "lg",
            "color": "#00fdff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "5px"
          }
        ],
        "position": "absolute",
        "offsetBottom": "198px",
        "offsetStart": "149px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "140px",
        "height": "45px",
        "backgroundColor": "#000000aa"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Selfbot Temp",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          },
          {
            "type": "text",
            "text": "Sel Temp Ajs",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          },
          {
            "type": "text",
            "text": "Sel Asis Ajs",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          },
          {
            "type": "text",
            "text": "Pro rom chat",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          },
          {
            "type": "text",
            "text": "HelperGolang",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetEnd": "5px"
          }
        ],
        "position": "absolute",
        "offsetStart": "7px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "120px",
        "height": "105px",
        "offsetTop": "100px",
        "backgroundColor": "#000000aa"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Rp.50K",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": "Rp.100",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": "Rp.150",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": "Rp.PmC",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": "Rp.350",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "weight": "bold",
            "offsetTop": "8px",
            "offsetStart": "5px"
          }
        ],
        "position": "absolute",
        "offsetStart": "169px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "120px",
        "height": "105px",
        "offsetTop": "100px",
        "backgroundColor": "#000000aa"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "offsetBottom": "15px"
          },
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "size": "full",
            "offsetBottom": "35px",
            "aspectRatio": "2:3"
          }
        ],
        "position": "absolute",
        "offsetStart": "118px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "60px",
        "height": "105px",
        "offsetTop": "100px",
        "backgroundColor": "#000000"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Tak Ada Yang Sempurna",
                "color": "#000000",
                "align": "center",
                "weight": "bold"
              }
            ],
            "backgroundColor": "#00fdff",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "10px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "bf Slot รับโปรโมทเว็บพนัน และสินค้าทุกชนิด ด้วยทีมงานมืออาชีพและเครื่องมือทันสมัย ถ้ามีโอกาสให้คุณได้ลูกค้าใหม่ๆจากทีมงานที่มีประสบการณ์สนใจติดต่อคลิ๊ก  !!!",
                "color": "#000000",
                "align": "center",
                "weight": "bold",
                "size": "xxs",
                "style": "italic",
                "wrap": True
              }
            ],
            "backgroundColor": "#ffffff",
            "borderWidth": "2px",
            "borderColor": "#000000",
            "cornerRadius": "10px",
            "height": "54px"
          }
        ],
        "position": "absolute",
        "offsetStart": "7px",
        "offsetEnd": "0px",
        "borderColor": "#00fdff",
        "borderWidth": "2px",
        "cornerRadius": "4px",
        "width": "282px",
        "height": "82px",
        "offsetTop": "208px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
            "size": "full",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "label": "action",
              "uri": "https://slotthai.ml"
            }
          }
        ],
        "position": "absolute",
        "width": "80px",
        "height": "80px",
        "offsetTop": "150px",
        "offsetStart": "230px"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#00fdff",
    "borderWidth": "2px",
    "cornerRadius": "15px"
  }
}
                                cl.postTemplate(to, data)
                                cl.leaveGroup(to)

                        elif text.lower() == "บอทออก":
                            if msg._from in admin:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    print ("Pamit semua group")

                        elif text.lower() == "ลบรัน":
                            if msg._from in admin:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    sendTextTemplate1(msg.to, "Done cancell {} Grup".format(str(len(ginvited))))
                                else:
                                    sendTextTemplate1(msg.to, "Nothing Invited")

                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "🔽ʙᴏᴛ ʀᴜɴ : " +waktu(eltime)
                               sendTextTemplate1(msg.to,bot)

                        elif cmd == "listpending":
                          if wait["selfbot"] == True:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                ret_ = "╭───「 Pending List 」"
                                no = 0
                                if group.invitee is None or group.invitee == []:
                                    return cl.sendReplyMessage(msg_id, to, "Tidak ada pendingan")
                                else:
                                    for pending in group.invitee:
                                        no += 1
                                        ret_ += "\n├≽ {}. {}".format(str(no), str(pending.displayName))
                                    ret_ += "\n╰───「 Total {} Pending 」".format(str(len(group.invitee)))
                                    #cl.sendReplyMessage(msg_id, to, str(ret_))
                                    data = {
                                        "type": "text",
                                        "text": "{}".format(str(ret_)),
                                        "sentBy": {
                                            "label": " 🔰〔 BF SLOT เข้าใจวัยรุ่น 〕🔰",
                                            "iconUrl": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
                                            "linkUrl": "line://nv/profilePopup/mid=uadef1340887c690dfad8b5307adcecf1"
                                        }
                                    }
                                    cl.postTemplate(to, data)

                        elif cmd == "delfriend on":
                            if msg._from in admin:                          
                                if wait["delFriend"] == True:
                                    sendTextTemplate1(to, "Send Contact !!!!")
                                else:
                                    wait["delFriend"] = True
                                    sendTextTemplate1(to, "Send Contact :)")

                        elif cmd == "delfriend off":
                            if msg._from in admin:                          
                                if wait["delFriend"] == False:
                                    sendTextTemplate1(to, "Udah Ga aktif !!!")
                                else:
                                    wait["delFriend"] = False
                                    sendTextTemplate1(to, "Berhasil off delete friend")

                        elif cmd.startswith("ลบเพื่อน "):
                              if msg._from in admin:
                                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cl.deleteContact(ls)
                                        sendTextTemplate1(to, "Udah Boss Ku")

                        elif cmd == "listmember":
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                num = 0
                                ret_ = "╔══[ List Member ]"
                                for contact in group.members:
                                    num += 1
                                    ret_ += "\n╠ {}. {}".format(num, contact.displayName)
                                ret_ += "\n╚══[ Total {} Members]".format(len(group.members))
                                sendTextTemplate2(to, ret_)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate23(msg.to, "  •⌻「Grup Info」⌻•\n\n Nama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                sendTextTemplate2(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sendTextTemplate23(msg.to, str(e))

                        elif cmd.startswith("ข้อมูลกลุ่ม"):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(danil.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔══「 Info Group 」"
                                ret_ += "\n┣[]► Nama Group : {}".format(G.name)
                                ret_ += "\n┣[]► ID Group : {}".format(G.id)
                                ret_ += "\n┣[]► Pembuat : {}".format(gCreator)
                                ret_ += "\n┣[]► Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n┣[]► Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n┣[]► Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣[]► Group Qr : {}".format(gQr)
                                ret_ += "\n┣[]► Group Ticket : {}".format(gTicket)
                                ret_ += "\n╚══「 Info Finish 」"
                                sendTextTemplate23(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem"):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = denal.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n┣[]► "+ str(no) + ". " + mem.displayName
                                sendTextTemplate23(to,"╔══「 Group Info 」\n┣[]► Group Name : " + str(G.name) + "\n┣══「Member List」" + ret_ + "\n╚══「Total %i Members」" % len(G.members))
                            except:
                                pass
                        elif cmd == "ชื่อเพื่อน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠[]► " + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate23(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")
#invite for mention

                        elif "เชิญ " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass

                        elif cmd == "ดูกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "●" + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate23(msg.to,"    ● GROUP LIST ●\n●\n"+ma+"\n    ●Total "+str(len(gid))+" Groups ●")

                        elif cmd == "ลิ้งกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "เปิดคิวอาร์กลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   if X.preventedJoinByTicket == True:
                                       X.preventedJoinByTicket = False
                                       cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to, "Nama : "+str(X.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "ปิดคิวอาร์กลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate1(msg.to, "ปิดลิ้งค์")

                        elif cmd == "ค้างเชิญ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  sendTextTemplate1(to, "ᴛᴏᴛᴀʟ {} ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                              else:
                                  sendTextTemplate1(to, "ʙᴇʀsɪʜ")
#===========BOT UPDATE============#
                        elif cmd == "เปลี่ยนรูปกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate1(msg.to,"☛ ส่งรูปมาจร้า")

                        elif cmd == "เปลี่ยนรูป":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                sendTextTemplate1(msg.to,"☛ ส่งรูปมาครับ")
                        elif cmd.startswith("ชื่อ: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                         
                        elif cmd.startswith("สเตตัส: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.statusMessage = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to, "✔sᴜᴋsᴇs " + string + "")
                                         
                        elif cmd == "!cl" or text.lower() == "ยกเลิกเชิญ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                           #     projoin.append(msg.to)
                                xyz = cl.getGroup(to)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in cl.profile.mid:targp.append(x)
                                imnoob = 'cancel.js gid={} token={}'.format(to, cl.authToken)
                                for x in targp:imnoob += ' uid={}'.format(x)
                                execute_js(imnoob)
                                   
                        elif cmd == "!ancel" or text.lower() == '.goo':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "Kosong.....")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Bots:
                                       klist=[mid]
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.00001)
                                       print (msg.to, [x])
                          if msg._from in admin:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for x in gs.members:
                                    targets.append(x.mid)
                                for a in admin:
                                    if a in targets:
                                        try:
                                            targets.remove(a)
                                        except:
                                            pass
                                for target in targets:
                                    try:
                                        klist=[mid]
                                        cl.kickoutFromGroup(msg.to,[target])
                                        time.sleep(0.00001)
                                        print (msg.to,[g.mid])
                                    except:
                                        pass
                                        
                                     
                        if text.startswith('เปืดคิวอาร์ '):
                            if msg._from in admin:
                	            separate = text.split(" ")
                	            number = text.replace(separate[0] + " ","")
                	            groups = cl.getGroupIdsJoined()
                	            ret_ = ""
                	            try:
                	                group = groups[int(number)-1]
                	                G = cl.getGroup(group)
                	                G.preventedJoinByTicket = False
                	                cl.updateGroup(G)
                	                try:
                	                    gCreator = G.creator.mid
                	                    dia = cl.getContact(gCreator)
                	                    zx = ""
                	                    zxc = ""
                	                    zx2 = []
                	                    xpesan = '「 Sukses Open Qr 」\n• Creator :  '
                	                    diaa = str(dia.displayName)
                	                    pesan = ''
                	                    pesan2 = pesan+"@a\n"
                	                    xlen = str(len(zxc)+len(xpesan))
                	                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                	                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                	                    zx2.append(zx)
                	                    zxc += pesan2
                	                except:
                	                    gCreator = "Tidak ditemukan"
                	                if G.invitee is None:
                	                    gPending = "0"
                	                else:
                	                    gPending = str(len(G.invitee))
                	                if G.preventedJoinByTicket == True:
                	                    gQr = "Tertutup"
                	                    gTicket = "Tidak ada"
                	                else:
                	                    gQr = "Terbuka"
                	                    gTicket = "http://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                	                timeCreated = []
                	                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                	                #ret_ += xpesan+zxc
                	                ret_ += "• Nama : {}".format(G.name)
                	                ret_ += "\n• Group Qr : {}".format(gQr)
                	                ret_ += "\n• Pendingan : {}".format(gPending)
                	                ret_ += "\n• Group Ticket : {}".format(gTicket)
                	                ret_ += ""
                	                cl.sendMessage(msg.to,ret_)
                	            except:pass
                     

#=============={{{{{BATAS}}}}}}}=========
                        elif cmd == "เปิดอ่าน":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "ระบบตรวจจับคนอ่านเปิดใช้งาน")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "ปิดอ่าน":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "ปิดระบบจับคนอ่านเรียบร้อยครับ")
                              else:
                                  sendTextTemplate(msg.to, "sɪᴅᴇʀ ᴅɪ ᴏғғ")
#=========== [ Hiburan] ============#
                        elif cmd.startswith("js: "):
                          if msg._from in admin:
                             separate = text.split(" ")
                             number = text.replace(separate[0] + " ","")
                             groups = cl.getGroupIdsJoined()
                             listGroup = groups[int(number)-1]
                             x = cl.getGroup(listGroup)
                             if x.members == None:nama = []
                             else:nama = [contact.mid for contact in x.members]
                             targets = []
                             for a in nama:
                             	if a not in ["ub40fc41841841f37c8ad66bc55051058","u723a47ca491b77de2eea720ec40538ac","uc1f01ad80551c2e5e35610fec7e43582",cl.profile.mid]:targets.append(a)
                             if targets:
                              lolz = 'simple.js gid={} token={}'.format(x.id, cl.authToken)
                              for target in targets:
                                lolz += ' uid={}'.format(target)
                              success = execute_js(lolz)
                              if success:sendTextTemplate1(to, "Success kickall %i members." % len(targets))
                              else:sendTextTemplate1(to, "Failed kick %i members." % len(targets))
                        elif cmd.startswith("jiran "):
                          if msg._from in admin:
                           separate = text.split(" ")
                           number = text.replace(separate[0] + " ","")
                           groups = cl.getGroupIdsJoined()
                           listGroup = groups[int(number)-1]
                           x = cl.getGroup(listGroup)
                           if x.invitee == None:nama = []
                           else:nama = [contact.mid for contact in x.invitee]
                           targets = []
                           for a in nama:
                           	if a not in ["ub40fc41841841f37c8ad66bc55051058","u723a47ca491b77de2eea720ec40538ac","uc1f01ad80551c2e5e35610fec7e43582",cl.profile.mid]:targets.append(a) 
                           nami = [contact.mid for contact in x.members]
                           targetk = []
                           lolz = 'dual.js gid={} token={}'.format(x.id, cl.authToken)
                           for a in nami:
                           	if a not in ["ub40fc41841841f37c8ad66bc55051058","u723a47ca491b77de2eea720ec40538ac","uc1f01ad80551c2e5e35610fec7e43582",cl.profile.mid]:targetk.append(a) 
                           for y in targets:
                           	lolz += ' uid={}'.format(y)
                           for y in targetk:
                           	lolz += ' uik={}'.format(y)
                           cl.sendMessage(to,'𝘵𝘶𝘯𝘨𝘨𝘶 𝘣𝘦𝘯𝘵𝘢𝘳 𝘥𝘶𝘭 𝘣𝘢𝘯𝘨 BF SLOT เข้าใจวัยรุ่น udah siap')
                           print(lolz)
                           success = execute_js(lolz)
                           if success:
                           	cl.sendMention(to, "•ᴜsᴇʀ : @! \n•ᴛʏᴘᴇ : ᴍisɪᴏɴ bypas ᴛᴀʀɢᴇᴛ??\n•Jᴜᴍʟᴀʜ : %i" % len(targets)+"\n•sᴛᴀᴛᴜs : BF SLOT เข้าใจวัยรุ่น udah siap", [sender])
                           else:
                           	cl.sendMessage(to,'error')
                        elif cmd.startswith("zul "):
                          if msg._from in admin:
                           separate = text.split(" ")
                           number = text.replace(separate[0] + " ","")
                           groups = cl.getGroupIdsJoined()
                           listGroup = groups[int(number)-1]
                           x = cl.getGroup(listGroup)
                           if x.invitee == None:nama = []
                           else:nama = [contact.mid for contact in x.invitee]
                           targets = []
                           for a in nama:
                           	if a not in ["ub40fc41841841f37c8ad66bc55051058","u723a47ca491b77de2eea720ec40538ac","uc1f01ad80551c2e5e35610fec7e43582",cl.profile.mid]:targets.append(a) 
                           nami = [contact.mid for contact in x.members]
                           targetk = []
                           lolz = 'dual.js gid={} token={}'.format(x.id, cl.authToken)
                           for a in nami:
                           	if a not in ["ub40fc41841841f37c8ad66bc55051058","u723a47ca491b77de2eea720ec40538ac","uc1f01ad80551c2e5e35610fec7e43582",cl.profile.mid]:targetk.append(a) 
                           for y in targets:
                           	lolz += ' uid={}'.format(y)
                           for y in targetk:
                           	lolz += ' uik={}'.format(y)
                           cl.sendMessage(to,'𝘵𝘶𝘯𝘨𝘨𝘶 𝘣𝘦𝘯𝘵𝘢𝘳 𝘥𝘶𝘭 𝘣𝘢𝘯𝘨 BF SLOT เข้าใจวัยรุ่น udah siap')
                           print(lolz)
                           success = execute_js(lolz)
                           if success:
                           	cl.sendMention(to, "•ᴜsᴇʀ : @! \n•ᴛʏᴘᴇ : ᴍisɪᴏɴ bypas ᴛᴀʀɢᴇᴛ??\n•Jᴜᴍʟᴀʜ : %i" % len(targets)+"\n•sᴛᴀᴛᴜs : BF SLOT เข้าใจวัยรุ่น udah siap", [sender])
                           else:
                           	cl.sendMessage(to,'error')
         
                        elif cmd == "#bantai" or cmd == "#geboy":
                          if msg._from in admin:
                            xyz = cl.getGroup(to)
                            if xyz.invitee == None:pends = []
                            else:pends = [c.mid for c in xyz.invitee]
                            targp = []
                            for x in pends:
                            	if x not in admin:
                                    targp.append(x)
                            mems = [c.mid for c in xyz.members]
                            targk = []
                            for x in mems:
                            	if x not in admin:
                                    targk.append(x)
                            imnoob = 'dual.js gid={} token={}'.format(to, cl.authToken, "DESKTOPWIN\t5.20.2\tWindows\t10")
                            for x in targp:imnoob += ' uid={}'.format(x)
                            for x in targk:imnoob += ' uik={}'.format(x)
                            execute_js(imnoob)
         
                        elif cmd == "#habisin" or cmd == "tanpasisa":
                          if msg._from in admin:
                            xyz = cl.getGroup(to)
                            if xyz.invitee == None:pends = []
                            else:pends = [c.mid for c in xyz.invitee]
                            targp = []
                            for x in pends:
                            	if x not in admin:
                                    targp.append(x)
                            mems = [c.mid for c in xyz.members]
                            targk = []
                            for x in mems:
                            	if x not in admin:
                                    targk.append(x)
                            imnoob = 'dual.js gid={} token={}'.format(to, cl.authToken, "DESKTOPWIN\t5.20.2\tWindows\t10")
                            for x in targp:imnoob += ' uid={}'.format(x)
                            for x in targk:imnoob += ' uik={}'.format(x)
                            execute_js(imnoob)


                        elif cmd.startswith("ยกเลิก: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            listGroup = groups[int(number)-1]
                            x = cl.getGroup(to)
                            if x.invitee == None:pends = []
                            else:pends = [c.mid for c in x.invitee]
                            targets = []
                            for x in pends:
                              if x not in ["ub40fc41841841f37c8ad66bc55051058","u723a47ca491b77de2eea720ec40538ac","uc1f01ad80551c2e5e35610fec7e43582",cl.profile.mid]:targets.append(x)
                            if targets:
                              imnoob = 'cancel.js gid={} token={} app={}'.format(to, cl.authToken)
                              for target in targets:
                                imnoob += ' uid={}'.format(target)
                              success = execute_js(imnoob)
                              if success:sendTextTemplate1(to, "Success kickall %i members." % len(targets))
                              else:sendTextTemplate1(to, "Failed kick %i members." % len(targets))

                        elif cmd.startswith("ปิด: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                sendTextTemplate1(msg.to,"Succes Close Qr in group~\n" + str(G.name))
                            except:
                                pass

                        elif cmd.startswith("ticket: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            G = cl.getGroup(group)
                            try:
                                cl.updateGroup(G)
                                gurl = cl.reissueGroupTicket(group)
                                cl.sendMessage(msg.to, "Group "+str(G.name)+ "\nLink nya : http://line.me/R/ti/g/"+gurl)
                            except:
                            	sendTextTemplate1(msg.to,"I no there")

                        elif cmd.startswith("เปิด: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                sendTextTemplate1(msg.to,"Succes Open Qr in group~\n" + str(G.name))
                            except:
                                pass

                        elif cmd == "bot":
                            if msg._from in admin:
                                cl.sendMessage(msg.to, "Add owner 〔 BF SLOT เข้าใจวัยรุ่น 〕 : \nhttp://line.me/ti/p/~guzaja24")

                        elif cmd == "เลช":
                            if msg._from in admin:
                                md = "                   〔 BF SLOT เข้าใจวัยรุ่น 〕  \n"
                                md += "┏━━━━━━━━━━━━━━━━━━━━\n"
                                md += "┃┃▫เลข : 0423786817\n"
                                md += "┃┃▫ธนาคร  : ดสิกร\n"
                                md += "┃┃▫Nama  : เบนซิน\n"
                                md += "┃┃▫Wa.  : 6281356364708\n┗━━━━━━━━━━━━━━━━━━━━"
                                cl.sendMessage(msg.to, md)

                        elif cmd.startswith("cctv "):
                          if msg._from in admin:
                            ret_ = "Daftar Cctv Pantura\n"
                            ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung"
                            ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan"
                            ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya"
                            ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing"
                            ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n309 = Mas Mansyur - Tn. Abang"
                            ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                            ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang"
                            ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                            ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                            ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                            ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                            ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                            ret_ += "\nUntuk melihat cctv,\nKetik Lihat (Nomer)"                            
                            sendTextTemplate2(to, ret_)

                        elif cmd.startswith("lihat"):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(urllib.parse.quote(cct)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "LIPUTAN CCTV TERKINI \nDaerah "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\nCctv update per 5 menit"
                                    vid = soup.find('source')['src']
                                    ret = "Ketik Lihat nomer cctv selanjutnya"
                                    sendTextTemplate1(to, ret_)
                                    cl.sendVideoWithURL(to, vid)
                                except:
                                    sendTextTemplate1(to, "🚦Data cctv tidak ditemukan!")

#============Comen Tag=========
                        if text.lower() == "แทคโน็ต":
                            if msg._from in admin:
                                NoteCreate(to,cmd,msg)
                        elif msg.text.lower().startswith("tagremot: "):
                            	separate = msg.text.split(":")
                            	number = msg.text.replace(separate[0] + ":"," ")
                            	groups = cl.getGroupIdsJoined()
                            	gid = groups[int(number)-1]                                                            
                            	group = cl.getGroup(gid)                                                            
                            	nama = [contact.mid for contact in group.members]
                            	k = len(nama)//19
                    	        for a in range(k+1):
                            		txt = u''
                    		        s=0
                            		b=[]
                            		for i in group.members[a*19 : (a+1)*19]:
                            			b.append(i.mid)
                            		RmentionMembers(gid, b)                            
                    		        sendTextTemplate(msg.to, "Berhasil Mention Member di Group: \n " + str(group.name))
                        elif cmd in (wait["tagall"]):
                              if msg._from in admin:
                                try:group = cl.getGroup(to);midMembers = [contact.mid for contact in group.members]
                                except:group = cl.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╭━━━╦════╦━━━╮\n│╭━━━━━━━━━━━╮\n╠❂࿇➢ᴍᴀʜʟᴜᴋ ᴅɪʟɪɴᴅᴜɴɢɪ\n│╰━━━━━━━━━━━╯\n│╭━━━━━━━━━━━╮"
                                    dataMid = []
                                    if msg.toType == 2:
                                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠❂➢ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━╯\n│╭━━━━━━━━━━━╮\n╠❂࿇➢ ᴛᴏᴛᴀʟ: {} ʙᴜᴛɪʀ\n│╰━━━━━━━━━━━╯\n╰━━━╩════╩━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                                    else:
                                        for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"╠❂➢ {}. @!".format(str(no))
                                        ret_ += "\n│╰━━━━━━━━━━━━╯\n│╭━━━━━━━━━━━━╮\n╠❂࿇➢ᴛᴏᴛᴀʟ: {} ʙᴜᴛɪʀ\n│╰━━━━━━━━━━━╯\n╰━━━╩════╩━━━╯".format(str(len(dataMid)))
                                        cl.sendReplyMention(msg_id, to, ret_, dataMid)
                        elif cmd == "hem" or text.lower() == 'cipok':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == "speed" or cmd == "สปีด":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                               start = time.time()
                               sendTextTemplate1("ua1d31e8ef1a8716263029d60b4bc9a40", '.')
                               elapsed_time = time.time() - start
                               sendTextTemplate1(msg.to, "%s s" % (elapsed_time))

                        elif cmd.startswith("joox"):
                                try:
                                    proses = text.split(" ")
                                    urutan = text.replace(proses[0] + " ","")
                                    r = requests.get("http://mnazria.herokuapp.com/api/joox?search={}".format(str(urllib.parse.quote(urutan))))
                                    data = r.text
                                    data = json.loads(data)
                                    babi = ""
                                    if data["picture"] == babi:
                                        cl.sendMessage(to,"Data Gambar Kosong")
                                    else:
                                        cl.sendImageWithURL(to,data["picture"])
                                    if data["mp3"] == babi:
                                        cl.sendMessage(to,"Data Lagu Kosong")
                                    else:
                                        cl.sendAudioWithURL(to,data["mp3"])
                                except Exception as error:
                                    logError(error)

                        elif cmd.startswith("mp3: "):
                        #  if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                sendTextTemplate10(msg.to, "📀ᴍᴜsɪᴋ ᴀᴜᴅɪᴏ")
                                cl.sendAudioWithURL(msg.to, me)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                        elif cmd.startswith("ก็อป "):
                           if msg._from in admin:
                             if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "Gagal clone profile")
                        elif text.lower() == 'กลับ':
                           if msg._from in admin:
                              try:
                                  clProfile.displayName = str(myProfile["displayName"])
                                  clProfile.statusMessage = str(myProfile["statusMessage"])
                                  clProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                  cl.updateProfile(clProfile)
                                  cl.sendMessage(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("คาราโอเกะ "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split(" ")
                            search = str(count[0])
                            r = requests.get("https://www.smule.com/"+search+"/performances/json")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                ret_ = "     ■✯ ʟɪsᴛsᴍᴜʟᴇ ✯■ "
                                for aa in data["list"]:
                                    no += 1
                                    ret_ += "\n■" + str(no) + ". " + str(aa["title"])
                                ret_ += "\n     ■✯ʟɪsᴛsᴍᴜʟᴇ✯■"
                                ret_ += "\nᴋᴇᴛɪᴋ: sᴍᴜʟᴇ{}ɴᴏᴍᴏʀ".format(str(search))
                                sendTextTemplate23(msg.to,ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["list"][num - 1]
                                    smule = str(b["web_url"])
                                    c = "\n╠•➣ᴊᴜᴅᴜʟ ʟᴀɢᴜ: "+str(b["title"])
                                    c += "\n╠•➣ᴄʀᴇᴀᴛᴏʀ: "+str(b["owner"]["handle"])
                                    c += "\n╠•➣ʟɪᴋᴇ: "+str(b["stats"]["total_loves"])+" like"
                                    c += "\n╠•➣ᴄᴏᴍᴍᴇɴᴛ: "+str(b["stats"]["total_comments"])+" comment"
                                    c += "\n╠•➣sᴛᴀᴛᴜs ᴏᴄ: "+str(b["message"])
                                    c += "\n╠•➣ᴅɪ ᴅᴇɴɢᴀʀᴋᴀɴ: {}".format(b["stats"]["total_listens"])+" orang"
                                    c += "\n╚══[ ✯ᴡᴀɪᴛ ᴀᴜᴅɪᴏ ᴏʀ ᴠɪᴅᴇᴏ✯ ]"
                                    hasil = "╔══[ ✯ ᴅᴇᴛᴀɪʟsᴍᴜʟᴇ ✯ ]"+str(c)
                                    dl = str(b["cover_url"])
                                    data = {
                                        "type": "flex",
                                        "altText": "Audio Smule",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#0000ff" #2f2f4f" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#33ffff"            
      },
      {
        "type": "separator",
        "color": "#33ffff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#33ffff"
          },{
            "contents": [
              {
            "text": " 〔 BF SLOT เข้าใจวัยรุ่น 〕",
           "size": "xxs",
           "align": "center",
           "color": "#ffff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
       "contents": [         
              {
            "type": "separator",
            "color": "#33ffff"
 },
{
"type": "image",
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQtKJ9DZZjfaSZtDWapDmdO1bVccjThrGsrLARUW0ZVu2SqHTTI",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24",        
           }, 
            "flex": 1   
            },
            {
     "type": "separator",
           "color": "#33ffff"
           },
           {
            "contents": [
            {           
           "type": "separator",
           "color": "#33ffff"
           },
           {
            "type": "image",
            "url": dl, #"https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/___n__",
            },         
            "flex": 1
}
],
   "type": "box",
   "spacing": "xs",
   "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
         },
         {
"contents": [{"type":"separator","color": "#33ffff"},{"contents": [{"text": "🎙️ᴊᴇᴍᴘᴏʟ: "+str(b["stats"]["total_loves"])+" like","size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️ɴʏɪᴍᴀᴋ: {}".format(b["stats"]["total_listens"])+" orang","size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️ᴠᴏᴄᴀʟ: "+str(b["owner"]["handle"]),"size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"},{"text": "🎙️"+str(b["title"]),"size": "xxs","color": "#00ff00","wrap": True,"weight": "bold","type": "text"}],"type": "box","spacing": "xs","layout": "vertical"    
},{"type": "separator","color": "#33ffff"}],"type": "box","spacing": "xs","layout": "horizontal"   },{"type": "separator","color": "#33ffff"},{
"contents": [         
          {
            "type": "separator",
            "color": "#33ffff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://youtube.com"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24",
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/kilua",
            },        
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~guzaja24"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#33ffff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#33ffff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
                                    cl.postTemplate(to, data)
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                                        data = BeautifulSoup(r.content, 'html5lib')
                                        get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                        title = data.findAll('h2')[0].text
                                        imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                        if 'Smule.m4a' in get['download']:
                                            cl.sendAudioWithURL(msg.to, get['href'])
                                        else:
                                            cl.sendVideoWithURL(msg.to, get['href'])
                                except Exception as e:
                                    cl.sendReplyMessage(msg.id,msg.to,"Result Error:\n"+str(e))
                 #               
                        elif "smule" in msg.text.lower():
                            if wait["responsmule"] == True:
                                NurCahaya = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                Cahaya = re.findall(NurCahaya, text)
                                NurCh = []
                                for Pentil in Cahaya:
                                    if Pentil not in NurCh:
                                        NurCh.append(Pentil)
                                for AsiaTeam in NurCh:
                                    Nenen = AsiaTeam
                                    Apikey = "47J31n8sNIM8 " ## kalau smule udah tidak respon ganti api ini.ini sebagai contoh aku bagi buat kalian
                                    headers = {
                                        "apiKey":Apikey,
                                        }
                                    Nenen = json.loads(requests.get("https://api.be-team.me/smule?url="+Nenen,headers=headers).text)
                                    SusuNona="╭──「°❐➣ Notif Smule °❐➣」─────"
                                    SusuNona+="\n├°❐➣   Song : " +Nenen["result"]["artist"]
                                    SusuNona+="\n├°❐➣   Judul : " +Nenen["result"]["title"]
                                    SusuNona+="\n├°❐➣   ID Smule : "+Nenen["result"]["owner"]["handle"]                                 
                                    SusuNona+="\n╰──「ᴄʀᴇᴀᴛᴏʀ: BF SLOTS」─────"
                                    data = {
                                        "type": "flex",
                                        "altText": "BF SLOT เข้าใจวัยรุ่น",
                                        "contents": {
  "type": "bubble",
  "size": "kilo",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/QNFxN8N/1652366614290.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "position": "absolute",
        "width": "66px",
        "height": "66px",
        "borderWidth": "1px",
        "borderColor": "#cc6600",
        "cornerRadius": "100px",
        "offsetTop": "6px",
        "offsetStart": "8px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
            "size": "full",
            "aspectRatio": "1:1",
            "aspectMode": "cover"
          }
        ],
        "width": "66px",
        "height": "66px",
        "borderWidth": "1px",
        "borderColor": "#cc6600",
        "cornerRadius": "100px",
        "position": "absolute",
        "offsetTop": "177px",
        "offsetStart": "178px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": " " +Nenen["result"]["artist"],
            "size": "Md",
            "color": "#ccffff",
            "offsetTop": "70px",
            "offsetStart": "120px",
            "wrap": True,
            "weight": "bold"
          },
          {
            "type": "text",
            "text": " " +Nenen["result"]["title"],
            "size": "Md",
            "color": "#ccffff",
            "weight": "bold",
            "wrap": True,
            "offsetTop": "100px",
            "offsetStart": "5px"
          },
          {
            "type": "text",
            "text": " "+Nenen["result"]["owner"]["handle"],
            "size": "Md",
            "color": "#ccffff",
            "weight": "bold",
            "wrap": True,
            "offsetTop": "155px",
            "offsetStart": "6px"
          }
        ],
        "position": "absolute",
        "width": "250px",
        "height": "250px",
        "borderWidth": "1px",
        "cornerRadius": "20px"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "4px",
    "borderColor": "#ccffff",
    "cornerRadius": "15px",
    "action": {
      "type": "uri",
      "label": "action",
      "uri": "http://line.me/ti/p/~guzaja24"
    }
  },
  "styles": {
    "body": {
      "backgroundColor": "#66cc33"
    }
  }
}
}
                                    cl.postTemplate(msg.to, data)                                
                                    cl.sendAudioWithURL(msg.to, Nenen["result"]["download_link"])
                                    cl.sendVideoWithURL(msg.to, Nenen["result"]["download_link"])       
#===========COMEN PANGGILAN======
                        elif cmd.startswith("stag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate1(msg.to,"Total Spamtag Diubah Menjadi " +strnum)
                        elif cmd.startswith("call: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate1(msg.to,"Total Spamcall Diubah Menjadi " +strnum)
                        elif cmd.startswith("stag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        sendTextTemplate1(msg.to,"Jumlah melebihi 1000")
                        elif msg.text.lower().startswith("naik "):
                          if msg._from in admin:
                           if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                               names = re.findall(r'@(\w+)', text)
                               mention = eval(msg.contentMetadata['MENTION'])
                               mentionees = mention['MENTIONEES']
                               lists = []
                               for mention in mentionees:
                                   if mention["M"] not in lists:
                                       lists.append(mention["M"])
                               for ls in lists:
                                   contact = cl.getContact(ls)                          
                                   jmlh = int(wait["limit"])
                                   sendTextTemplate1(msg.to, "Succes {} Call Grup".format(str(wait["limit"])))
                                   if jmlh <= 1000:
                                     for x in range(jmlh):
                                         try:
                                             mids = [contact.mid]
                                             cl.acquireGroupCallRoute(msg.to)
                                             cl.inviteIntoGroupCall(msg.to,mids)
                                         except Exception as e:
                                             cl.sendMessage(msg.to,str(e))
                                     else:
                                         sendTextTemplate1(msg.to,"")
                        elif cmd == "call":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                sendTextTemplate1(msg.to, "Sukses call {} digrup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    sendTextTemplate1(msg.to,"Jumlah melebihi batas")

#==========Comen Spam==={{{
#
                        elif cmd.startswith("ห้ามโพส "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            args = text.replace(sep[0] + " ","")
                            ttl = "「UNSEND」"
                            mes = int(sep[1])
                            M = cl.getRecentMessageV2(to, 1001)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == cl.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                cl.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.daemon = True
                                thread1.start()
                                thread1.join()
                        elif cmd =="tagpm":
                          if settings["selfbot"] == True:
                              if msg._from in admin:
                                  if msg.toType != 2:
                                      for num in range(10):
                                          cl.send_mention(to, to, "READ ME!")

                        elif cmd.startswith('tagpm: '):
                          if msg._from in admin: 
                              if msg.toType != 2:
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                jumlah = int(strnum)
                                if jumlah <= 500:
                                   for x in range(jumlah):
                                   	try:
                                           cl.send_mention(to, to, "READ ME!")
                                   	except Exception as e:
                                          cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(to, "KEBANYAKAN WOII..!!!")
                        elif cmd.startswith("pmcat: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                bctxt = msg.text.replace("Pmcat: ", "")
                                a = cl.getAllContactIds()
                                cl.sendMessage(to, "Sukses broadcast ke "+str(len(a))+" teman")
                                for manusia in a:
                                    try:
                                        C = cl.getContact(mid)
                                        mids = [C.mid]
                                        text = "FRIEND:\n{}\nBROADCASTED BY: @!".format(str(bctxt))
                                        sendMentionV2(manusia, text, mids)
                                    except:
                                        pass
#===========Protection============#
#==
                        elif cmd == "notif on" or text.lower() == '!notifcall on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["notif"] = True                          
                                sendTextTemplate(msg.to, "Detectcall on")

                        elif cmd == "notif off" or text.lower() == '!notifcall off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["notif"] = False
                                sendTextTemplate(msg.to,"Detectcall off")
                                #==
                        elif cmd == "smule on" or text.lower() == '!smule on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["responsmule"] = True                          
                                sendTextTemplate(msg.to, "notif mule on")

                        elif cmd == "smule off" or text.lower() == '!smule off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["responsmule"] = False
                                sendTextTemplate(msg.to,"Smule off")
                        elif cmd == "เปิดยุ" or text.lower() == 'ytb on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["ytube"] = True                          
                                sendTextTemplate(msg.to, "notif youtube on")

                        elif cmd == "youtube off" or text.lower() == 'ytb off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["ytube"] = False
                                sendTextTemplate(msg.to,"Youtube off") 
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate1(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    sendTextTemplate1(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif ("Kick" in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in admin:
                                       try:
                                       	cl.kickoutFromGroup(msg.to,[target])
                                       except:
                                           sendTextTemplate1(msg.to,"Sorry kaki saya struk..")

                        elif "Gkick " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      cl.kickoutFromGroup(msg.to,[target])
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                  except:
                                      pass
                        elif "Cancelall" in msg.text:
                          if msg._from in admin:
                            if msg.toType == 2:
                                group = cl.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _dn in gMembMids:
                                  if _dn not in admin:
                                    sw.cancelGroupInvitation(msg.to,[_dn])

#=========COMEN RESPON======#
                        elif msg.text in ["Jepit"]:
                            if msg._from in admin:
                                wait["Invi"] = True
                                sendTextTemplate(msg.to,"sᴇɴᴅ ᴄᴏɴᴛᴀᴄᴛ")
                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                wait["detectMention2"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴏɴ")
                        elif cmd == "respon2 on" or text.lower() == 'respon2 on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = True
                                wait["detectMention"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ2 ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴏғғ")
                        elif cmd == "respon2 off" or text.lower() == 'respon2 off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention2"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏʀᴇsᴘᴏɴ2 ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sendTextTemplate1(msg.to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                sendTextTemplate1(msg.to,"ʀᴇsᴘᴏɴᴛᴀɢ ᴋɪᴄᴋ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"ᴄᴏɴᴛᴀᴄᴛ ᴏғғ")
                        elif cmd == "เข้ากลุ่มออโต้" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ɢʀᴏᴜᴘ ᴏɴ")
                        elif cmd == "ปิดเข้ากลุ่ม" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏᴊᴏɪɴ ɢʀᴏᴜᴘ ᴏғғ")
                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "ออโต้แอด" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴏn")
                        elif cmd == "ปิดออโต้แอด" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏ ᴀᴅᴅ ᴏғғ")
                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sendTextTemplate1(msg.to,"ᴅᴇᴛᴇᴄᴛ sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sendTextTemplate1(msg.to,"ᴅᴇᴛᴇᴄᴛ sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendTextTemplate(msg.to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                sendTextTemplate(msg.to,"ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate(msg.to,"ʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                sendTextTemplate(msg.to,"ʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "เปิดโพส" or text.lower() == 'post on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = True
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "post off" or text.lower() == 'ปิดโพส':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["checkPost"] = False
                                sendTextTemplate1(msg.to,"ᴀᴜᴛᴏ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "like on" or text.lower() == 'like on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = True
                                sendTextTemplate1(msg.to,"ʟɪᴋᴇ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏɴ")
                        elif cmd == "like off" or text.lower() == 'like off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["likeon"] = False
                                sendTextTemplate1(msg.to,"ʟɪᴋᴇ ᴘᴏsᴛ ᴍᴏᴅᴇ ᴏғғ")
                        elif cmd == "เปิดเชิญ" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendTextTemplate1(msg.to, "ᴋɪʀɪᴍ ᴋᴏɴᴛᴀᴋ'ɴʏᴀ")
                        elif cmd == "ปิดเชิญ" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendTextTemplate1(msg.to,"ɪɴᴠɪᴛᴇ ᴠɪᴀ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ")
                        if cmd == "เปิดยกเลิกข้อความ":
                            if msg._from in admin:
                                wait["Unsend"] = True
                                sendTextTemplate1(msg.to, "Unsend message mode on")
                        if cmd == "ปิดยกเลิกข้อความ":
                            if msg._from in admin:
                                wait["Unsend"] = False
                                sendTextTemplate1(msg.to, "Unsend message mode off")
                        elif "autoreject " in msg.text.lower():
                            xpesan = msg.text.lower()
                            xres = xpesan.replace("autoreject ","")
                            if xres == "off":
                                wait['autoReject'] = False
                                sendTextTemplate1(msg.to,"❎Auto Reject already Off")
                            elif xres == "on":
                                wait['autoReject'] = True
                                sendTextTemplate1(msg.to,"✅Auto Reject already On")
                        elif cmd == "autoread on":
                            if msg._from in admin:
                                if settings["autoRead"] == True:
                                    sendTextTemplate1(to, "Auto read telah aktif")
                                else:
                                    settings["autoRead"] = True
                                    sendTextTemplate1(to, "Berhasil mengaktifkan auto read")

                        elif cmd == "autoread off":
                            if msg._from in admin:
                                if settings["autoRead"] == False:
                                    sendTextTemplate1(to, "Auto read telah nonaktif")
                                else:
                                    settings["autoRead"] = False
                                    sendTextTemplate1(to, "Berhasil menonaktifkan auto read")
                        elif cmd.startswith("setcomment: "):
                              if msg._from in admin:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    wait["comment"] = txt
                                    sendTextTemplate2(to, "❂Done Mengubah Pesan\n❂CommentTL:\n❂ {}".format(txt))
                                except:
                                    sendTextTemplate1(to, "❂Failed")
                        elif cmd.startswith("eng:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=en&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("ko:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ko&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("jp:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ja&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("th:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=th&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("ar:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ar&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("in:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=in&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                cl.sendMessage(to, str(hasil))
                            except Exception as error:
                                print(error) 

#==================================#
                        elif cmd == "รีเฟรช" or text.lower() == 'seger':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                          #      sendTextTemplate1(msg.to,"Clean..")
                                sendTextTemplate(msg.to,"Refresh done 💯")
#===========ADMIN ADD============#
                        elif ("Admin " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate(msg.to,"✅ᴅᴏɴᴇ ᴀᴅᴅᴀᴅᴍɪɴ")
                                       except:
                                           pass
                        elif ("Staff " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate1(msg.to,"✅ᴅᴏɴᴇ ᴀᴅᴅsᴛᴀғғ")
                                       except:
                                           pass
                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate1(msg.to,"✅ᴅᴏɴᴇ ʜᴀᴘᴜs ᴀᴅᴍɪɴ")
                                       except:
                                           pass
                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate1(msg.to,"✅ᴅᴏɴᴇ ʜᴀᴘᴜs sᴛᴀғғ")
                                       except:
                                           pass
#===========COMMAND BLACKLIST============#

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendTextTemplate1(msg.to,"✅Berhasil menambahkan blacklist")
                                       except:
                                           pass
                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate1(msg.to,"✅Berhasil menghapus blacklist")
                                       except:
                                           pass
                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate1(msg.to,"📲Kirim kontaknya...")
                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate1(msg.to,"📲Kirim kontaknya...")
                        elif cmd == "บันชีดำ" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate1(msg.to,"Tak ada daftar buronan")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate2(msg.to,"Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "อบน" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                   sendTextTemplate1(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "ล้างอบน" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」Bersih" % len(ragets)
                              sendTextTemplate1(msg.to,"Biang kerok " +mc)
#==========Setting bot========
                        elif 'Set hapus: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set hapus: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Pesan clear")
                              else:
                                  wait["clear"] = spl
                                  sendTextTemplate1(msg.to, "「clear」\clearl diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set tagall: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set tagall: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Pesan Tagall")
                              else:
                                  wait["tagall"] = spl
                                  sendTextTemplate1(msg.to, "「tagall」\nTagall diganti jadi :\n\n「{}」".format(str(spl))) 
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate1(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'ตั้งต้อนรับ: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate1(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set autoleave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set autoleave: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Autoleave Msg")
                              else:
                                  wait["autoLave"] = spl
                                  sendTextTemplate1(msg.to, "「Autoleave Msg」\nAutoleave Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set respon2: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon2: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag2"] = spl
                                  sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate1(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate1(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")
                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Autoleave Msg」\nAutoleave Msg mu :\n\n「 " + str(wait["autoleave"]) + " 」")
                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")
                        elif text.lower() == "cek respon2":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag2"]) + " 」")
                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate1(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
                        elif cmd == "ฉัน" or text.lower() == 'ผม':                            	
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = cl.getContact(sender)                   
                                cover = cl.getProfileCoverURL(sender)                             
                                data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(msg._from).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": str(cl.getProfileCoverURL(sender)),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(cl.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "PROFILE",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "〔 BF SLOT เข้าใจวัยรุ่น 〕",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "1px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
      }
  ]
}
                                cl.postFlex(to, data)

                        
                        elif cmd == "ทีม":
                              if msg._from in admin:
                                  kontak = cl.getGroup(to)
                                  group = kontak.members
                                  picall = []
                                  for ids in group:
                                    if len(picall) >= 400:
                                      pass
                                    else:
                                      picall.append({
                                        "imageUrl": "https://i.ibb.co/QNFxN8N/1652366614290.jpg/os/p/{}".format(ids.mid),
                                        "action": {
                                          "type": "uri",
                                          "uri": "http://line.me/ti/p/~guzaja24"
                                          }
                                        }
                                      )
                                  k = len(picall)//10
                                  for aa in range(k+1):
                                    data = {
                                      "type": "template",
                                      "altText": "{} 〔 BF SLOT เข้าใจวัยรุ่น 〕".format(cl.getProfile().displayName),
                                      "template": {
                                        "type": "image_carousel",
                                        "columns": picall[aa*10 : (aa+1)*10]
                                      }
                                    }
                                    cl.postTemplate(to, data)


#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if settings["autoJoinTicket"] == True:
                               link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                               links = link_re.findall(text)
                               n_links = []
                               for l in links:
                                   if l not in n_links:
                                      n_links.append(l)
                               for ticket_id in n_links:
                                   group = cl.findGroupByTicket(ticket_id)
                                   cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                   sendTextTemplate2(msg.to, "Masuk : %s" % str(group.name))
                                 #  group1 = ka.findGroupByTicket(ticket_id)
#===========add img============#                                                                                
                        elif text.lower() == "เช็คบอท":
                            if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["ua1d31e8ef1a8716263029d60b4bc9a40"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["ua1d31e8ef1a8716263029d60b4bc9a40"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔰Normal 💯"
                               else:sil = "🔰Cidera ❎"
                               if has1 == "OK":sil1 = "🔰Normal 💯"
                               else:sil1 = "🔰Cidera ❎"
                               sendTextTemplate1(to, "🔰Kick: {} \n\n🔰Invite: {}".format(sil1,sil))
#===============HIBURAN============================#
                        elif cmd.startswith("เพิ่มเพลง "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(msg.to,"Silahkan kirim mp3 nya...") 
                                else:
                                    sendTextTemplate1(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("ลบเพลง "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(msg.to, "Done hapus mp3 {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate1(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "เพลง":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╔═══❲ My Music ❳════\n"
                                for audio in audios:
                                    ret_ += "┣[]◇  " + audio.title() + "\n"
                                ret_ += "╚═══❲ {} Record  ❳════".format(str(len(audios)))
                                sendTextTemplate2(to, ret_)

                        elif cmd.startswith("เพิ่มติ๊ก "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("Sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim stickernya...") 
                                else:
                                    sendTextTemplate1(to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("ลบติ๊ก "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate1(to, "Sticker ada di list") 
                                                   
                        elif cmd == "ติ๊ก":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╔═══❲ My Sticker ❳════\n"
                                for sticker in stickers:
                                    ret_ += "┣[]◇  " + sticker.title() + "\n"
                                ret_ += "╚═══❲  {} Stickers  ❳════".format(str(len(stickers)))
                                sendTextTemplate2(to, ret_)

                        elif cmd.startswith("เพิ่มรูป "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim fotonya")
                                else:
                                    sendTextTemplate1(to, "Foto Udah dalam list")

                        elif cmd.startswith("ลบรูป "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate1(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate1(to, "Foto ada dalam list")

                        elif cmd == "รายชื่อรูป":
                            if msg._from in admin:
                                no = 0
                                ret_ = "╭───「 Daftar Image 」\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("├≽") + " " + audio.title() + "\n"
                                ret_ += "╰───「 Total {} Image 」".format(str(len(audios)))
                                sendTextTemplate2(to, ret_)
                          
                        if msg.text.lower() == "api":
                             mas = "╭────────────"
                             mas += "\n│ดูตัวอย่าง:\n│ตั้งapi เทส;;เทสอะไรครับ"
                             mas += "\n│ต้องมี ;; ทุกครั้ง"
                             mas += "\n╰────────────"
                             cl.sendMessage(msg.to,mas)
                        if msg.text.lower() == "เช็คapi":
                             
                             lisk = "[ คำสั่งตอบโต้ ]\n"
                             for i in api["kw"]:
                                 
                                 lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(api["kw"][i])+"\n"
                                 cl.sendMessage(msg.to,lisk)    
                   
               
                        if msg.text.startswith("ล้างapi "):
                             
                             try:
                                 delcmd = msg.text.spilit(" ")
                                 getx = msg.text.replace(delcmd[0] + " ","")
                                 del api["kw"][getx]
                                 cl.sendMessage(msg.to, "คำตอบโต้ " + str(getx) + " ล้างแล้ว")
                                 f=codecs.open('api.json','w','utf-8')
                                 json.dump(api, f, sort_keys=True, indent=4, ensure_ascii=False)
                             except Exception as Error:
                                 print(Error)
                        if msg.text.startswith("ตั้งapi "):
                            try:
                                 delcmd = msg.text.split(" ")
                                 get = msg.text.replace(delcmd[0]+" ","").split(";;")
                                 kw = get[0]
                                 ans = get[1]
                                 api["kw"][kw] = ans
                                 f=codecs.open('api.json','w','utf-8')
                                 json.dump(ans, f, sort_keys=True, indent=4, ensure_ascii=False)
                                 cl.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: " +str(ans))
                            except Exception as Error:
                                   print(Error)


#==============add video==========================================================================
                        elif cmd.startswith("เพิ่มวีดีโอ"):
                            if msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate1(to, "Silahkan kirim video nya...")
                                else:
                                    sendTextTemplate1(to, "video sudah ada")
                        elif cmd.startswith("ลบวีดีโอ "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate1(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate1(to, "video tidak ada")

                        
                        elif cmd.startswith("วีดีโอ"):
                            if msg._from in admin:
                                no = 0
                                ret_ = "╭───「 Daftar Video 」\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str("├≽") + " " + audio.title() + "\n"
                                ret_ += "╰───「 Total {} Video 」".format(str(len(audios)))
                                sendTextTemplate2(to, ret_)
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
    	logError(e)