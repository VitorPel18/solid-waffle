import tensorflow as tf 
import tensorflow_datasets as tfds 
from tensorflow import keras 
from keras import layers 
from keras import Sequential

(train_x, train_y), (test_x, test_y) = tf.keras.datasets.cats_vs_dogs.load_data()
train_x = train_x.astype("float32)") / 255.0
test_x = test_x.astype("float32") / 255.0 

train_x - train_x.reshape(-1, 224, 224, 1)
test_x = test_x.reshape(-1, 224, 224, 1)

model = keras.Sequential([
tf.keras.layers.Conv2d(filter=32, kernel=(5, 5), actvation="relu"),
tf.keras.layers.MaxPooling2D(pool_size=(2, 2), padding="valid")

                        ])