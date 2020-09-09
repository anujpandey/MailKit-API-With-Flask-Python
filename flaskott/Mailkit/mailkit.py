import json
import requests
import config
from flaskott.Mailkit import config
import xml.etree.ElementTree as ET
import base64
from xml.etree import ElementTree as et
from xml.etree.ElementTree import parse, tostring
def call_mailkit_campaigns_list(client_id,client_MD5,ID_message):

    payload = {
    'id': client_id,
    'md5':client_MD5,
    'function':'mailkit.campaigns.list',
    'ID_message': ID_message
    }
    payload = json.dumps(payload)
    response = requests.request("POST", config.Config.URL_json, headers=config.Config.headers_json, data=payload)
    return (response.text.encode('utf8'))


def get_allow_Mail_ID(res):
    root = ET.fromstring(res)
    for ID_ALLOW_EMAIL in root.iter("i4"):
        ID_ALLOW_EMAIL = str(ID_ALLOW_EMAIL.text)
        ID_ALLOW_EMAIL  = convertToBase64(ID_ALLOW_EMAIL)
    return (ID_ALLOW_EMAIL)

def convertToBase64(ID_ALLOW_EMAIL):
    b = bytes(ID_ALLOW_EMAIL, 'utf-8')
    EncodedString = base64.b64encode(b)
    EncodedString = EncodedString.decode("utf-8")
    return (EncodedString)

def call_allow_Mail_ID(client_id,client_MD5):

    payload = "<?xml version=\"1.0\"?>\n<methodCall>\n<methodName>mailkit.profile.emails.list</methodName>\n<params>\n <param>\n  <value>\n   <int>136307099</int>\n  </value>\n </param>\n <param>\n  <value>\n   <string>7768bd290b939222e3a33fafb3d7a877</string>\n  </value>\n </param>\n</params>\n</methodCall>"
    response = requests.request("POST", config.Config.URL_xml, headers=config.Config.headers_xml, data=payload)
    res = (response.text.encode('utf8'))
    ID_ALLOW_EMAIL = get_allow_Mail_ID(res)
    #print(ID_ALLOW_EMAIL)
    return (ID_ALLOW_EMAIL)

def put_base64_2_payload(payload):
    root = ET.fromstring(payload)

    data1 = root.find(".//member/[name='name']")
    data1_val = data1.find(".//value/string")
    data1_val.text = Name_of_campaign

    data2 = root.find(".//member/[name='subject']")
    data2_val = data2.find(".//value/string")
    data2_val.text = Subject_of_campaign

    data3 = root.find(".//member/[name='ID_allow_email']")
    data3_val = data3.find(".//value/string")
    data3_val.text = ID_ALLOW_EMAIL


#client_id,client_MD5,func_Called,name_of_campaign, subject_of_campaign, ID_of_sender_address,type_message
def call_create_mailkit_campaigns(client_id,client_MD5,name_of_campaign, subject_of_campaign,type_message):
    #global Name_of_campaign, Subject_of_campaign, ID_ALLOW_EMAIL
    ID_ALLOW_EMAIL = call_allow_Mail_ID(client_id,client_MD5)
    Name_of_campaign  = convertToBase64(name_of_campaign)
    Subject_of_campaign  = convertToBase64(subject_of_campaign)

    payload = "<?xml version=\"1.0\"?>\n <methodCall>\n  <methodName>mailkit.campaigns.create</methodName>\n  <params>\n   <param>\n   <value>\n    <int>136307099</int>\n   </value>\n   </param>\n   <param>\n   <value>\n    <string>7768bd290b939222e3a33fafb3d7a877</string>\n   </value>\n   </param>\n   <param>\n   <value>\n    <struct>\n     <member>\n      <name>name</name>\n      <value>\n       <string>Anuj Pandey</string>\n      </value>\n     </member>\n     <member>\n      <name>subject</name>\n      <value>\n       <string>subject</string>\n      </value>\n     </member>\n     <member>\n      <name>ID_allow_email</name>\n      <value>\n       <string>ID of sending email address</string>\n      </value>\n     </member>\n     <member>\n      <name>type_message</name>\n      <value>\n       <string>email</string>\n      </value>\n     </member>\n     <member>\n      <name>ID_delivery_feed</name>\n      <value>\n       <string>ID of delivery feed datasource</string>\n      </value>\n     </member>\n     <member>\n      <name>google_analytics</name>\n      <value>\n       <string>true|false</string>\n      </value>\n     </member>\n     <member>\n      <name>analytic_name</name>\n      <value>\n       <string>name for analytics</string>\n      </value>\n     </member>\n     <member>\n      <name>ID_tagset</name>\n      <value>\n       <string>ID of tagset</string>\n      </value>\n     </member>\n     <member>\n      <name>content</name>\n      <value>\n       <string>content 1</string>\n      </value>\n     </member>\n     <member>\n      <name>reply_to</name>\n      <value>\n       <string>email@domain.com</string>\n      </value>\n     </member>\n     <member>\n      <name>unsubscribe_email</name>\n      <value>\n       <string>email@domain.com</string>\n      </value>\n     </member>\n     <member>\n      <name>web_template</name>\n      <value>\n       <string>true|false</string>\n      </value>\n     </member>\n     <member>\n      <name>style_inline</name>\n      <value>\n       <string>true|false</string>\n      </value>\n     </member>\n     <member>\n      <name>ID_unsubscribe_group</name>\n      <value>\n       <string>ID of topic</string>\n      </value>\n     </member>\n    </struct>\n   </value>\n   </param>\n </params>\n</methodCall>"

    root = ET.fromstring(payload)
    prop = root.find(".//member/[name='ID_allow_email']")
    ID_allow_email = prop.find(".//value/string")
    ID_allow_email.text = ID_ALLOW_EMAIL

    prop = root.find(".//member/[name='name']")
    name = prop.find(".//value/string")
    name.text = Name_of_campaign

    prop = root.find(".//member/[name='subject']")
    subject = prop.find(".//value/string")
    subject.text = Subject_of_campaign

    payload = ET.tostring(root)

    response = requests.request("POST", config.Config.URL_xml, headers=config.Config.headers_xml, data=payload)
    res = (response.text.encode('utf8'))

    root = ET.fromstring(res)
    for campaign_mailkit_list in root.iter("i4"):
        campaign_mailkit_list = str(campaign_mailkit_list.text)
    return(campaign_mailkit_list)

def mailkit_mailinglist_list():

    payload = "<?xml version=\"1.0\"?>\n<methodCall>\n<methodName>mailkit.mailinglist.list</methodName>\n<params>\n <param>\n  <value>\n   <int>136307099</int>\n  </value>\n </param>\n <param>\n  <value>\n   <string>7768bd290b939222e3a33fafb3d7a877</string>\n  </value>\n </param>\n</params>\n</methodCall>"
    response = requests.request("POST", config.Config.URL_xml, headers=config.Config.headers_xml, data=payload)
    return (response.text.encode('utf8'))

def call_sendemailMail(client_id,client_MD5,campaign_ID,Send_to,subject,content):
    #call_create_mailkit_campaigns()
    mailinglist_list  = mailkit_mailinglist_list()

    root = ET.fromstring(mailinglist_list)
    for ID_EMAIL in root.iter("i4"):
        ID_EMAIL = str(ID_EMAIL.text)
        #ID_EMAIL  = convertToBase64(ID_EMAIL)


    payload = "<?xml version=\"1.0\"?>\n<methodCall>\n  <methodName>mailkit.sendmail</methodName>\n  <params>\n    <param>\n      <value>\n        <int>136307099</int>\n      </value>\n    </param>\n    <param>\n      <value>\n        <string>7768bd290b939222e3a33fafb3d7a877</string>\n      </value>\n    </param>\n    <param>\n      <value>\n        <int>mailinglist_id</int>\n      </value>\n    </param>\n    <param>\n      <value>\n        <int>campaign_id</int>\n      </value>\n    </param>    \n    <param>\n      <value>\n        <struct>\n          <member>\n            <name>send_to</name>\n            <value>\n              <string>email@sample.com</string>\n            </value>\n          </member>\n          <member>\n            <name>subject</name>\n            <value>\n              <string>optional subject</string>\n            </value>\n          </member>\n          <member>\n            <name>message_data</name>\n            <value>\n              <string>optional message body</string>\n            </value>\n          </member>\n          <member>\n            <name>content</name>\n            <value>\n              <struct>\n                <member>\n                  <name>var1</name>\n                  <value>\n                    <string>variable 1</string>\n                  </value>\n                </member>\n                <member>\n                  <name>other_name</name>\n                  <value>\n                    <string>variable 2</string>\n                  </value>\n                </member>\n              </struct>\n            </value>\n          </member>\n        </struct>\n      </value>\n    </param>\n    </params>\n</methodCall>"

    root = ET.fromstring(payload)
    ID_allow_email = root.findall(".//value/int")
    for ID_allow_email in ID_allow_email:
        if (ID_allow_email.text) == "mailinglist_id":
            ID_allow_email.text = ID_EMAIL
        elif (ID_allow_email.text) == "campaign_id":
            ID_allow_email.text = campaign_ID

    value_string = root.find(".//member/[name='send_to']")
    value_string = value_string.find(".//value/string")
    value_string.text = Send_to

    value_string = root.find(".//member/[name='subject']")
    value_string = value_string.find(".//value/string")
    value_string.text = subject

    message_body = convertToBase64(content)
    body = root.find(".//member/[name='message_data']")
    body = body.find(".//value/string")
    body.text = message_body

#----------------------Content_____________________
#    content  = convertToBase64(content)
#    content_data = root.find(".//member/[name='var1']")
#    content_data_val = content_data.find(".//value/string")
#    content_data_val.text = content
##----------------------Content_____________________
    payload = ET.tostring(root)
    response = requests.request("POST", config.Config.URL_xml, headers=config.Config.headers_xml, data=payload)
    print(response.text.encode('utf8'))
    return (response.text.encode('utf8'))
