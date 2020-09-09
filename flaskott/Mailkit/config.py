
import json
class Config:
    URL_json = 'https://api.mailkit.eu/json.fcgi'
    URL_xml = 'https://api.mailkit.eu/rpc.fcgi'


    headers_json = {
    'Content-Type': 'application/json'
    }
    headers_xml = {
    'Content-Type': 'text/xml'
    }
