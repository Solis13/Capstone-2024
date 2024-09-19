numbers = ['one','two','three']

try:
    with open('numbers.txt', 'a') as number_file:
        for n in numbers:
          number_file.write(n + '\n')

except OSError:
   print('Error writing to file.')
