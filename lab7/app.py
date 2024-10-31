# HTML file in templaes/view.html
# Requirements.txt shows the packages I used but it also includes the dependecies of the packages. 
# I used Flask and Segno PIP install.

from flask import Flask, render_template, request
import segno
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def control():
    if request.method == "POST":
        data = request.form["data"]
        # I added  micro = False to my segno variable because when I only generated using a single word the QR would come out as a micro QR. 
        # My phone wouldnt recognize the micro QR. From the documentation I read, segno automatically does this. 
        qr = segno.make(data, micro = False) 
        buffer = io.BytesIO()
        qr.save(buffer, kind='svg', scale=5, dark='darkblue', nl=False)
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return render_template("view.html", data=data, img_str=img_str)
    
    return render_template("view.html", data=None, img_str=None)

if __name__ == "__main__":
    app.run(debug=True)
