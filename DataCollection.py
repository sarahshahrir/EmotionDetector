import cv2 # import that takes pictures

# define our camera
# we define "0" bcs we are taking the 0th camera, as in 1st camera
cam = cv2.VideoCapture(0)

# define width and height
cam.set(3, 100) # 3 means width
cam.set(4, 100) # 4 means height

# define number of images per emotion
number_of_images = 10 # when you train your model, this number should be pretty high
current_images = 0
while current_images < number_of_images:
    ret, frame = cam.read(0) # take picture out of 0th camera
    cv2.imshow('frame', frame) # display for us pictures being taken
    cv2.imwrite(f'SurprisedImages/IMG_{current_images}.png', frame) # put pictures in folder

    if cv2.waitKey(20) == ord('q'):
        # every 20ms it checks what key you are pressing
        # if you are pressing 'q', it'll end the program
        break
    current_images += 1