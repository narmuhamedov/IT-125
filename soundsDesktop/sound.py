import tkinter as tk
import pygame
import os

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abs_path(file):
    return os.path.join(BASE_DIR, file)

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def create_app():
    root = tk.Tk()
    root.title("Animal Sounds")
    root.geometry('300x250')
    root.resizable(False, False)

    tk.Button(root, text="Мышь", font=("Arial", 14),
              command=lambda: play_sound(abs_path("sounds/mouse.mp3"))).pack(pady=10)
    tk.Button(root, text="Кошка", font=("Arial", 14),
              command=lambda: play_sound(abs_path("sounds/cat.mp3"))).pack(pady=10)
    tk.Button(root, text="Собака", font=("Arial", 14),
              command=lambda: play_sound(abs_path("sounds/dog.mp3"))).pack(pady=10)

    root.mainloop()

create_app()
