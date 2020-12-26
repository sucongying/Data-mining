import glob
import os
import pandas as pd
import numpy as np
#
#
#
#将所有数据显示，而不是有省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
#
#
#
# #直接合并数据源
# #读取两个数据源
# inputfile = "F:/wechat/WeChat Files/wxid_rf64u7wjcmqv12/FileStorage/File/2020-11/*.csv"
# outputfile = "F:/wechat/WeChat Files/wxid_rf64u7wjcmqv12/FileStorage/File/2020-11/result.csv"
# #用csv_list保存两个数据源
# csv_list = glob.glob(inputfile)
# #去除第二个数据源表头
# filepath = csv_list[0]
# df = pd.read_csv(filepath)
# df = df.to_csv(outputfile, index=False)
# for i in range(1, len(csv_list)):
#      filepath = csv_list[i]
#      df = pd.read_csv(filepath)
#      df = df.to_csv(outputfile, index=False, header=False, mode='a+')
# #print("合并完成")
#
#
#
# #读取合成的数据
# f="F:/wechat/WeChat Files/wxid_rf64u7wjcmqv12/FileStorage/File/2020-11/result.csv"
# df=pd.read_csv(f,header=0,encoding="gbk",engine='python')





##填充缺失值
# def fillackofvalue(xx,df):# #发现空值从另外一个数据源找到对应值并填充
#     xx_list=df[df[xx].isnull()].index.tolist()
#     for i in range(len(xx_list)):
#         for j in range(len(df)):
#             if df.Name[j] == df.Name[xx_list[i]] and j != xx_list:
#                 df.loc[df.index[xx_list[i]], xx] = df.loc[df.index[j], xx]
# def fillrest(df):
#     #填充剩下没有对照的数据，以平均值填充
#     df.loc[df.C3.isnull(), 'C3'] = 80
#     df.loc[df.C4.isnull(), 'C4'] = int(df.C4.mean() + 0.5)
#     df.loc[df.C5.isnull(), 'C5'] = int(df.C5.mean() + 0.5)
#     df.loc[df.Constitution.isnull(), 'Constitution'] = "general"
#
# fillackofvalue('C1',df)
# fillackofvalue('C2',df)
# fillackofvalue('C3',df)
# fillackofvalue('C4',df)
# fillackofvalue('C5',df)
# fillackofvalue('C6',df)
# fillackofvalue('C7',df)
# fillackofvalue('C8',df)
# fillackofvalue('C9',df)
# fillackofvalue('Constitution',df)
# fillackofvalue('Height',df)
# fillrest(df)
# # print(df)
#
#
#
# #print(df.isnull().sum())
# #
# #
# # #规范化ID号（六位，202打头,后面0添加以学号具体情况）、性别（male、female）、身高单位（cm）
# f1=r"F:\wechat\WeChat Files\wxid_rf64u7wjcmqv12\FileStorage\File\2020-11\data1.csv"
# df1=pd.read_csv(f1,header=0,encoding="gbk",engine='python')
# #print(df.info())
# for i in range(len(df1)):
# #由于之前合数据已经将ID的类型转为int64，所以直接将字符串202000转为int就可以直接相加
#     df.loc[df.index[i],'ID']=int('202000')+df.ID[i]
# #print(df)
# for i in range(len(df)):
##发现性别为boy就改为male，性别为girl改为female
#     if df.Gender[i]=="boy":
#         df.loc[df.index[i],'Gender']="male"
#     elif df.Gender[i]=="girl":
#         df.loc[df.index[i],'Gender']="female"
# #print(df.info())
# for i in range(len(df)):
##将单位都为米即身高都是小数都将它乘100使得单位变为厘米
#     if df.Height[i]<3.0:
#         df.loc[df.index[i],'Height']=df.Height[i]*100
# #print(df)
#
#
#
# #去重复值
# #print(df.loc[df.duplicated()])
# #print(df.duplicated().sum())
# df.drop_duplicates(inplace=True)  #将完全一样的数据直接删除
# df.sort_values(by='ID',ascending=True,inplace=True)   #按照ID升序排序，为之后重新定索引做准备
##观察数据发现有些人姓名及所有成绩都一样，要么性别不一样，要么ID不一样，完全就是一个人，所以下面在以ID为基准将同ID的随机删除
# df.drop_duplicates(subset=['ID'],keep='last',inplace=True)
# df.sort_values(by='ID',ascending=True,inplace=True)
# df.index=range(df.shape[0])   #重新建立索引
# #print(df)


#
#
# #导出数据
# # df.to_csv("result(washed).csv",index=False)


#读取已清洗的数据源
filepath=r"D:\python\result(washed).csv"
df=pd.read_csv(filepath,encoding="gbk",header=0,engine="python")
# print(df)


# 1.	学生中家乡在Beijing的所有课程的平均成绩。
# def courseaverage(xx):
##用来计算北京学生的平均成绩，不包括体育成绩
##xx代表传入的列名
#     xx_list=df.loc[df["City"]=="Beijing",xx].tolist() #先用xx_list列表存放传入数据
#     sum=0 #sum用来计算列表中所有数字总和
#     for i in xx_list:
#         sum+=i
#     average=sum/len(xx_list)  #average用来存平均成绩
#     print(xx+"平均成绩："+str(average))
# courseaverage("C1")
# courseaverage("C2")
# courseaverage("C3")
# courseaverage("C4")
# courseaverage("C5")
# courseaverage("C6")
# courseaverage("C7")
# courseaverage("C8")
# courseaverage("C9")


#2.	学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。
# quantity=0    ##学生数量quantity
# for i in range(len(df)):
#     if df.City[i]=="Guangzhou" and df.Gender[i]=="male" and df.C1[i]>=80 and df.C9[i]>=9.0:
#         #print(df.loc[df.index[i],:])
#         quantity+=1
# print("学生中家乡在广州，课程1在80分以上的男同学的数量为"+str(quantity))


# 3.	比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
##量化体育成绩（bad=60，general=75，good=85，excellent=95）
# GZ_score=0    #广州女学生体育总成绩
# GZ_sum=0  #广州女学生数量
# SH_score=0    #上海女学生体育总成绩
# SH_sum=0  #上海女学生数量

# for i in range(len(df)):
##量化广州女学生体育成绩
#     if df.City[i]=="Guangzhou" and df.Gender[i]=="female" and df.Constitution[i]=="bad":
#         GZ_score+=60
#         GZ_sum+=1
#     elif df.City[i]=="Guangzhou" and df.Gender[i]=="female" and df.Constitution[i]=="general":
#         GZ_score += 75
#         GZ_sum += 1
#     elif df.City[i] == "Guangzhou" and df.Gender[i] == "female" and df.Constitution[i] == "good":
#         GZ_score += 85
#         GZ_sum += 1
#     elif df.City[i] == "Guangzhou" and df.Gender[i] == "female" and df.Constitution[i] == "excellent":
#         GZ_score += 95
#         GZ_sum += 1
# for i in range(len(df)):
##量化上海女学生成绩
#     if df.City[i]=="Shanghai" and df.Gender[i]=="female" and df.Constitution[i]=="bad":
#         SH_score+=60
#         SH_sum+=1
#     elif df.City[i]=="Shanghai" and df.Gender[i]=="female" and df.Constitution[i]=="general":
#         SH_score += 75
#         SH_sum += 1
#     elif df.City[i] == "Shanghai" and df.Gender[i] == "female" and df.Constitution[i] == "good":
#         SH_score += 85
#         SH_sum += 1
#     elif df.City[i] == "Shanghai" and df.Gender[i] == "female" and df.Constitution[i] == "excellent":
#         SH_score += 95
#         SH_sum += 1
# GZ_average=GZ_score/GZ_sum    #广州女学生体育平均成绩
# SH_average=SH_score/SH_sum    #上海女学生体育平均成绩
# print("广州女学生体育总成绩="+str(GZ_score)+"\t广州女学生数量="+str(GZ_sum)+"\t广州女学生平均体育成绩"+str(GZ_average))
# print("上海女学生体育总成绩="+str(SH_score)+"\t上海女学生数量="+str(SH_sum)+"\t上海女学生平均体育成绩"+str(SH_average))
# if GZ_average<SH_average:
#     print("上海较强！")
# elif GZ_average==SH_average:
#     print("两地一样强！")
# else:
#     print("广州较强！")


# 4.	学习成绩和体能测试成绩，两者的相关性是多少？（九门课成绩分别与体能成绩计算相关性）
#量化体育成绩（bad=60，general=75，good=85，excellent=95）
# def averagecourse(x,num):#计算成绩平均数
#     x_sum = 0 #用来存放成绩总和
##由于体育成绩是字符串不是数，所以加判断来分辨要计算的是体育成绩还是学科成绩
#     if x!="Constitution":
#         for i in range(num):
#             x_sum+=df[x][i]
#     else:
##体育成绩量化
#         for i in range(len(df)):
#             if df[x][i] == "bad":
#                 x_sum += 60
#             elif df[x][i] == "general":
#                 x_sum += 75
#             elif df[x][i] == "good":
#                 x_sum += 85
#             elif df[x][i] == "excellent":
#                 x_sum += 95
#     return x_sum / num    #返回成绩平均值
#
# def covariance(x,y,num,a,b):#计算协方差
##运用公式cov（x，y）=E(xy）-E（x）E（y)，a表示学科成绩，b表示体育成绩，num表示学生数量
##
#     xy_sum = 0    #xy表示学习成绩和体育成绩相乘，xy_sum表示总和
#     for i in range(num):
#         if df[y][i] == "bad":
#             xy_sum += 60 * df[x][i]
#         elif df[y][i] == "general":
#             xy_sum += 75 * df[x][i]
#         elif df[y][i] == "good":
#             xy_sum += 85 * df[x][i]
#         elif df[y][i] == "excellent":
#             xy_sum += 95 * df[x][i]
#     xy_average=xy_sum/num #E（xy）
#     return xy_average-a*b #返回协方差
#
# def variance(x,num,average):#计算方差
#     x_sum=0   #x_sum表示学科成绩-学科成绩平均值（average）然后平方，最后所有项求和
#     if x!="Constitution":
#         for i in range(num):
#             x_sum += (df[x][i] - average) **2
#     else:
#         for i in range(num):
#             if df[x][i] == "bad":
#                 x_sum += (60 - average) **2
#             elif df[x][i] == "general":
#                 x_sum += (75 - average) **2
#             elif df[x][i] == "good":
#                 x_sum += (85 - average) **2
#             elif df[x][i] == "excellent":
#                 x_sum += (95 - average) **2
#     return x_sum / num    #返回方差
#
# def correlation(x,y):#计算相关系数
##运用公式r=cov（x，y）/（std（x）*std（y））
#     num=len(df)   #学生数量
#     x_average=averagecourse(x,num)
#     y_average=averagecourse(y,num)
#     x_var=variance(x,num,x_average)   #学科成绩方差
#     y_var=variance(y,num,y_average)   #体育成绩方差
#     Var=np.sqrt(x_var*y_var)  #学科成绩和体育成绩方差相乘后开方
#     covar=covariance(x,y,num,x_average,y_average) #协方差
#     return covar/Var  #返回相关系数
# #
# #
# #
# C1_r=correlation("C1","Constitution")
# print("课程C1和体育成绩Constitution这两者的相关系数："+str(C1_r))
# C2_r=correlation("C2","Constitution")
# print("课程C2和体育成绩Constitution这两者的相关系数："+str(C2_r))
# C3_r=correlation("C3","Constitution")
# print("课程C3和体育成绩Constitution这两者的相关系数："+str(C3_r))
# C4_r=correlation("C4","Constitution")
# print("课程C4和体育成绩Constitution这两者的相关系数："+str(C4_r))
# C5_r=correlation("C5","Constitution")
# print("课程C5和体育成绩Constitution这两者的相关系数："+str(C5_r))
# C6_r=correlation("C6","Constitution")
# print("课程C6和体育成绩Constitution这两者的相关系数："+str(C6_r))
# C7_r=correlation("C7","Constitution")
# print("课程C7和体育成绩Constitution这两者的相关系数："+str(C7_r))
# C8_r=correlation("C8","Constitution")
# print("课程C8和体育成绩Constitution这两者的相关系数："+str(C8_r))
# C9_r=correlation("C9","Constitution")
# print("课程C9和体育成绩Constitution这两者的相关系数："+str(C9_r))











