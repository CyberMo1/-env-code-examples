def average (values):
 return sum(values) / len(values)

# Running it on [72, 55, 101, 90]
data = [72, 55, 101, 90]
result = average(data)
print("Average:", result)

stations = [
    ["A1", 67], 
    ["B2", 82],
    ["C3", 97],
    ["D4", 130],
    ["E5", 146]
]
for station in stations:
    print(f"{station[0]} -> {station[1]}")

def report_status(stations, threshold=100):

   for station in stations:
       name, pm25 = station
       if pm25 > threshold:
           print (f"{name}: {pm25} exceeds threshold!") 
       else:
           print (f"{name}: {pm25} is within safe limits.")

report_status(stations, threshold=100)
