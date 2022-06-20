from info import *
from repmsg import *
from botcmd import *
from telebtn import *

@tb.message_handler(commands=["start", "help"])
def tele_commands(m):
    bot_cmds(m)

@tb.message_handler(func=lambda m: True)
def rms(m):
    msg_replys(m)

@tb.callback_query_handler(func=lambda call: True)
def calls_handler(call):
    call_result(call)

print("tb is starting...")
tb.infinity_polling()