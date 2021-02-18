import smtplib

my_email = "obumanichebe@gmail.com"
password = 'stevengerad8'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="bumski10.oa@gmail.com", msg='Hello')

