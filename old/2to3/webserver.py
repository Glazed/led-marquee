#Copyright Jon Berg , turtlemeat.com

import inspect
import string,cgi,time,urllib.request,urllib.parse,urllib.error
from os import curdir, sep
from http.server import BaseHTTPRequestHandler, HTTPServer
from marqueewriter import MarqueeWriter
from spamFilter import SpamFilter

## TODO: it really sucks that we need to use a global variable
marquee = MarqueeWriter("/dev/tty.usbserial", 115200)

        #"com3"               on windows try using http://plugable.com/drivers/prolific/ (not tested yet)
        #"/dev/tty.usbserial"    on mac w/ http://plugable.com/drivers/prolific/


spam = SpamFilter(3,4)


class WebServer(BaseHTTPRequestHandler):

    
    
    def __init__(self, one, two, three):
        BaseHTTPRequestHandler.__init__(self, one, two, three)
        
    
    def do_GET(self):
        try:
            f = open(curdir + sep + "uploadText.html",'rb') 
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
                
            return
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
     

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        length= int(self.headers['content-length'])

        #remote_host = self.headers['host']
        remote_host = self.client_address[0]
        #print '> Host is: ' + str(remote_host)



        
        txt = self.rfile.read(length)
        
        message = ""
        if (urllib.parse.unquote_plus(txt[:7]) == "textTo="):
           message = urllib.parse.unquote_plus(txt[7:]).upper()
        else:
            message = urllib.parse.unquote_plus(txt.upper())

        print('> New web message recieved: ', message)
        message=spam.check(remote_host,message)
        
        marquee.queueMessage(message)
        
        self.wfile.write((txt[7:]))
        return
