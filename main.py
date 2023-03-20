# python3

def parallel_processing(n, m, data):

    finish_time = [0] * n
    result = []

    for i in range(m):

        min_finish_time = min(finish_time)
        min_thread_index = finish_time.index(min_finish_time)
        start_time = finish_time[min_thread_index]
        result.append((min_thread_index, start_time))
        finish_time[min_thread_index] += data[i]
    
    return result


def main():

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()