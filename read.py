data = []
count = 0
with open('reviews.txt', 'r') as file:
	for line in file:
		data.append(line)
		count = count + 1 
		if count % 100000 == 0:
			print(len(data))
print('readin finished, total is', len(data), 'of comments')
print('---------')
print(data[0])
print('---------')
print(data[1])

sum_len = 0
for singal_character in data:
	sum_len = sum_len + len(singal_character)
print('the average of words is', sum_len/len(data))
