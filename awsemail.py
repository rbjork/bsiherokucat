#import boto3
#from botocore.exceptions import ClientError

import requests

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "QuoteRequest <enquire@boundarysolutions.com>"
# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT = "dklein@boundarysolutions.com"
AWS_REGION = "us-west-2"
SUBJECT = "Request for Quote"
CHARSET = "UTF-8"

CONFIGURATION_SET = "ConfigSet"

def sendEmail(senderName, subject, bodytext):
    BODY_TEXT = bodytext
    BODY_HTML = """<html>
            <head></head>
            <body>
              <h1>{}</h1>
              <p>{}</p>
            </body>
            </html>""".format(subject, senderName, bodytext)

    # client = boto3.client('ses',region_name=AWS_REGION)  # disabled due to migration to non aws platform
    # try:
    #     response = client.send_email(
    #         Destination={
    #             'ToAddresses': [
    #                 RECIPIENT,
    #             ],
    #         },
    #         Message={
    #             'Body': {
    #                 'Html': {
    #                     'Charset': CHARSET,
    #                     'Data': BODY_HTML,
    #                 },
    #                 'Text': {
    #                     'Charset': CHARSET,
    #                     'Data': BODY_TEXT,
    #                 },
    #             },
    #             'Subject': {
    #                 'Charset': CHARSET,
    #                 'Data': SUBJECT,
    #             },
    #         },
    #         Source=SENDER,
    #         ConfigurationSetName=CONFIGURATION_SET,
    #     )
    # # Display an error if something goes wrong.
    # except ClientError as e:
    #     print(e.response['Error']['Message'])
    # else:
    #     print("Email sent! Message ID:"),
    #     print(response['MessageId'])


def sendEmailByAPIGateway(senderName, subject, bodytext):
    orderdata = {"subject":subject, "sender":senderName, "bodytext":bodytext}
    headers = {"Content-Type": "application/json", "x-api-key": "0eup5py6mu4BU4AUpgXYv2nojcd14CauXT5gD99e"}
    r = requests.post('https://z12t0wnq6e.execute-api.us-west-2.amazonaws.com/bsiorderequest/countymeta', json=orderdata, headers=headers)
    print("sendEmailByAPIGateway response",r.status_code)



#from django.contrib.gis.geoip2 import GeoIP2

# def get_user_location(ip):  # ip is a string of format dd(d).dd(d).dd(d).dd(d)
#     g = GeoIP2()
#     country = g.country('www.boundarysolutions.com')
#     city = g.city(ip)
#     loc = str(g.geos(ip).wkt)
#     return {"city":city, "location":loc}

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def sendUserInfo(senderIP, webpage):  # ip can be gotten from the request object
    print("sendUserInfo",senderIP, webpage)
    #location = get_user_location(senderIP)
    logdata = {"senderip":senderIP, "webpage":webpage}
    headers = {"Content-Type": "application/json", "x-api-key": "cNJtoxCNACZoLnJbfe0H2vyYC8lb0DT9KZoTarg7"} # need key
    r = requests.post('https://s35wqli2bc.execute-api.us-west-1.amazonaws.com/parcelcatone/logging', json=logdata, headers=headers) # need url
    print("sendUserInfo",r.status_code)
    return r
