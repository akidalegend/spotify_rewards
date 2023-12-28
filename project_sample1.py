"""I need to create a Spotify Rewards System where we can give different rewards based on the number of hours of
music listened to and the number of months they are subscribed to."""

import os
import pandas as pd

# Specify the path to your Excel file
excel_file_path = Spotify_Dataset.xlsx

# Check if the file exists
if os.path.exists(excel_file_path):
    # Read the Excel file into a pandas DataFrame using the variable
    df = pd.read_excel(excel_file_path)

    # Display the DataFrame
    print(df)
else:
    print(f"Error: File not found at {excel_file_path}")

for index, row in df.iterrows():
    user_name = row["Name"]
    months_premium = row["No of Months on Premium"]
    hours = row["No of Hours Listened p.m"]
for index, row in df.iterrows():
    if months_premium == 1 and hours >= 97:
        print(f"Congratulations, {user_name}! You've been a loyal subscriber for 1 month.")
    elif months_premium == 3 and hours >= 292:
        print(f"For being a loyal subscriber for 3 months, we're sending a gift card of £5 to your address.")
        address = input("Please enter your address below: ")
        print(f"Thank you, {user_name}! We will send the gift card to {address}. ")
    elif months_premium == 6 and hours >= 97*6:
        print(f"Wow {user_name}! You've been with us for 6 months now ")
    elif months_premium == 9 and hours >= 97 * 9:
        print(f"Wow {user_name}! You've been with us for 9 months now ")
    elif months_premium == 12 and hours >= 97 * 12:
        print(f"Wow {user_name}! You've been with us for 12 months now ")
    elif months_premium == 18 and hours >= 97 * 18:
        print(f"Wow {user_name}! You've been with us for 18 months now ")
    elif months_premium == 21 and hours >= 97 * 21:
        print(f"Wow {user_name}! You've been with us for 21 months now ")
    elif months_premium >= 24 and hours >= 97 * 24:
        print(f"Wow {user_name}! You've been with us for 24 months now ")



