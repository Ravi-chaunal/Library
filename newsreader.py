import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak =Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("News for today.. lets begin")
    ulr ="https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d49e31ffbef1414ea1aa8298d4ef02d8"
    news=requests.get(url).text
    news_dict=json.loads(news)
    arts_dict=news_dict['article']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("moving on the next news ")

    speak("Thanku for listening..")