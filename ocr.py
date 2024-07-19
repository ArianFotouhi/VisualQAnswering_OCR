import cv2
import easyocr
import numpy as np




def ocr_image(image_path):
    closeness = 70
    # Initialize the easyocr Reader
    reader = easyocr.Reader(['en'])

    # Load the image using OpenCV
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the image
    results = reader.readtext(gray_image)

    # Create a list to store the results
    output = []

    # Define a function to calculate distance between two boxes
    def calculate_distance(box1, box2):
        x1, y1 = box1
        x2, y2 = box2
        return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Loop through each detected text box to group close texts
    for i in range(len(results)):
        (bbox, text, _) = results[i]
        if text.strip():  # Check if text is not empty
            # Calculate the center of the bounding box
            x_center = (bbox[0][0] + bbox[2][0]) / 2
            y_center = (bbox[0][1] + bbox[2][1]) / 2

            # Find close texts
            close_texts = []
            for j in range(len(results)):
                if i != j and results[j][1].strip():  # Exclude the same box and empty text
                    other_bbox = results[j][0]
                    other_x_center = (other_bbox[0][0] + other_bbox[2][0]) / 2
                    other_y_center = (other_bbox[0][1] + other_bbox[2][1]) / 2
                    distance = calculate_distance((x_center, y_center), (other_x_center, other_y_center))
                    if distance < closeness:  
                        close_texts.append(results[j][1].strip())

            # Append the results
            output.append({
                'text': text,
                'close_texts': close_texts
            })
    
    
    print(output)
    return output


