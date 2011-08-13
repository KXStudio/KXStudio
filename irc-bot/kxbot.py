#!/usr/bin/env python

import socket

network = 'barjavel.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )

print irc.recv ( 4096 )
irc.send ( 'NICK kxbot\r\n' )
irc.send ( 'USER kxbot kxbot kxbot :KXStudio Bot\r\n' )
irc.send ( 'JOIN #kxstudio\r\n' )

i = 0
while True:
  data = irc.recv(4096)

  if data.find('PING') != -1:
    irc.send('PONG ' + data.split() [ 1 ] + '\r\n')

  if data.find('!kxbot quit') != -1:
    irc.send('PRIVMSG #kxstudio :Ok, cya!\r\n')
    irc.send('QUIT\r\n')

  if data.find('hi kxbot') != -1:
    irc.send('PRIVMSG #kxstudio :Hey you\r\n')

  if data.find('kxbot: think') != -1:
    irc.send('ME #kxstudio :is thinking...\r\n')

  elif (i == 20):
    irc.send('PRIVMSG #kxstudio :Have to go now...\r\n')
  elif (i >= 21):
    irc.send('PRIVMSG #kxstudio :I\'ll be happy to stay longer next time!\r\n')
    irc.send('QUIT\r\n')

  if (data):
    print data

  i += 1
  print i
