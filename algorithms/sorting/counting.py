import sys
import itertools

def dict_counter(n, nums):
    counts = dict()
    for i in range(n):
        counts[i] = 0
    for x in nums:
        counts[x] += 1
    return counts

def dict_data_counter(n, data):
    count_data = dict()
    for i in range(n):
        count_data[i] = []
    for k, v in data:
        count_data[k].append(v)
    return count_data

def cumulative_count(max_num, num_dict):
    counts = [0 for _ in range(max_num)]
    counts[0] = len(num_dict[0])
    for k, v in [(k, len(v)) for k, v in num_dict.items() if k is not 0]:
        counts[k] += v + counts[k - 1]
    return counts


if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        k, v = [x for x in input().split()]
        k = int(k)
        l.append((k,v))
    count_data = dict_data_counter(100, l)
    cumulative_count = cumulative_count(100, count_data)
    print(" ".join(str(x) for x in cumulative_count))

    #print(" ".join(itertools.chain.from_iterable([str(k)]*v for k, v in counter(n, [int(x) for x in input().split()]).items())))
