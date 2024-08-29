#How many class are you taking?
list_of_classes = []

while True:
    class_name = input ('Enter class name or press enter to stop')

    if class_name == '':
       break
    

    else :list_of_classes.append(class_name)

print(list_of_classes)
    