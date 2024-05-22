import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date, datetime
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv('API_KEY')
position = [300, 430, 560, 690, 830]

ind = ["Kolkata", "Delhi", "Srinagar", "Kochi", "Pune"]
africa = ["Cape Town","Marrakesh", "Cairo","Lagos", "Johannesburg"]
uk = ["London", "Manchester", "Leeds", "Edinburgh", "Glasgow"]

country_list = [uk, africa, ind]
name = ['United_kingdom', 'Africa', 'India']

c = 0

for country in country_list:

    img =  Image.open("post.png")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Inter.ttf", size=50)
    content = "Current Weather Info"
    color = 'rgb(255,255,255)'
    (x,y) = (59,55)
    draw.text((x,y), content, color, font=font)

    font = ImageFont.truetype("Inter.ttf", size=30)
    content = date.today().strftime("%A - %B %d, %Y")
    color = 'rgb(255,255,255)'
    (x,y) = (70, 145)
    draw.text((x,y), content, color, font=font)
    
    font = ImageFont.truetype("Inter.ttf", size=30)
    content = datetime.now().strftime("%H:%M:%S")
    color = 'rgb(255,255,255)'
    (x,y) = (850, 145)
    draw.text((x,y), content, color, font=font)
    
    
    index = 0
    for city in country:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api)
        response = requests.get(url)
        data = json.loads(response.text)
        # print(data)
            
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = city
        color = 'rgb(0,0,0)'
        (x,y) = (140,position[index])
        draw.text((x,y), content, color, font=font)

        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(255,255,255)'
        (x,y) = (600, position[index])
        draw.text((x,y), content, color, font=font)

        font = ImageFont.truetype("Inter.ttf", size=50)
        content =str(data['main']['humidity']) + "%"
        color = 'rgb(255,255,255)'
        (x,y) = (800, position[index])
        draw.text((x,y), content, color, font=font)
        
        index += 1
        


    img.show()
    # img_pdf = img.convert('RGB')
    # name = name[c]
    img.save("{}.png".format(name[c]))
    c +=1
