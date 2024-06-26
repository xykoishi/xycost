#!/usr/bin/env python
# coding: utf-8

# In[19]:


from geojson import Point, Feature, FeatureCollection, dump
import csv
    

# In[20]:


CsvFile = 'Mybills.csv'
GeojsonFile = 'Mybills.geojson'

path = '/Users/koishi/Library/Mobile Documents/com~apple~CloudDocs/eCXY/家財管理/xycost/Data/'

# In[21]:


# Generate the intermid file for checking
fo_csv = open(path+CsvFile, 'r', encoding='utf-8')
PointsData = csv.DictReader(fo_csv)

# Generate the final Geojson file
fo_csv = open(path+CsvFile, 'r', encoding='utf-8')   # 还要再写一次，否则下面的程序运行后输出为空，why？
PointsData = csv.DictReader(fo_csv)

ft_all = []
for i, p in enumerate(PointsData):
    lat, lon = p['纬度'], p['经度']
    ft = Feature(geometry = Point((float(lon), float(lat),)),
         properties = {'year': int(p['年']), 'month': int(p['月']), 'day': int(p['日']),
                        #'marker-size': 'medium','marker-symbol': ''
                        })
    ft_all.append(ft)
ft_colct = FeatureCollection(ft_all)

with open(path+GeojsonFile, 'w') as fw_g:
    dump(ft_colct, fw_g, indent=2)
fw_g.close()
fo_csv.close()

