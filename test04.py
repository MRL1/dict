#将列表 li = ["alex", "seven"] 转换成字典且字典的key按照 10 开始向后递增
li = ["alex", "seven"]
dic = {}
k = 10
for i in li:
    dic[k] = i
    k+=1
print(dic)