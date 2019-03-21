import requests
import time
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

class TextService:
    
    _key = ''
    _base_url = ''

    def __init__(self, region, key):
        self._key = key
        self._base_url = '{}.api.cognitive.microsoft.com'.format(region)

    def BuildDocumentList(self, textlist):
        body = dict()

        docs = []

        for i, t in enumerate(textlist):
            doc = dict()
            doc["id"] = str(i)
            doc["text"] = t
            docs.append(doc)

        body["documents"] = docs
        return body

    def DetectLanguage(self, documents):
        data = self._doPostRequest('/text/analytics/v2.0/languages', documents, None)
        return data

    def AnalyzeSentiment(self, documents):
        data = self._doPostRequest('/text/analytics/v2.0/sentiment', documents, None)
        return data

    def ExtractKeyPhrases(self, documents):
        data = self._doPostRequest('/text/analytics/v2.0/keyPhrases', documents, None)
        return data

    def IdentityEntities(self, documents):
        data = self._doPostRequest('/text/analytics/v2.1-preview/entities', documents, None)
        return data

    def _doGetRequest(self, url, params):
        
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self._key,
        }

        try:
            conn = http.client.HTTPSConnection(self._base_url)
            conn.request("GET", "%s?%s" % (url, params), None, headers)
            response = conn.getresponse()
            data = response.read()
            jData = json.loads(data.decode('utf8'))
            conn.close()
            return jData
        except Exception as e:
            print('Error: %s' % str(e))

    def _doPostRequest(self, url, body, params=None):
        
        headers = {
            'Ocp-Apim-Subscription-Key': self._key,
            'Content-Type': 'application/json'
        }

        try:
            conn = http.client.HTTPSConnection(self._base_url)
            conn.request("POST", "%s" % url, json.dumps(body), headers)
            response = conn.getresponse()
            data = response.read()
            jData = json.loads(data.decode('utf8'))
            conn.close()
            return jData
        except Exception as e:
            print('Error: %s' % str(e))

  

  