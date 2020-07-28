print("importing")
import requests
import json



apikey="AIzaSyAh-K5EbPnXBnfn51ahxkrj_Y6cQlSkQTI"
channel_id="UC4dtpe-zy-ek92CEmFqMFDw"



def get_latest_video_id():
	url=f"https://www.googleapis.com/youtube/v3/search?channelId={channel_id}&order=date&key={apikey}"
	page=requests.get(url)
	content=json.loads(page.text)
	global videoid,tagvideoid
	videoid=content["items"][0]["id"]["videoId"]
	tagvideoid=content["items"][1]["id"]["videoId"]
	return videoid


def get_video_details(_id=get_latest_video_id()):
	url=f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={_id}&key={apikey}"
	page=requests.get(url)
	details=json.loads(page.text)
	global title,description,thumbnail,videolink,channellink,channelname,videotags
	title=details["items"][0]["snippet"]["title"]
	description=details["items"][0]["snippet"]["description"]
	thumbnail=details["items"][0]["snippet"]["thumbnails"]["standard"]["url"]
	videolink="https://www.youtube.com/watch?v="+details["items"][0]["id"]
	channellink="https://www.youtube.com/channel/"+details["items"][0]["snippet"]["channelId"]
	channelname=details["items"][0]["snippet"]["channelTitle"]
	from urllib.request import urlretrieve
	urlretrieve(thumbnail,filename="thumbnail.png")
	url=f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={tagvideoid}&key={apikey}"
	page=requests.get(url)
	details=json.loads(page.text)
	videotags=details["items"][0]["snippet"]["tags"]


print("getting details")
get_video_details()

instagram_username="abhithegreat75memes"
instagram_password="ABCD1234$"

def instagram_send():
	from instabot import Bot
	bot=Bot()
	bot.login(username=instagram_username,password=instagram_password)
	bot.upload_photo("thumbnail.png",caption=text)



def automate_video_changes():
	import webbrowser
	import pyautogui
	import os
	import time
	editbutton=(484,386)
	description=(330,448)
	tags=(317,621)
	endscreen=(1300,423)
	videocombo=(346,332)
	save1=(1094,186)
	discard=(986,187)
	save2=(1245,202)
	webbrowser.open_new_tab(f"https://studio.youtube.com/video/{videoid}/edit/basic")
	time.sleep(15)
	i=True
	pyautogui.click(description[0],description[1])
	with open("ytdescription.txt","r") as f:
		descriptiontxt=f.read().format(title)
	pyautogui.typewrite(descriptiontxt,interval=0.05)
	located=True
	while located:
		pyautogui.hscroll(-100)
		if pyautogui.locateOnScreen("tags.png"):
			located=False
	pyautogui.click("tags.png")
	tagstxt=""
	for tag in videotags:
		tagstxt+=tag+","
	tagstxt+=title+","
	for word in title.split(" "):
		tagstxt+=word+","
	pyautogui.typewrite(tagstxt,interval=0.05)
	located=True
	while located:
		pyautogui.hscroll(100)
		if pyautogui.locateOnScreen("endscreen.png"):
			located=False
	pyautogui.click("endscreen.png")
	time.sleep(5)
	pyautogui.click(videocombo[0],videocombo[1])
	time.sleep(5)
	pyautogui.click(save1[0],save1[1])
	time.sleep(5)
	pyautogui.click(discard[0],discard[1])
	time.sleep(5)
	pyautogui.click(save2[0],save2[1])


def check_discord():
	import os

	import discord
	from discord.ext import commands

	TOKEN = "NzI0MTE4MjYwNzc3MzUzMjc2.Xu7hrg.F_soT6RsHG7M-79NgsKeNELP1t4"
	
	print("starting bot")
	bot = commands.Bot(command_prefix='-')
	@bot.command(name='update')
	async def update(ctx):
		if str(ctx.message.channel.id) == "737705726176395375":
			# print("automating video changes")
			# automate_video_changes()
			print("posting to instagram")
			instagram_send()
	bot.run(TOKEN)


print("closed")
check_discord()