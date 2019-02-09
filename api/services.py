#6524096937

from bs4 import BeautifulSoup
import requests

def getTrainDetails(train_no):
    url='https://www.travelkhana.com/travelkhana/utilities/train-stations/' + str(train_no)
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    details = []
    for name in soup.find_all("div",class_="col-md-12 heading-wrap"):
        name.has_attr("h1")
        details.append(name.text.split('Route and Schedule')[0].strip('\n'))
    
    for train_details in soup.find_all("th",class_="station-name"):
        details.append(train_details.text)
    return [details[0],details[1], details[-1]]

def getPnrDetails(pnr):
    url='https://www.railyatri.in/pnr-status/' + str(pnr)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    details = []
    for train_details in soup.find_all("p",class_="pnr-bold-txt"):
        details.append(str(train_details.text).strip())
    return details
