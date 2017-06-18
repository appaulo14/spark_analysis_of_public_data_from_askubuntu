# Finding the Most Common Topics on askubuntu.com
## Abstract
This article focuses on analyzing the questions on askubuntu.com to find the most common topics asked about in order to better understand what areas of Ubuntu may need more attention for bug fixing and also what features might be good to add in future releases o Ubuntu. Analyzed public data on askubuntu HDInsights with Spark and found most common topics to identify what areas Ubuntu developers might benefit from focusing on. Tags were the most useful. Word counting the titles and body text was less useful. Future research might try using a natural language parsing library such as [NLTK](http://www.nltk.org/) to better identify topics asked about and also better identify what type of questions are asked for each topics. 

## Introduction
Big Data consists of largs amounts of unstructured or semi-structed data that can be analyzed to derrive new insights that can not easily be found by manually search the data. For example, one could parse gigabytes of server log files to find common causes of errors or slowdowns on a cluster of servers. Another example would be analyzing tweets from Twitter to determine public sentiment about a product. A third example would be analyzing customer buying behavior to better deliver targeted advertising. 

This article focuses on analyzing the questions on askubuntu.com to find the most common topics asked about in order to better understand what areas of Ubuntu may need more attention for bug fixing and also what features might be good to add in future releases o Ubuntu.

I'm in no way affiliated with Ubuntu itself. This analysis is for demonstration purposes only. 

## Methods
The data was obtained from the [Stack Exchange Data Dump on archive.org](https://archive.org/details/stackexchange), after which it was extracted out of its 7z achived and the XML files were uploaded to HDFS storage on Microsoft Azure. From there, the Spark code was developed in Python in an HD Insights cluster following this [Azure HD Insights/Spark guide](https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-apache-spark-jupyter-spark-sql). The tags (Tags.xml), question titles(Posts.xml), and body of the questions(Posts.xml) were analyzed. 

Spark Version: 2.0
Exact command run: spark-submit find_top_tags_for_askubuntu.com.py
TODO: Upload/mention results files. 

Used Jypter notebooks for prototyping. 

## Results
### Top 25 Tags
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


### Top 25 words in body of question, filtering out generic words such as prepositions and conjunctions
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
    <tr><td>24</td><td>files</td><td>97827</td></tr>
</tbody>
</table>

### Top 100 words in Title
TODO

## Discussion/Conclusion
TODO: Add 1st place mentions, etc. 
Tags were the most useful. The most common questions seemed to be about Ubuntu LTS releases (12.04, 14.04, 16.04), with all three recent LTS releases being in the top 6 tags. A lot of questions are related to booting (boot (3rd place),grub2, uefi). This might be due to the wide variety of hardware Ubuntu but can't say for sure. A lot about windows too (dual-boot,windows,windows-7,windows-8). Networking issues common (5th place for networking), 10th place for wireless, and XYZ place of network-manager. Drivers in 8th place. Graphis: ATI/NVidia, multiple monitors,  compiz. Sounds issues (sound, pulseaudio).  Various others here and there. 

~~This section should be a discussion of the results and the implications on the field, as well as other fields. The hypothesis should be answered and validated by the interpretation of the results.  This section should also discuss how the results relate to previous research mentioned in the literature review, any cautions about the findings, and potential for future research.~~

Future research might try using a natural language parsing library such as [NLTK](http://www.nltk.org/) to better identify topics asked about and also better identify what type of questions are asked for each topics. 

TODO: How useful was this? 

Maybe also looks at scores in the future. 

Maybe focus on less than top 100. 
