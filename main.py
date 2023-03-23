#coding=utf-8
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
 
app = Client("my_account", api_id=config['pyrogram']['api_id'], api_hash=config['pyrogram']['api_hash'])
 
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("smtype", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(" ", maxsplit=2)[2]
    text = orig_text
    tbp = "" 
    typing_symbol = msg.text.split(" ", maxsplit=2)[1]
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
 

 
app.run()