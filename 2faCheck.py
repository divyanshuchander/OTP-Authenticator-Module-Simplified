'''Actual Authenticator'''
import os
from twilio.rest import Client
import datetime as dt
from random import randint as otp

def otpAuth():
    accSID = os.environ['TWILIO_ACCOUNT_SID']
    authToken = os.environ['TWILIO_AUTH_TOKEN']
    pNum = os.environ['P_NUM']
    vNum = os.environ['V_NUM']

    client = Client(accSID, authToken)
    otpGen = otp(1000,9999)
    message = "Hi! OTP requested at {} is = {}".format(dt.datetime.now(),otpGen)

    try:
        message = client.messages \
                    .create(
                        body= message,
                        from_= vNum,
                        to= pNum
                    )
        print("OTP Sent :)")
    except:
        print("OTP Not Sent :\(")

    otpEnter = int(input("Please enter the OTP:\t"))
    if otpEnter == otpGen:
        print("OTP Verified :)")
        return True
    else:
        print("OTP Not Verified :\(")
        return False

if __name__ == "__main__":
    otpAuth()


