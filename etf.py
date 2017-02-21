import urllib2
import threading
 
def checkETF():
    threading.Timer(10.0, checkETF).start()
    target_url = "https://www.sec.gov/rules/sro/batsbzx.htm"
    data = urllib2.urlopen(target_url).read(20000) #set to only check first 20000 chars
    eachWord = data.split()
 
    if "Bitcoin" in eachWord:
        print "Found"
    else:
        print "Nothing"
 
checkETF()