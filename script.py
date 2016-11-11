import robobrowser
url = 'https://mahe5.dvois.com/24online/webpages/client.jsp'
br = robobrowser.RoboBrowser()
br.open(url)
form=br.get_forms()[0]
form['username']= 'username' #Change this
form['password']= 'password' #Change this too 
form.serialize()
br.submit_form(form)
print "\n\n\n Forget that warning, You are logged in bitch!"
