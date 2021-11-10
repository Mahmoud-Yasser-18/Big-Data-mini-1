#
# Cleaning outputs if exits
echo "Removing files first 🤌🤌🤌"
rm -rf ./mp-author-sort-subreddits/output
rm -rf ./mp-authors-count-in-subreddits/output
rm -rf ./mp-subreddits-count/output
rm -rf ./mp-subreddits-sort/output
rm -rf ./mp-topic-count-in-subreddits/output
rm -rf ./mp-topic-subreddits-sort/output
echo "Starting maps-reduce jobs 🚀🚀🚀🚀"
export hadoop_home="/home/mahmoud/Desktop/CIE427/hadoop-3.3.1/"

echo "  Getting the top subreddits 🚀🚀"
echo "    Counting each subreddits occurance 🚀"
export working_path="./mp-subreddits-count/"
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
    echo "    Failed: Counting each subreddits occurance 😭😭, see the logs on logs.txt in the map reduce folder "
    exit 1
fi
echo "    Done: Counting each subreddits occurance 😉, see the logs on logs.txt in the map reduce folder "


####################################################################################################################
####################################################################################################################

echo "    Task: Extracting top subreddits 🚀"
export working_path="./mp-subreddits-sort/"
export input_path="./mp-subreddits-count/output/part-00000"
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
    echo "    Failed: Extracting top subreddits 😭😭, see the logs on logs.txt in the map reduce folder "
    exit 1
fi

echo "    Done: Extracting top subreddits 😉, see the logs on logs.txt in the map reduce folder "

cp './mp-subreddits-sort/output/part-00000' './mp-authors-count-in-subreddits/'
cp './mp-subreddits-sort/output/part-00000' './mp-author-sort-subreddits/'
cp './mp-subreddits-sort/output/part-00000' './mp-topic-count-in-subreddits/'
cp './mp-subreddits-sort/output/part-00000' './mp-topic-subreddits-sort//'
####################################################################################################################
####################################################################################################################


echo "  Getting top authos in top subreddits 🚀🚀"
echo "    Task: Count the authors 🚀"

export working_path="./mp-authors-count-in-subreddits/"
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
    echo "    Failed: Count the authors 😭😭, see the logs on logs.txt in the map reduce folder "
    exit 1
fi

echo "    Done: Count the authors 😉, see the logs on logs.txt in the map reduce folder "

####################################################################################################################
####################################################################################################################


echo "    Task: Extracting top 10 authors for the top 10 subreddits 🚀🚀"

export working_path="./mp-author-sort-subreddits/"
export input_path="./mp-authors-count-in-subreddits/output/part-00000"
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
    echo "    Failed: Getting Top 10 the authors 😭😭, see the logs on logs.txt in the map reduce folder "
    exit 1
fi

echo "    Done: Getting Top 10 authors  😉, see the logs on logs.txt in the map reduce folder "

####################################################################################################################
####################################################################################################################


echo "  Getting top topics in top subreddits 🚀🚀"
echo "    Task: Count the topics 🚀"

export working_path="./mp-topic-count-in-subreddits/"
export input_path="./sample"
{
$hadoop_home/bin/hadoop jar $hadoop_home/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-input $input_path \
-output $working_path/output \
-file $working_path/mapper.py \
-file $working_path/reducer.py \
-file $working_path/topic_list.py \
-file $working_path/forbidden.py \
-mapper 'python mapper.py' \
-reducer 'python reducer.py' 
}&> $working_path/logs.txt
rm mapper.py 
rm reducer.py

export check_word=$(tail -1 $working_path/logs.txt)

if [[ "$check_word" = *"Failed"* ]]
then
    echo "    Failed: Count the topics 😭😭, see the logs on logs.txt in the map reduce folder "
    exit 1
fi

echo "    Done: Count the topics 😉, see the logs on logs.txt in the map reduce folder "

####################################################################################################################
####################################################################################################################


echo "    Task: Extracting top 10 topics for the top 10 subreddits 🚀🚀"

export working_path="./mp-topic-subreddits-sort/"
export input_path="./mp-topic-count-in-subreddits/output/part-00000"
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
    echo "    Failed: Extracting top 10 topics 😭😭, see the logs on logs.txt in the map reduce folder "
    exit 1
fi

echo "    Done: Extracting top 10 topics  😉, see the logs on logs.txt in the map reduce folder "