# 🎉 Birthday Email Automation 🎉

A Python script that automatically sends birthday wishes to contacts from a CSV file, selecting a random birthday message template and delivering it through email. Perfect for ensuring no one’s birthday is missed!

--- 
## 📋 Prerequisites
1. **Python Libraries**:
   - datetime for handling dates.
   - pandas for working with CSV files.
   - random for selecting random letter templates.
   - smtplib for sending emails.
   - dotenv for environment variable management.
2. **Environment Variables**:
   - EMAIL: Your email address used for sending emails.
   - PASSWORD: The email account password.
3. **Email Provider**:
   - Currently set up for Gmail SMTP (smtp.gmail.com) on port 587.
4. **Data Files**:
   - birthdays.csv: A file that contains columns name, email, year, month, day to store birthday information.
   - letter_templates: A folder containing pre-written birthday letter templates named as letter_1.txt, letter_2.txt, etc.

## 🚀 Usage
1. Set Up Environment Variables:
   - Add your email and password to a .env file as shown below:
  ```python
  EMAIL=youremail@example.com
  PASSWORD=yourpassword
  ```
2. Prepare birthdays.csv File:
  - Ensure birthdays.csv has the following format:
  ```python
  name,email,year,month,day
  John Doe,johndoe@example.com,1990,11,8
  ```
3. Add Templates:
- Inside the letter_templates folder, add text files named letter_1.txt, letter_2.txt, etc.
- Each file should contain a message with [NAME] as a placeholder for the recipient's name.
4. Run the Script:
- Simply run the script, and if today matches a birthday in birthdays.csv, it will send an email automatically.

## 📝 Code Explanation
```python
from datetime import datetime
import pandas
import random
import smtplib
import os
from dotenv import load_dotenv
```
- Imports: Imports required modules, including datetime to check the current date and smtplib to send emails.
```python
load_dotenv()
myEmail = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
```
- Load Environment Variables: Fetches EMAIL and PASSWORD from .env for secure handling of sensitive information.
```python
today = datetime.now()
todayTuple = (today.month, today.day)
```
- Get Today’s Date: Determines today’s month and day.
```python
data = pandas.read_csv("birthdays.csv")
birthdayDict = {(dataRow["month"],dataRow["day"]): dataRow for (index, dataRow) in data.iterrows()}
```
- Load and Parse Birthdays: Reads birthdays.csv and creates a dictionary with keys as date tuples and values as row data.
```python
if todayTuple in birthdayDict:
    birthdayPerson = birthdayDict[todayTuple]
    filePath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(filePath) as letterFile:
        contents = letterFile.read()
        contents = contents.replace("[NAME]", birthdayPerson["name"])
```
- Select and Customize Letter: Checks if today is a birthday, selects a random letter template, and customizes it with the recipient’s name.
```python
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(myEmail, password)
        connection.sendmail(from_addr=myEmail, to_addrs=birthdayPerson["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")
```
- Send Email: Establishes a secure SMTP connection, logs in, and sends the customized email.

## 🎨 Customization
- Add more templates to letter_templates to keep messages fresh.
- Extend the CSV file with additional contacts.



🎉 Happy Automating! 🎉
