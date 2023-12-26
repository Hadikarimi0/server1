import os
os.system("pip install rubpy==6.4.6")
from rubpy.sync import Client
from time import sleep


#guid = "c0Balnh03d6f6fba81235d6eba42f0e5"
#guid2 = #"c0yQCt0fbc97596f766c6ba037c652b2"
#tim = 2
#user = "jsjshsbshshsjsjs"
#user2 = "pahlavan"

with Client(session='bot') as client:
	while True:
	
	   h1 = client.update_channel_username(channel_guid=guid, username=user)
	   h2 = client.update_channel_username(channel_guid=guid2, username=user2)

	   sleep(tim)
	   print(h1,h2)
	   
