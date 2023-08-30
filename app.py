from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Hello")

@app.route("/",methods=['post'])
def qr():
    memory=BytesIO()
    data = request.form.get('gen')
    img = qrcode.make(data)
    img.save(memory)
    memory.seek(0)
    out = base64.b64encode(memory.getvalue()).decode('utf-8')
    imga = f"data:image/png;base64,{out}"

    return render_template("index.html",data=imga)


if __name__ == '__main__':
    app.run(debug=True)
