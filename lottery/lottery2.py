import tkinter as tk
from tkinter import messagebox, simpledialog, font

class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("抽籤應用程式")
        self.root.geometry("350x500")  # 設置視窗寬高為 400x400

        self.entries = []

        # 設置字體
        self.font = font.Font(size=16)

        # 工號框架
        self.frame_id = tk.Frame(root)
        self.frame_id.pack(pady=5)
        
        self.label_id = tk.Label(self.frame_id, text="工號：", font=self.font)
        self.label_id.pack(side=tk.LEFT)

        self.entry_id = tk.Entry(self.frame_id, font=self.font)
        self.entry_id.pack(side=tk.LEFT)
        
        # 姓名字框架
        self.frame_name = tk.Frame(root)
        self.frame_name.pack(pady=5)
        
        self.label_name = tk.Label(self.frame_name, text="名字：", font=self.font)
        self.label_name.pack(side=tk.LEFT)

        self.entry_name = tk.Entry(self.frame_name, font=self.font)
        self.entry_name.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.add_button = tk.Button(self.button_frame, text="添加", font=self.font, command=self.add_entry)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.load_button = tk.Button(self.button_frame, text="從檔案加載", font=self.font, command=self.load_from_file)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.listbox = tk.Listbox(root, font=self.font)
        self.listbox.pack(pady=5)

        self.delete_button = tk.Button(root, text="刪除選中的", font=self.font, command=self.delete_entry)
        self.delete_button.pack(pady=5)

        self.draw_button = tk.Button(root, text="隨機選擇一個人", font=self.font, command=self.draw_lottery)
        self.draw_button.pack(pady=5)

    def add_entry(self):
        employee_id = self.entry_id.get()
        employee_name = self.entry_name.get()
        if employee_id and employee_name:
            self.entries.append((employee_id, employee_name))
            self.listbox.insert(tk.END, f"{employee_id} - {employee_name}")
            self.entry_id.delete(0, tk.END)
            self.entry_name.delete(0, tk.END)
        else:
            messagebox.showwarning("輸入錯誤", "請輸入工號和名字")

    def delete_entry(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.listbox.delete(index)
            del self.entries[index]
        else:
            messagebox.showwarning("刪除錯誤", "請選擇要刪除的條目")

    def draw_lottery(self):
        if self.entries:
            import random
            selected = random.choice(self.entries)
            self.entries.remove(selected)
            self.update_listbox()
            messagebox.showinfo("抽籤結果", f"抽中的人是：{selected[1]} ({selected[0]})")
        else:
            messagebox.showwarning("抽籤錯誤", "沒有可選擇的人")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for entry in self.entries:
            self.listbox.insert(tk.END, f"{entry[0]} - {entry[1]}")

    def load_from_file(self):
        try:
            with open("data.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines[1:]:  # 跳過第一行（標題行）
                    employee_id, employee_name = line.strip().split("\t")
                    self.entries.append((employee_id, employee_name))
                    self.listbox.insert(tk.END, f"{employee_id} - {employee_name}")
            messagebox.showinfo("加載成功", "已成功從檔案加載數據")
        except Exception as e:
            messagebox.showerror("加載錯誤", f"無法從檔案加載數據：{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()
