!pip install pyshorteners
#importing Package
import pyshorteners
#requesting url
url = input('Enter the url that has to be Shortened: ')
#defing the Function()
def shortenurl(url):     
    l = pyshorteners.Shortener()
    print("shortenurl:- ",l.tinyurl.short(url))  
#printing url
print(" ")
#call() function
shortenurl(url) 
#url Shorten
a = input( )
print("Your URL has benn Sucessfully Shortened")
# A CODE BY LIKITH SAI--
