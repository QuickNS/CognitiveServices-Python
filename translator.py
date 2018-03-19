import http.client, urllib.request, urllib.parse, urllib.error, base64, json
from xml.etree import ElementTree

class TranslatorService:

    key = ''

    def __init__(self, key):
        self.key = key

    def translate(self, textToTranslate, to_lang, use_nn=True):

        if use_nn:
            category = 'generalnn'
        else:
            category = 'general'

        # Define the request headers.
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }

        params = urllib.parse.urlencode({
        # Request parameters
        'text': textToTranslate,
        'to': to_lang,
        'category' : category
        })

        try:
            #conn = http.client.HTTPSConnection('localhost',port=8888 )
            #conn.set_tunnel('api.microsofttranslator.com')
            conn = http.client.HTTPSConnection('api.microsofttranslator.com')
            conn.request("GET", "/V2/Http.svc/Translate?%s" % params, None, headers)
            response = conn.getresponse()
            data = response.read()
            # parse xml return values
            translation = ElementTree.fromstring(data.decode('utf-8'))
            conn.close()
            return translation.text

        except Exception as e:
            print('Error: %s' % str(e))
            
    def translateArray(self, list_strings, to_lang, use_nn=True):
        
        if use_nn:
            category = 'generalnn'
        else:
            category = 'general'

        # Define the request headers.
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Content-Type' : 'text/xml; charset=utf-8'
        }

        strings_xml = ''
        for i in list_strings:
            strings_xml = strings_xml + '<string xmlns=\"http://schemas.microsoft.com/2003/10/Serialization/Arrays\">{}</string>'.format(i)
        
        body = "<TranslateArrayRequest>"  + \
                    "<AppId />" + \
                    "<Options>" + \
                        "<Category xmlns=\"http://schemas.datacontract.org/2004/07/Microsoft.MT.Web.Service.V2\">{}</Category>".format(category) + \
                        "<ContentType xmlns=\"http://schemas.datacontract.org/2004/07/Microsoft.MT.Web.Service.V2\">text/plain</ContentType>" + \
                        "<ReservedFlags xmlns=\"http://schemas.datacontract.org/2004/07/Microsoft.MT.Web.Service.V2\" />" + \
                        "<State xmlns=\"http://schemas.datacontract.org/2004/07/Microsoft.MT.Web.Service.V2\" />" + \
                        "<Uri xmlns=\"http://schemas.datacontract.org/2004/07/Microsoft.MT.Web.Service.V2\" />" + \
                        "<User xmlns=\"http://schemas.datacontract.org/2004/07/Microsoft.MT.Web.Service.V2\" />" + \
                    "</Options>" + \
                    "<Texts>" + \
                    strings_xml + \
                    "</Texts>" + \
                    "<To>{}</To>".format(to_lang) + \
                    "</TranslateArrayRequest>"
              
        try:
            #conn = http.client.HTTPSConnection('localhost',port=8888 )
            #conn.set_tunnel('api.microsofttranslator.com')
            conn = http.client.HTTPSConnection('api.microsofttranslator.com')
            conn.request("POST", "/V2/Http.svc/TranslateArray", body.encode('utf8'), headers)
            response = conn.getresponse()
            data = response.read()
            # parse xml return values
            translations = ElementTree.fromstring(data.decode('utf-8'))
            conn.close()
            translation_list = []
            for child in translations.iter('{http://schemas.datacontract.org/2004/07/Microsoft.MT.Web.Service.V2}TranslatedText'):
                translation_list.append(child.text)
            return translation_list    

        except Exception as e:
            print('Error: %s' % str(e))
            
    def detect(self, textToDetect):
        # Define the request headers.
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }

        params = urllib.parse.urlencode({
        # Request parameters
        'text': textToDetect,
        })

        try:
            conn = http.client.HTTPSConnection('api.microsofttranslator.com')
            conn.request("GET", "/V2/Http.svc//Detect?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            # parse xml return values
            detection = ElementTree.fromstring(data.decode('utf-8'))
            conn.close()
            return detection.text

        except Exception as e:
            print('Error: %s' % str(e))

    def getLanguagesForTranslate(self):
        # Define the request headers.
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
        }

        try:
            conn = http.client.HTTPSConnection('api.microsofttranslator.com')
            conn.request("GET", "/V2/Http.svc//GetLanguagesForTranslate", "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            response = ElementTree.fromstring(data.decode('utf-8'))
            conn.close()
           
            language_list = []
            for child in response.iter('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}string'):
                language_list.append(child.text)
            return language_list    

        except Exception as e:
            print('Error: %s' % str(e))    
            
    def getLanguageNames(self, langCodes, locale):
        
        # Define the request headers.
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Content-Type' : 'text/xml; charset=utf-8'
        }

        params = urllib.parse.urlencode({
        # Request parameters
        'locale': locale,
        })
        
        strings_xml = ''
        for i in langCodes:
            strings_xml = strings_xml + '<string>{}</string>'.format(i)
        
        body = "<ArrayOfstring xmlns:i=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns=\"http://schemas.microsoft.com/2003/10/Serialization/Arrays\">"  + \
                    strings_xml + \
                "</ArrayOfstring>"
    
    
        try:
            conn = http.client.HTTPSConnection('api.microsofttranslator.com')
            conn.request("POST", "/V2/Http.svc/GetLanguageNames?%s" % params, body.encode('utf8'), headers)
            response = conn.getresponse()
            data = response.read()
            # parse xml return values
            langs = ElementTree.fromstring(data.decode('utf-8'))
            conn.close()
            language_list = []
            for child in langs.iter('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}string'):
                language_list.append(child.text)
            return language_list    

        except Exception as e:
            print('Error: %s' % str(e))   

