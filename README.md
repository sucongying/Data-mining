# Data-mining
| 技术| 说明|
| ---| ---|
| pd.set_option('display.max_columns', 1000) <br> pd.set_option('display.width', 1000) <br> pd.set_option('display.max_colwidth', 1000) <br> pd.set_option("display.max_columns",None) <br> pd.set_option("display.max_rows",None)| 将pandas读的文件数据全部显示，而不是部分显示|
| pd.read_csv(filepath)| 读csv文件 <br> 参数：filepath文件地址|
| pd.to_csv(outputfile, index=False)| 导出csv文件 <br> 参数：outputfile文件存放地址 <br> index索引值是否导出到文件，false表示否|
| pd.loc[pd.index[i],'ID']| pd.loc[]用来定位第几行第几列数据，pd.index[i]用来找第i+1行数据|
| pd.drop_duplicates(subset=['ID'],keep='last',inplace=True)| 删除重复行 <br> subset根据某一列重复来删除重复值 <br> keep重复是删除哪一个，默认删除第一个，last删除后一个 <br> inplace是否在生成副本做修改，true不生成|
| pd.sort_values(by='ID',ascending=True,inplace=True)| 根据值大小排序 <br> by按照某一列值排序 <br> ascending序列方向，true表示升序 <br> inplace是否在生成副本做修改，true不生成|
