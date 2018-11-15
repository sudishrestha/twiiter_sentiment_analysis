from Tkinter import *
import time
import io
import re
import os
import subprocess

countP = 0
countN = 0
countS = 0
root=Tk()
root.minsize(800,700)
root.title('Sentiment Checker')

sentence="Enter the keyword to search  "
sentence=sentence.upper()
labelSentence=Label(root,text=sentence)
labelSentence.pack(side=TOP, padx=10,pady=5)
words=sentence.split(" ")
lengthOfArray=len(words)
textbox1=Text(root,width=10, height=1)
textbox1.pack(side=TOP, padx=10,pady=10)
textbox1.focus_set()
label=Label(root,text='Enter time in seconds:')
label.pack(side=TOP, padx=10,pady=5)

textbox=Text(root,width=10, height=1)
textbox.pack(side=TOP, padx=10,pady=10)

countP = 0
countN = 0
countS = 0
def onSearch():
    keyword=textbox.get("1.0",END)
    keyword1=textbox1.get("1.0",'end-1c')
    k = int(keyword)
    proc1 = subprocess.Popen("python test.py", shell=True)
    time.sleep(k)
    proc1.kill()
    display= " DATA EXTRACTION COMPLETED!!!"
    subprocess.Popen("python helper.py", shell=True)
    displayLabel.config(text=display)
    os.chdir(r'C:\Users\sudishrestha\Desktop\september 8')
    #time.sleep(int(keyword));
    fname = io.open('streamser.txt', encoding ='latin2')
    countP = 0
    countN = 0
    countS = 0
    for line in fname:
        if "Sentiment" in line:
            print "*********************"
            b =line[11:]
            print b[:-2]
            if b[:-2] == "negative":
                countN = countN+1;
            if b[:-2] == "positive":
                countP = countP+1;
            if b[:-2] == "neutral":
                countS = countS+1;
            print "*********************"
        elif "text" in line:
            a =line[15:]
            print "Keyword :" + a[:-2]
            
        elif "relevance" in line:
            c = line[20:]
            print "relevance = " + c[:-4]
    print "Negative count "
    print countN
    print "Positive count "
    print countP
    print "Neutral count "
    print countS
    from subprocess import call
    #call("notepad streams.txt")
    #displayLabel1.config(text="Negative Count =" + str(countN))  
searchButton=Button(root,text='Search',width=10,command=onSearch).pack()
displayLabel=Label(root,text="")
displayLabel.pack()


root.mainloop()
