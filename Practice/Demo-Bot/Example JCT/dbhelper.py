import sqlite3
import requests
import json
from google.cloud import translate

#format: translate word/ to language
import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def Speechtotext(speech_file):
# Instantiates a client
    client = speech.SpeechClient()

# The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(speech_file),
        'resources',
        'audio.raw')

# Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')

# Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        audio=str('Transcript: {}'.format(result.alternatives[0].transcript))
    return audio

def send_message(text, chat_id):
     url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
     get_url(url)

def definelanguage(input):
    respuesta = input
    if "german" in input.lower():
        respuesta=["de","german"]
    elif "english" in  input.lower():
        respuesta=["en","english"]
    elif "spanish" in input.lower():
        respuesta=["es","spanish"]
    elif "chinese" in input.lower():
        respuesta=["zh-CN","chinese"]
    elif "russian" in input.lower():
        respuesta=["ru","russian"]
    elif "korean" in input.lower():
        respuesta=["ko","korean"]
    elif "japanese" in input.lower():
        respuesta=["ja","japanese"]
    elif "italian" in input.lower():
        respuesta=["it","italian"]
    return respuesta

def traductor(usertext):
 # Instantiates aient
    translate_client = translate.Client()
    text = str(findword(usertext)[0])
# The target language
    target = str(findword(usertext)[1])
# Translates some text into 'target' language
    translation = translate_client.translate(text,target_language=target)
    traduccion=str(u'Text: {}'.format(text))+"\n"+str(u'Translation to ')+str(findword(usertext)[2])+' : {}'.format(translation['translatedText'])
    return traduccion

def findword(allthetext):
    keyword = "translate"
    keyword2 = "to"
    all_text = str(allthetext).lower()
    finaltext=all_text
    language="english"
    languagekey="en"
    if keyword in all_text:
        newtext=all_text.replace("translate","")
        finaltext=newtext[newtext.find('translate')+1:newtext.find('()')]
        if keyword2 in newtext:
            languagekey= definelanguage(newtext.replace("to",""))[0]
            language=definelanguage(newtext.replace("to",""))[1]
    else: 
        newtext=all_text
    
    result=[finaltext,languagekey,language]
    return result



