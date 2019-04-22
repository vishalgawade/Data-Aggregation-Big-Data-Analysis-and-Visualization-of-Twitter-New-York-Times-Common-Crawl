<p align="center">Data Intensive Computing</br>Hadoop - MapReduce - Tableau </p>

------

![show](https://github.com/vishalgawade/Data-Aggregation-Big-Data-Analysis-and-Visualization-of-Twitter-New-York-Times-Common-Crawl/blob/master/images/show.png)

Goal
---
Learn Parallel Processing of Big Data using Hadoop MapReduce and Build Analysis and Visualization Dashboard(s) using Tableau</br>


Topic:
---
We used Sports as our main topic for Data Collection.Subtopic and keywords that we used for collection are baseball, Soccer,Tennis, Rugby, Golf.

#### Data Collection from below three sources:

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

#### Explanation of Mapper (Word Count):

-   Read the data file (data that are collected from different sources).

-   Remove special character, stop words and other irrelevant
    characters.

-   Perform lemmatization on words

-   For all words in data Emit (word, 1)

#### Explanation of Reducer (Word Count):

-   Read input data from Mapper.

-   Combine the data using word as key and increment the count(value) of
    each key for every word.

-   Finally sort the data in descending order of count. (Word with the
    highest count stored at first)

-   For first 10 words -\> Emit the (word, count)

#### Explanation of Mapper (Word Co-occurrence):

-   Read the input (that we get after reducer of word count)

-   Remove special character, stop words and other irrelevant
    characters.

-   Perform lemmatization on word

-   For all words w1 in doc, which is in top10 words

    For all words w2 in Neighbours(w1)

    Emit (w1-w2, 1)

#### Explanation of Reducer (Co-occurrence):

-   Read input data from Mapper.

-   Combine the data using word pair as key and increment the
    count(value) of each key for every word pair.

-   Finally sort the data in descending order of count. (Word pair with
    the highest count stored at first)

-   For first 10 words -\> Emit (word pair, count)

**Flow Chart:**

![f1](https://github.com/vishalgawade/Data-Aggregation-Big-Data-Analysis-and-Visualization-of-Twitter-New-York-Times-Common-Crawll/blob/master/images/flowchart.jpeg)

While doing all this on AWS, we install all dependencies that are
required to run the code. To install the dependencies, we made a bash
file "install\_dependencies.sh" which install all required dependencies.
Below are the screenshots to explain the steps.

![l1](https://github.com/vishalgawade/Data-Aggregation-Big-Data-Analysis-and-Visualization-of-Twitter-New-York-Times-Common-Crawll/blob/master/images/Picture_1.png)

![l2](https://github.com/vishalgawade/Data-Aggregation-Big-Data-Analysis-and-Visualization-of-Twitter-New-York-Times-Common-Crawll/blob/master/images/Picture_2.png)

![l3](https://github.com/vishalgawade/Data-Aggregation-Big-Data-Analysis-and-Visualization-of-Twitter-New-York-Times-Common-Crawll/blob/master/images/Picture_3.png)

![l4](https://github.com/vishalgawade/Data-Aggregation-Big-Data-Analysis-and-Visualization-of-Twitter-New-York-Times-Common-Crawll/blob/master/images/Picture_4.png)

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

About folder structure:
---
###### Part1- Data Collection
###### Part2- Trying demo on apache hadoop
###### Part3- Big Data Analysis on AWS EMR and Visualization in Tableau 

License
---
Copyright {2019} 
{Vishal Gawade vgawade@buffalo.edu & Deepak Goyal dgoyal2@buffalo.edu} 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
