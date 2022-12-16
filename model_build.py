import pickle
import numpy as np

class ModelBuild:
    def __init__(self):
        self.model = pickle.load(open('model.pkl', 'rb'))

    def make_prediction(self, data):
        data = np.array(data)
        pred = self.model.predict(data.reshape(1,-1))
        return pred