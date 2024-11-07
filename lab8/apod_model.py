import requests 


class ApodModel:
    
    NASA_API_URL = "https://api.nasa.gov/planetary/apod"
    
    def __init__(self, api_key = "KAHHF1p9oZSJMvh7uEyHqUOZetDJh0x2QY6yfT5E" ):
        self.api_key = api_key
        
        
    def get_apod(self, date = None):
        
        param = {"api_key": self.api_key, "date": date}
        
        response = requests.get(self.NASA_API_URL, params = param)
        
        if response:
            return response.json()
        else:
            return ("Error Code: {response.status_code}")
        
        
        