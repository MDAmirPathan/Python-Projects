import win32com.client
from datetime import datetime as dt
import speech_recognition as sr
import webbrowser as wb
import smtplib
from time import sleep


sender = "nitinmadas24@gmail.com"
password = "indiaisawe#24"
port = 465
server = "smtp.gmail.com"

#server = smtplib.SMTP_SSL(server,port)
#server.login(sender,password)

r = sr.Recognizer()

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def speak(message):
	speaker.Speak(str(message))
	print("Done") 

def wish():
	if 4 < dt.now().hour <12:
		print("Good Morning")
		speak("Good Morning")
	elif 12 <=  dt.now().hour < 16:
		print("Good Afternoon")
		speak("Good Afternoon")
	elif 16 <= dt.now().hour <19:
		print("Good Evening")
		speak("Good Evening")
	else:
		print("Have a great Night")
		speak("Have a great Night")

def microphone_input():
	try:
		with sr.Microphone() as source1:
			
			r.adjust_for_ambient_noise(source1,duration=0.2)
			print("Listening...")
			audio = r.listen(source1)
			mic_input = r.recognize_google(audio)
			print(f'You Said: {mic_input}')
			speak(mic_input)
			command(mic_input)

	except sr.RequestError as err:
		print(f"Error Occured {err}")
	except sr.UnknownValueError as unerr:
		print(f"Error Occured: {unerr}")
	
	return mic_input

def message_input():
	try:
		with sr.Microphone() as source2:
			
			r.adjust_for_ambient_noise(source2,duration=0.2)
			print("Recording message...")
			audio = r.listen(source2)
			message_input = r.recognize_google(audio)
			print(f'Your Message: {message_input}')
			speak(message_input)
			return message_input

	except sr.RequestError as err:
		print(f"Error Occured {err}")
	except sr.UnknownValueError as unerr:
		print(f"Error Occured: {unerr}")


def send_mail(content,sender_name):
	if "nitin" in sender_name:
		server.sendmail(sender , "nitinmadas2016@gmail.com",content)
	elif "navdish" in sender_name:
		server.sendmail(sender , "gangadharinavdish@gmail.com",content)
	else:
		server.sendmail(sender , "nitinmadas2016@gmail.com",content)

def command(cmd):
	if "google" in cmd.lower():
		wb.open("https://www.google.com")
	elif "youtube" in cmd.lower():
		wb.open("https://www.youtube.com")
	elif "mail" in cmd.lower():
		email_content = message_input()
		send_mail(email_content,cmd.lower()) 


if __name__=="__main__":
	wish()
	for i in range(4):
		sleep(5)
		microphone_input()

