#!/usr/bin/env python

import socket, sys
from random import randint

class IRC(object):
    def __init__(self, network, port):
        super(IRC, self).__init__()

        self.network = network
        self.port = port

        self.nick = None
        self.room = None

    def setNick(self, nick):
        self.nick = nick

    def setRoom(self, room):
        if (type(room) != str or len(room) <= 1 or room[0] != '#'):
          print "Invalid room name"
          return

        self.room = room

    def getUserFromMessage(self, message):
        user = None

        if ("@" in message):
          message = message.split("@", 1)[0]
          if ("!~" in message):
            user = message.split("!~", 1)[1]

        return user

    def sendHello(self, irc, user=None, data=None):
        if (user == None):
          user = self.getUserFromMessage(data)

        hello_messages = [
          "hello",
          "hello there",
          "hey",
          "hey there",
          "hi",
          "hi there",
          "howdy",
          "oh, nice to see you",
          "whats up",
        ]

        message  = hello_messages[randint(0, len(hello_messages)-1)]
        say_user = bool(randint(0, 3)) # 75% chance yes

        if (say_user and user != None):
          irc.send('PRIVMSG %s :%s %s\r\n' % (self.room, message, user))
        else:
          irc.send('PRIVMSG %s :%s\r\n' % (self.room, message))

    def exec_(self):
        if (self.nick == None):
          print "Nick not defined yet"
          return 1

        if (self.room == None):
          print "Room not defined yet"
          return 1

        irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        irc.connect((self.network, self.port))

        print irc.recv(4096)

        irc.send('NICK %s\r\n' % (self.nick))
        irc.send('USER %s %s %s :%s\r\n' % (self.nick, self.nick, self.nick, self.nick))
        irc.send('JOIN %s\r\n' % (self.room))

        while True:
          data = irc.recv(4096)

          # PING PONG

          if data.find('PING') != -1:
            irc.send('PONG ' + data.split() [ 1 ] + '\r\n')


          # Conversations with kxbot (direct)

          if data.find('kxbot: ') != -1:
            user = self.getUserFromMessage(data)

            if (user != None):

              if 'kxbot: hello' in data:
                self.sendHello(irc, user)
              elif 'kxbot: hey' in data:
                self.sendHello(irc, user)
              elif 'kxbot: hi' in data:
                self.sendHello(irc, user)
              elif 'kxbot: howdy' in data:
                self.sendHello(irc, user)
              elif 'kxbot: whats up' in data:
                self.sendHello(irc, user)
              elif 'kxbot: what\'s up' in data:
                self.sendHello(irc, user)

              elif 'kxbot: tell ' in data:
                irc.send('PRIVMSG %s :TODO\r\n' % (self.room, user))

          # Hello messages

          elif 'hello kxbot' in data:
            self.sendHello(irc, data=data)
          elif 'hello there kxbot' in data:
            self.sendHello(irc, data=data)
          elif 'hey kxbot' in data:
            self.sendHello(irc, data=data)
          elif 'hey there kxbot' in data:
            self.sendHello(irc, data=data)
          elif 'hi kxbot' in data:
            self.sendHello(irc, data=data)
          elif 'hi there kxbot' in data:
            self.sendHello(irc, data=data)
          elif 'howdy kxbot' in data:
            self.sendHello(irc, data=data)
          elif 'whats up kxbot' in data:
            irc.send('PRIVMSG %s :nothing really...\r\n' % (self.room))
          elif 'what\'s up kxbot' in data:
            irc.send('PRIVMSG %s :nothing...\r\n' % (self.room))

          # Commands
          elif data.find('!p kxstudio git clone') != -1:
            irc.send('PRIVMSG %s :git clone git://kxstudio.git.sourceforge.net/gitroot/kxstudio/kxstudio\r\n' % (self.room))

          elif data.find('!p kxstudio git') != -1:
            irc.send('PRIVMSG %s :http://kxstudio.git.sourceforge.net\r\n' % (self.room))

          elif data.find('!p kxstudio download') != -1:
            irc.send('PRIVMSG %s :http://kxstudio.sourceforge.net/download\r\n' % (self.room))

          elif data.find('!p kxstudio help') != -1:
            irc.send('PRIVMSG %s :http://kxstudio.sourceforge.net/help\r\n' % (self.room))

          elif data.find('!p kxstudio paste ') != -1:
            irc.send('PRIVMSG %s :TODO\r\n' % (self.room))

          elif data.find('!p kxstudio paste') != -1:
            irc.send('PRIVMSG %s :http://kxstudio.sourceforge.net/paste\r\n' % (self.room))

          elif data.find('!p kxstudio') != -1:
            irc.send('PRIVMSG %s :http://kxstudio.sourceforge.net\r\n' % (self.room))

          elif data.find('!p festige git') != -1:
            irc.send('PRIVMSG %s :FeSTige does not have a git repo\r\n' % (self.room))

          elif data.find('!p festige') != -1:
            irc.send('PRIVMSG %s :http://festige.sourceforge.net\r\n' % (self.room))

          elif data.find('!p') != -1:
            irc.send('PRIVMSG %s :Invalid KXStudio Team project\r\n' % (self.room))

          elif data.find('!quit') != -1:
            irc.send('PRIVMSG %s :Ok, cya!\r\n' % (self.room))
            irc.send('QUIT\r\n')

          if (data):
            print data

        return 0

#--------------- main ------------------
if __name__ == '__main__':

    # Create object
    my_irc = IRC('barjavel.freenode.net', 6667)

    # Set basic data
    my_irc.setNick("kxbot")
    my_irc.setRoom("#kxstudio")

    # App-Loop
    sys.exit(my_irc.exec_())
