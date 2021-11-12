
import matplotlib.pyplot as plt
import os
os.system("rm -rf ./out_pics")
os.system("mkdir ./out_pics")
left = list(range(1,11))
print(left)
def plot_bar(left,height,tick_label,colors,xlabel,ylabel,title):
    # plotting a bar chart
    plt.bar(left, height, tick_label = tick_label,
            width = 0.8, color = colors)
    
    # naming the x-axis
    plt.xlabel(xlabel)
    # naming the y-axis
    plt.ylabel(ylabel)
    # plot title
    plt.title(title)
    plt.savefig(f"./out_pics/{title}.png")
    # function to show the plot
    plt.show()


## Reading files and ploting 

f=open('./all_outputs/sub.txt','r')
lines=f.readlines()
sub_list=[line.split('\t')[0] for line in lines ][::-1]
sub_count_list=[int(line.split('\t')[1].replace("\n","")) for line in lines ][::-1]

plot_bar(left,sub_count_list,sub_list,['black'],"Top Subreddits",'Replies',"Replies per top Subreddits")
##############################################################################


f=open('./all_outputs/author_per_topic_per_sub.txt','r')
lines=f.readlines()
author_per_topic_per_sub_list=[line.split('\t')[0].split("_sep_") for line in lines ][::-1]
author_per_topic_per_sub_count_list=[int(line.split('\t')[1].replace("\n","")) for line in lines ][::-1]


##############################################################################

f=open('./all_outputs/authors_per_sub.txt','r')
lines=f.readlines()
authors_per_sub_list=[line.split('\t')[0].split("_sep_") for line in lines ][::-1]
authors_per_sub_count_list=[int(line.split('\t')[1].replace("\n","")) for line in lines ][::-1]


##############################################################################

f=open('./all_outputs/conv_cont.txt','r')
lines=f.readlines()
conv_cont_list=[line.split('\t')[0].split("_sep_") for line in lines ][::-1]
conv_cont_count_list=[int(line.split('\t')[1].replace("\n","")) for line in lines ][::-1]


##############################################################################

f=open('./all_outputs/emotion.txt','r')
lines=f.readlines()
emotion_list=[line.split('\t')[0].split("_sep_") for line in lines ][::-1]
emotion_count_list=[int(line.split('\t')[1].replace("\n","")) for line in lines ][::-1]


##############################################################################

f=open('./all_outputs/topic_per_sub.txt','r')
lines=f.readlines()
topic_per_sub_list=[line.split('\t')[0].split("_sep_") for line in lines ][::-1]
topic_per_sub_count_list=[int(line.split('\t')[1].replace("\n","")) for line in lines ][::-1]


##############################################################################

f=open('./all_outputs/topic_up.txt','r')
lines=f.readlines()
topic_up_list=[line.split('\t')[0].split("_sep_") for line in lines ][::-1]
topic_up_count_list=[int(line.split('\t')[1].replace("\n","")) for line in lines ][::-1]


##############################################################################


