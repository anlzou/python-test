'''
    结果:error
    edge、ie无法查看
    chrome没有生成数据
'''

import browserhistory as bh
import pandas as pd
pd.DataFrame.from_dict(bh.get_browserhistory()['chrome']) #查看指定浏览器的记录
# bh.get_browserhistory()
bh.write_browserhistory_csv()