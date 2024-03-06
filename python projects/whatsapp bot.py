import pywhatkit
try:
    pywhatkit.sendwhatmsg("+91xxxxxxxxxx","xyz",8,00)
    print("Successfully Sent!")
except:
    print("An Unexpected Error!")