import pandas as pd
import matplotlib.pyplot as plt


# 初始化
def info():
    print('欢迎进入系统！')
    print('柱状图: a')
    print('饼状图: b')
    print('折线图: c')
    print('散点图: d')
    print('请选择功能，输入序号并回车确认')
    code = input()
    print('请输入文件路径（全称）')
    # path = 'D:/MyProject/PythonProject/robot/src/static/111.xlsx'
    fpath = input()
    if code == 'a':
        byBar(fpath)
    if code == 'b':
        byPie(fpath)
    if code == 'c':
        byArea(fpath)
    if code == 'd':
        byScatter(fpath)


# 柱状图
def byBar(fp):
    # item = pd.read_excel("file_drivers/基础数据.xlsx", skiprows=3, usecols="A:B")
    item = pd.read_excel(fp, skiprows=0, usecols="A:C")
    print(item)
    item.plot.bar(x='ID', y=['Name', 'Arg'], color=['orange', 'red'])
    # 标题
    plt.title('this is bar!', fontsize=16, fontweight='bold')
    # x轴标题
    plt.xlabel('ID_TEST', fontweight='bold')
    # y轴标题
    plt.ylabel('INFO_TEST', fontweight='bold')
    # 倾斜x轴上的标注
    ax = plt.gca()
    ax.set_xticklabels(item['ID'], rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# 饼状图
def byPie(fp):
    item = pd.read_excel(fp, skiprows=0, usecols="A:D", index_col='ID')
    print(item)
    # 逆时针
    item['Arg'].plot.pie(fontsize=8, startangle=-270)
    # 顺时针
    # item['Arg'].plot.pie(fontsize=8, counterclock=False, startangle=-270)
    # 标题
    plt.title('test_pie', fontsize=16, fontweight='bold')
    # 饼块标题
    plt.ylabel('Arg', fontsize=12, fontweight='bold')
    plt.show()


# 折线图
def byArea(fp):
    item = pd.read_excel(fp, skiprows=0, usecols="A:D", index_col='ID')
    print(item)
    print(item.columns)
    # 一条折线
    # item.plot(y='Arg')
    # 多条折线
    item.plot(y=['Name', 'Arg', 'Rank'])
    # 是否开启叠加
    # item.plot.area(y=['Name', 'Arg', 'Rank'])  # 折线
    # item.plot.bar(y=['Name', 'Arg', 'Rank'], stacked=True) #柱状

    # 标题
    plt.title('test_zxt', fontsize=16, fontweight='bold')
    # y轴标题
    plt.ylabel('Y', fontsize=12, fontweight='bold')
    # # x轴标题
    # plt.xticks(item.index, fontsize=8)
    plt.xlabel('X', fontsize=12, fontweight='bold')
    plt.show()


# 散点图
def byScatter(fp):
    item = pd.read_excel(fp, skiprows=0, usecols="A:D")
    print(item)
    item.plot.scatter(x='Arg', y='ID')
    plt.show()


# 功能测试
if __name__ == "__main__":
    path = 'static/111.xlsx'
    byBar(path)
    byPie(path)
    byArea(path)
    byScatter(path)
