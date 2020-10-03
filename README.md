# Fetch-PDF-from-arXiv
Python program to fetch PDF from arXiv

## Necessary Libraries:
urllib, click, feedparser, logging, ssl for myDownload.py.\
unittest, myDownload, timeit for UnitTest.py.

To install click, use ```pip install click```, the installation into a **virtualenv** is heavily recommended.\
For more information on **virtuallenv**, please check the official documenet: [virtualenv](https://click.palletsprojects.com/en/5.x/quickstart/)

To install feedparser, use ```pip install click```. For more information, please check the official document:[feedparser](https://pypi.org/project/feedparser/)

## Command lines
This program enable 5 command line options
####  1, --help 
This command allows the users to check on avaiable command lines, and display them in the terminal\
Example: ```$[User] myDownload.py --help```

####  2, --search TEXT 
This command allows the users to input for a searching keyword, only one word is allowed.\
Default searching keyword is set to "Economy".\
Example: ```$[User] myDownload.py --search cnn```

####  3, --thread TEXT 
This command allows the users to input the max number of threads to download files.\
Default number of threads is set to 3
Example: ```$[User] myDownload.py --search cnn --thread 5```
This command allows the users to download default number of files in 5 threads with keyword "cnn"

####  4, --jobs TEXT 
This command allows the users to input the max number of files to download .\
Default number of files is set to 1.\
Example: ```$[User] myDownload.py --search cnn --thread 5 --jobs 10```
This command allows the users to download 10 files in 5 threads with keyword "cnn".

####  5, --titleasname BOOLEAN 
This command allows the users to download the files with their titles as names rather than their arXiv IDs .\
Example Download File Name: With --titleasname command: **Economy.pdf**, without --titleasname command: **1604.03265v2.pdf**
Default boolean value is set to **False**. To enable this command, please set boolean value to **True**
Example: ```$[User] myDownload.py --search cnn --titleasname True```

## UnitTest
There are 3 unit tests.

#### 1, When number of download file is 0 
Check if exception raised when the input number of file is 0.

#### 2, Compare the download speed for ten files and one file when number of thread is set to 1
Error message occured when the download speed for one file is slower than that of ten files.

#### 3, Compare the download speed for ten files when thread is set to 1 and 10, respectively.
Error message occured when the download speed for ten threads is slower than that of one file.
