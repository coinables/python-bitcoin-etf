import urllib.request
import threading
 
def checkETF():
    threading.Timer(90.0, checkETF).start() #set to 90 second refresh rate
    target_url = "https://www.sec.gov/rules/sro/batsbzx.htm"
    data = urllib.request.urlopen(target_url).read(20000) #set to only check first 20000 chars
    eachWord = data.split()
 
    if "Bitcoin" in eachWord:
        print("THERES AN UPDATE ON THE BITCOIN ETF!")
    else:
        print("Nothing")
 
checkETF()
