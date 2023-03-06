"""
This function translate from french to english
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

def englishToFrench(english_text):
    """
    This function translate from english to french
    """
    model_id = 'en-fr'
    language_translator.set_service_url(url)
    translation = language_translator.translate(text = english_text,model_id = model_id).get_result()
    french_text = json.dumps(translation["translations"][0]["translation"],indent=2,ensure_ascii=False)
    return french_text

def frenchToEnglish(french_text):
    """
    This function translate from french to english
    """
    model_id = 'fr-en'
    language_translator.set_service_url(url)
    translation = language_translator.translate(text = french_text,model_id = model_id).get_result()
    english_text = json.dumps(translation["translations"][0]["translation"],indent=2,ensure_ascii=False)
    return english_text
