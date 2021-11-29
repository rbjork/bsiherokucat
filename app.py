from flask import Flask, request, render_template, session, jsonify
from flask_session import Session

#from awsemail import sendEmailByAPIGateway, sendUserInfo, get_client_ip
from Pricing import Pricing
import random
import pdb
import json
import os
import random
import json
from datetime import datetime

app = Flask(__name__)


sess = Session()
st = [c for c in "abcdefghijklmnopqrstuvwxyz"]
random.shuffle(st)

SHOPPING_CART = "SHOPPINGCART"

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
# 	)



@app.route('/', methods=['GET','POST'])
def bsicatalog():
	return render_template("ParcelCatalog.html")

userCache = {}


def saveUserCounties(userIP,counties):
	data = {'date':datetime.today().day,'counties':counties}
	#userCache[userIP] = data
	with open("./requests/request_{}.txt".format(userIP),'w') as fw:
		fw.write(json.dumps(data))
		fw.close()

def getUserCounties(userIP):
	with open("./requests/request_{}.txt".format(userIP),'r') as fr:
		data = json.load(fr)
		fr.close()
	return data['counties']

#Gets around issue of Session probs.  But this does not give quote numbers
@app.route('/requestforquote', methods=['POST','GET'])
def request4quote():
	try:
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
		letters = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ'
		bsicode = []
		for i in range(5):
			bsicode.append(letters[random.randrange(25)]);
		bsicodestr = ''.join(bsicode)
		#pdb.set_trace()
		counties = json.loads(request.form.get('shoppingcartfips'));
		#counties = json.loads(request.form.getlist('counties')[0])
		numinstock, pricestock, numnotinstock, pricens, numtotal, totalprice = Pricing().computeprice(counties)
	except Exception as e:
		counties = None
	return render_template("requestforquote.html",counties=counties, bsicode=bsicodestr, numinstock=numinstock, pricestock=pricestock,
        numnotinstock=numnotinstock, pricens=pricens, numtotal=numtotal, price=totalprice)



@app.route('/quoteform')
def quoteform():
	letters = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ'
	bsicode = []
	for i in range(5):
		bsicode.append(letters[random.randrange(25)])
	bsicodestr = ''.join(bsicode)
	try:
		#pdb.set_trace()
		counties = getUserCounties(request.remote_addr) #session[SHOPPING_CART]
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
		sender = request.form.get('Email')
		print(message, sender)
		if not os.path.exists("./requests"):
			os.mkdir("requests")
		with open("./requests/request_{}.txt".format(sender.replace("@","_")),'w') as fw:
			fw.write(message)
			fw.close()

	except Exception as e:
		print(str(e))
		return HttpResponse('Invalid Request Quote Form data.')

	recipients = ['ronaldbjork@sbcglobal.net','INFO@boundarysolutions.com']
	#sendEmailByAPIGateway(sender,subject,message)
	return render_template("requestsent.html")


@app.route('/requests')
def getCustomers():
	search_dir = "./requests"
	files = os.listdir(search_dir)
	reqfiles = [os.path.join(search_dir, f) for f in files]
	 # add path to each file
	reqfiles.sort(key=lambda x: os.path.getmtime(x))
	reqfiles.reverse()
	return render_template("requests.html", reqfiles=reqfiles)


@app.route('/clearrequest')
def clearrequests():
	search_dir = "./requests"
	files = os.listdir(search_dir)
	reqfiles = [os.path.join(search_dir, f) for f in files]
	for f in reqfiles:
		os.remove(f)
	return jsonify({'success':True})


@app.route('/getcustomer',methods=['POST'])
def getcustomer():
	file = request.form.get('customers')
	with open('{}'.format(file),'r') as fr:
		data = fr.read()
		fr.close()
	return render_template("customerrequest.html",customer=data)

if __name__ == "__main__":
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run()
