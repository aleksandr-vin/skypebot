import Skype4Py
import sys

TOPIC_NAME = 'hd-testing'

skype = Skype4Py.Skype()
skype.Attach()

print 'Your full name:', skype.CurrentUser.FullName

chat = skype.Chat('#aleksandr.vin/$446238d781b259fe')
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
