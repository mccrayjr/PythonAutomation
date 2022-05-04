#! /usr/bin/env python3
#sInternet Message Access Protocol
import imapclient
import pyzmail


conn= imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('username', "password")

conn.select_folder('INBOX', readonly=True) # you can use conn.list_folders to list all folders

UIDs = conn.search(['SINCE 20-Aug-2022'])
rawMsg =conn.fetch([4742], ['BODY[]', 'FLAGS'])

message = pyzmail.Pyzmessage.factory(rawMsg[4742][b'BODY[]'])

message.get_subject()
message.get_addresses('from') #or to
message.text_part.charset
message.text_part.get_payload().decode('UTF-8')

# to delete
conn.select_folder('INBOX', readonly=False)
conn.delete_messages([4247, 8080, 3000])
