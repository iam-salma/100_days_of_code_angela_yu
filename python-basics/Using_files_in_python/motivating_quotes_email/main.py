import smtplib
import datetime as dt
import random

email = "salmasyed1360@gmail.com"
password = "Syedali2000!"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 0:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# import smtplib
#
# email = "salmasyed1360@gmail.com"
# password = "aphwopwdfhdflmgi"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs="salmajed1360@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )


# import datetime

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)
