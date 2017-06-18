import re
from pyspark import SparkContext
from pyspark import SQLContext
sc         = SparkContext(appName = "find_top_tags_for_askubuntu.com")
sqlContext = SQLContext(sc)


# Read in as a text file instead of XML because Stack Exchange XML uses self-enclosing tags,
# which aren't supported by com.databricks:spark-xml
entire_file_rdd = sc.textFile('wasb:///datasets/stackexchange/askubuntu.com/Tags.xml')

# Filter out any lines not containing rows of the data. 
rows_rdd = entire_file_rdd.filter(lambda line: "row" in line)
rows_rdd.count()

# Parse the tags and tag counts out of the text, turing them into key-value pairs.
tag_count_pairs = rows_rdd.filter(lambda line: len(line) > 0) \
                          .filter(lambda line: re.search('TagName="(\S+)"',line) and re.search('Count="(\d+)"',line)) \
                          .map(lambda line:(re.search('TagName="(\S+)"',line).group(1),re.search('Count="(\d+)"',line).group(1)))

# Sort the tag counts by reversing the keys and values, sorting, and then reversing again. 
reversed_top_tag_count_pairs = tag_count_pairs.map(lambda (k,v): ((int(v),k))).sortByKey(ascending=False)
top_tag_count_pairs = reversed_top_tag_count_pairs.map(lambda (k,v): ((v,k)))

# Save results to a text file for later analysis. 
top_tags_df = sqlContext.createDataFrame(top_tag_count_pairs, ["tag", "count"])
dest_dir    = 'wasb:///analysis_results/stackexchange/askubuntu.com/top_tags'
top_tags_df.coalesce(1).write.csv(dest_dir, header=True,mode='Overwrite')
