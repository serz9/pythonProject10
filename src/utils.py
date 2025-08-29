import os.path
import json
from selenium import webdriver
from dotenv import load_dotenv
import pyaudio
import speech_recognition as sr

#r=sr.Recognizer()
#with sr.Microphone() as mc:
   # audio=r.listen(mc)
   # text=r.recognize_google(audio,language='ru-RU')

#print(text)
import pyttsx3
load_dotenv()
#cr=webdriver.Chrome()
#cr.get('https://ananas-72.ru')
y=os.path.join(os.getcwd(),'data','operations.json')
a=''

with open('C:\\Users\\serzh\\PycharmProjects\\pythonProject10\\operations',encoding='utf-8') as file:
     for i in file:
         a=a+i

audio=pyttsx3.init()
audio.say(a)
audio.runAndWait()




aa=os.path.abspath(__file__)
print(aa)
#bb=os.listdir(r'C:\\Users\\serzh\\PycharmProjects\\pythonProject10\\date\\operations.json')
##cc=os.listdir(r'C:\\Users\\serzh\\PycharmProjects\\pythonProject10\\src\\utils.py')
dt=os.getcwd()
#print(cc)
print(dt)
def jsn_date(path_)  :
    date_path = path_
    data=[]
    try:
        if not os.path.isfile(date_path):
            print(data)
            return data
        else:
            with open(date_path,'r',encoding='utf-8') as file:
                data_=json.load(file)
                print(data_)

            if isinstance(data_,list):
                print('данные являются списком')
                if all(isinstance(item, dict) for item in data_):
                    print('файл является списком словарей ')
                else:
                    return data
            if len(data_)==0:
                print(data)
                return(data)

            return data_
    except Exception as e :
        print(f'ошибка {e}')





jsn_date('C:/Users/serzh/PycharmProjects/pythonProject10/date/operations.json')