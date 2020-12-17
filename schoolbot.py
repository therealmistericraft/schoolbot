# coding=utf-8

#1 imports
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from time import sleep
import threading
import json

#2 settings

#2.1 Activate Intents from API
intents = discord.Intent.defaults()
intents.members = True
intents.reactions = True

#3 instance variables
prefix = ""
lang = ""

#4 initalizing

#4.1 prefix
prefixfile = open('prefix.txt', 'r')
data = prefixfile.read()
data = data.split('\n')
custom_prefixes = data[0]
custom_prefixes = ast.literal_eval(custom_prefixes)
default_prefix = '%'
prefixfile.close()
