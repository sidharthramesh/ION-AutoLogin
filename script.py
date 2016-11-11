import robobrowser
url = 'https://mahe5.dvois.com/24online/webpages/client.jsp'
br = robobrowser.RoboBrowser()
br.open(url)
form=br.get_forms()[0]
form['username']= '150101312'
form['password']= 'tornadoalert'
form.serialize()
br.submit_form(form)
print "\n\n\n Forget that warning, You are logged in bitch!"