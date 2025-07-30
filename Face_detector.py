

import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def capture_and_send_email():
    # Initialize the camera
    camera = cv2.VideoCapture(0)
    
    # Capture an image
    ret,img = camera.read()

    # Save the captured image
    image_path = 'FaceDetectedImage.jpg'
    cv2.imwrite(image_path, img)

    # Release the camera
    camera.release()

    # Perform face detection using Haar Cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Save the image with face detection bounding boxes
    cv2.imwrite(image_path, img)

    # Send the email
    send_email(image_path)

def send_email(image_path):
    # Email configuration
    sender_email = 'xxxxxxx@gmail.com'//put email of sender
    sender_password = 'yyyy kkkk nnnn llll'//enter senders password
    receiver_email = 'yyyyyyyy@gmail.com'//put email of receiver
    subject = 'Face Detection Alert'

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the image to the email
    with open(image_path, 'rb') as img_file:
        img_data = img_file.read()
        image = MIMEImage(img_data, name='FaceDetectedImage.jpg')
        msg.attach(image)

    # Connect to the email server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    

capture_and_send_email()  # This should align with the other code in the function
print("Face detected successfully and sended to the receiver Email")