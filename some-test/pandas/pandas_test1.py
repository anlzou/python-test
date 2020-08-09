#
# @Date        : 2020-08-09 11:42:30
# @LastEditors : anlzou
# @Github      : https://github.com/anlzou
# @LastEditTime: 2020-08-09 12:00:19
# @FilePath    : \python\some-test\pandas\pandas_test1.py
# @Describe    :
#
import pandas as pd
from pandas import Series, DataFrame

'''
# 假设粘贴板内容为一下数据：
Sep	2018	Sep.1	2017	Change	Programming	Language	Ratings	Change.1
0	0	1	1	NaN	Java	17.436%	+4.75%	NaN	NaN
1	1	2	2	NaN	C	15.447%	+8.06%	NaN	NaN
2	2	3	5	change	Python	7.653%	+4.67%	NaN	NaN
3	3	4	3	change	C++	7.394%	+1.83%	NaN	NaN
4	4	5	8	change	Visual	Basic	.NET	5.308%	+3.33%
5	5	6	4	change	C#	3.295%	-1.48%	NaN	NaN
6	6	7	6	change	PHP	2.775%	+0.57%	NaN	NaN
7	7	8	7	change	JavaScript	2.131%	+0.11%	NaN	NaN
8	8	9	-	change	SQL	2.062%	+2.06%	NaN	NaN
9	9	10	18	change	Objective-C	1.509%	+0.00%	NaN	NaN
'''


# 获取粘贴版的内容
pb = pd.read_clipboard()
# print(pb)

# print(type(pb))

# 读取索引，该操作作用很大，可以读取行的索引，以此可以通过该索引进行访问
# print(pb.columns)

# 通过标签获取内容
# print(pb.Ratings)
