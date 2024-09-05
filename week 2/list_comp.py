# The casses for student is registered 
classes_registered = ['ITEC 1150','ITEC 1100', 'ENGL 1340', 'MATH 1100']

# Make a list for ITEC only
only_itec = [ c for c in classes_registered if c.startswith('ITEC')]
print(only_itec)

# Temperature every day. Record -1 if not possible to take measurement.
high_temps = [-1, 78, 72, 67, -1, 54, 78, 67, -1, 70 ]

# Make a list of only numbers that represent a valid temperature measurement
only_real_measurements = [ temp for temp in high_temps if temp != -1]
print(only_real_measurements)

temp_celsius = [ (temp_f - 32) * 5/9 for temp_f in only_real_measurements ]
print(temp_celsius)

average = sum(temp_celsius) / len(temp_celsius)
print(f'The average is {average:.2f}C')


numbers = [2,4,6]
plus_one = [ n+1 for n in numbers]
print(plus_one)


numbers = [0,9,0,3,4,6,5,2]
numbers_no_zeros = [n for n in numbers if n != 0]
print(numbers_no_zeros)

#we put the *2 to duplicate the number 
numbers = [0,10,4,0,32]
numbers_doubled_no_zeros = [n *2 for n in numbers if n !=0 ]