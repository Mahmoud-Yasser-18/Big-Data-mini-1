
## Gathering the outsputs in one folder
rm -rf  ./all_outputs
mkdir all_outputs

cp './Task1/mp-author-sort-subreddits/output/part-00000' './all_outputs/authors_per_sub.txt'
cp './Task1/mp-author-topic-sort-subreddits/output/part-00000' './all_outputs/author_per_topic_per_sub.txt'
cp './Task1/mp-subreddits-sort/output/part-00000' './all_outputs/sub.txt'
cp './Task1/mp-topic-subreddits-sort/output/part-00000' './all_outputs/topic_per_sub.txt'

cp './Task2/mp-conv-count/output/part-00000' './all_outputs/conv_cont.txt'
cp './Task3/mp-topic-up-sort/output/part-00000' './all_outputs/topic_up.txt'
cp './Task4/mp-emotion-count/output/part-00000' './all_outputs/emotion.txt'

python generate_graphs.py