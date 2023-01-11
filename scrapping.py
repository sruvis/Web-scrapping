from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = "https://www.google.com/"
link = "https://www.google.com/search?q=AI+assisted+offside+decisions+in+FIFA+world+cup&source=lnms&tbm=nws&sa=X&ved=2ahUKEwj6pbSl9L_8AhUJacAKHZxTBhwQ_AUoAXoECAEQAw&biw=1920&bih=1001&dpr=2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def news(link):
    req = Request(link, headers=headers)
    webpage = urlopen(req).read()
    with requests.Session() as c:
        soup = BeautifulSoup(webpage,'html.parser')
        #print(soup)
        for item in soup.find_all('div',attrs={"class":"Gx5Zad fP1Qef xpd EtOod pkphOe"}):
            raw_link = (item.find('a', href=True)["href"])
            news_link = (raw_link.split("/url?esrc=s&q=&rct=j&sa=U&url=")[1]).split("&ved=2")[0]
            title =(item.find('div', attrs={"class":"BNeawe vvjwJb AP7Wnd UwRFLe"}).get_text())
            title = title.replace(","," ")
            news_summary = (item.find('div', attrs={"class":"BNeawe s3v9rd AP7Wnd"}).get_text().split())
            news_summary = " ".join(news_summary[:-3])
            news_summary = news_summary.replace(","," ")
            news_source = (item.find('div', attrs={"class":"BNeawe UPmit AP7Wnd lRVwie"}).get_text())
            news_source = news_source.replace(","," ")
            print(title)
            print(news_summary)
            print(news_link)
            print(news_source)        
            print("")
            doc = open("data_01092022_08012023.csv","a")
            doc.write("{},{},{},{} \n".format(title, news_summary, news_link, news_source))
            doc.close()
        next = soup.find('a', attrs={"aria-label" : "Next page"})
        next = (next['href'])
        link = root + next
        news(link)
news(link)    