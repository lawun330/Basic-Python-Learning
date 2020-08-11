import matplotlib.pyplot as plt
import numpy as np 


x = np.linspace(0,10,10)
y = x**2
#basic methods
'''
plt.subplot(2,2,1)
plt.plot(x,y,'b--') #blue color
plt.xlabel('x')
plt.ylabel('y')
plt.title('y=x^2')

plt.subplot(2,2,2)
plt.plot(x,y,'r+') #red color
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([]) #set or remove x,y marks on axis
plt.yticks([])

plt.subplot(2,2,3)
plt.plot(x,y,'g*') #green color
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2,2,4)
plt.plot(x,y,'yo-') #yellow color
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([])
plt.yticks([])

plt.show()'''

##################

#formal Object oriented method

#figure, axes and plotting
fig 	= plt.figure() #create a blank figure
#adjusting axes
axes 	= fig.add_axes([0.1,0.1,0.8,0.8]) #add axes [left, bot, width, height]
axes2 	= fig.add_axes([0.2,0.4,0.3,0.4])

axes.plot(x, y, 'b',label= 'y = x**2')
axes.set_xlabel('Set X Label') # Notice the use of set_ to begin methods
axes.set_ylabel('Set y Label')
axes.set_title('Set Title')
axes.legend(loc=4) 
# 1 upper right
# 2 upper left
# 3 lower left
# 4 lower right
# 0 let matplot choose # default
axes2.plot(y, x, 'r',label= 'y = sqrt(x)')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title');
axes2.legend() #legend() add the legend at label = '' 
plt.show(fig) #notice that the two plots are not within or inserted, it is all about co-ordinating in blanket

#subplot method as figure() alternative
fig, axes = plt.subplots() #empty tuples is same as figure()
axes.plot(x, y, 'g')
axes.set_xlabel('Set X Label') # Notice the use of set_ to begin methods
axes.set_ylabel('Set y Label')
axes.set_title('Set Title')
plt.show(fig)

#subplotting
fig, axes = plt.subplots(2,1) #1,2 or 2,1 for now

for ax in axes:
	ax.plot(x,y,'p')
	ax.set_xlabel('Set X Label') # Notice the use of set_ to begin methods
	ax.set_ylabel('Set y Label')
	ax.set_title('Set Title')
plt.show(fig)

#sizing the figure
fig = plt.figure(figsize=(8,4), dpi=100)
#figsize - width and height in a tuple (inch unit sys)
#dpi - dot per inch (pixel per inch)

ax  = fig.add_axes([0.1,0.1,0.8,0.8])

#alpha for opacity, by default is 1
#alpha<1 for less opacity
ax.plot(x,x+1,color='#8B008B',alpha=1) 

plt.show(fig)

#save figure
# fig.savefig('filename.png',dpi=200) #we can save in different pixel format

#NOTE - in subplot we don't need to add axes, but in figure case, we need to add axes

###########################

#all possible lines
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')

# custom dash
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="blue", lw=1, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=1, ls='-', marker='s') #s for square
ax.plot(x, x+12, color="blue", lw=1, ls='--', marker='1') # 1 for some shape

# marker size and color
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")

plt.show(fig)

###########################

#range of axes

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3)
#set limit for x and y 
axes[2].set_xlim([2, 5])
axes[2].set_ylim([0, 60])
axes[2].set_title("custom axes range");

plt.show(fig)

###########################

#scatter plots
plt.scatter(x,y)
plt.show()

#draw histograms
from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data)
plt.show()

# rectangular box plot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data,vert=False,patch_artist=False)  
#vert for verticle or horizontal
#patch_artist for color fill
plt.show()