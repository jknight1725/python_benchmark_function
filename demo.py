def time_efficiency(func, *args):
    start_time = process_time()
    func(*args)
    end_time = process_time()
    return {
        'start': start_time,
        'end': end_time,
        'total': end_time - start_time
    }


def print_time_report(time):
    print(f"Starts at: {time['start']}\nEnds at: {time['end']}\nTime taken to execute the function: {time['total']}\n")
    
#Example function given to show syntax
def sum_up(large_num):
    return int((large_num * (large_num + 1)) / 2)
    

def prompt_for_num():
    return int(input("Enter a number: "))
    
print_time_report(time_efficiency(sum_up, prompt_for_num()))
