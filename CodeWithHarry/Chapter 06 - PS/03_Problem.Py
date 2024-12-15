# Classifying Spam Content

'''
Make Money
Buy Now
Subscribe
Click Here
Visit Our Website
Limited Time Offer
Double Your Income
'''

message = input("Enter your message: ")
message = message.lower()

spam_1 = "Make Money"
spam_2 = "Buy Now"
spam_3 = "Subscribe"
spam_4 = "Click Here"
spam_5 = "Visit Our Website"
spam_6 = "Limited Time Offer"
spam_7 = "Double Your Income"

condition = (spam_1.lower() in message) or (spam_2.lower() in message) or (spam_3.lower() in message) or (spam_4.lower() in message) or (spam_5.lower() in message) or (spam_6.lower() in message) or (spam_7.lower() in message)

if condition:
    print("This message contains spam content")
else:
    print("This message does not contain spam content")