'''File to enter your local environment variables'''

accSID = input("Copy & Paste your Account SID:\t")
accAuthToken = input("Copy & Paste Your Account Auth Token:\t")
pNum = input("Enter Your Phone Num registered with Twilio!:(+91...)\t")
vNum = input("Enter Your Test Number provided by Twilio!:\t")
if accSID and accAuthToken:
    with open('twilio.env' , 'w+') as fh:
        fh.write("export TWILIO_ACCOUNT_SID='{0}'\n".format(accSID))
        fh.write("export TWILIO_AUTH_TOKEN='{0}'\n".format(accAuthToken))
        fh.write("export  VNUM='{0}'\n".format(vNum))
        fh.write("export PNUM='{0}'\n".format(pNum))
        


    print("Env file updated. Please run source ```./twilio.env``` command in your shell")
else:
    print("Something is Wrong!!!")
