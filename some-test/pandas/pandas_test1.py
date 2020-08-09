#
# @Date        : 2020-08-09 11:42:30
# @LastEditors : anlzou
# @Github      : https://github.com/anlzou
# @LastEditTime: 2020-08-09 11:43:01
# @FilePath    : \python\some-test\pandas\pandas_test1.py
# @Describe    :
#
import pandas as pd

##############################
# 获取粘贴版的内容
##############################
pb = pd.read_clipboard()
print(pb)
