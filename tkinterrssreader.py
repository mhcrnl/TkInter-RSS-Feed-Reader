from Tkinter import *
import time
import sys
import feedparser


root = Tk()
root.geometry("600x500")
root.title("Gogogogogoogogo")
myContainer = Frame(root)
myContainer.pack(side=TOP, expand=YES, fill=BOTH)
feeds = []
fullFeeds = []
Title = []
Time = []
Link = []
TimeStamp = []

HLabel1 = Label(myContainer, text = "Title", fg = "blue")
HLabel2 = Label(myContainer, text = "Time", fg = "blue")
HLabel3 = Label(myContainer, text = "Link", fg = "blue")
HLabel4 = Label(myContainer, text = "TimeStamp", fg = "blue")

HLabel1.grid(row=0, column=0)
HLabel2.grid(row=0, column=1)
HLabel3.grid(row=0, column=2)
HLabel4.grid(row=0, column=3)


def main():
    choice = raw_input("Press 1 to refresh RSS feed, 2 to add a new feed or 3 to quit: ")
    if choice == "1":
        showFeed()
        main()
    if choice == "2":
        addNewFeed()
        main()
    if choice == "3":
        sys.exit()
    else:
        "Please enter a valid number."


def addNewFeed():
    newFeed = raw_input("Please enter an RSS feed you'd like added: ")
    feeds.append(newFeed)
    for i in feeds:
        d = feedparser.parse(i)
        for j in range(0, len(d)):
            parsedTime = time.mktime(d.entries[j].published_parsed)
            displayTime = time.strftime("%Y-%m-%d %H:%M:%S", d.entries[j].published_parsed)
            theTuple = (parsedTime, d.entries[j].title, displayTime, d.entries[j].link)
            fullFeeds.append(theTuple)
    sortList()
    showFeed()


def sortList():
    fullFeeds.sort()

def showFeed():
    for i in range(0, len(fullFeeds)):
        myLabel1 = Label(myContainer, text = fullFeeds[i][1])
        Title.append(myLabel1)
        myLabel2 = Label(myContainer, text = fullFeeds[i][2])
        Time.append(myLabel2)
        myLabel3 = Label(myContainer, text = fullFeeds[i][3])
        Link.append(myLabel3)
        myLabel4 = Label(myContainer, text = fullFeeds[i][0])
        TimeStamp.append(myLabel4)
    for i in range(0, len(fullFeeds)):
        Title[i].grid(row=i+1, column=0, sticky=W)
        Time[i].grid(row=i+1, column=1, sticky=W)
        Link[i].grid(row=i+1, column=2, sticky=W)
        TimeStamp[i].grid(row=i+1, column=3, sticky=W)

main()
root.mainloop()
