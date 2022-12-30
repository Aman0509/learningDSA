# Find number of days above average temperature


def above_avg_temp():
    try:
        num_of_days = int(input("Enter no. of days - "))
        days_temp = []
        for i in range(num_of_days):
            days_temp.append(float(input(f"Day's {i+1} temperature - ")))
        avg = sum(days_temp) / len(days_temp)
        c = [j for j in days_temp if j > avg]
        return avg, len(c)
    except (ValueError, ZeroDivisionError):
        return "Error!"


print(above_avg_temp())
