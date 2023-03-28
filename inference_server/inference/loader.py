import pickle


def load(filename: str):
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model
    #y_pred = loaded_model.predict(x_test)
    #result = loaded_model.score(x_test, y_test)