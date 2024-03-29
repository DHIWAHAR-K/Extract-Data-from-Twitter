import os
import tweepy as tw
import pandas as pd
from datetime import datetime, timedelta

from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font

wn = tk.Tk()
wn.geometry("500x500")
wn.configure(bg='azure2')
wn.title("Twitter Data Scraper")
searchWord = tk.StringVar()
direc=tk.StringVar(wn)
n=tk.IntVar(wn)

headingFrame1 = tk.Frame(wn,bg="gray91",bd=5)
headingFrame1.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.16)

headingLabel = tk.Label(headingFrame1, text=" Welcome to DataFlair Twitter Data Srcaper", fg='grey19', font=('Courier',12,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


tk.Label(wn, text='Enter the word to be searched on twitter',bg='azure2', font=('Courier',10)).place(x=20,y=150)

tk.Entry(wn, textvariable=searchWord,  width=35,font=('calibre',10,'normal')).place(x=20,y=170)

tk.Label(wn, text='Please enter number of data values you require',bg='azure2', anchor="e").place(x=20, y=200)
tk.Entry(wn,textvariable=n, width=35, font=('calibre',10,'normal')).place(x=20,y=220)

#Getting the path of the folder
tk.Label(wn, text='Please enter the folder location where csv file is to be saved',bg='azure2', anchor="e").place(x=20, y=250)
tk.Entry(wn,textvariable=direc, width=35, font=('calibre',10,'normal')).place(x=20,y=270)

ScrapeBtn = tk.Button(wn, text='Scrape', bg='honeydew2', fg='black', width=15,height=1,command=scrapeData)
ScrapeBtn['font'] = font.Font( size=12)
ScrapeBtn.place(x=15,y=350)

QuitBtn = tk.Button(wn, text='Exit', bg='old lace', fg='black',width=15,height=1, command=wn.destroy)
QuitBtn['font'] = font.Font( size=12)
QuitBtn.place(x=345,y=350)

wn.mainloop()


def scrapeData():
    consumer_key= ''
    consumer_secret= ''
    access_token= ''
    access_token_secret= ''

    path = direc.get()
    search_words = searchWord.get()
    no=n.get()

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
   
    tweets = tw.Cursor(api.search_tweets,
                q=search_words,
                lang="en").items(no)
    users_locs = [[tweet.created_at, tweet.id, tweet.user.screen_name,tweet.text]
            for tweet in tweets]
    twitterDf = pd.DataFrame(data=users_locs,
                        columns=['location', "id","user","Content"])
    path=path+"/TwitterCSV.csv"
    twitterDf.to_csv(path)
    messagebox.showinfo("Twitter Data Scraper","CSV file is saved successfully!")
    
    
unicode_str = u"aaÃ§Ã§Ã§Ã&Ã"
encoded_str = unicode_string.encode('utf-8')
print(encoded_str)