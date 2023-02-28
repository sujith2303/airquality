'''
import keras
import numpy as np
X = np.array(list(range(700))).reshape(-1,7)
y = np.array(list(range(0,200,2)))
model = keras.Sequential(
    [
        keras.Input(shape=(7,)),
        keras.layers.Dense(1, activation="sigmoid"),
    ]
)
model.compile(loss="binary_crossentropy")
model.fit(X, y, batch_size=3, epochs=5, validation_split=0.2)

print(model.summary())
model.save('model.h5')

'''


import numpy as np
from keras.models import load_model 

def pre(array):
    print('Working')
    print(array)
    model = load_model('model.h5')
    print(model.summary())
    array = np.expand_dims(array,axis = 0)
    return model.predict(array)


model = load_model('model.h5')
array = np.array([1,2,3,4,5,6,7])
response =  model.predict(np.expand_dims(array,axis=0))
print(response)
