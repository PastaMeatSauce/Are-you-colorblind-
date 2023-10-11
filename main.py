from flask import Flask, render_template, redirect, request, url_for
from PIL import Image
import os

def fixImages():
  for filename in os.listdir("static"):
    im1 = Image.open("static/" + filename)
    newsize = (700,700)
    im1 = im1.resize(newsize)
    im1.save("static/" + filename[:len(filename)-4]+".png")


#fixImages()
app = Flask(__name__)
#return redirect("http://www.example.com", code=302)
testDict = {
  "1" : 7,
  "2" : 2,
  "3" : 15,
  "4" : 1,
  "5" : 2,
  "6" : 45,
  "7" : 4,
  "8" : 6,
  "9" : 6,
}


  
@app.route('/')
def func1():
    return render_template("choice.html")
@app.route('/trackswitch', methods = ["GET", "POST"])
def redir():
	if request.method == "POST":
		a = request.form['answer']
	if a == "Color":
		return redirect('https://visually-impaired-coding-with-frends.darrenfarnswort.repl.co/test/test1/0')
	if a == "Amsler":
		return redirect('https://visually-impaired-coding-with-frends.darrenfarnswort.repl.co/amslerTest')

@app.route('/amslerTest')
def amsler():
	return render_template("amsler.html")


@app.route('/test/checkAns', methods = ["GET", "POST"])
def checkAns():
  global total
  if request.method == 'POST':
    num = request.form['number']
    testNum = request.form['testNum']
    total = request.form['total']
  total = int(total)
  if testDict[testNum] == int(num):
    total += 1
  testNum = int(testNum) + 1
  if testNum <= 9:
    return redirect('https://visually-impaired-coding-with-frends.darrenfarnswort.repl.co/test/test'+str(testNum)+"/"+ str(total) )
  else:
    return redirect('https://visually-impaired-coding-with-frends.darrenfarnswort.repl.co/test/results')


@app.route('/test/<name>/<total>', methods = ["GET", "POST"])
def test(name, total):
  file = url_for('static', filename=f'{name}.png')
  return render_template("index.html", user_image = file, number = name[4:], tot = total)


 
@app.route('/test/results')
def results():
  global total
  return render_template("result.html", total = total, outof = len(testDict))


app.run(host='0.0.0.0', port=81, debug = True)

