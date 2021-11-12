echo "TASK 4 🚀🚀🚀🚀🚀🚀🚀"

# Cleaning outputs if exits
echo "Removing files first 🤌🤌🤌"
rm -rf './mp-emotion-count/output'
rm -rf './mp-emotion-count/logs.txt'



echo "Starting maps-reduce jobs 🚀🚀🚀🚀"
export hadoop_home="/home/mahmoud/Desktop/CIE427/hadoop-3.3.1/"
#export hadoop_home="/usrs/bin/hadoop-3.3.1/"


echo "  Emotion analysis for top subreddits 🚀🚀"
echo "    Task: counting emotion for subreddits 🚀"

export working_path="./mp-emotion-count/"
export input_path="../sample"
{
$hadoop_home/bin/hadoop jar $hadoop_home/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-input $input_path \
-output $working_path/output \
-file $working_path/mapper.py \
-file $working_path/reducer.py \
-file $working_path/get_emotion.py \
-mapper 'python mapper.py' \
-reducer 'python reducer.py' 
}&> $working_path/logs.txt
rm mapper.py 
rm reducer.py
rm get_emotion.py
export check_word=$(tail -1 $working_path/logs.txt)

if [[ "$check_word" = *"Failed"* ]]
then
    echo "    Failed: counting emotion for subreddits 😭😭, see the logs on logs.txt in the map reduce folder."
    exit 1
fi

echo "    Done: counting emotion for subreddits 😉, see the logs on logs.txt in the map reduce folder."

