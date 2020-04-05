import matplotlib.pyplot as plt

'''
How to use:
1. All files you want to find should be stored in the data dir
2. Just the name of the file you wnat is need 
(ex: if the path of the file is "data/file.txt" you just need "file.txt"
if the path of the file is "data/date/file.txt" you need "data/file.txt")
3. The interval should be a number. This number can be an integer or a float
(it will be converted into a float)
'''

file_name = input('What file would you like to plot?: ')
interval = input('At what interval (in seconds) are you collecting data?: ')

f = open('data/' + file_name, 'r')
r = f.read()

y = r.split(',')

x = []
val = 0.0
for _ in range(len(y)):
    x.append(val)
    val += float(interval)

plt.plot(x, y)

x_label = 'Time (' + interval + ' s)'
plt.xlabel(x_label)

y_label = 'Analog Value'
plt.ylabel(y_label)

title = 'Plot of ' + file_name
plt.title(title)

save = input('Do you want to save the plot? (yes/no): ')
if save.lower() == 'yes' or save.lower() == 'y':
    save_dir = input('Where do you want this data to be stored?: ')
    plt.savefig(save_dir)

show = input('Do you want to show the plot? (yes/no): ')
if show.lower() == 'yes' or show.lower() == 'y':
    plt.show()
