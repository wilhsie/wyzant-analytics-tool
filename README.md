# y hello there

## Dependencies
Python 3

Selenium Python Package
Pip3 install selenium

Selenium Webdriver
https://github.com/mozilla/geckodriver/releases

## wat dis?
This program returns lesson data from your Wyzant Tutor account in JSON format:

[
	{
		"date": “1/29/2021”, 
		"length": "95 min", 
		"earned": "$95.00", 
		"student": “Azula F.”
	},
	…
]

## y tho?
I wrote this a while ago before Wyzant had any visual analytics.  I wanted to visualize all of my lesson data and graph it.  I also have a Jupyter notebook that wrangles all of the JSON into nice graphs.  I might upload that later to my github.  Buttt yeh, until then.

## how to use~
In wyzant_object.py make these three changes:
1. Change executable_path variable to point to your selenium web driver ( line 8 )
2. Change send_keys parameter to your Wyzant username ( line 14 )
3. Change send_keys parameter to your Wyzant password ( line 17 )

Run wyzant_testsuite.py

Data will populate inside of notebooks/tutoring_data.txt
