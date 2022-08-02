# python-plot-s-use
python 製作圖表

import matplotlib.pyplot as plt
#Matplotlib 中文標籤
plt.rcParams['font.sans-serif']=['SimSun']
plt.rcParams['axes.unicode_minus']=False
#定義各區的確診人數
day=["7/14","7/15", "7/16", "7/17", "7/18",] #X軸上的值
Taipei=["2457","2266", "2355", "1577", "2778",]#台北的確診人數
Neihu=["312","324", "316", "203", "305",]#內湖區的確診人數
Shilin=["243","241", "283", "193", "285",]#士林區的確診人數
Datong=["98","93", "108", "79", "115",]#大同區的確診人數

#製作圖表 plot
plt.title("7/14~7/18台北及台北各區之確診人數")
plt.plot(day, Taipei, 'r--', label='台北')
plt.plot( day, Neihu, 'b', label='內湖')
plt.plot( day, Shilin, 'g^', label='士林')
plt.plot( day, Datong, 'k:', label='大同')
#X軸的標籤
plt.xlabel("日期")
#Y軸的標籤
plt.xlabel("人數")
plt.legend()#縮圖丟預設的右上

#製作圖表 subplot  s
fig, axs = plt.subplots(3, 1)
axs[0].plot(day,Neihu,"r")
axs[1].plot(day,Shilin,"b-")
axs[2].plot(day,Datong,"c-")
axs[0].title.set_text("內湖")
axs[1].title.set_text("士林")
axs[2].title.set_text("大同")


fig, axs = plt.subplots(3, 1)
axs[0].plot(day,Neihu,"r-")
axs[1].plot(day,Shilin,"b")
axs[2].plot(day,Datong,"c--")
axs[0].title.set_text("內湖")
axs[1].title.set_text("士林")
axs[2].title.set_text("大同")

plt.savefig("1.jpg")
plt.show()
