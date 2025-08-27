
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    df = pd.read_csv('aqx_p_250.csv')
    latest = df.loc[0, 'monitordate']
    x = []
    y = []
    for i in range(len(df)):
        row = df.loc[i]
        if row['monitordate'] == latest:
            x.append(f"{row['itemengname']}({row['itemunit']})")
            y.append(row['concentration'])
    df = pd.read_html('https://zh.wikipedia.org/zh-tw/Wikipedia:%E7%BB%9F%E8%AE%A1')
    print(df)
    return render_template('index.html', x=x, y=y)

app.run('localhost', debug=True)