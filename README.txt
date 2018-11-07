# OverwatchDSApp
Personal data science project to help analyze my performance in overwatch.

Stage 1: The Database

The database will contain tables of Maps, Heroes, General Match Stats, and Specific Match Stats.
The database is farily modifiable so as to work with other competetive games in the future.
I.E. for CS:GO replace the Heroes table with Guns. While it would be nice to use an API to 
scrape the match data off of Blizzard's servers, I do not believe one exists.

Stage 1.5: The GUI
If a GUI is implemented to insert data into the database, the language used will likely be C#
in order to utilize LINQ or Python to utilize NoSQL.

Stage 2: The Machine Learning Algorithm
After spending an unspecified amount of time collecting match data competetive overwatch, I 
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
