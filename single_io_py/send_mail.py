#!/usr/bin/python3

from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

import smtplib
import time

class sendEmail:
    def __init__(self,from_addr,password,to_addr,smtp_server):
        self.from_addr = from_addr
        self.password = password
        self.to_addr = to_addr
        self.smtp_server = smtp_server
        self.cur_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        self.start_time = "\nStart time :"+self.cur_time

    def _format_addr(self,s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_alert(self):
        
        self.cur_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        self.stop_time = "\nHalt time :"+self.cur_time
        
        self.alert = self.start_time + "\n--------" +self.stop_time
        
        self.msg = MIMEText(self.alert, 'plain', 'utf-8')
        
        self.msg['From'] = self._format_addr('RPi UPSPACK V2 <%s>' % self.from_addr)
        self.msg['To'] = self._format_addr('To Admin <%s>' % self.to_addr)
        self.msg['Subject'] = Header('From UPS Alert', 'utf-8').encode()

        
        self.server = smtplib.SMTP(self.smtp_server, 25)
        #self.server.set_debuglevel(1)
        print("starting sending Alert email\n")
        self.server.login(self.from_addr, self.password)
        self.server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        self.server.quit()
        print("email have been sent out!\n")


if __name__ == "__main__":
    print("This is email alert class file.\n")
    #test = sendEmail("xxx@163.com","password","xxx@163.com","smtp.xxx.com")
    #test.send_alert();