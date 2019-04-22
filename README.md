Data Intensive Computing (CSE 587)

Lab-2 (Report)

Submitted by:

Deepak Goyal (dgoyal2)

Vishal Gawade (vgawade)

**Topic:** We used Sports as our main topic for Data Collection.
Subtopic and keywords that we used for collection are baseball, Soccer,
Tennis, Rugby, Golf.

Data Collection from below three sources:

1.  **New York Times**: To collect data from New York times, we use New
    York times article search api which gives the articles urls. We
    stored the 100 articles urls into .csv for every subtopic. After
    getting the urls we read the urls from .csv one by one and fetch the
    article data using urllib and requests library & process the data
    using Beautifulsoup library and store in .txt files. Code for the
    New York times are placed as part1 -\> code -\>
    nyTimes\_Articles\_Collection.py & part1 -\> code -\>
    nyTimes\_Data\_Collection.ipynb. Collected Data are placed in part1
    -\> Data -\> NYT

2.  **Common Crawl**: To collect data from common crawl, we use common
    crawl warc files to fetch the data. We read the data from warc
    files; check for the language and search for our keywords in the
    articles and store the corresponding article data into .txt files if
    it matches. Warc and langdetect libraries of python are used to
    reach the extract the relevant data. Code for this are placed as
    part1 -\> code -\> common\_crawl.ipynb. Collected Data are placed in
    part1 -\> Data -\> Commoncrawl

3.  **Twiiter:** To collect tweets data from twitter search api, we use
    the R language. We store the collected tweets in the .csv files.
    After that we process the tweets and remove the irrelevant emojis,
    special characters and store it in the .txt files. Code for this are
    placed as part1 -\> code -\> crawl\_tweets.ipynb. Collected Data are
    placed in part1 -\> Data -\> Twitter**.**

After Collecting the data from above three sources, we process the data
in mapper and reducer to get the word count of each word in the data
files. Sort the word in descending order using word count. Get the top
10 words that repeated most of the times. On the basis of top 10 words,
we process the data to get word co-occurrence of these top 10 words. We
used AWS to implement and run mapper and reducer.

Explanation of Mapper (Word Count):

-   Read the data file (data that are collected from different sources).

-   Remove special character, stop words and other irrelevant
    characters.

-   Perform lemmatization on words

-   For all words in data Emit (word, 1)

Explanation of Reducer (Word Count):

-   Read input data from Mapper.

-   Combine the data using word as key and increment the count(value) of
    each key for every word.

-   Finally sort the data in descending order of count. (Word with the
    highest count stored at first)

-   For first 10 words -\> Emit the (word, count)

Explanation of Mapper (Word Co-occurrence):

-   Read the input (that we get after reducer of word count)

-   Remove special character, stop words and other irrelevant
    characters.

-   Perform lemmatization on word

-   For all words w1 in doc

    For all words w2 in Neighbours(w1)

    Emit (w1-w2, 1)

Explanation of Reducer (Co-occurrence):

-   Read input data from Mapper.

-   Combine the data using word pair as key and increment the
    count(value) of each key for every word pair.

-   Finally sort the data in descending order of count. (Word pair with
    the highest count stored at first)

-   For first 10 words -\> Emit (word pair, count)

**Flow Chart:**

![D:\\Downloads\\visualization.jpg](media/image1.jpeg){width="4.25in"
height="8.313043525809274in"}

While doing all this on AWS, we install all dependencies that are
required to run the code. To install the dependencies, we made a bash
file "install\_dependencies.sh" which install all required dependencies.
Below are the screenshots to explain the steps.

![](media/image2.tiff){width="6.5in" height="3.5217388451443568in"}

![C:\\Users\\Deepak\\Desktop\\2.png](media/image3.png){width="6.5in"
height="3.6260870516185477in"}

![C:\\Users\\Deepak\\Desktop\\3.png](media/image4.png){width="6.5in"
height="3.504348206474191in"}

![C:\\Users\\Deepak\\Desktop\\4.png](media/image5.png){width="6.5in"
height="3.5739129483814525in"}

After performing the Mapper and reducer, we get the word count and word
co-occurrence for all the three sources (NY times, Twitter and Common
Crawl). We also perform mapper and reducer on sub topic for each data
sources, which gives us word count (top 10 words) and word
co-occurrence.

We make 21-word cloud as below:

-   3 for word count (top 10); for each data source (NY times, Twitter
    and Common Crawl)

-   3 for word co-occurrence (top 10); for each data source (NY times,
    Twitter and Common Crawl)

-   15 for word count (top 10); for each subtopic and for each data
    source (NY times, Twitter and Common Crawl) (5 subtopic \* 3 data
    source = total 15)

We used Tableau to perform visualization on each of the above the word
cloud. We make web page of this visualization where you can view by
selecting different like for word count and word co-occurrence. We have
deployed the code; you can click on the below link to view the
visualization:

[Link to Visualization results](https://vishalgawade.github.io/wordcloud_hadoop/visualization.html)
