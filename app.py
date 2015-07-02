#!/usr/bin/env python

import Skype4Py
import sys
import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read(['skypebot.cfg', os.path.expanduser('~/.skypebot.cfg')])

TOPIC_NAME=config.get('topic', 'name')
CHAT_ID=config.get('chat', 'id')

print 'Topic:   ', TOPIC_NAME
print 'Chat ID: ', CHAT_ID

print 'Attaching to Skype via Skype4Py...'
skype = Skype4Py.Skype()
skype.Attach()

print 'Your full name:', skype.CurrentUser.FullName

chat = skype.Chat(CHAT_ID)
if TOPIC_NAME != chat.Topic:
    print 'ERROR: chat topic mismatch (expected: {}, but found: {})!'.format(TOPIC_NAME, chat.Topic)
    exit(1)

print 'Chat "{}" found'.format(chat.Topic)

if len(sys.argv) == 1:
    print 'WARN: message not specified, try adding command-line arguments.'
    exit(2)

for text in sys.argv[1:]:
    message = 'Bot: {}'.format(text)
    print "sending: ", message
    chat.SendMessage(message)
