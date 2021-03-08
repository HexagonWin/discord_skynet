########################################################
######## Bot SKYnet for GNU/Linux by HexagonWin ########
######## Proudly written in GNU nano            ########
######## This software is distributed with GPL  ########
######## Mod is possible, but you have to       ########
######## Re-distribute the whole source code    ######## 
########################################################

##########################################################
######## System Software Requirements            #########
######## Python >= 3.7 + discord.py              #########
######## whiptail + dialog + gdialog             #########
######## bash + wget + screenfetch + zenity      #########
######## scrot + etc python libraries mentioned  #########
########$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#########
######## *SKYnet is tested in Debian GNU/Linux 9 #########
######## *But will work for other systems        #########
##########################################################

##############################################################
#### Change var bid, master                               ####
#### Change /home/humane/bots/ to your bot files location ####
##############################################################

from discord.ext import commands
from setstat import bstat
import discord
import asyncio
import os
import subprocess as sp
import time
import random
import string

bot = commands.Bot(command_prefix='./')
client = discord.Client()
bid = "#BotUserID"
master = "#AdminUserID"
buid_error = "ERROR : Bot User ID Mismatch // SKYnet can't start"

#SkyOTP Generator
#def pwgen(size=6, chars=string.ascii_uppercase + string.digits):
#	return ''.join(random.choice(chars) for _ in range(size))

@bot.event
async def on_ready():
	os.system('echo "100" | dialog --gauge "Load final script - Bootstrap SKYnet" 10 70 0')
	time.sleep(2)
	os.system('whiptail --title "SKYnet - Main system start" --infobox "SKYnet Boot . . ." 10 35')
	time.sleep(3)
	if bid == bot.user.id:
		print("Bot User ID : " + str(bot.user.id))
		print("Master ID : " + str(master))
		await bot.change_presence(activity=discord.Game(name=bstat))
		print("Done!!")
		time.sleep(2)
		os.system("clear")
		os.system("./linerx")
	else:
		print(buid_error)

@bot.command()
async def mention(ctx,mid='None', secx=3, repet=1, description='just a test command'):
	if mid == 'None':
		mid = ctx.author.id
	await ctx.send("Mentioning user " + str(mid) + " in " + str(secx) + " seconds")
	time.sleep(secx)
	hmeny = 1
	while hmeny <= repet:
		await ctx.send("<@" + str(mid) + ">")
		hmeny += 1
		time.sleep(0.1)
	await ctx.send("Done")
	os.system('whiptail --title "SKYnet - User log" --infobox "User Mention" 10 35')

#@bot.command(pass_context=True)
#async def dget(ctx, fadre=None, description='Just type ./dget to see description.'):
#		if fadre == None:
#			embed=discord.Embed(title="SKYnet - Commands dGet", description="How to use ./dget")
#			embed.add_field(name="Example", value="./dget /home/huname/file.txt", inline=False)
#			embed.set_footer(text="Powered by QEMU/KVM virtual guest aincradtest")
#			await ctx.send(embed=embed)
#		else:
#			await ctx.send('`Your File is available`')
#			await ctx.send(file=discord.File(fadre)

@bot.command()
async def screenfetch(ctx, description='Screenfetch result realtime. However the ascii art isnt displaying correctly.'):
	os.system('whiptail --title "SKYnet - User log" --infobox "User Screenfetch" 10 35')
	output = sp.getoutput('screenfetch')
	seout = "```" + output + "```"
	await ctx.send(seout)

#@bot.command(pass_context=True, description='Almost full bash shell running in the aincradtest server.')
#async def bash(ctx, type):
#	await ctx.send("OTP verification process start - send password in 10 seconds")
#	otpass = pwgen()
#	print(otpass)
#	os.system("./skyotp.sh " + otpass)
#	time.sleep(10)
#	print(ctx.message.content)
#	if ctx.message.content == otpass:
#		await ctx.send("OTP verification success")
#		outt = sp.getoutput(type)
#		seoutt = "```" + outt + "```"
#		await ctx.send(seoutt)
#	else:
#		await ctx.send("OTP verification error")

@bot.command()
async def shot(ctx, description='Take a panorama of Bot-Host.'):
	await ctx.send("Awaiting host order ...")
	os.system("zenity --error --text='SKYnet - Shot / Check SCREEN'")
	os.system("cd /home/huname/bots/shots && scrot screen.png")
	yesornoo = input("[HTK/Panorama Temp OTP System] : Enter y/n :")
	if yesornoo ==  "y":
		print("Access allowed, Panorama process start...")
		print("[Take a panorama] Wait 3 seconds . . .")
		time.sleep(1)
		print("[Take a panorama] Wait 2 seconds . .")
		time.sleep(1)
		print("[Take a panorama] Wait 1 seconds .")
		time.sleep(1)
		print("Shooting panorama . . .")
		os.system("cd /home/huname/bots/shots && scrot screen.png")
		await ctx.send(file=discord.File("/home/huname/bots/shots/screen.png"))
		await ctx.send('Took a `Panorama`')
		print("Took a Panorama")
		await ctx.send("Successful")
		time.sleep(2)
		os.system("./linerx")
	else:
		await ctx.send("Denied, shot not sent")
		time.sleep(2)
		os.system("./linerx")

@bot.command()
async def cinvite(ctx, description='Creates an invitation link to this server. It would last for 300 .'):
	clink = await ctx.channel.create_invite(max_age=300)
	await ctx.send(clink)

#@bot.command(pass_context=True, description='du means Download and Upload. It downloads the file to the aincradtest server and uploads it back to the discord server. Only small files are supported')
#async def du(ctx, fadr=None):
#	if fadr == None:
#		await ctx.send("Hey link the file")
#	else:
#		os.system("cd /home/huname/bots/downloads/ && wget -O FILE " + fadr)
#		await ctx.send(file=discord.File("/home/huname/bots/downloads/FILE"))

@bot.command()
async def cls(ctx, amount=5):
	await ctx.channel.purge(limit=amount)

@bot.command()
async def perm(ctx):
	if ctx.author.id == master:
		await ctx.send('Hi master')
	else:
		await ctx.send('Who the hell are you??')

@bot.command()
async def info(ctx):
	rawtux = sp.getoutput('cat /home/huname/bots/linuxtux.txt')
	a = "```" + rawtux
	output = sp.getoutput('uname -a')
	seout = "bot SKYnet V-1.1a-rd | System"  + output
	b = seout
	cctime = sp.getoutput('date')
	c = "System current time " + cctime
	btimecat = sp.getoutput('cat /home/huname/bots/bootime.txt')
	d = btimecat + "```"
	await ctx.send(a + "\n" + b + "\n" + c + "\n" + d + "\n")

@bot.command()
async def invite(ctx):
	await ctx.send("http://discord.com/oauth2/authorize?client_id=" + bid + "&permissions=8&scope=bot")

bot.run('ODE2NDg3MzM4MDAyODc0MzY5.YD7rFg.n_YTNxDllWHNIsX2KMTKGecBfYQ')
