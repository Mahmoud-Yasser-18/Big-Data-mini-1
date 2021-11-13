import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility

f=open('./all_outputs/emotion.txt','r')
lines=f.readlines()

authors_per_sub_list=sorted([(line.split('\t')[0].split("_sep_"),int(line.split('\t')[1].replace("\n","")) )for line in lines if line.split('\t')[0].split("_sep_")[1] in [ " happy", " sad"," fearful"," loved"]])
print(authors_per_sub_list)
users_list=[]
for i in range(len(authors_per_sub_list)):
    print(authors_per_sub_list[i])
    # users_list.append(authors_per_sub_list)
print(users_list)
yticks__= [sub for ([sub,emo],numb) in authors_per_sub_list]
yticks__ = list(dict.fromkeys(yticks__))[:5]


users_list_num=[]
for i in range(5):
    users_list_num.append([numb for ([sub,emo],numb) in authors_per_sub_list[i*4:(i+1)*4]])
print(users_list_num)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

colors = ['r', 'g', 'b', 'y','r']*2


yticks = list(range(0,len(yticks__)))
i=0
for c, k in zip(colors, yticks):
    # Generate the random data for the y=k 'layer'.
    xs = np.arange(4)
    ys = users_list_num[i]
    i+=1

    # You can provide either a single color or an array with the same length as
    # xs and ys. To demonstrate this, we color the first bar of each set cyan.
    cs = [c] * len(xs)

    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    ax.bar(xs, ys, zs=k,zdir='y', color=cs, alpha=0.8)

# users_list_name[0][0]="deleted"
ax.set_yticks(yticks)
ax.set_yticklabels(yticks__)
ax.set_xticks([0,1,2,3])
ax.set_xticklabels(["fearful", "happy", "loved", "sad"])  



plt.show()
