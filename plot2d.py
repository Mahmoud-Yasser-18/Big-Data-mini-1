import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility

f=open('./all_outputs/topic_per_sub.txt','r')
lines=f.readlines()
authors_per_sub_list=[line.split('\t')[0].split("_sep_") for line in lines ][::-1]
authors_per_sub_count_list=[int(line.split('\t')[1].replace("\n","")) for line in lines ][::-1]
left= list(range(1,len(authors_per_sub_count_list)))
users_list_num=[]
users_list_name=[]

for i in range(10):
    users_list_num.append(authors_per_sub_count_list[i*10:(i+1)*10])
    users_list_name.append([auto for  sub,auto in authors_per_sub_list[i*10:(i+1)*10]])

yticks__= [sub for sub,auto in authors_per_sub_list]
yticks__ = list(dict.fromkeys(yticks__))


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b', 'y','r','g']


yticks = list(range(0,5))
i=0
for c, k in zip(colors, yticks):
    # Generate the random data for the y=k 'layer'.
    xs = np.arange(5)
    ys = users_list_num[i][:5]
    i+=1

    # You can provide either a single color or an array with the same length as
    # xs and ys. To demonstrate this, we color the first bar of each set cyan.
    cs = [c] * len(xs)

    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    ax.bar(xs, ys, zs=k,zdir='y', color=cs, alpha=0.8)

# users_list_name[0][0]="deleted"
ax.set_yticks(yticks)
ax.set_yticklabels(yticks__[:5])
ax.set_xticks(yticks)
ax.set_xticklabels(users_list_name[0][:5])  

plt.show()
