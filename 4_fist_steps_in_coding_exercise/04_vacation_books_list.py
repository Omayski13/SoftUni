book_lists = int(input())
readed_lists_for_hour = float(input())
needed_days = int(input())

total_time_for_reading = book_lists // readed_lists_for_hour
needed_hours = total_time_for_reading // needed_days

print (needed_hours)