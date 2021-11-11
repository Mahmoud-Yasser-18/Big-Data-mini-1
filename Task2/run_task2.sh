####################################################################################################################
####################################################################################################################

# Cleaning outputs if exits
echo "Removing files first 🤌🤌🤌"
rm -rf ./mp-author-sort-subreddits/output
rm -rf ./mp-author-count-in-subreddits/output
rm -rf ./mp-subreddits-count/output
rm -rf ./mp-subreddits-sort/output
rm -rf ./mp-topic-count-in-subreddits/output
rm -rf ./mp-topic-subreddits-sort/output
rm -rf ./mp-author-topic-count-in-subreddits/output
rm -rf ./mp-author-topic-sort-subreddits/output
rm -rf ./mp-author-sort-subreddits/logs.txt
rm -rf ./mp-author-count-in-subreddits/logs.txt
rm -rf ./mp-subreddits-count/logs.txt
rm -rf ./mp-subreddits-sort/logs.txt
rm -rf ./mp-topic-count-in-subreddits/logs.txt
rm -rf ./mp-topic-subreddits-sort/logs.txt
rm -rf ./mp-author-topic-count-in-subreddits/logs.txt
rm -rf ./mp-author-topic-sort-subreddits/logs.txt
echo "Starting maps-reduce jobs 🚀🚀🚀🚀"
export hadoop_home="/home/mahmoud/Desktop/CIE427/hadoop-3.3.1/"

echo "  Getting the top subreddits 🚀🚀"
echo "    Counting each subreddits occurance 🚀"


echo "  Getting 10 top authors in top 10 topics in top 10 subreddits 🚀🚀"
export working_path="./mp-author-topic-count-in-subreddits/"
export input_path="./sample"
{
$hadoop_home/bin/hadoop jar $hadoop_home/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-input $input_path \
-output $working_path/output \
-file $working_path/mapper.py \
-file $working_path/reducer.py \
-mapper 'python mapper.py' \
-reducer 'python reducer.py' 
}&> $working_path/logs.txt
rm mapper.py 
rm reducer.py

export check_word=$(tail -1 $working_path/logs.txt)

if [[ "$check_word" = *"Failed"* ]]
then
    echo "    Failed: Count authors in top 10 topics in top 10 subreddits 😭😭, see the logs on logs.txt in the map reduce folder."
    exit 1
fi

echo "    Done: Count authors in top 10 topics in top 10 subreddits 😉, see the logs on logs.txt in the map reduce folder."

####################################################################################################################
####################################################################################################################


echo "    Task: Extracting top 10 authors in top 10 topics in top 10 subreddits 🚀🚀"

export working_path="./mp-author-topic-sort-subreddits/"
export input_path="./mp-author-topic-count-in-subreddits/output/part-00000"
touch $working_path/logs.txt

{
$hadoop_home/bin/hadoop jar $hadoop_home/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-input $input_path \
-output $working_path/output \
-file $working_path/mapper.py \
-file $working_path/reducer.py \
-mapper 'python mapper.py' \
-reducer 'python reducer.py' 
}&> $working_path/logs.txt
rm mapper.py 
rm reducer.py

export check_word=$(tail -1 $working_path/logs.txt)
if [[ "$check_word" = *"Failed"* ]]
then
    echo "    Failed: Extracting top 10 authors in top 10 topics in top 10 subreddits 😭😭, see the logs on logs.txt in the map reduce folder."
    exit 1
fi


echo "    Done: Extracting top 10 authors in top 10 topics in top 10 subreddits 😉, see the logs on logs.txt in the map reduce folder."

####################################################################################################################
####################################################################################################################
