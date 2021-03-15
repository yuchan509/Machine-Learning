# Modeling
import numpy as np 
import mglearn
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import warnings
warnings.simplefilter('ignore')

data_generator   = ImageDataGenerator( rescale=1./255 )
traingen         = data_generator.flow_from_directory("img",target_size=(98, 98), class_mode='sparse', batch_size=800)
x_train, y_train = traingen.next()  

x_reshape        = x_train.reshape(len(x_train), -1)  
model            = MLPClassifier( hidden_layer_sizes=(90, 22) ,verbose=1, tol=1e-6,  solver='lbfgs' )
print("Training...")
model.fit( x_reshape, y_train )
print("Finish")
print( f'Accuracy of model : {model.score( x_reshape, y_train )}' )

joblib.dump( model, 'Test.pkl' )