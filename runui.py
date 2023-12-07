import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class SignLanguageDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language Detector")

        # UI Components
        self.image_label = tk.Label(self.root)
        self.image_label.pack(padx=10, pady=10)

        self.select_button = tk.Button(self.root, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=10)

        self.detect_button = tk.Button(self.root, text="Detect Sign Language", command=self.detect_sign_language)
        self.detect_button.pack(pady=10)

        # OpenCV variables
        self.video_capture = cv2.VideoCapture(0)  # 0 corresponds to the default camera
        self.update()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo

    def detect_sign_language(self):
        # Replace this command with your YOLOv5 detection command
        # Example: subprocess.run(["python", "detect.py", "--source", "your_input.jpg", "--weights", "your_model.pt"])
             run(["python3", "detect.py", "--source", "0", "--weights", "runs/train/exp6/weights/best.pt"])
       

    def update(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame = frame.resize((300, 300), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(frame)

            self.image_label.config(image=photo)
            self.image_label.image = photo

            self.root.after(30, self.update)  # Update frames every 30 milliseconds

if __name__ == "__main__":
    root = tk.Tk()
    app = SignLanguageDetectorApp(root)
    root.mainloop()
