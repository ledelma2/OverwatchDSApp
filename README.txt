# OverwatchDSApp
Personal data science project to help analyze my performance in overwatch.

Stage 1: The Database

The database will contain tables of Maps, Heroes, General Match Stats, and Specific Match Stats.
The database is farily modifiable so as to work with other competetive games in the future.
I.E. for CS:GO replace the Heroes table with Guns. While it would be nice to use an API to 
scrape the match data off of Blizzard's servers, I do not believe one exists.

EDIT 11/13/18:
Data input has begun, though inserting data by hand after every match is incredibly tedious. To
bypass this process I'm going to be creating a simple webscraper in Python to get my updated
total data for the competitive season, and then calculate the the current match data by comparing
to previous total data.

EDIT 11/16/18:
Because Blizzard's site is very "rich" in HTML I'm also going to be utilizing the python-overwatch
API to help gather info. However, I may also have to make changes to the package's main script
since, for some reason, I get a "HeroNotFound" exception when looking for Brigitte.

EDIT 1/23/19:
The "HeroNotFound" exception was due to the python-overwatch API using an array of size 2 to access
both quickplay and competetive stats. When quickplay stats are missing the real competitive index gets
decremented by 1 therefore forcing the "HeroNotFound" exception. After finishing the whole project I
will likely go and add a fix for this bug, but for now I will just put play time in qp for all heroes
to avoid the bug. Added support for Ashe.

EDIT 1/24/19:
Added database access through the use of the pyodbc module (https://github.com/mkleehammer/pyodbc). 
Connection the microsoft access database is now possible.

Stage 1.5: The GUI
If a GUI is implemented to insert data into the database, the language used will likely be C#
in order to utilize LINQ or Python to utilize NoSQL.

Stage 2: The Machine Learning Algorithm
After spending an unspecified amount of time collecting match data from competetive overwatch, I 
will load the data into the database and utilize a machine learning algorithm to analyze my
performance. The algorithm in question will likely be a Neural Network or a K-Means Clustering
algorithm. The language used for this stage will almost certainly be Python for its ML library
and dynamic type inferencing.

Stage 3: Data Analysis
With the machine learning algorithm (hopefully) working within acceptable error numbers, we need
to find a way to visualize the data. The most important categories I would like to display are
match time, queue size, number of hero swaps, and role(s) played in relation Win% and Average SR
change. I would like to use R for this task, however since I do not know R, I may use Python and
its associated graphing library if R proves to be to difficult.
