def average(array):
    distinct_heights = set(arr)  
    avg = sum(distinct_heights) / len(distinct_heights)  
    return round(avg, 3)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)