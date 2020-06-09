from flask import Flask,render_template, request, jsonify, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'BRUH'])
def index():
    if request.method == "GET":
        
        return render_template('index.html', title="Cheers Mate! 🍻")
    else:
        return redirect("https://www.youtube.com/watch?v=2ZIpFytCSVc")
