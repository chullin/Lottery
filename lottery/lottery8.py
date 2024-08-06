import tkinter as tk
from tkinter import messagebox, font

class LotteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("抽籤應用程式")
        
        # 定義視窗寬高變數
        self.weight = 700
        self.height = 300
        
        self.root.geometry(f"{self.weight}x{self.height}")

        self.entries = []
        self.results = []  # 保存抽籤結果

        # 設置字體
        self.font = font.Font(size=16)
        self.font2 = font.Font(size=25)

        # 工號框架
        self.frame_id = tk.Frame(root)
        self.frame_id.pack(pady=5)
        
        # 姓名框架
        self.frame_name = tk.Frame(root)
        self.frame_name.pack(pady=5)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.load_button = tk.Button(self.button_frame, text="載入資料", font=self.font, command=self.reload_from_file)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.label_selected = tk.Label(root, text="", font=self.font)
        self.label_selected.pack(pady=20)

        # 抽籤按鈕框架
        self.action_button_frame = tk.Frame(root)
        self.action_button_frame.pack(pady=(0, 10))  # 顶部和按钮之间的距离

        self.draw_button = tk.Button(self.action_button_frame, text="抽籤", font=self.font, command=self.draw_lottery)
        self.draw_button.pack(pady=5)

        # 結果字體按鈕框架
        self.font_button_frame = tk.Frame(root)
        self.font_button_frame.pack(pady=(0, 20))  # 底部和按钮之间的距离

        self.enlarge_button = tk.Button(self.font_button_frame, text="結果字體放大", font=self.font, command=self.enlarge_font)
        self.enlarge_button.pack(side=tk.LEFT, padx=5)

        self.shrink_button = tk.Button(self.font_button_frame, text="結果字體縮小", font=self.font, command=self.shrink_font)
        self.shrink_button.pack(side=tk.LEFT, padx=5)

        # self.save_button = tk.Button(root, text="保存結果", font=self.font, command=self.save_results)
        # self.save_button.pack(padx=5)

    def draw_lottery(self):
        if self.entries:
            import random
            selected = random.choice(self.entries)
            self.entries.remove(selected)
            self.results.append(selected)
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

    def enlarge_font(self):
        current_size = self.font2.actual()['size']
        if current_size + 5 <= 50:  # 设置一个上限，避免字体过大
            self.font2.configure(size=current_size + 5)
            self.weight += 50
            self.height += 5
            self.root.geometry(f"{self.weight}x{self.height}")

    def shrink_font(self):
        current_size = self.font2.actual()['size']
        if current_size - 5 >= 10:  # 设置一个下限，避免字体过小
            self.font2.configure(size=current_size - 5)
            self.weight -= 50
            self.height -= 5
            self.root.geometry(f"{self.weight}x{self.height}")

    def save_results(self):
        try:
            with open("Results.txt", "w", encoding="utf-8") as file:
                for result in self.results:
                    file.write(f"{result[0]}\t{result[1]}\n")
            messagebox.showinfo("保存成功", "結果已成功保存到 Results.txt")
            self.results = [] # 保存成功后清空抽籤結果
        except Exception as e:
            messagebox.showerror("保存錯誤", f"無法保存結果：{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryApp(root)
    root.mainloop()
