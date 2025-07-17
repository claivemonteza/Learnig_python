import smtplib
import getpass

# If you want to see the SMTP messages that are being sent back 
# and forth by the smtplib module behind the scenes, you can set 
# the debug level on the SMTP or SMTP_SSL object. The examples in 
# this lesson won’t show the debug output, but you might find it interesting!

mail_server = smtplib.SMTP_SSL('smtp.example.com')


# Now that we’ve made a connection to the SMTP server, the next thing we 
# need to do is authenticate to the SMTP server. Typically, email providers 
# wants us to provide a username and password to connect. 
# Let's put the password into a variable so it's not visible on the screen.
mail_server.set_debuglevel(1)

# The example above uses the getpass module so that passers-by 
# won't see the password on the screen. Watch out, though; 
# the mail_pass variable is still just an ordinary string!
mail_pass = getpass.getpass('Password? ')


# Now that we have the email user and password configured, 
# we can authenticate to the email server using the SMTP object's 
# login method.
mail_server.login(sender, mail_pass)


#Alright! We're connected and authenticated to the SMTP server. 
# Now, how do we send the message?
mail_server.send_message(message)



# Okay, well that last bit was pretty easy! We did the hard part first! The 
# send_message method returns a dictionary of any recipients that weren’t able 
# to receive the message. Our message was delivered successfully, so send_message 
# returned an empty dictionary. Finally, now that the email is sent, let's close the connection to the mail server.
mail_server.quit()