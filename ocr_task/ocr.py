import easyocr
import cv2
import re


reader = easyocr.Reader(['en'])

images = ["images/img1.jpg", "images/img2.jpg", "images/img3.png"]

pattern = r'[A-Z]{4}\d{6,7}' 

for img_path in images:
    img = cv2.imread(img_path)
    texts = reader.readtext(img, detail=0)

    combined = "".join(texts).upper()     
    combined = re.sub(r'[^A-Z0-9]', '', combined) 

    match = re.search(pattern, combined)
    
    print(f"\nImage: {img_path}")
    if match:
        print("Номер контейнера:", match.group())
    else:
        print("Номер не найден")