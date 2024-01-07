months = input ("Enter months: ")
days = input ("Enter days: ")
days_total = int(months)*30 + int(days)
days_left = 360 - (days_total)

result = f"The remaining days is {days_left}."
print (result)
