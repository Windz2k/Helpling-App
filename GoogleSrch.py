# Packages Required
from tkinter import *
import requests, webbrowser, pyperclip, re
from bs4 import BeautifulSoup as Soup
import sys
from PIL import ImageTk, Image
import tkinter



def createAString(lst):
    toReturn = ""
    for i in range(len(lst)): 
        if i == len(lst) - 1:
            toReturn += lst[i]
        else:
            toReturn += lst[i]+"+"
    return toReturn

# An example of a google search of red apples is https://www.google.com/search?q=red+apples 
# There must be a + between each word to be able to search with google
def createAString1(format):
    format = format.split(" ")
    return createAString(format)



# Handles The Search 
def search_param():
    global search_bar
    
    lsts_of_websites=[]
    
    # Gets The String Entered in The Search Bar
    url_to_change = search_bar.get()
    url = createAString1(url_to_change)
    
    # Produces a Request
    response = requests.get("https://www.google.com/search?q=" + str(url), headers=headers)
    response.raise_for_status()


    searchBlockSoup = Soup(response.text,"html.parser")
    linkElems = searchBlockSoup.find_all(class_="g")
    
    for i in range(5):
        try:    

            website = url_extra2.search(str(linkElems[i].find_all(class_="r"))).group()
            print(website, end="\n")
            print(end="\n\n")
            
            website2 = str(website)
            
            if (website2.find("https://")==-1): 
                lsts_of_websites.append("https://" + website2)
                
            else :
                lsts_of_websites.append(website2)
                
        except:
            print("Error" + str(i) , end="\n")
    open_webrowser(lsts_of_websites)
    
    # Deletes The Search Bar
    search_bar.destroy()
    
    # Recreates The Search Bar
    search_bar = Entry(root, text="Enter what you wish to search")
    search_bar.grid(row=0,column=0)
    
# Opens The First Three Most Recommended Websites    
def open_webrowser(lst):
    for i in range(3):
        webbrowser.open(lst[i])


# The Tkinter Root Which Essentially is the Structure/Host For The App
root = Tk("Google Search")
root.title("Searching Made Easy")

# Widgets Inside The Root
search_bar = Entry(root, text="Enter what you wish to search")
search = Button(root, text="SEARCH", command=search_param,padx=60)
img =ImageTk.PhotoImage(Image.open("172635-logo#14_duster7_20fps-4fbad9-medium-1435890431.jpeg"))
label = Label(root, image=img)

# Regular Expression (re) to match website links such as https://bbc.co.uk/news/
url_extra2 = re.compile(r"(https://)?\w+(\-|\.)?\w+\.(com|co\.uk|org|net)/(([A-Za-z0-9](-|/)?){0,})?")

# Search My User Agent and replace it with the information "Mozilla....."
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

# The Way In Which The Widgets Are Placed Inside The Root
label.grid(row=1, column=0, columnspan=2)
search_bar.grid(row=0,column=0)
search.grid(row=0, column=1)

# Allows The App To Remain Open and Closes on the Close Button
root.mainloop()
