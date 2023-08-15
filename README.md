# telegram-group-members-extraction
scrape and extract more than 10k members from telegram groups.

This repository contains scripts to facilitate the extraction of members from Telegram groups, categorizing between groups with less than 10k members and those with more than 10k members.

## How to Run

### Groups with Less Than 10k Members

Execute the `less_than_10k.py` script.

### Groups with More Than 10k Members

Execute the `more_than_10k.py` script.

Before Running, please ensure you have the necessary packages installed, including Telethon.

## Prerequisites

Before you begin, make sure you have the following:

1. A Telegram account with a phone number from any country.
2. Visit [my.telegram.org](https://my.telegram.org) to create a development app in the designated section. Obtain your `api_id` and `api_hash`.
3. Join the groups from which you wish to extract member data using the phone number associated with your `api_id` and `api_hash`.
4. Run the desired code and input the prompted credentials.
5. If you are running the code for the first time, you will need to log in, and a verification code will be sent via a Telegram chat.
6. For subsequent runs, you won't need to log in again; your session will be stored in a file named `{phone_number}.session`.

Feel free to contribute to this repository and enhance its capabilities!

---

**Note:** Please ensure compliance with Telegram's terms of service and API usage guidelines when utilizing these scripts.