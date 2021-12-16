# secret-santa-organizer
This is a little program to organize secret santa within your group secretly.

All you need to do is :
1. Create an email id for your secret santa lets call it santaEmailId
2. Go to Google Account https://myaccount.google.com/?utm_source=account-marketing-page&utm_medium=go-to-account-button&pli=1
3. Choose Security > Go to 'Less Secure app access' > Turn On the access
3. Open email_sender.py > Update default value of sender with santaEmailId > Add/Update default value of password with password of santaEmailId > Save
4. Open main.py > Update user_list in Line 56 with users of your group. > Save
5. Run command python3 main.py

Mails will be sent to all your group members with name of their secret child.

==========================================
#Later you can clean up the sent mail(if you want it to stay secret) and share the credentials with your group. Anyone can communicate with others secretly through this.


#Hope you have fun.
