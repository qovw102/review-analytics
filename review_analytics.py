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

world_count = {}
for d in data:
    words = d.strip().split()
    #print(words)
    for word in words:
        if word in world_count:
            world_count[word] += 1
        else:
            world_count[word] = 1

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

for word in world_count:
    if world_count[word] > 1000000:
        print(word, world_count[word])

while True:
    word = input('please enter keyword: ')
    if word == 'q':
        print('離開')
        break
    if word in world_count:
        print(word, '出現過次數:', world_count[word])
    else:
        print('這個字未出現過!')

