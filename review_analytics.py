# review-analytics
data = []
#count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        #count += 1
        #if count % 10000 == 0:
        #    print(len(data))
print('檔案讀取結束共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('平均留言長度為:', sum_len/len(data))

new = []
counter_100 = 0
for s in data:
    if len(s) < 100:
        new.append(s)
        counter_100 += 1
print('共有', len(new), '筆資料字數少於100')