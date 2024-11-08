from datetime import datetime
import pandas
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

myEmail = os.getenv("YOUR_EMAIL")
password = os.getenv("YOUR_PASSWORD")



today = datetime.now()
todayTuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdayDict = {(dataRow["month"],dataRow["day"]): dataRow for (index, dataRow) in data.iterrows()}

if todayTuple in birthdayDict:
    birthdayPerson = birthdayDict[todayTuple]
    filePath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(filePath) as letterFile:
        contents = letterFile.read()
        contents = contents.replace("[NAME]", birthdayPerson["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(myEmail, password)
        connection.sendmail(from_addr=myEmail, to_addrs=birthdayPerson["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")
