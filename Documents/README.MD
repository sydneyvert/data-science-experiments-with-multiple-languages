# [Save and load variables in python](http://www.jessicayung.com/how-to-use-pickle-to-save-and-load-variables-in-python/)
## Save
    import pickle
    with open('../data/data.pickle', 'wb') as f:
      pickle.dump(data, f)
## Load
    import pickle
    with open('../data/data.pickle', 'rb') as f:
      data = pickle.load(f)
