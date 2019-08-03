from flask import Flask, render_template, request, redirect
import urllib.request
import json
import ssl

app = Flask(__name__)


@app.route("/")
def default_apod():
    api_key = 'DEMO_KEY'
    url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key

    gcontext = ssl.SSLContext()

    apodurlobj = urllib.request.urlopen(url, context=gcontext)

    apodread = apodurlobj.read()

    data = json.loads(apodread.decode("utf-8"))

    return render_template(data['media_type'] + '.html', name=data['title'], media=data['url'], date = data['date'])


@app.route("/<date>/media")
def apod(date):
    api_key = 'DEMO_KEY'
    url = "https://api.nasa.gov/planetary/apod?date=" + date + "&api_key=" + api_key

    gcontext = ssl.SSLContext()

    apodurlobj = urllib.request.urlopen(url, context=gcontext)

    apodread = apodurlobj.read()

    data = json.loads(apodread.decode("utf-8"))

    return render_template(data['media_type']+'.html', name = data['title'], media = data['url'], date = data['date'])


@app.route('/<date>')
def info(date):
    api_key = 'DEMO_KEY'
    url = "https://api.nasa.gov/planetary/apod?date=" + date + "&api_key=" + api_key

    gcontext = ssl.SSLContext()

    apodurlobj = urllib.request.urlopen(url, context=gcontext)

    apodread = apodurlobj.read()

    data = json.loads(apodread.decode("utf-8"))

    return data


@app.route("/changeDate", methods=["GET", "POST"])
def changeDate():
    req = request.form
    return redirect(req['date'] + "/media")

if __name__ == "__main__":
    app.run(debug=False)