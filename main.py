# importing libraries
import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

# adding TLS security
server.starttls()
email = 'your email'
password = 'you app password'
server.login(email, password)

# generate OTP using random.randint() function
otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
msg = 'Hello, Your OTP is '+str(otp)

# email id of sender
sender = 'sender`s email'

# email of receiver
receiver = 'receiver`s email'

# sending otp
server.sendmail(sender, receiver, msg)
server.quit()

# verification of otp
user_otp = str(input("Enter your OTP: "))
if otp == user_otp:
    print("OTP Verified!")
else:
    print("Sorry! Please Enter Valid OTP")