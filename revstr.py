import urllib.request, urllib.error, urllib.parse

link = "http://www.chiquitooenterprise.com/password"
 
print(urllib.request.urlopen("http://www.chiquitooenterprise.com/password?code=" + str(urllib.request.urlopen(link).read()).strip("\'b")[::-1]).read().decode('utf-8'))
