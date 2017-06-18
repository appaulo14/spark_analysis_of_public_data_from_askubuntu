import re
from HTMLParser import HTMLParser
from pyspark import SparkContext
from pyspark import SQLContext
sc         = SparkContext(appName = "find_top_tags_for_askubuntu.com")
sqlContext = SQLContext(sc)


def find_top_words_for_field(field,rows_rdd):
    field_rdd = rows_rdd.filter(lambda line: re.search(field + '="([^"]*)" ',line)) \
                        .map(lambda line:(re.search(field + '="([^"]*)" ',line).group(1)))
    
    # Use the filter function to remove lines with no text.
    # Remove HTML escape characters and puncuation marks.
    parser             = HTMLParser()
    filtered_field_rdd = field_rdd.map(lambda line: parser.unescape(line)) \
                                  .map(lambda line: re.sub("<\w+>","",line)) \
                                  .map(lambda line: re.sub("<\w+/>","",line)) \
                                  .map(lambda line: re.sub("</\w+>","",line)) \
                                  .map(lambda line: re.sub("([^A-Za-z0-9 .-])","",line)) \
                                  .filter(lambda line: len(line) > 0)
                        
    # Ideally it would be good to use a library such as NLTK for language parsing instead of ignoring this long list of words.
    # However, I didn't use it to avoid external dependencies and keep this script simple. 
    words_to_ignore = ['a','an','the','and','of','i','but','for','with','this','it','in','you','is','that','are','am','href']
    words_to_ignore += ['to','as','be','or','on','have','if','not','s','t','your','com','from','http','will','so','my','there']
    words_to_ignore += ['more','rel','nofollow','what','by','at','more','also','about','would','should','has','do','than','they']
    words_to_ignore += ['which','was','get','any','www','just','when','then','may','very','https','could','them','might','me']
    words_to_ignore += ['does','no','noreferrer','want','we','here','question','how','can','cannot','after','problem','use']
    words_to_ignore += ['help','once','7','where','problem','problems','hard','why']
    flattened_rdd = filtered_field_rdd.flatMap(lambda line: re.split('\s+',line)) \
                                      .map(lambda line: line.lower()) \
                                      .filter(lambda line: line not in words_to_ignore)
            
    # Create key-value pairs of each word and how many times it occurs. 
    word_count_pairs = flattened_rdd.filter(lambda word: len(word) > 0).map(lambda word:(word.lower(),1)) \
                                     .reduceByKey(lambda v1,v2: v1 + v2).sortByKey(ascending=False)

    # Sort the tag counts by reversing the keys and values, sorting, and then reversing again. 
    top_words_pairs  = word_count_pairs.map(lambda (w,c): (c,w)).sortByKey(ascending=False).map(lambda (c,w): (w,c))
    return top_words_pairs

def write_top_words_to_file(field,top_word_pairs):
    top_words_df = sqlContext.createDataFrame(top_word_pairs.take(1000), ["word", "count"])
    dest_dir      = 'wasb:///analysis_results/stackexchange/askubuntu.com/top_' + field.lower() + '_words'
    top_words_df.coalesce(1).write.csv(dest_dir, header=True,mode='Overwrite')


### Processing starts ###

# Read in as a text file instead of XML because Stack Exchange XML uses self-enclosing tags,
# which aren't supported by com.databricks:spark-xml
entire_file_rdd = sc.textFile('wasb:///datasets/stackexchange/askubuntu.com/Posts.xml')

# Filter out any lines not containing rows of the data. 
rows_rdd = entire_file_rdd.filter(lambda line: "row" in line)

# Find the top words in the title of each post. 
top_title_word_pairs = find_top_words_for_field('Title',rows_rdd)

# Find the top words in the body of each post.
top_body_word_pairs = find_top_words_for_field('Body',rows_rdd)

# Save results to text files for later analysis. 
write_top_words_to_file('Title',top_title_word_pairs)
write_top_words_to_file('Body',top_body_word_pairs)
