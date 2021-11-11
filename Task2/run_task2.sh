####################################################################################################################
####################################################################################################################
echo "TASK 2 🚀🚀🚀🚀🚀🚀🚀"

# Cleaning outputs if exits
echo "Removing files first 🤌🤌🤌"
rm -rf './mp-conv-count/output'
rm -rf './mp-conv-sort/output'
rm -rf './mp-conv-count/logs.txt'
rm -rf './mp-conv-sort/logs.txt'


echo "Starting maps-reduce jobs 🚀🚀🚀🚀"
export hadoop_home="/home/mahmoud/Desktop/CIE427/hadoop-3.3.1/"

echo "  Getting rate of replies per controversiality 🚀🚀"
echo "    Task: Counting replies per controversiality 🚀"

export working_path="./mp-conv-count/"
export input_path="../sample"
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
    echo "    Failed: Counting replies per controversiality 😭😭, see the logs on logs.txt in the map reduce folder."
    exit 1
fi

echo "    Done: Counting replies per controversiality 😉, see the logs on logs.txt in the map reduce folder."

####################################################################################################################
####################################################################################################################


echo "    Task: sorting replies per controversiality 🚀🚀"

export working_path="./mp-conv-sort/"
export input_path="./mp-conv-count/output/part-00000"
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
    echo "    Failed: sorting replies per controversiality 😭😭, see the logs on logs.txt in the map reduce folder."
    exit 1
fi


echo "    Done: sorting replies per controversiality 😉, see the logs on logs.txt in the map reduce folder."
