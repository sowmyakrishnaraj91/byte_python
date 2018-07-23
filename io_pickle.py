import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple','mango','carrot']

f = open(shoplistfile,'wb')
#print(type(f))
pickle.dump(shoplist,f)

f.close()

del shoplist


f = open(shoplistfile,'rb')

storedlist = pickle.load(f)

#print(f)

