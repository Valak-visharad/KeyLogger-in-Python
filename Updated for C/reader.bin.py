import pickle
file=input('Enter the name of the file along address :')
with open(file,'rb+') as f:
    data=pickle.load(f)
    print(data)
