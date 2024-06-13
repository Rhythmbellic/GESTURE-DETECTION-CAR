import cv2
import numpy as np
import keyboard
import serial
from keras.models import load_model

# Load the model
model = load_model("keras2.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Reshape
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace 'COM9' with the actual serial port your Arduino is connected to
ser = serial.Serial('COM9', 9600, timeout=1)

def send_serial_data(data):
    ser.write(data.encode())

def predict_and_send(frame):
    # Convert the OpenCV BGR image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Resize the image to be at least 224x224 and then crop from the center
    size = (224, 224)
    image = cv2.resize(image, size, interpolation=cv2.INTER_LANCZOS4)

    # Turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predict the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence = np.max(prediction)

    # Plot the class name and confidence on the frame
    cv2.putText(frame, f'Prediction: {class_name}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Confidence: {confidence:.2f}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Send serial data based on the predicted class only if 'p' is pressed
    if keyboard.is_pressed('p'):
        if class_name == "1 s\n":
            move_forward()
        elif class_name == "2 w\n":
            move_backward()
        elif class_name == "3 d\n":
            turn_right()
        elif class_name == "4 a\n":
            turn_left()
        elif class_name == "0 spaxe\n":
            stop()

def move_forward():
    print("Moving forward")
    send_serial_data('F')

def move_backward():
    print("Moving backward")
    send_serial_data('B')

def turn_left():
    print("Turning left")
    send_serial_data('L')

def turn_right():
    print("Turning right")
    send_serial_data('R')

def stop():
    print("Stopping")
    send_serial_data('S')

cap = cv2.VideoCapture(0)

if __name__ == "__main__":
    try:
        while True:
            ret, frame = cap.read()

            # Perform prediction and display on the frame
            predict_and_send(frame)

            # Display the frame
            cv2.imshow('Prediction', frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        ser.close()
        cap.release()
        cv2.destroyAllWindows()
        print("Serial connection closed.")
