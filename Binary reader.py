from pickle import *

def read(file):
    try:
        with open(file,'rb') as file_obj:
            for i in range(10000):
                print(load(file_obj),end='\t')        
    except FileNotFoundError:
        print('Input file does not exist')
    except EOFError:
        print('\n\n........................END OF FILE...............')
    


#__Main__

file = input('Filename : ')
print(read(file))
input()
