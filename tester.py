#overwatch data retriever
#utilizes both the python-overwatch api and beautiful soup to retrive data
from bs4 import BeautifulSoup
from overwatch import Overwatch


overwatch = Overwatch(battletag="Serb#11472")
print(overwatch(mode="cp", hero="ashe", filter="combat"))
