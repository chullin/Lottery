import tkinter as tk
from tkinter import messagebox, font

class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("抽籤應用程式")
        self.root.geometry("500x200")  # 設置視窗寬高為 400x400

        self.entries = []

        # 設置字體
        self.font  = font.Font(size=16)
        self.font2 = font.Font(size=25)

        # 工號框架
        self.frame_id = tk.Frame(root)
        self.frame_id.pack(pady=5)
        
        # 姓名字框架
        self.frame_name = tk.Frame(root)
        self.frame_name.pack(pady=5)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.load_button = tk.Button(self.button_frame, text="載入資料", font=self.font, command=self.reload_from_file)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.label_selected = tk.Label(root, text="", font=self.font)
        self.label_selected.pack(pady=20)

        self.draw_button = tk.Button(root, text="抽籤", font=self.font, command=self.draw_lottery)
        self.draw_button.pack(pady=5)

    def draw_lottery(self):
        if self.entries:
            import random
            selected = random.choice(self.entries)
            self.entries.remove(selected)
            self.label_selected.config(text=f"抽中的人是：{selected[1]} ({selected[0]})", font=self.font2)
        else:
            messagebox.showwarning("抽籤錯誤", "沒有可選擇的人")

    def reload_from_file(self):
        try:
            with open("data.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                self.entries.clear()
                self.label_selected.config(text="")
                added_entries = 0
                for line in lines[:]:
                    employee_id, employee_name = line.strip().split("\t")
                    if (employee_id, employee_name) not in self.entries:
                        self.entries.append((employee_id, employee_name))
                        added_entries += 1
            if added_entries > 0:
                messagebox.showinfo("加載成功", f"已成功從檔案重新加載 {added_entries} 條新數據")
            else:
                messagebox.showinfo("加載結果", "檔案中沒有新數據被添加")
        except Exception as e:
            messagebox.showerror("加載錯誤", f"無法從檔案加載數據：{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()
