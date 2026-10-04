import os
import glob
import numpy as np
from PIL import Image

def load_data_split(split_path):

    X_list = []
    y_list = []

    class_map = {"circles": 0, "squares": 1}

    for class_name, label in class_map.items():
        search_pattern = os.path.join(split_path, class_name, "*.png")

        #list containing the paths of all matching files
        file_paths = glob.glob(search_pattern) 

        for path in file_paths:
            img = Image.open(path).convert("L")
            img_array = np.array(img, dtype=np.float32)
            img_normalized = img_array / 255.0
            vector = img_normalized.flatten()   

            X_list.append(vector)
            y_list.append(label)

    
    X = np.array(X_list)
    y = np.array(y_list)

    indices = np.arange(len(y))
    np.random.seed(42)
    np.random.shuffle(indices)

    return X[indices], y[indices]

if __name__ == "__main__":
    X_train, y_train = load_data_split("dataset/train")
    X_test, y_test = load_data_split("dataset/test")

    print(f"X_train shape: {X_train.shape}  |  y_train shape: {y_train.shape}")
    print(f"X_test shape:  {X_test.shape}  |  y_test shape:  {y_test.shape}")
    print(f"Sample pixel range: Min = {X_train.min()}, Max = {X_train.max()}")
