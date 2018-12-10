# 请循环输出所有的key
d={'k1': "v1", "k2": "v2", "k3": [11,22,33]}
for k,v in d.items():
    print(k)
print()
for k in d.keys():
    print(k)
print('*'*40)
#请循环输出所有的value
for v in  d.values():
    print(v)
for k,v in d.items():
    print(v)

print('*'*40)
#请循环输出所有的key和value
for k in  d.keys():
    print(k ,':', d[k])
for k,v in d.items():
    print(k,':',v)