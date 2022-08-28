from ast import main
from mimetypes import init
from multiprocessing.spawn import _main
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="E:\Internship\download.ico",
        timeout=1
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    while True:
        notifyMe("Covid-19", "Let's stop the spread of this virus together")
        myHtmlData=getData("https://prsindia.org/covid-19/cases")
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        result=soup.find_all("tbody")[0].find_all("tr") # result ek list ki tarah hai jisme sarre tr stored hai.
        states=['Uttar Pradesh', 'Bihar', 'Chhattisgarh']
        for row in result:
            temp=row.find_all("td")
            sn=temp[0].get_text()
            state=temp[1].get_text()
            cnf_cases=temp[2].get_text()
            active=temp[3].get_text()
            cured=temp[4].get_text()
            death=temp[5].get_text()
            if(state in states):
                nTitle="Cases of Covid-19"
                nText=f"{sn}.{state}\nConfirmed:{cnf_cases} Active:{active}\nCured:{cured}\nDeaths:{death}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(60)
    
    