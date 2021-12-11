'''This module - converts an english text to french and vice versa
'''
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Suchit's Code starts :

#Using the apikey to authenticate
authenticator = IAMAuthenticator(apikey)
#LanguageTranslatorV3 module requires a version
VERSION = "2018-05-01"
#Create an instance (lng_lt) of the LanguageTranslatorV3 to access it's methods
lng_lt = LanguageTranslatorV3(version=VERSION,authenticator=authenticator)
#Passing the service_url
lng_lt.set_service_url(url)


#Create English (en) to French (fr) translation function
def english_french(english_text):
    '''Function translates english text to french'''
    #Invoke the traslate method from the instance (lng_lt)
    english_to_french = lng_lt.translate(\
    text=english_text, model_id='en-fr')
    #See the translated result
    result = english_to_french.get_result()
    #The 'result' is in the 'Dictionary' format, so need to extract the full string / message
    french_text = result["translations"][0]["translation"]
    #return the final text message stored in 'frenchText'
    return french_text


#Create French (fr) to English (en) translation function
def french_english(french_text):
    '''Function translates french text to english'''
    #Invoke the traslate method from the instance (lng_lt)
    french_to_english = lng_lt.translate(\
    text=french_text, model_id='fr-en')
    #See the translated result
    result = french_to_english.get_result()
    #The 'result' is in the 'Dictionary' format, so need to extract the full string / message
    english_text = result["translations"][0]["translation"]
    #return the final text message stored in 'englishText'
    return english_text

# Suchit's Code ends
