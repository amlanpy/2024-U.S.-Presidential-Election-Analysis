# 2024-U.S.-Presidential-Election-Analysis

SENTIMENT ANALYSIS (AMLAN)

First to do the scrapping, go to https://console.apify.com/
Search for the trudax/reddit-scrapper and run the scrapping according to all the filters needed.
Download the results as any file you want.
2 example results downloaded as Excel files have been attached to the repository.
Copy one of the file paths to the Reddit_sentiment_analysis.py code and run the code.
The code will print out sentiment scores for each sentence extracted in the scrapping process.
The 2 Excel data sets for demo - https://github.com/amlanpy/2024-U.S.-Presidential-Election-Analysis/blob/main/dataset_reddit-scraper_2024-12-03_15-53-03-836.xlsx and https://github.com/amlanpy/2024-U.S.-Presidential-Election-Analysis/blob/main/dataset_reddit-scraper_2024-12-03_18-01-45-440.xlsx

BOT DETECTION (CHRISTINE)

Run CIS400project.py and it will ask you to type in a subreddit that you want to look into, then it will ask for the number of posts/comments that you want to look for, after answering the two questions it will start crawling and shows you who seems like a bot and who seems like a human. 


TWEET SCRAPING AND ANALYSIS (RICHARD)

The "aug_chunk_116.csv.zip" is a compressed file of all of the tweets related to the elections with a time frame of around August 16-17. The first thing to do is to is to manually get rid of all of the non relevant information and simply it. There are two simplified datasets. One of them has ten thousand tweets while the other has fifty thousand. To get data, go to the "twttrrunner.py" file and on line four, choose the txt file that you wish to analyze. There are six functions that are available. The "getAllUsernames" function gets all of the usernames in the text file and the getAllHashtags does the same for the hashtags. The "getNumUsernames" and "getNumHashtags" gets you only the first number of hashtags or usernames that you decide to get. Likewise, "getAllText" gives you all of the tweeted text and "getNumText" gives you a specific amount that you choose. There are two ranking functions that are available to gather relevent data to see if there are trends present. The first one is "allHashtagRankingTopTen" which prints out a list of the top tep most reocurring hashtags and how many times they have appeared. The "allLikesRankingTopTen" will print out the ten most liked tweets from greatest to least with the text of the tweet also being printed.
