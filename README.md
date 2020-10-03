# Fetch-PDF-from-arXiv
Python program to fetch PDF from arXiv

## Necessary Libraries:
urllib, click, feedparser, logging, ssl

To install click, use ```pip install click```, the installation into a **virtualenv** is heavily recommended.
For more information on **virtuallenv**, please check the official documenet: [virtualenv](https://click.palletsprojects.com/en/5.x/quickstart/)

To install feedparser, use ```pip install click```. For more information, please check the official document:[feedparser](https://pypi.org/project/feedparser/)

## Command lines
This program enable 5 command line options
####  1, --search TEXT 
This command allows the users to input for a searching keyword, only one word is allowed
Example: ```$[User] myDownload.py --search cnn```
