# Finding the Most Common Topics on askubuntu.com
## Abstract
This article focuses on analyzing the questions on askubuntu.com to find the most common topics asked about in order to better understand what areas of Ubuntu may need more attention for bug fixing and also what features might be good to add in future releases of Ubuntu. To do this, I analyzed public data from askubuntu.com using Azure HDInsights with Spark. Tags were the most useful. Word counting the titles and body text was less useful. Future research might try using a natural language parsing library such as [NLTK](http://www.nltk.org/) to better identify topics asked about and also better identify what type of questions are asked for each topic. 

## Introduction
Big Data consists of largs amounts of unstructured or semi-structed data that can be analyzed to derrive new insights that can not easily be found by manually search the data. For example, one could parse gigabytes of server log files to find common causes of errors or slowdowns on a cluster of servers. Another example would be analyzing tweets from Twitter to determine public sentiment about a product. A third example would be analyzing customer buying behavior to better deliver targeted advertising. 

This article focuses on analyzing the questions on askubuntu.com to find the most common topics asked about in order to better understand what areas of Ubuntu may need more attention for bug fixing and also what features might be good to add in future releases of Ubuntu.

I'm in no way affiliated with Ubuntu itself. This analysis is for demonstration purposes only. 

## Methods
The data was obtained from the [Stack Exchange Data Dump on archive.org](https://archive.org/details/stackexchange), after which it was extracted out of its 7z achived and the XML files were uploaded to HDFS storage on Microsoft Azure.

After the files were uploaded to Azure, two Spark 2.0 scripts were written and executed in Python (find_top_tags_for_askubuntu.com.py and find_top_words_for_askubunut.com.py) in an HD Insights cluster following this [Azure HD Insights/Spark guide](https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-apache-spark-jupyter-spark-sql). 

These scripts can be run from a Spark 2.0 cluster using the following commands:    
```spark-submit find_top_tags_for_askubuntu.com.py```   
```spark-submit find_top_words_for_askubuntu.com.py```    

The results from these scripts are saved in the results section of this repository. For find_top_words_for_askubuntu.com.py, only the top 1,000 results are saved due to size limitations. 

## Results
### Table 1: Top 25 Tags
<table>
<thead><tr><td><b>Rank</b></td><td><b>Tag</b></td><td><b>count</b></td></tr></thead>
<tbody>
    <tr><td>1</td><td>14.04</td><td>21148</td></tr>
    <tr><td>2</td><td>12.04</td><td>17412</td></tr>
    <tr><td>3</td><td>boot</td><td>13098</td></tr>
    <tr><td>4</td><td>command-line</td><td>12294</td></tr>
    <tr><td>5</td><td>networking</td><td>12101</td></tr>
    <tr><td>6</td><td>16.04</td><td>11278</td></tr>
    <tr><td>7</td><td>dual-boot</td><td>10458</td></tr>
    <tr><td>8</td><td>drivers</td><td>9723</td></tr>
    <tr><td>9</td><td>unity</td><td>9122</td></tr>
    <tr><td>10</td><td>wireless</td><td>9018</td></tr>
    <tr><td>11</td><td>server</td><td>8852</td></tr>
    <tr><td>12</td><td>apt</td><td>8589</td></tr>
    <tr><td>13</td><td>grub2</td><td>7755</td></tr>
    <tr><td>14</td><td>partitioning</td><td>7474</td></tr>
    <tr><td>15</td><td>installation</td><td>7221</td></tr>
    <tr><td>16</td><td>nvidia</td><td>6498</td></tr>
    <tr><td>17</td><td>gnome</td><td>5818</td></tr>
    <tr><td>18</td><td>system-installation</td><td>5651</td></tr>
    <tr><td>19</td><td>upgrade</td><td>5507</td></tr>
    <tr><td>20</td><td>bash</td><td>5470</td></tr>
    <tr><td>21</td><td>usb</td><td>5404</td></tr>
    <tr><td>22</td><td>package-management</td><td>5356</td></tr>
    <tr><td>23</td><td>11.10</td><td>5125</td></tr>
    <tr><td>24</td><td>software-installation</td><td>5054</td></tr>
    <tr><td>25</td><td>sound</td><td>4961</td></tr>
</tbody>
</table>

### Table 2: Top 25 Words in Title of Questions 
|Rank|Word       |Count|
|--- | ---       | --- |
|1   |ubuntu     |71478|
|2   |install    |19539|
|3   |14.04	    |12902|
|4   |windows    |12491|
|5   |boot	    |11096|
|6   |error	    |9763|
|7   |16.04	    |9562|
|8   |file	    |9426|
|9  |cant	    |9348|
|10  |12.04	    |9318|
|11  |installing |8392|
|12  |-	        |8332|
|13  |working	|8046|
|14  |using	    |7860|
|15  |screen	    |7003|
|16  |server	    |6999|
|17  |files	    |6851|
|18  |usb	    |6647|
|19  |work	    |5557|
|20  |installation |5438|
|21  |system	      |5340|
|22  |command	  |5055|
|23  |update	      |5006|
|24  |drive	      |4921|
|25  |upgrade	  |4898|


### Table 3: Top 25 Words in Body of Question
*Filtering out generic words such as prepositions and conjunctions
<table>
<thead><tr><td><b>Rank</b></td><td><b>word</b></td><td><b>count</b></td></tr></thead>
<tbody>
    <tr><td>1</td><td>ubuntu</td><td>385199</td></tr>
    <tr><td>2</td><td>install</td><td>264532</td></tr>
    <tr><td>3</td><td>file</td><td>210150</td></tr>
    <tr><td>4</td><td>using</td><td>176274</td></tr>
    <tr><td>5</td><td>all</td><td>151640</td></tr>
    <tr><td>6</td><td>0</td><td>143552</td></tr>
    <tr><td>7</td><td>-</td><td>141588</td></tr>
    <tr><td>8</td><td>windows</td><td>141341</td></tr>
    <tr><td>9</td><td>installed</td><td>140034</td></tr>
    <tr><td>10</td><td>apt-get</td><td>131660</td></tr>
    <tr><td>11</td><td>like</td><td>130961</td></tr>
    <tr><td>12</td><td>sudo</td><td>127988</td></tr>
    <tr><td>13</td><td>boot</td><td>120906</td></tr>
    <tr><td>14</td><td>system</td><td>117750</td></tr>
    <tr><td>15</td><td>its</td><td>114235</td></tr>
    <tr><td>16</td><td>some</td><td>113739</td></tr>
    <tr><td>17</td><td>need</td><td>111594</td></tr>
    <tr><td>18</td><td>run</td><td>111025</td></tr>
    <tr><td>19</td><td>up</td><td>110354</td></tr>
    <tr><td>20</td><td>one</td><td>108843</td></tr>
    <tr><td>21</td><td>command</td><td>105521</td></tr>
    <tr><td>22</td><td>error</td><td>102161</td></tr>
    <tr><td>23</td><td>1</td><td>101823</td></tr>
    <tr><td>24</td><td>only</td><td>100010</td></tr>
    <tr><td>25</td><td>files</td><td>97827</td></tr>
</tbody>
</table>

## Discussion/Conclusion
Tags were the most useful. The most common questions seemed to be about Ubuntu LTS releases (12.04, 14.04, 16.04), with all three recent LTS releases being in the top 6 tags. A lot of questions are related to booting (boot: 3rd place, dual-boot: 7th place, grub2: 13th place). This might be due to the wide variety of hardware Ubuntu but can't say for sure. Networking-related questions were common (networking: 5th place, wireless: 10th place). Many people seem to be interested in running Ubuntu as a server, judging by the server tag coming in at 11th place. Other notably high tags were related to drivers, graphics, installation, patitioning, and sound, again possibly due to the wide variety of hardware on which Ubuntu can run (drivers: 8th place, nvdia: 16th place, installation: 15th place, parititioning: 14th place, sound: 25th place). 

Word counting did not provide much useful information compared to tag counting. A lot of the words were pronouns, prepositions, conjunctions, or other words that do not provide any meaningful information. I tried to filter such words out but it was difficult due to the large number of such words. 

The information collected here may be useful what common problems Ubuntu users face and also what features they are most interested in.

Future research might try using a natural language parsing library such as [NLTK](http://www.nltk.org/) to better identify topics asked about and also better identify what type of questions are asked for each topics. 

