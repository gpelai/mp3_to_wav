import tkinter as tk
from tkinter import Tk, filedialog, messagebox
import os

class Menu:
    def __init__(self):
        self.root = Tk()

    def select_folder(self, alert:str):
        try:
            self.alert(alert)
            self.root.withdraw()
            folder_path = filedialog.askdirectory(title="Select folder")
            return folder_path
        except Exception as e:
            print(f"[WARNING] {e}")
            return None
        
    def get_files(self, folder_path:str):
        files_list = []

        try:
            for file in os.listdir(folder_path):
                files_list.append(os.path.join(folder_path, file))
            return files_list
        except Exception as e:
            print(f"[WARNING] {e}")
            return None
        
    def alert(self, alert:str):
        try:
            messagebox.showinfo("Info", alert)
        except Exception as e:
            print(f"[WARNING] {e}")
            return None