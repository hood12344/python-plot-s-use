import matplotlib.pyplot as plt # 匯入matplotlib 的pyplot 類別，並設定為plt
from matplotlib.font_manager import FontProperties # 中文字體
import matplotlib.image as mpimg

測試by Dong
# 換成中文的字體
# plt.rcParams['font.新細明體'] = ['SimSun'] # 步驟一（替換sans-serif字型）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）


img=mpimg.imread('python.png')
plt.imshow(img,extent=[0,6, 0, 400], aspect='auto')

list1=[[260,282,288,261,173,204,325],
      [483,474,462,526,370,466,619],
      [582,493,504,492,389,527,561]]
plt.plot(["07-13", "07-14", "07-15", "07-16", "07-17", "07-18", "07-19"], list1[0],"b--",label='八德')
plt.plot(["07-13", "07-14", "07-15", "07-16", "07-17", "07-18", "07-19"], list1[1],"r--",label='中壢')
plt.plot(["07-13", "07-14", "07-15", "07-16", "07-17", "07-18", "07-19"], list1[2],"y--",label="桃園")
plt.legend(loc='upper left')         # 自動改變顯示的位置

y=0
while y<len(list1):
    x=1
    list2=list1[y]
    while x<len(list2):
        plt.text(x, list2[x]+10, list2[x])
        x=x+1
    y=y+1



plt.title("桃園市 八德區,中壢區,桃園區 單日確診人數(近7日)")
plt.ylabel('單日新增確診人數') # 顯示Y 座標的文字
plt.xlabel('日期') # 顯示Y 座標的文字


#plt.text(70, 10, 'Hello! powenko.com')
#plt.text(70, 10, 'Hello! powenko.com')

plt.savefig('myyyy.png')

plt.show() # 繪製