import cv2

# Get a list of the available pre-trained models for the Darknet framework
models = cv2.dnn.NMSBoxes([],[0],[0], "dn")

# Print the list of available models
print('Available models:')
for model in models:
    print(model)