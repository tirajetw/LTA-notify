import os
import requests
import time
url = 'https://notify-api.line.me/api/notify'
token = 'n7RoF4WUEykfxveaFdPdI7mXdbLa2jQApby8FlUQZPh'
tokenEE = '7mw8f104EQAeUFdrxVnqKJa8b27vgg2uCexLoBRywVY'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
headers2 = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+tokenEE}

path = r'C:\Users\tirajet_w\Desktop\iMacros\Downloads'
path2 = r'C:\Users\tirajet_w\Desktop\Firefox'
os.chdir(path)

while(1):
	os.chdir(path2)
    #os.system('"C:\Program Files (x86)\Ipswitch\iMacros\iMacros.exe" -macro checkLTA')
	os.system('ff.exe imacros://run/?m="checkLTA.iim"')
	
	os.chdir(path)
	f1 = open('oldTXT.txt', 'r', encoding="utf8")
	f2 = open('currentTXT.txt', 'r', encoding="utf8")
	
	if f1.read() != f2.read():
		msg = 'LTA มีอัพเดท'+' ตรวจสอบได้ที่ "https://lta.eng.cmu.ac.th/259192/student/announcement"'
		r = requests.post(url, headers=headers , data = {'message':msg})
		print(r.text)
		print("Have update!")
		print("Delay for notify.")
		for x in range(60):
			print(x)
			time.sleep(1)
		r = requests.post(url, headers=headers2 , data = {'message':msg})
		print(r.text)
		os.chdir(path2)
		os.system('ff.exe imacros://run/?m="updateTXT.iim"')
		print("Updated oldTXT")
		
	else:
		print("No update...")
	for x in range(60):
		print(x)
		time.sleep(1)

