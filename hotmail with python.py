import smtplib
  
smtpserver = 'smtp.live.com'
AUTHREQUIRED = 1 # if you need to use SMTP AUTH set to 1
smtpuser = 'user@hotmail.com'  # for SMTP AUTH, set SMTP username here
smtppass = 'password'  # for SMTP AUTH, set SMTP password here
     
RECIPIENTS = 'user@hotmail.com'
SENDER = 'sender@hotmail.com'
mssg = "test message"
s = mssg   
 
server = smtplib.SMTP(smtpserver,587)
server.ehlo()
server.starttls() 
server.ehlo()
server.login(smtpuser,smtppass)
server.set_debuglevel(1)
server.sendmail(SENDER, [RECIPIENTS], s)
server.quit()