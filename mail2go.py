from os import environ
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# read MailerToGo env vars
# mailertogo_host     = environ.get('MAILERTOGO_SMTP_HOST')
# mailertogo_port     = environ.get('MAILERTOGO_SMTP_PORT', 587)
# mailertogo_user     = environ.get('MAILERTOGO_SMTP_USER')
# mailertogo_password = environ.get('MAILERTOGO_SMTP_PASSWORD')
# mailertogo_domain   = environ.get('MAILERTOGO_DOMAIN', "boundarysolutions.com")

def sendEmail(customeremail,text):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Quote Request'
    msg['From'] = customeremail
    msg['To'] = 'dklein@boundarysolutions.com'
    textmsg = MIMEText(text,'plain')
    msg.attach(textmsg)
    smtp  smtplit.SMTP(SMTP_ADDRESS)
    smtp.sendmail(SMTP_ADDRESS,useremail,msg.as_string())
    smtp.quit()


def sendEmail2(customername, customeremail, text):
    # sender
    #sender_user = useremail
    sender_email = customeremail
    sender_name = customername

    # recipient
    recipient_email = 'dklein@boundarysolutions.com' # change to recipient email. Make sure to use a real email address in your tests to avoid hard bounces and protect your reputation as a sender.
    recipient_name = 'Dennis dklein'

    # subject
    subject = 'Request For Quote'

    # text body
    body_plain = (text)

    # html body
    line_break = '\n' #used to replace line breaks with html breaks


    # create message container
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = email.utils.formataddr((sender_name, sender_email))
    message['To'] = email.utils.formataddr((recipient_name, recipient_email))

    # prepare plain and html message parts
    part1 = MIMEText(body_plain, 'plain')
    #part2 = MIMEText(body_html, 'html')

    # attach parts to message

    message.attach(part1)
    #message.attach(part2)

    # send the message.
    try:
        server = smtplib.SMTP(mailertogo_host, mailertogo_port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(mailertogo_user, mailertogo_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.close()
    except Exception as e:
        print ("Error: ", e)
    else:
        print ("Email sent!")
