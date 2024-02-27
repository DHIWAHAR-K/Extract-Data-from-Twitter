# Extracting Data from Twitter using Python

## Overview

This Python script demonstrates the process of extracting data from Twitter using the `tweepy` library. The script utilizes the Twitter API to fetch tweets based on specified criteria. Explore this script to understand the basics of extracting data from Twitter in Python.

## Script Components

- **Library Installation:** Installing the necessary library (`tweepy`).
- **Twitter Developer Account:** Obtaining API credentials from the Twitter Developer platform.
- **Authentication:** Authenticating with the Twitter API using obtained credentials.
- **Data Extraction:** Fetching tweets based on search criteria or user timeline.
- **Data Processing:** Cleaning and organizing the extracted data.
- **Output Display:** Displaying the fetched tweets or saving them to a file.

## Requesting the Twitter API
Twitter API gives us developer access to connect to Twitter and extract or modify data. and Here are the steps to follow to get the Twitter API:

1. Use this link to request an API by providing required inputs. It might take 2-3 hours to get the approval.
2. Once you get the approval, you will be able to see your project by going to the dashboard.
3. If you observe clearly, under the ‘Access Token and Secret’, you will be initially having ‘Created with Read Only permissions.
4. And we need to change this to ‘Read and Write’ for serving our purpose of extracting and writing data.
5. For this, we choose the Setting tab and click on the edit option in User authentication settings

## Running the Script

1. Install the required library by running `pip install tweepy` in your Python environment.
2. Obtain API credentials by creating a Twitter Developer account and creating an app.
3. Open and run the Python script (`twitter_data_extraction.py`) in a Python environment.
4. The script will authenticate, fetch tweets based on specified criteria, and display or save the data.

## Customization

- Modify the script to extract tweets based on specific hashtags, users, or keywords.
- Experiment with additional parameters provided by the Twitter API for more refined searches.
- Adapt the code to include sentiment analysis or other data processing techniques.

## License

This Twitter Data Extraction in Python is open-source and distributed under the [MIT License](LICENSE). Feel free to modify and use the code for your Twitter data extraction projects or educational purposes!
