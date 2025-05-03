import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg
import cv2

def display_house(house_id, df, folder='Train'):

    house_data = df.loc[df["House ID"] == house_id]
    if house_data.empty:
        print(f"House ID {house_id} Not Found")
        return
    
    num_bathrooms = house_data["Price"].values[0]
    filename = f"{house_id}.jpg"
    img_path = os.path.join(folder, filename)
    
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        return
    
    img = mpimg.imread(img_path)
    height, width, _ = img.shape
    

    plt.figure(figsize=(12,12))
    plt.imshow(img)
    plt.title(f"House ID: {house_id} - Price: ${num_bathrooms}", fontsize=14)
    plt.axis('off')
    
    plt.axvline(x=width/2, color='white', linewidth=2)
    plt.axhline(y=height/2, color='white', linewidth=2)

    plt.text(width*0.25, height*0.05, "Bathroom",
             color='white', fontsize=12, ha='center', va='top',
             bbox=dict(facecolor='black', alpha=0.5))
    plt.text(width*0.75, height*0.05, "Bedroom",
             color='white', fontsize=12, ha='center', va='top',
             bbox=dict(facecolor='black', alpha=0.5))
    plt.text(width*0.25, height*0.55, "Kitchen",
             color='white', fontsize=12, ha='center', va='top',
             bbox=dict(facecolor='black', alpha=0.5))
    plt.text(width*0.75, height*0.55, "Front view",
             color='white', fontsize=12, ha='center', va='top',
             bbox=dict(facecolor='black', alpha=0.5))

    plt.show()
    
def load_and_preprocess_image(house_id, folder='Train', img_size=(224, 224)):

    filename = f"{house_id}.jpg"
    path = os.path.join(folder, filename)
    
    img = cv2.imread(path)               
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, img_size)
    img = img / 255.0
    return img
