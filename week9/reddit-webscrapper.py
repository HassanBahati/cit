from tkinter import *
import tkinter as tk
import time
import threading
from tkinter.filedialog import askopenfilename
import praw
import datetime
root = tk.Tk()
def app():
    global te
    te = text_entry.get()
    if te == "":
        app()
    run(te)
def run(subreddit):
    # Authentication
    reddit = praw.Reddit(
        client_id="",
        client_secret="",
        user_agent="Paul Sun",
    )
    print(reddit.read_only)
    import time
    local_time = time.localtime()
    hr = local_time.tm_hour
    min = local_time.tm_min
    sec = local_time.tm_sec
    #DATE AND MODEL COLUMN
    global current_time
    current_time = f"{hr}-{min}-{sec}"
    data = open(f'./{subreddit}_{current_time}.csv', 'a', encoding="utf-8")
    print(data.encoding)
    data.write("topic, description, comments, link, date" + "\n")
    from praw.models import MoreComments
    #links = []
    for submissions in reddit.subreddit(subreddit).new(limit=2):
        # if submissions.selftext returns blank, probably crossposted!
        time = submissions.created
        date = datetime.datetime.fromttimestamp(time)
        postlink="https://www.reddit.com/"+submissions.permalink
        #links.append(postlink)
        desc = submissions.selftext.replace(",", "")
        desc = desc.replace("\n", " ")
        print(desc)
        title = submissions.title.replace(",", "")
        if desc == "":
            desc = submissions.url# LINK POSTS SHOULD RESULT IN URL
        #data.write("\n")
        comment_list =  []
        x = ""
        #output_textbox.insert(INSERT, f'TITLE {title}, {desc}')
        for comment in submissions.comments.list():
            #output_textbox.insert(INSERT, f'{comment.body}' + "\n")
            comment.body = comment.body.replace(",", "")
            #comment_list.append(comment.body)
            x += f' [next comment] {comment.body}'
            print(comment.body)
        comment_list.append(x)
        data.write(f'{title}, {desc}, {comment_list}, {postlink}, {date}')
        #print(f'{title}, {desc}, {comment_list}')
        data.write("\n")
        #print("------------------------------------")
import pandas as pd
def csv_to_excel():
    fn = askopenfilename()
    csv = pd.read_csv(fn)
    csv.to_excel("./data.xlsx")
text_entry = tk.Entry(width=100)
text_entry.pack()
download_button = tk.Button(text="download text", command=app)
download_button.pack()
download_button = tk.Button(text="to excel", command=csv_to_excel)
download_button.pack()
output_textbox = tk.Text()
output_textbox.pack()
root.mainloop()