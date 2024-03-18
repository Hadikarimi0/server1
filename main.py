from pyrubi import Client
from threading import Thread
import random
from pyrubi.types import Message
import copy
bot = Client(session="bot1")
#gap = bot.join_chat('https://rubika.ir/joing/GACEACIF0BUNDVUWLFUZMIKRAGUCTDRZ')['group']['group_guid']
#print(gap)
hh = bot.get_messages('c0oX5T0640e874edc13442cb4dd0a403',None)['messages'][:1]
for m in hh:
    xx = bot.get_download_link('c0oX5T0640e874edc13442cb4dd0a403',m['message_id'])

branch = 'c0Btppl0cf8316d9e79486d5a8bd8d86'
ids = []
ids2 = []
black_list = []
guid2 = ""
on_off = True
robo = ['bot2','bot3']
guid = "g0EVYQf06e7cc64c53b48fcd9cae6be3"
bot.send_text(guid, 'bot is online|')
def send(m):
    global ids
    messages = bot.get_messages(guid,None)['messages'][:10]
    for m in messages:
        try:
            mesID = m['message_id']
            if m['forwarded_from']['type_from'] == 'Channel':
                ids.append(mesID)
                dd = bot.forward_messages(guid, ids, branch)
                ids.clear()
        except:pass
def send2(m):
    global ids2, guid
    try:
        
        t = m.text.split('@')[1]
        guid2 = bot.get_chat_info_by_username(t)
        #guid2['chat']['last_message_id']
        messages = bot.get_messages(guid2['channel']['channel_guid'],None)['messages'][:5]
        for mm in messages:
            try:
                mesID = mm['message_id']
                ids2.append(mesID)
                dd = bot.forward_messages(guid2['channel']['channel_guid'], ids2, branch)
                ids2.clear()
            except:pass
    except:pass
    # messages = bot.get_messages(guid,None)['messages'][:10]
    # for m in messages:
    #     try:
    #         mesID = m['message_id']
    #         if m['forwarded_from']['type_from'] == 'Channel':
    #             ids.append(mesID)
    #             dd = bot.forward_messages(guid, ids, branch)
    #             ids.clear()
    #     except:pass
@bot.on_message(filters=["Group"])
def update(m : Message):
    global ids, branch, on_off, guid, black_list,guid2, robo
    admin = ("u0DISjB08d1903459b86f3c9ddb48e01","u0GiiET0a65d5cf14a41b44f44449e87")

    if m.object_guid == guid:
        text = m.text
        print(m.text)
        if text.lower() == '#on':
            #for ad in admin:
                if m.author_guid in admin:
                    on_off = True
                    m.reply('ربات با موفقیت روشن شد')
        elif text.lower() == '#off':
            #for ad in admin:
                if m.author_guid in admin:
                    on_off = False
                    m.reply('ربات با موفقیت خاموش شد')
        elif text == 'یک عضو از طریق لینک به گروه افزوده شد.':
            m.reply(f"@@Hello welcome to the group@@(https://rubika.ir/robot_help)")
        elif on_off == True:
            
            if text.lower() == "new":
                #for ad in admin:
                    if m.author_guid in admin:
                        for chanel in bot.get_messages_by_id(m.object_guid, [m.reply_message_id])["messages"]:
                            if chanel['forwarded_from']['type_from'] == 'Channel':
                                del branch
                                branch = chanel['forwarded_from']['object_guid']
                                print(branch)
                                m.reply(f"شعبه چنل با موفقیت دریافت شد")
            elif text== "جوین":
                #for ad in admin:
                try:
                    if m.author_guid in admin:
                        for chanel in bot.get_messages_by_id(m.object_guid, [m.reply_message_id])["messages"]:
                            if chanel['forwarded_from']['type_from'] == 'Channel':
                                bot.join_chat(chanel['forwarded_from']['object_guid'])
                                m.reply("ربات با موفقیت داخل چنل عضو شد ")
                except:pass
            if text.startswith('for @'):
                
                Thread(target=send2,args=[m]).start()
            elif m.is_forward == True:
                messages = bot.get_messages(guid,None)['messages'][:10]
                for m in messages:
                    try:
                        Thread(target=send,args=[m]).start()
                        # mesID = m['message_id']
                        # if m['forwarded_from']['type_from'] == 'Channel':
                        #     ids.append(mesID)
                        #     dd = bot.forward_messages(guid, ids, branch)
                        #     ids.clear()
                    except:pass
            elif text.count('\n') == 2 or text.count('\n') == 3 or text.count('\n') == 4 or text.count('\n') == 5 or text.count('\n') == 6:
                try:
                    if not "فور" in text:
                        if not m.is_forward == True:
                            if not text.lower().endswith("for"):
                                if not m.message_type == "Image":
                                    bo = random.choices(robo)
                                    bot = Client(session=f"{bo}")
                                    bot.send_text(branch,text)
                                else:
                                    jj = bot.get_download_link(m.object_guid,m.message_id)
                                    l = bot.send_image(branch,jj,text=m.text,thumbnail=xx)
                except:pass
            elif text.startswith("فور ") or text.endswith("فور") or text.lower().startswith("for"):
                if not "for @" in m.text:
                    bot.forward_messages(m.object_guid,[m.message_id],branch)

bot.run()
