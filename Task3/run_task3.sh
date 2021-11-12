echo "TASK 3 🚀🚀🚀🚀🚀🚀🚀"

# Cleaning outputs if exits
echo "Removing files first 🤌🤌🤌"
rm -rf './mp-topic-up-count/output'
rm -rf './mp-topic-up-sort/output/'
rm -rf './mp-topic-up-count/logs.txt'
rm -rf './mp-topic-up-sort/logs.txt/'


echo "Starting maps-reduce jobs 🚀🚀🚀🚀"
export hadoop_home="/home/mahmoud/Desktop/CIE427/hadoop-3.3.1/"
#export hadoop_home="~/hadoop/hadoop-3.3.1/"


echo "  Getting Top topics that has the most upvotes and the most down votes 🚀🚀"
echo "    Task: Counting upvotes& downvotes per topic 🚀"

export working_path="./mp-topic-up-count/"
export input_path="../sample"
{
$hadoop_home/bin/hadoop jar $hadoop_home/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-input $input_path \
-output $working_path/output \
-file $working_path/mapper.py \
-file $working_path/reducer.py \
-file $working_path/forbidden.py \
-file $working_path/topic_list.py \
-mapper 'python mapper.py' \
-reducer 'python reducer.py' 
}&> $working_path/logs.txt
rm mapper.py 
rm reducer.py
rm forbidden.py
rm topic_list.py
export check_word=$(tail -1 $working_path/logs.txt)

if [[ "$check_word" = *"Failed"* ]]
then
    echo "    Failed: Counting upvotes& downvotes per topic 😭😭, see the logs on logs.txt in the map reduce folder."
    exit 1
fi

echo "    Done: Counting upvotes& downvotes per topic 😉, see the logs on logs.txt in the map reduce folder."

####################################################################################################################
####################################################################################################################


echo "    Task: Extracting top 10 upvotes&downvotes  🚀🚀"

export working_path="./mp-topic-up-sort/"
export input_path="./mp-topic-up-count/output/part-00000"
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
    echo "    Failed: Extracting top 10 upvotes&downvotes  😭😭, see the logs on logs.txt in the map reduce folder."
    exit 1
fi


echo "    Done: Extracting top 10 upvotes&downvotes  😉, see the logs on logs.txt in the map reduce folder."
