from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
import chat
import random
import os
import emj_pred
import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

import speech_recognition as sr
r = sr.Recognizer()

import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')

font = ImageFont.truetype("arial.ttf",25)
font_txt = ImageFont.truetype("arial.ttf",18)
# Raspberry Pi configuration.
DC = 24
RST = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Create TFT LCD display class.
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

# Initialize display.
disp.begin()
import os
arr = os.listdir("/home/pi/Desktop/chatbot/emj")
print(arr)
print('Loading image...')

#draw = disp.draw()
def draw_rotated_text(image, text, position, angle, font, fill):
    # Get rendered font width and height.
    draw = ImageDraw.Draw(image)
    width, height = draw.textsize(text, font=font)
    # Create a new image with transparent background to store the text.
    textimage = Image.new('RGBA', (width, height), (255,255,255))
    # Render the text.
    textdraw = ImageDraw.Draw(textimage)
    textdraw.text((0,0), text, font=font, fill=fill)
    # Rotate the text image.
    rotated = textimage.rotate(angle, expand=1)
    # Paste the text into the image, using it as a mask for transparency.
    image.paste(rotated, position, rotated)
def draw_image(buf,img):
    buf.paste(img)

# Write two lines of white text on the buffer, rotated 90 degrees counter clockwise.
emoji_class={"joy":5, 'fear':4, "anger":2, "sadness":4, "disgust":1, "guilt":4,"neutral":2}
disp.clear((255,255,255))
# Load an image
def get_image(emoji_prediction):
    pth=emoji_prediction+str(random.randint(1,emoji_class[emoji_prediction]))+".jpg"
    image = Image.open("emj/"+str(pth))
    image = image.resize((240, 240))
    return image

draw_rotated_text(disp.buffer, 'Emojo Chatbot', (30, 260), 0, font, fill=(0,0,0))
draw_image(disp.buffer,get_image("joy"))
disp.display()
while(True):
        disp.clear((255,255,255))
        ip_user=""

        #Record and store Audio from User via Bluetooth Headset
        os.system("arecord --device=plughw:1,0 --duration=5 temp.wav")

        #Convert stored Audio to Text Voice Recognition
        with sr.AudioFile('home/pi/temp.wav') as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize using Google Cloud Speech API
            ip_user= r.recognize_google(audio_data)
        chat_response=chat.find(ip_user)
        emoji_prediction=emj_pred.predict_emoji(chat_response)

        draw_rotated_text(disp.buffer, chat_response, (10, 250), 0, font_txt, fill=(0,0,0))
        draw_image(disp.buffer,get_image(emoji_prediction))
        disp.display()
        
        #Play Sound Text to Speech
        engine.setProperty('rate', 100)
        engine.say(chat_response)
        engine.runAndWait()
        time.sleep(1)
