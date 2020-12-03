import requests
import time
import hashlib
import sys

t1=3

user=sys.argv[1]
passw=sys.argv[2]

def hashb(first):
  h = hashlib.sha256()
  h.update(
        str(first).encode('utf-8') 
        )
  return h.hexdigest()
  	#first=""
	#print ("HASHPY",hashb(first))

def Postsubmit5000():
	#print ("u/p:",user,passw)
	in_values = {'author':user,'content':passw}
	req = requests.post('http://127.0.0.1:5000/submit',data = in_values)
	print("1.[BS1] ------> [DRONE] : |SUBMIT REPLY|",req.text[1090:1123],"|\n")

def Mine5000():
	req = requests.get('http://127.0.0.1:5000/minem')
	print("2.[BS1] ------> [DRONE] : |MINE REPLY",req.text,"|\n")

def Getchain8000():
	req = requests.get('http://127.0.0.1:8000/chain')
	lenght =len(req.text)
	print("3.[MGS] ------> [DRONE] : |READ_CHAIN_TOTAL CHAIN LENGHT    :",lenght,"|")
	print("3.[MGS] ------> [DRONE] : |READ_CHAIN_GET_BLOCK_HASH:     ",req.text[-81:-17],"|\n")
	second=req.text[-81:-17]
	return second

def Getchain5000():
	req = requests.get('http://127.0.0.1:5000/getm')
	lenght =len(req.text)
	print("4.[BS1] ------> [DRONE] : |READ_CHAIN_BS1_TOTAL CHAIN LENGHT:",lenght,"|")
	print("4.[BS1] ------> [DRONE] : |READ_CHAIN_BS1_GET_BLOCK_HASH: ",req.text[-81:-17],"|\n")
	first=req.text[-81:-17]
	return first

def GetHashchain5000():
	req = requests.get('http://127.0.0.1:5000/hashgetm')
	print("6.[BS1] ------> [DRONE] : |MPUSH_GETCHAIN_OTP_HASH_REPLY",req.text,"|\n")
	#print("GEThashchain5000 VALUE :",req.text)
	return req.text
def Unblock5000():
	req = requests.get('http://127.0.0.1:5000/unblock')
	print ("8.[BS1] ------> [DRONE] : |UNBLOCK_CHANNEL_2_REPLY:[ACK]|",req.text,"|\n")

def pPostsubmit5000():
	#print ("u/p:",user,passw)
	in_values = {'author':user,'content':passw}
	req = requests.post('http://127.0.0.1:5000/submit',data = in_values)
	print("9.[BS1] ------> [DRONE] : |HO_REGISTRATION_REPLY|",req.text[1090:1123],"|")

def pMine5000():
	req = requests.get('http://127.0.0.1:5000/minem')
	print("9.[BS1] ------> [DRONE] : |ACK_MINE REPLY",req.text,"|\n")	

def nPostsubmit5000():
	#print ("u/p:",user,passw)
	in_values = {'author':user,'content':passw}
	req = requests.post('http://127.0.0.1:5000/submit',data = in_values)
	print("9.[BS1] ------> [DRONE] : |NACK_REPLY|",req.text[1090:1123],"|")

def nMine5000():
	req = requests.get('http://127.0.0.1:5000/minem')
	print("9.[BS1] ------> [DRONE] : |NACK_MINE REPLY",req.text,"|\n")
	

#Main()
print ("\n0.[DRONE] : Start process....")
print ("0.[DRONE] |USER/PASS|:",user,"/",passw,"\n")
time.sleep (t1)
print ("1.[DRONE] ------> [BS1] :|POST|BS1_ADDRESS|PORT:5000|SUBMIT_USER/PASS|")
time.sleep (t1)
Postsubmit5000()
print ("2.[DRONE] ------> [BS1] :|GET |BS1_ADDRESS|PORT:5000|MINE_REQUEST    |")
time.sleep (t1)
Mine5000()
print ("3.[DRONE] ------> [MGS] :|GET |MGS_ADDRESS|PORT:8000|READ_CHAIN      |")
time.sleep (t1)
a=Getchain8000()
print ("4.[DRONE] ------> [BS1] :|GET |BS1_ADDRESS|PORT:5000|READ_CHAIN_BS1  |")
time.sleep (t1)
b=Getchain5000()
if a == b:
		print ("5.[DRONE] ------> [DRONE] [MSS-BS1]BLOCK_VERIFICATION[PASSED]\n|",a,"=",b,"|\n")
		time.sleep (t1)
a1=hashb(a)
b1=hashb(b)

time.sleep (t1)
print ("6.[DRONE] ------> [BS1] :|GET |BS1_ADDRESS|PORT:5000|PUSH_GETCHAIN_OTP_HASH\n")
input ("[FOR DEMO PURPOSES] PRESS ENTER TO CONTINUE...\n")
time.sleep (t1)
c=GetHashchain5000()
#print ("VERIFICATION HASH3", c)
if a1 == c:
		print ("7.[DRONE] ------> [DRONE] [BS1/DRONE] HASH2_OTP_VERIFICATION[PASSED]\n|",a1,"=",c,"|\n")
		time.sleep (t1)
		print ("8.DRONE] ------> [BS1] :|GET |BS1_ADDRESS|PORT:5000|UNBLOCK_CHANNEL_2|")
		time.sleep (t1)
		Unblock5000()
		user='HANDOVER[OK]'
		passw='DRONE1'
		print ("9.[DRONE] ------> [BS1] :|POST|BS1_ADDRESS|PORT:5000|HO_INFO_REQ|")
		pPostsubmit5000()
		time.sleep (t1)
		print ("9.[DRONE] ------> [BS1] :|POST|BS1_ADDRESS|PORT:5000|HO_BCHREGISTER_REQ|")
		pMine5000()
else :
	print ("[DRONE] WARNING! HASH2_OTP_VERIFICATION[FAILED] \n")
	
	print ("7.[DRONE] ------> [DRONE] [BS1/DRONE] HASH2_OTP_VERIFICATION[FAILED]\n",a1,"=",c,"|\n")
	user='HANDOVER[FAILED]'
	passw='BS1_REJECTED'
	time.sleep (t1)
	print ("9.[DRONE-FAILED] ------> [BS1] :|POST|BS1_ADDRESS|PORT:5000|HO_FAIL_INFO_REQ|")
	nPostsubmit5000()
	time.sleep (t1)
	print ("9.[DRONE-FAILED] ------> [BS1] :|POST|BS1_ADDRESS|PORT:5000|HO_FAIL_BCHREGISTER_REQ|")
	nMine5000()
	time.sleep (t1)
print ("10.[DRONE] :********************** Handover Process complete*******************8\n\n")


