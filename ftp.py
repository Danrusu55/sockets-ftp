#!/usr/bin/python
from ftplib import FTP
import Tkinter
from Tkinter import *

class FtpProgram:
    def __init__(self,top):
        self.top = top
        self.ftpConn = ''
    def downloadFile(self,fileWithPath):
        text = Text(top)
        try:
            localfile = open('downloaded','wb')
            ftpConn = FTP(eHost.get())
            ftpConn.login(eUser.get(),ePass.get())
            ftpConn.retrbinary('RETR ' + fileWithPath,localfile.write,1024)
            text.insert(INSERT, "Connection + download successful")
        except:
            text.insert(INSERT, "Connection / download failed")
        text.pack(side = LEFT)
        ftpConn.quit()
    def uploadFile(self,fileWithPath):
        text = Text(top)
        try:
            ftpConn = FTP(eHost.get())
            ftpConn.login(eUser.get(),ePass.get())
            ftpConn.storbinary('STOR ' + uploaded,open(fileWithPath, 'rb'))
            text.insert(INSERT, "Connection + upload successful")
        except:
            text.insert(INSERT, "Connection / upload failed")
        text.pack(side = LEFT)
        ftpConn.quit()
    def listFiles(self,path):
        text = Text(top)
        data = []
        try:
            localfile = open('downloaded','wb')
            ftpConn = FTP(eHost.get())
            ftpConn.login(eUser.get(),ePass.get())
            ftpConn.dir(data.append)
            for line in data:
                text.insert(INSERT, line)
        except:
            text.insert(INSERT, "Connection / list files failed")
        text.pack(side = LEFT)
        ftpConn.quit()

#def buildGUI(ftpProgram):
top =Tkinter.Tk()
ftpProgram = FtpProgram(top)

labelframe = LabelFrame(top, text="Connect first")
labelframe.pack(fill="both", expand="yes")

Label(top,text="host").pack(side = LEFT)
eHost= Entry(top, bd =5)
eHost.insert(END, '')
eHost.pack(side= LEFT)
host = eHost.get()

Label(top,text="user").pack(side = LEFT)
eUser = Entry(top, bd =5)
eUser.insert(END, '')
eUser.pack(side= LEFT)
user = eUser.get()

Label(top,text="password").pack(side = LEFT)
ePass = Entry(top, bd =5)
ePass.insert(END, '')
ePass.pack(side= LEFT)
password = ePass.get()

Label(top,text="file with path").pack(side = LEFT)
ePath = Entry(top, bd =5)
ePath.insert(END, '')
ePath.pack(side= LEFT)
fileWithPath = ePath.get()

bConnect = Button(top, text ="Connect", command = lambda: ftpProgram.conn(host,user,password))
bConnect.pack()

bUpload = Button(top, text ="Upload", command = lambda: ftpProgram.uploadFile(fileWithPath))
bUpload.pack()
bDownload = Button(top, text ="Download", command = lambda: ftpProgram.downloadFile(fileWithPath))
bDownload.pack()
bList = Button(top, text ="List", command = lambda: ftpProgram.listFiles(fileWithPath))
bList.pack()

top.mainloop()

#buildGUI(ftpProgram)
#ftpProgram.downloadFile(fileToDownload)
