import pandas as pd
import matplotlib.pyplot as plt


def crateFile():
    # 简单入门
    # df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tom', 'Nick', 'six']})
    # df = df.set_index("ID")
    # df.to_excel("file_drivers/1.xlsx")
    # 进阶
    ids = [1, 2, 3]
    l1 = [1, 2, 3]
    l2 = [10, 20, 30]
    l3 = [100, 200, 300]
    s1 = pd.Series(l1, index=ids, name="A")
    s2 = pd.Series(l2, index=ids, name="B")
    s3 = pd.Series(l3, index=ids, name="C")
    # 以列的形式加入
    print("以列的形式加入")
    df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
    print(df)
    # 以行的形式加入
    print("以行的形式加入")
    df = pd.DataFrame([s1, s2, s3])
    print(df)
    print("crated sussry!")


def readFile():
    # 从第一行读取
    # item = pd.read_excel("file_drivers/统计算法模板：21年7月 传图规律.xlsx", header=0)
    # 定义开始读取的行与列
    item = pd.read_excel("file_drivers/统计算法模板：21年7月 传图规律.xlsx", skiprows=3, usecols="B:JF",
                         dtype={'观察号码': str})
    print(item.shape)
    print(item)
    # print(item.columns)
    # # 前三行
    # print(item.head(3))
    # # 尾三行
    # print(item.tail(3))


# 柱状图
def _bar():
    # item = pd.read_excel("file_drivers/基础数据.xlsx", skiprows=3, usecols="A:B")
    item = pd.read_excel("file_drivers/111.xlsx", skiprows=0, usecols="A:C")
    print(item)
    # item.plot.bar(x='商户名称', y='2020-11-05 00:00:00', title=' 柱状图')
    # item.plot.bar(x='ID', y='Name', title='this is bar!')
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
def _pie():
    item = pd.read_excel("file_drivers/111.xlsx", skiprows=0, usecols="A:D", index_col='ID')
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
def _zxt():
    item = pd.read_excel("file_drivers/111.xlsx", skiprows=0, usecols="A:D", index_col='ID')
    print(item)
    print(item.columns)
    # 一条折线
    # item.plot(y='Arg')
    # 多条折线
    # item.plot(y=['Name', 'Arg', 'Rank'])
    # 是否开启叠加
    # item.plot.area(y=['Name', 'Arg', 'Rank']) #折线
    item.plot.bar(y=['Name', 'Arg', 'Rank'], stacked=True) #柱状

    # 标题
    plt.title('test_zxt', fontsize=16, fontweight='bold')
    # y轴标题
    plt.ylabel('Y', fontsize=12, fontweight='bold')
    # # x轴标题
    # plt.xticks(item.index, fontsize=8)
    plt.xlabel('X', fontsize=12, fontweight='bold')
    plt.show()


# 散点图
def _sdt():
    item = pd.read_excel("file_drivers/111.xlsx", skiprows=0, usecols="A:D")
    print(item)
    item.plot.scatter(x='Arg', y='ID')
    plt.show()


if __name__ == "__main__":
    # crateFile()
    # readFile()
    # _bar()
    # _pie()
    # _zxt()
    _sdt()