import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import TensorBoard

train_data_dir = "./train_data"
validation_data_dir = "./validation"

img_width, img_height = 500, 375

#randomizace dat, simulace vsehomozenho, at se model lepe uci
train_datagen = ImageDataGenerator(rescale=1./255,  # Pixely jsou 1/0 - binary scale
                                   shear_range=0.2,  # Random rozhozeni - simulace ruzneho pohledu
                                   zoom_range=0.2,  # Random zoom - ruzny pohled
                                   horizontal_flip=True)  # Random flipnuti - random pohled

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=32,  # Kolik fotek se procesuje v jednom treninku
    class_mode='binary'  # Binarni klasifikace - dog: 0, cat: 1
)

validation_generator = train_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=32,
    class_mode='binary'
)

print(train_generator.class_indices)  # Print labelu kategorii (dog: 0, cat: 1)
print(train_generator.samples)  # Print kolik fotek je na trenink
print(validation_generator.samples)  # Print kolik fotek je na validaci

#Convolutional Neural Network (CNN) model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3))) # prvni layer - filtry
model.add(MaxPooling2D((2, 2))) # dalsi layer - zmenseni fotek
model.add(Conv2D(64, (3, 3), activation='relu')) # dalsi layer - filtr dalsi
model.add(MaxPooling2D((2, 2))) # dalsi layer - zase zmenseni fotek
model.add(Flatten())  # dalsi layer - prevod na 1D vektor
model.add(Dense(128, activation='relu'))  # hidden layer - skryte layer NN
model.add(Dense(1, activation='sigmoid'))  # vystupni layer - sigmoid!!!!

log_dir = os.path.join("logs", "fit")  # logy, pro vizualizaci
tensorboard_callback = TensorBoard(log_dir=log_dir)

#Kompilace modelu
model.compile(loss='binary_crossentropy',
              optimizer='adam',  # optimalizace
              metrics=['accuracy'])  # Monitoring presnosti

#Trenink modelu
model.fit(train_generator,
          epochs=10,  # jak moc chceme mucit PC a jak moc presny vysledek chcem (vetsi cislo -> vetsi CBT pro PC ale lepsi vysledek)
          validation_data=validation_generator,
          callbacks=[tensorboard_callback])

#Ulozeni naseho milaska
model.save('dog_cat_classifier.h5')
