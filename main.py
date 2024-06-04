from datetime import datetime, timedelta

# Define the values
regular_hour_value = float(input("Enter the value per regular hour: "))  # Value per regular hour
overtime_hour_value = regular_hour_value * 1.25  # Value per overtime hour

def calculate_salary(start_times, end_times, regular_hour_value, overtime_hour_value):
    total_regular_hours = 0
    total_overtime_hours = 0
    total_salary = 0

    for start_time, end_time in zip(start_times, end_times):
        # Convert start and end times to datetime objects
        start_time = datetime.strptime(start_time, "%H:%M")
        end_time = datetime.strptime(end_time, "%H:%M")

        # Calculate the total hours worked for each day, including a 1-hour lunch break
        total_hours = (end_time - start_time - timedelta(hours=1)).total_seconds() / 3600

        # Calculate the regular hours
        regular_hours = min(total_hours, 8)

        # Calculate the overtime hours (between 22:30 and 5:30)
        overtime_start = datetime.strptime("22:30", "%H:%M")
        overtime_end = datetime.strptime("05:30", "%H:%M") + timedelta(days=1)
        if start_time < overtime_start and end_time > overtime_end:
            overtime_hours = 8
        elif start_time < overtime_start:
            overtime_hours = min((overtime_start - start_time).total_seconds() / 3600, total_hours - regular_hours)
        elif end_time > overtime_end:
            overtime_hours = min((end_time - overtime_end).total_seconds() / 3600, total_hours - regular_hours)
        else:
            overtime_hours = 0

        # Update totals
        total_regular_hours += regular_hours
        total_overtime_hours += overtime_hours
        total_salary += (regular_hours * regular_hour_value) + (overtime_hours * overtime_hour_value)

    return total_regular_hours, total_overtime_hours, total_salary

# Example usage
num_days = int(input("Enter the number of workdays: "))
start_times = []
end_times = []

# Loop to get the start and end times for each workday
for day in range(num_days):
    start_time = input(f"Enter the start time of workday {day+1} (HH:MM): ")
    end_time = input(f"Enter the end time of workday {day+1} (HH:MM): ")

    # Add the start and end times to the workdays list
    start_times.append(start_time)
    end_times.append(end_time)

regular_hours, overtime_hours, total_salary = calculate_salary(start_times, end_times, regular_hour_value, overtime_hour_value)

print(f"Total Regular Hours: {regular_hours}")
print(f"Total Overtime Hours: {overtime_hours}")
print(f"Total Salary: {total_salary}")




