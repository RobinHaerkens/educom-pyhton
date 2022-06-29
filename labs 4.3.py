#lab 4.3.1.6
def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0 and year % 4 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
#Lab 4.3.1.7
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    x = is_year_leap(year)
    if x == True:
        month_days[1] = 29
        return month_days[month-1]
    if x == False:
        month_days[1] = 28
        return month_days[month-1]

#lab 4.3.1.8
def day_of_year(year, month, day):
    if year < 1582 or month > 12 or month < 1 or day > 31 or day < 1:
        print("Parameter error")
        return None

    total_days = 0
    for i in range(1,13):
        if i <= month:
            total_days +=days_in_month(year,i)   
    return total_days   

print(day_of_year(2000, 12, 31))


#lab 4.3.1.9
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()



#4.3.1.10
def liters_100km_to_miles_gallon(liters):
    miles = 100000/1608.344
    gallon_per_100km = liters/3.785311784
    gpm = miles/gallon_per_100km
    return gpm

def miles_gallon_to_liters_100km(miles):
    meters = 1608.344*miles
    liters_per_100km = (100000/meters)*3.785311784
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))