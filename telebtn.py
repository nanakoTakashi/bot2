from info import *

blist1 = types.InlineKeyboardMarkup()
ba1 = types.InlineKeyboardButton(
    text="yes", callback_data="loveYes"
)
ba2 = types.InlineKeyboardButton(
    text="no", callback_data="loveNo"
)

blist1.add(ba1)
blist1.add(ba2)

blist2 = types.InlineKeyboardMarkup()
bb1 = types.InlineKeyboardButton(
    text="OWNER", 
    url="https://t.me/nnk0o"
)
bb2 = types.InlineKeyboardButton(
    text="CHANNEL", 
    url="https://t.me/pjpppppp"
)

blist2.add(bb1)
blist2.add(bb2)

#call
def call_result(call):
#    chat_id = call.m.chat.id
    if call.data=="loveYes":
        tb.send_message(call.message.chat.id, "loveeee")
    if call.data=="loveNo":
        tb.send_message(call.message.chat.id, "noo")  