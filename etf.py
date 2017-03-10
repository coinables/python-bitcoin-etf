#urllib needed to fetch urls and threading needed for timer
import urllib2
import threading

#create a function that starts the timer and checks the page
def checkETF():
    #initiate timer for every 90 seconds
    threading.Timer(90.0, checkETF).start()
    #define the page we want to check
    target_url = "https://www.sec.gov/rules/sro/batsbzx.htm"
    #call urllib to the access the target_url then add the read property to limit how many characters
    data = urllib2.urlopen(target_url).read(20000) #set to only check first 20000 chars
    #take every word and put it into a list
    eachWord = data.split()
    
    #if operation to compare each word in the list to "bitcoin"
    if "Bitcoin" in eachWord:
        print "Found"
    else:
        print "Nothing"
      
#run the function 
checkETF()
