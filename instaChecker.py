import requests
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

face = """""
  ____          _          _   ____        
 / ___|___   __| | ___  __| | | __ ) _   _ 
| |   / _ \ / _` |/ _ \/ _` | |  _ \| | | |
| |__| (_) | (_| |  __/ (_| | | |_) | |_| |
 \____\___/ \__,_|\___|\__,_| |____/ \__, |
                                     |___/ 
 ____                       _              _   _____ 
|  _ \ _ __ ___   __ _ _ __| | ____      _| |_|___ / 
| | | | '_ ` _ \ / _` | '__| |/ /\ \ /\ / / __| |_ \ 
| |_| | | | | | | (_| | |  |   <  \ V  V /| |_ ___) |
|____/|_| |_| |_|\__,_|_|  |_|\_\  \_/\_/  \__|____/ 
                                                     

	"""
print(bcolors.HEADER + face)
payload = "https://insta-node.herokuapp.com/_validate_username?username="
w = raw_input(bcolors.OKBLUE+ ('Enter UserList: '))
wordlist = open(w, "r")

for awa in wordlist:
    check = requests.get(payload+awa)

    prof = check.content

    if "true" in prof:

        print(bcolors.OKGREEN + "Avilavle ----> "+awa)

    elif "false" in prof:

        print(bcolors.FAIL + "Taken -----> "+awa)




