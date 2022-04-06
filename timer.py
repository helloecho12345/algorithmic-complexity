import time 

def bubble_sort(lst):
    length = len(lst)
    for i in range(length):
        for j in range(length - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                print(lst)
    print(lst)


# num_list = [34, 2, 76, 0, -1, 200]
num_list = [i for i in range(1000)]

def timer(algo, data):
	before = time.perf_counter()
	algo(data)
	after = time.perf_counter()
	total = after - before
	return total

print(timer(bubble_sort, num_list))
