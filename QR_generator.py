import qrcode

print("---------Welcome To Payment Accept App---------")

#Taking UPI_ID From User

USER_Id = input("Enter Your UPI ID : ")

#UPI_ID Payment Formate

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#UPI_ID Payment URL Based ON THE UPI_ID and PAyment Apps
#You Can Modify URL Based On App

phonepe_url = f'upi://pay?pa={USER_Id}&pn=Recipient%20Name'
paytm_url = f'upi://pay?pa={USER_Id}&pn=Recipient%20Name'
google_pay_url = f'upi://pay?pa={USER_Id}&pn=Recipient%20Name'

#create QR_CODE for each app

phonepe_qr_code = qrcode.make(phonepe_url)
paytm_qr_code = qrcode.make(paytm_url)
google_pay_qr_code = qrcode.make(google_pay_url)

print("1: Phonepe")
print("2: Paytm")
print("3: Google Pay")

#Display The QR Code Using pillow library

#geting User's Payment App From User 

Users_Payment_app = int(input("Enter Your Payment App Option : "))

if Users_Payment_app == 1:
    phonepe_qr_code.show()

elif Users_Payment_app == 2:
    paytm_qr_code.show()

elif Users_Payment_app == 3:
    google_pay_qr_code.show()

else:
    print("---------Enter Valid Option---------")


#created by Bhavesh
