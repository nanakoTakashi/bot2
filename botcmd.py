from info import *
from telebtn import *

def bot_cmds(m):
    t = m.text
    chat_id = m.chat.id
    
    if t=="/start":
        if m.chat.type == "private" :
            tb.send_message(chat_id, "p")
        if m.chat.type == "group" or m.chat.type == "supergroup" :
            tb.reply_to(m, "g")
    elif t=="/help":
        tb.send_message(chat_id, "Helping")
                