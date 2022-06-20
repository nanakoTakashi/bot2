import os
import json
import telebot
import random
import time
from telebot import types
from telebot.apihelper import ApiTelegramException
from decouple import config
from googletrans import Translator

TOKEN = config("API-TOKEN")

teleToken = TOKEN
tb = telebot.TeleBot(teleToken)