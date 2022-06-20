from info import *
from telebtn import *

def msg_replys(m):
    t = m.text
    if t == "hi" :
        tb.reply_to(m, "hello")
    elif t == "bye" :
        tb.reply_to(m, "bye bye!")
    
    elif t=="love":
        tb.reply_to(m,
         "love???" , reply_markup=blist1
         )                