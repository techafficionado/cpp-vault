import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from os.path import basename


#########################################################################################
# Send Email
#########################################################################################
def sendEmail(fname):
    global g_conf
    smtpsvr = None
    recepients = None
    subject = None
    try:
        try:
            if g_conf:
                smtpsvr = g_conf["smtpserver"]
                recepients =  g_conf["recepients"]
                subject = g_conf["subject"]
                text = g_conf["text"]
        except Exception as e:
            logger.error("Exception:"+str(e))
            smtpsvr= "10.10.10.10"
            recepients = "abc@xyz.com"
            subject = "My Report"
            text = "PFA the  Report"

        logger.info("Sending Email to Recepients: " + str(recepients))

        sm = smtplib.SMTP(smtpsvr) 

        msg = MIMEMultipart()
        msg['To'] = recepients
        msg['From'] = "donotreply@xyz.com"
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        with open(fname,"rb") as f:
            part = MIMEApplication(f.read(), Name=basename(fname))

        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(fname)
        msg.attach(part)

        sm.sendmail('donotreply@xyz.com',recepients.split(","), msg.as_string())
    except Exception as e:
        logger.error("Exception: " + str(e))

