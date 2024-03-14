n = int(input())
l = []
min_num = '1'
max_num = '9'

for i in range(1,len(str(n))):
    l.append((int(max_num)-int(min_num)+1)*i)
    min_num += '0'
    max_num += '9'

res = sum(l) + (n-int(min_num)+1)*len(str(n))
print(res)
