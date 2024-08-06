import tkinter as tk
from tkinter import messagebox, font

class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("抽籤應用程式")
        self.root.geometry("400x400")  # 設置視窗寬高為 400x400

        self.entries = []

        # 設置字體
        self.font = font.Font(size=16)

        # 工號框架
        self.frame_id = tk.Frame(root)
        self.frame_id.pack(pady=5)
        
        # self.label_id = tk.Label(self.frame_id, text="工號：", font=self.font)
        # self.label_id.pack(side=tk.LEFT)

        # self.entry_id = tk.Entry(self.frame_id, font=self.font)
        # self.entry_id.pack(side=tk.LEFT)
        
        # 姓名字框架
        self.frame_name = tk.Frame(root)
        self.frame_name.pack(pady=5)
        
        # self.label_name = tk.Label(self.frame_name, text="名字：", font=self.font)
        # self.label_name.pack(side=tk.LEFT)

        # self.entry_name = tk.Entry(self.frame_name, font=self.font)
        # self.entry_name.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # self.add_button = tk.Button(self.button_frame, text="手動添加內容", font=self.font, command=self.add_entry)
        # self.add_button.pack(side=tk.LEFT, padx=5)

        self.load_button = tk.Button(self.button_frame, text="載入資料", font=self.font, command=self.reload_from_file)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.label_selected = tk.Label(root, text="", font=self.font)
        self.label_selected.pack(pady=20)

        # self.delete_button = tk.Button(root, text="刪除選中的", font=self.font, command=self.delete_entry)
        # self.delete_button.pack(pady=5)

        self.draw_button = tk.Button(root, text="隨機選擇一個人", font=self.font, command=self.draw_lottery)
        self.draw_button.pack(pady=5)

    # def add_entry(self):
    #     employee_id = self.entry_id.get()
    #     employee_name = self.entry_name.get()
    #     if employee_id and employee_name:
    #         if (employee_id, employee_name) not in self.entries:
    #             self.entries.append((employee_id, employee_name))
    #             self.entry_id.delete(0, tk.END)
    #             self.entry_name.delete(0, tk.END)
    #         else:
    #             messagebox.showwarning("重複條目", "這個工號和名字已經存在")
    #     else:
    #         messagebox.showwarning("輸入錯誤", "請輸入工號和名字")

    # def delete_entry(self):
    #     selected = self.entries
    #     if selected:
    #         self.entries = []
    #         self.label_selected.config(text="")
    #     else:
    #         messagebox.showwarning("刪除錯誤", "沒有條目可刪除")

    def draw_lottery(self):
        if self.entries:
            import random
            selected = random.choice(self.entries)
            self.label_selected.config(text=f"抽中的人是：{selected[1]} ({selected[0]})")
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
