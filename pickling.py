import pickle
def save():
    bipin={'key':'bipin','name':'bipin kumar','age':90}
    pramod={'key':'pramod','name':'pramod kumar','age':80}

    db={}
    db['bipin']=bipin
    db['pramod']=pramod

    f=open('xyz.txt',"ab")
    pickle.dump(db,f)
    f.close()
def load():
    f=open('xyz.txt','rb')
    db=pickle.load(f)
    for key in db:
        print(key,':',db[key])
        f.close()
save()
load()



