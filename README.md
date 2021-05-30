# emojo_chatbot
A Visual Chatbot which responds with Voice and Emotions using Raspberry Pi

# Inspiration and Problem
Nearly 1 out of 5 people are suffering from some kind of Mental Health Issues, these numbers have drastically increased since the start of pandemic. According to researchers watching a movie/series helps for Mental Health. It has huge impact on our brain function, social connections, productivity and creativity. And having your close people near  you to understand your problems you is difficult during this pandemic.

To solve this issue we have created a Visual Chatbot which responds with Voice and Emotions. This chatbot will help Users as a Virtual Friend which will chat with him/her and also show his emotions with help of Emojis.  Currently there is no such device which helps user in this way. To have a similar language as Movie/Series we have used dialouges from F.R.I.E.N.D.S TV Series for our Chatbot ,which will help user for more easy and amusing conversation. Also with this we have also analysed Emotions from Text and displayed respective emojis on Screen for better visual conversation. Along with this we have added Voice Recognition for Chatbot , so user can Speak and Hear the Chatbot instead of tradition method of reading or writing chat.

# Technology Stack
* We have used Raspberry Pi and TFT Display to make the project.
* For Chatbot we have used Python, NLTK and for Dataset we have used F.R.I.E.N.D.S Corpus which contained all dialouges.
* For Emotions we scraped Emoji Images from Google Search and the emojis were predicted using Text Classification Model.
* For the TFT Display we have use Adafruit_ILI9341 Library to create the GUI.
* For Voice Recognition , we used Bluetooth Headset to take the Input Voice from User and use Google Cloud Speech API of speech_recognition package for Speech to Text.
* And for Text to Speech  from Chatbot we used pyttsx package.

# Connections
For Display ( 2.8" TFT Display ILI9341)
1. Raspberry Pi 3.3V power to TFT Vin.
2. Raspberry Pi ground to TFT GND.
3. Raspberry Pi SCLK to TFT CLK.
4. Raspberry Pi MOSI to TFT MOSI.
5. Raspberry Pi CE0 to TFT CS.
6. Raspberry Pi GPIO 18 to TFT D/C.
7. Raspberry Pi GPIO 23 to TFT RST.

And for Bluetooth Connection:
* Connect the device : `bluetoothctl connect 9F:3A:66:06:7C:EA` the id is id of your headset , you can find it when scanning on your phone.

For Speaker:
* Connect the Aux Cable Directly to Raspberry Pi 

# To Run the Bot:
1. Install the Adafruit Display Library on RPi:
```
cd ~
git clone https://github.com/adafruit/Adafruit_Python_ILI9341.git
cd Adafruit_Python_ILI9341
sudo python setup.py install
```
2. Install the Python Packages:
```
pip3 install pyttsx Adafruit_GPIO Pillow nltk sklearn speech_recognition
```
3. Make the Connections and Connect the Bluetooth Headset
4. Then Run the Bot
```
git clone https://github.com/aniketdhole07/emojo_chatbot
cd emojo_chatbot
python3 main.py
```
