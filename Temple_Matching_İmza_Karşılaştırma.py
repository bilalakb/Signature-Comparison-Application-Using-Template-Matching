import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def compare_signatures(img1, img2):
    img1_resized = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
    result = cv2.matchTemplate(img1_resized, img2, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val

def open_file_dialog(title):
    file_path = filedialog.askopenfilename(
        initialdir=r"C:\python\imza\imza1.png",  # Burayı kendi kullanıcı adınıza göre güncelleyin
        filetypes=[("Image files", "*.png;*.jpg")],
        title=title
    )
    if file_path:
        print(f"Seçilen dosya: {file_path}")
    return file_path

def load_image(file_path, size=(300, 300)):
    if not file_path:
        raise ValueError("Dosya yolu belirtilmemiş!")
    img = cv2.imread(file_path)
    if img is None:
        raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized_img = cv2.resize(gray_img, size)
    return resized_img

def get_similarity_description(score):
    if score >= 0.9:
        return "Çok Benzer"
    elif score >= 0.7:
        return "Benzer"
    elif score >= 0.5:
        return "Orta Derece Benzerlik"
    elif score >= 0.3:
        return "Düşük Benzerlik"
    else:
        return "Çok Düşük Benzerlik"

def on_compare_button_click():
    if not (file_path1 and file_path2):
        messagebox.showwarning("Uyarı", "İki imza dosyası da seçilmelidir!")
        return

    try:
        img1 = load_image(file_path1)
        img2 = load_image(file_path2)
    except Exception as e:
        messagebox.showerror("Hata", str(e))
        return

    score = compare_signatures(img1, img2)
    description = get_similarity_description(score)

    result_label.config(text=f"Benzerlik Skoru: {score:.4f}")
    description_label.config(text=f"Açıklama: {description}")

    img1_display = ImageTk.PhotoImage(image=Image.fromarray(img1))
    img2_display = ImageTk.PhotoImage(image=Image.fromarray(img2))

    img1_label.config(image=img1_display)
    img1_label.image = img1_display
    img2_label.config(image=img2_display)
    img2_label.image = img2_display

def select_signature1():
    global file_path1
    file_path1 = open_file_dialog("İmza 1 Dosyasını Seçin")
    if file_path1:
        file_name = file_path1.split('/')[-1]
        sig1_label.config(text=f"İmza 1: {file_name}")

def select_signature2():
    global file_path2
    file_path2 = open_file_dialog("İmza 2 Dosyasını Seçin")
    if file_path2:
        file_name = file_path2.split('/')[-1]
        sig2_label.config(text=f"İmza 2: {file_name}")

file_path1 = None
file_path2 = None

# Tkinter arayüzü
root = tk.Tk()
root.title("İmza Karşılaştırma")
root.geometry("1000x800")  # Daha geniş pencere
root.configure(bg="#e0f7fa")  # Arka plan rengini belirle

# İmza seçim butonları
select_btn1 = tk.Button(root, text="İmza 1 Seç", command=select_signature1, bg="#00bcd4", fg="white", font=("Helvetica", 12, "bold"))
select_btn1.pack(pady=10)

sig1_label = tk.Label(root, text="İmza 1: Seçiniz", bg="#e0f7fa", font=("Helvetica", 12))
sig1_label.pack()

select_btn2 = tk.Button(root, text="İmza 2 Seç", command=select_signature2, bg="#00bcd4", fg="white", font=("Helvetica", 12, "bold"))
select_btn2.pack(pady=10)

sig2_label = tk.Label(root, text="İmza 2: Seçiniz", bg="#e0f7fa", font=("Helvetica", 12))
sig2_label.pack()

# Karşılaştırma butonu
compare_btn = tk.Button(root, text="İmzaları Karşılaştır", command=on_compare_button_click, bg="#ff5722", fg="white", font=("Helvetica", 14, "bold"))
compare_btn.pack(pady=20)

# Sonuç etiketi
result_label = tk.Label(root, text="Benzerlik Skoru: -", bg="#e0f7fa", font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

# Açıklama etiketi
description_label = tk.Label(root, text="Açıklama: -", bg="#e0f7fa", font=("Helvetica", 12))
description_label.pack(pady=10)

# İmza görüntüleri için etiketler
img1_label = tk.Label(root, bg="#e0f7fa")
img1_label.pack(side=tk.LEFT, padx=20)

img2_label = tk.Label(root, bg="#e0f7fa")
img2_label.pack(side=tk.RIGHT, padx=20)

root.mainloop()
