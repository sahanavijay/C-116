from flask import Flask,render_template
app=Flask(__name__)
@app.route("/index")
def first_flask():
    return render_template('index.html')
app.run()


