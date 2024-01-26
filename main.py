
import tkinter as tk
import cv2

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(text="Нажмите кнопку //Первоначальная обработка// для того, чтобы выделить объекты", font=("Arial", 12))
        self.label.pack()

        self.btn = tk.Button(self, text="Первоначальная обработка",
                             command=self.button1)

        self.btn2 = tk.Button(self, text="Вырезать",
                             command=self.button2, state=tk.DISABLED)

        self.btn.pack(padx=120, pady=30)
        self.btn2.pack(padx=120, pady=30)

    def button1(self):
        src = cv2.imread('bottles.jpg')
        thresh = 245
        maxValue = 255
        th, dst = cv2.threshold(src, int(thresh), int(maxValue), cv2.THRESH_BINARY)
        cv2.imwrite("Handfile.png", dst)

        self.label.config(text="Обработка завершена")
        self.btn2.config(state=tk.NORMAL)
        self.label2 = tk.Label(text="Нажмите кнопку для того, чтобы вырезать объекты", font=("Arial", 12))
        self.label2.pack()

    def button2(self):
        original_image = cv2.imread("bottles.jpg")
        image = cv2.imread("Handfile.png")
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
        image_copy = image.copy()
        for i in range(0, len(contours)):
            area = cv2.contourArea(contours[i])
            print(area)
            if(area < 20000 and area > 5000):
                x, y, w, h = cv2.boundingRect(contours[i])
                cropped_img = original_image[y:y + h, x:x + w]
                img_name = str(i) + ".jpg"
                cv2.imwrite(img_name, cropped_img)

        self.label2.config(text="Выполнено")


if __name__ == "__main__":
    app = App()
    app.title("textt")

    app.mainloop()


