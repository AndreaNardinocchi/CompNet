import os
 
def captureImagePath(path):
    print("Picture taken!!!\n")
    os.system(f"fswebcam --no-banner {path}")
        
if __name__ == "__main__":
    captureImagePath("./images/image.jpg")

