from flask import Flask, request, render_template, session, jsonify, Response
from flask_session import Session

#from awsemail import sendEmailByAPIGateway, sendUserInfo, get_client_ip
#from mail2go import *

import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from os import environ

from Pricing import Pricing
import random
import pdb
import json
import os
import random
import json
#import pandas as pd
from datetime import datetime
from werkzeug.utils import secure_filename


#import psycopg2
app = Flask(__name__)

sess = Session()
st = [c for c in "abcdefghijklmnopqrstuvwxyz"]
random.shuffle(st)

userCache = {}
SMTP_ADDRESS = "mail.boundarysolutions.com"
PASSWORD = "XIDIqMpZ3"
SHOPPING_CART = "SHOPPINGCART"

app.config['UPLOAD_FOLDER'] = "static/images"

# from flask_mail import Mail
# mail = Mail(app)
# app.config.update(
# 	DEBUG=True,
# 	#EMAIL SETTINGS
# 	MAIL_SERVER='smtp.gmail.com',
# 	MAIL_PORT=465,
# 	MAIL_USE_SSL=True,
# 	MAIL_USERNAME = 'your@gmail.com',
# 	MAIL_PASSWORD = 'yourpassword'
# )

#import pandas as pd

metadatafile = "QUOTEPAGE.xlsx"
#
#
# @app.route('/populate')
# def populate():
# 	countiesDF = pd.read_excel(metadatafile)
# 	rn = {col:col.replace('%','').strip() for col in countiesDF.columns}
# 	cdfrn = countiesDF.rename(columns=rn)
# 	states = list({c['ST'].strip().upper() for i,c in cdfrn.iterrows() if len(c['ST']) == 2})
# 	cdf = cdfrn.set_index('ST')
# 	cdfn = cdf.copy()
# 	pdb.set_trace()
# 	cdfn.loc[:,cdf.columns[[2,4,5,6,7]]] = cdf.loc[:,cdf.columns[[2,4,5,6,7]]].apply(lambda x:(100*x[0:]/x[0]).round(0),axis=1)
# 	cdfn.loc[:,'PARC_COUNT'] = cdf.loc[:,'PARC_COUNT']
# 	cdfn = cdfn.fillna('')
# 	#pdb.set_trace()
# 	cdfn.loc[:,"VERSIONDATE"] = cdfn.loc[:,"VERSIONDATE"].apply(lambda x: str(x)[0:10])
# 	#pdb.set_trace()
# 	reshtml = render_template("ordergeneratorgrouped.html",counties = cdfn, states = states)
# 	with open('./templates/parcelcat.html','w') as fw:
# 		fw.write(reshtml)
# 		fw.close()
# 	return reshtml


@app.route('/uploadphoto', methods=['GET','POST'])
def uploadphoto():
	before = ""
	after = ""
	message = "Submitted"
	try:
		if len(request.files) > 0:
			for name in request.files:
				file = request.files[name]
				if name == 'photobefore':
					before = file.filename
				if name == 'photoafter':
					after = file.filename
				if not file.filename == '':
					filename = secure_filename(file.filename)
					file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
					message = "file written " + os.getcwd() + "/static/images/" + filename
                        #file.save(os.path.join("./",filename))
	except Exception as e:
		message = "dir:" + os.getcwd() + " error:" + str(e)
	return message


@app.route('/bsiquantarium', methods=['GET','POST'])
def bsiquantarium():
	return render_template("BSIQ.html")


@app.route('/', methods=['GET','POST'])
def bsicatalog():
	return render_template("ParcelCatalog.html")

@app.route("/getbody", methods=['GET'])
def getbody():
	return render_template("ParcelCatalogBody.html")


def saveUserCounties(userIP,counties):
	print("saveUserCounties")
	data = {'date':datetime.today().day,'counties':counties}
	if not os.path.exists("./requests"):
		os.mkdir('./requests')
	print("WRITES TO LOG ","./requests/request_{}.txt".format(userIP))
	with open("./requests/request_{}.txt".format(userIP),'w') as fw:
		fw.write(json.dumps(data))
		fw.close()
		print("Write succeeded")

def getUserCounties(userIP):
	print("FILE EXISTS",os.path.exists("./requests/request_{}.txt".format(userIP)))
	with open("./requests/request_{}.txt".format(userIP),'r') as fr:
		data = json.load(fr)
		fr.close()
	return data['counties']

#Gets around issue of Session probs.  But this does not give quote numbers
@app.route('/requestforquote', methods=['POST','GET'])
def request4quote():
	try:
		print("CALLED request4quote")
		print("CALLING saveUserCounties")
		counties1 = json.loads(request.form.getlist('counties')[0])
		saveUserCounties(request.remote_addr, counties1)
	except Exception as e:
		pass
		#session[SHOPPING_CART] = {}
	return jsonify({'count':0})


# This is the version that should be used to get quote numbers - it uses session object.
@app.route('/requestforquote2', methods=['POST','GET'])
def request4quote2():
	try:
		print("CALLED request4quote2")
		letters = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ'
		bsicode = []
		for i in range(5):
			bsicode.append(letters[random.randrange(25)]);
		bsicodestr = ''.join(bsicode)
		counties = json.loads(request.form.get('shoppingcartfips'));
		#counties = json.loads(request.form.getlist('counties')[0])
		numinstock, pricestock, numnotinstock, pricens, numtotal, totalprice = Pricing().computeprice(counties)
	except Exception as e:
		counties = None
	return render_template("requestforquote.html",counties=counties, bsicode=bsicodestr, numinstock=numinstock, pricestock=pricestock,
        numnotinstock=numnotinstock, pricens=pricens, numtotal=numtotal, price=totalprice)

@app.route('/countyparcels/quoteform')
@app.route('/quoteform')
def quoteform():
	letters = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ'
	bsicode = []
	for i in range(5):
		bsicode.append(letters[random.randrange(25)])
	bsicodestr = ''.join(bsicode)
	try:
		#pdb.set_trace()
		print("Calling getUserCounties")
		counties = getUserCounties(request.remote_addr) #session[SHOPPING_CART]
		print("Number of counties",len(counties))
		numinstock, pricestock, numnotinstock, pricens, numtotal, totalprice = Pricing().computeprice(counties)
	except Exception as e:
		counties = None
		return render_template("requestforquote.html",counties=[], bsicode='', numinstock=0, pricestock=0,
	        numnotinstock=0, pricens=[], numtotal=0, price=0)

	return render_template("requestforquote.html",counties=counties, bsicode=bsicodestr, numinstock=numinstock, pricestock=pricestock,
        numnotinstock=numnotinstock, pricens=pricens, numtotal=numtotal, price=totalprice)


@app.route('/sendquoterequestflaskmail', methods=['POST'])
def sendquoterequestfm():
	msg = Message(subject="Request For Quote",
				  body="Marin, Sonoma",
                  sender="grbtxtmsg@gmail.com",
                  recipients=["dklein@boundarysolutions.com"])
	mail.send(msg)
	return render_template("requestsent.html")


# Replace Django request.POST[*] with request.form.get(*)
@app.route('/sendquoterequest', methods=['POST'])
def sendquoterequest():
	subject = "Request for Quote" #form.cleaned_data['subject']
	try:
		pricetable = request.form.get('pricetabletext')
		fips = request.form.get('fipsorder').replace(' ','\n\r')
		deploypref = request.form.get('deploypref')
		message = "Name: " + request.form.get('FirstName') + " " + request.form.get('LastName') + "  ORG:" + request.form.get('Org')  \
                  + "  Email:" + request.form.get('Email') +  "  Phone:" + request.form.get('Phone') + "\n Comments:" + request.form.get('Comments') + "\n  Order:\n" \
                  + " User Count:" + request.form.get('usercount') + '\n' + fips +'\n' +  deploypref + '\n' + pricetable
		senderemail = request.form.get('Email')
		print(message, senderemail)
		# if not os.path.exists("./requests"):
		# 	os.mkdir("requests")
		# with open("./requests/request_{}.txt".format(sender.replace("@","_")),'w') as fw:
		# 	fw.write(message)
		# 	fw.close()

	except Exception as e:
		print(str(e))
		return Response('Invalid Request Quote Form data.',status=201, mimetype='application/text')

	recipients = ['ronaldbjork@sbcglobal.net','INFO@boundarysolutions.com']
	#sendEmailByAPIGateway(sender,subject,message)
	sendername = request.form.get('FirstName') + " " + request.form.get('LastName')
	sendEmail(sendername, senderemail, message)
	return render_template("requestsent.html")


@app.route('/requests')
def getCustomers():
	search_dir = "./requests"
	if os.path.exists(search_dir):
		files = os.listdir(search_dir)
		reqfiles = [os.path.join(search_dir, f) for f in files]
		 # add path to each file
		reqfiles.sort(key=lambda x: os.path.getmtime(x))
		reqfiles.reverse()
	else:
		os.mkdir(search_dir)
		reqfiles = []
	return render_template("requests.html", reqfiles=reqfiles)


@app.route('/clearrequests')
def clearrequests():
	search_dir = "./requests"
	files = os.listdir(search_dir)
	reqfiles = [os.path.join(search_dir, f) for f in files]
	for f in reqfiles:
		os.remove(f)
	return jsonify({'success':True})


@app.route('/deletecustomerrequest', methods=['POST'])
def deletecustomerrequest():
	data = request.data;
	filepath = data.decode('ascii')[1:-1]
	if os.path.exists(filepath):
		os.remove(filepath.strip())
	return jsonify({'success':True})


@app.route('/getcustomer',methods=['POST'])
def getcustomer():
	file = request.form.get('customers')
	with open('{}'.format(file),'r') as fr:
		data = fr.read()
		fr.close()
	return render_template("customerrequest.html", customer=data)


# def sendEmail(customername, customeremail, text):
# 	msg = MIMEMultipart('alternative')
# 	msg['Subject'] = 'Quote Request'
# 	msg['From'] = customeremail
# 	msg['To'] = 'quotepage@boundarysolutions.com'
# 	textmsg = MIMEText(text,'plain')
# 	msg.attach(textmsg)
# 	smtp = smtplib.SMTP(SMTP_ADDRESS)
# 	smtp.login("quotepage",PASSWORD)
# 	smtp.sendmail(SMTP_ADDRESS, customeremail, msg.as_string())
# 	smtp.quit()


def sendEmail(customername, customeremail, text):

	mailertogo_port     = environ.get('MAILERTOGO_SMTP_PORT', 587)
	mailertogo_host     = environ.get('MAILERTOGO_SMTP_HOST')
	mailertogo_user     = environ.get('MAILERTOGO_SMTP_USER')
	mailertogo_password = environ.get('MAILERTOGO_SMTP_PASSWORD')
	mailertogo_domain   = environ.get('MAILERTOGO_DOMAIN', "bsiquotepage.com")

	print('mailertogo_host',mailertogo_host)
	print('mailertogo_port',mailertogo_port)
	print('mailertogo_user',mailertogo_user)
	print('mailertogo_password',mailertogo_password)
	print('mailertogo_domain',mailertogo_domain)

	sender_user = "quotepage"
	sender_email = "@".join([sender_user, mailertogo_domain])
	sender_name = 'customer'

	# recipient
	recipient_email = 'dklein@boundarysolutions.com' # change to recipient email. Make sure to use a real email address in your tests to avoid hard bounces and protect your reputation as a sender.
	recipient_name = 'Dennis'
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
		print("mailertogo_host",mailertogo_host)
		server = smtplib.SMTP(mailertogo_host, mailertogo_port)
		#rtn = server.connect(mailertogo_host, mailertogo_port)
	except Exception as e:
		print ("Error: ", e)
	else:
		print ("Connected!")
	try:
		server.ehlo()
		server.starttls()
		server.ehlo()
	except Exception as e:
		print ("Error: ", e)
	else:
		print ("ehlo and startls ok!")
	try:
		server.login(mailertogo_user, mailertogo_password)
	except Exception as e:
		print ("Error: ", e)
	else:
		print ("Login ok!")
	try:
		server.sendmail(sender_email, recipient_email, message.as_string())
		server.sendmail(sender_email, 'grbtxtmsg@gmail.com', message.as_string())
		server.close()
	except Exception as e:
		print ("Error: ", e)
	else:
		print ("Login and Email sent!")



if __name__ == "__main__":
	#res = populate()
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run()
