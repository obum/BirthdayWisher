import smtplib  # Allows dev to send email messages using python
import datetime as dt
import random

now = dt.datetime.now()
week_day = now.weekday()  # gets week day as integer
print(week_day)

with open('quotes.txt') as quote_data:
    quote_list = quote_data.readlines()

random_quote = random.choice(quote_list)

print(random_quote)

my_email = "obumanichebe@gmail.com"
password = 'stevengerad8'

if week_day == 3:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()  # secures connection with  the email sever.
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="bumski10.oa@gmail.com",
                            msg=f'Subject:Weekly Motivational Quotes\n\n{random_quote}')
