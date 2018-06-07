import matplotlib as mpl
mpl.use('Agg') # avoid using x server
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pickle
import sys

# argv[1] -  pickle file name
# argv[2] - title

# opening the pickle file
pickleFile = open(sys.argv[1],'rb')
Statistic = pickle.load(pickleFile)
pickleFile.close()

# plotting
fig, ax = plt.subplots()
ax.set_xscale('log')
plt.plot(Statistic["mean_episode_rewards"], color="blue")
plt.plot(Statistic["best_mean_episode_rewards"], color="red")
ax.set_xlabel("Time Step",fontsize=12)
ax.set_ylabel("Reward",fontsize=12)
blue_patch = mpatches.Patch(color='blue', label='100-episode mean reward')
red_patch = mpatches.Patch(color='red', label='best mean reward')
ax.legend(handles=[blue_patch, red_patch], prop={'size': 10})
ax.set_title(sys.argv[2],fontsize=14)
plt.savefig(sys.argv[1] + '.png')
print("Plot Generated Successfully")
