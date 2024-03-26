from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

model = load_model('dog_cat_classifier.h5')

def classify_image(img_path):
    img = image.load_img(img_path, target_size=(500, 375))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    prediction = model.predict(x)
    print(prediction)
    if prediction < 0.5:
        print("Je to cici")
    else:
        print("Je to pejsek")

while True:
    image_path = input("Enter the image path: ")
    classify_image(image_path)
