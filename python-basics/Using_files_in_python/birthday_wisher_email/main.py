# #################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter images and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
from datetime import datetime
import pandas
import random

email = "salmasyed1360@gmail.com"
password = "vgynpnjmaxjpcpub"

today = datetime.now()
# today_tuple = (today.month, today.day)
today_tuple = (1, 6)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    detail = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", detail["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=detail["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
