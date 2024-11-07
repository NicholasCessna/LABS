# Controller logic with connections to the html templates for the home and history pages
# and the apod_model script for api(database) retrieval
# A link to the "History" page is ate the bottom of the landing page marked by "View Past Images"
# I also added a "Click Here" that links to the photos URL and displays it a bit larger via the website.

from flask import Flask, render_template, request
from apod_model import ApodModel
from datetime import datetime


app = Flask(__name__)
apod_model = ApodModel()

@app.route("/")
def home():
    apod_data = apod_model.get_apod()
    if "error" in apod_data:
        return apod_data("error")
    
    home_layout = render_template("home.html",
                                  date = apod_data.get("date"),
                                  title = apod_data.get("title"),
                                  image_url = apod_data.get("url"), 
                                  description = apod_data.get("explanation"), 
                                  copyright = apod_data.get("copyright"))
    
    return home_layout

@app.route("/history", methods=["GET"])
def history():
    date = request.args.get("date")
    today_date = datetime.today().strftime('%Y-%m-%d')  
    error_message = None  
    
    apod_data = None
    if date:
        apod_data = apod_model.get_apod(date)

        if "error" in apod_data:
            error_message = apod_data["error"]
            apod_data = {"title": "", "url": "", "explanation": "", "copyright": ""}
    else:
        apod_data = {"title": "", "url": "", "explanation": "", "copyright": ""}
    
    history_layout = render_template("history.html", 
                           selected_date=date,
                           title=apod_data.get("title"),
                           image_url=apod_data.get("url"),
                           description=apod_data.get("explanation"),
                           copyright=apod_data.get("copyright"),
                           today_date=today_date,  # Pass today's date to the template
                           error_message=error_message)

    return history_layout

if __name__ == "__main__":
    app.run(debug = True)