import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master :tk.Tk):
        super().__init__(master)
        master.title("GUI Sample")
        master.geometry("400x400")
        
        # 実行内容
        self.grid()
        self.create_widget()

    # create_widgetメソッドの定義
    def create_widget(self):
        # label1
        self.label1 = tk.Label(self,text="ラベル１")
        self.label1.grid()

        # button1_text
        self.button1_text = tk.StringVar()
        self.button1_text.set("push")
        def button1_clicked():
            self.button1_text.set("pushed")
        
        # button1
        self.button1 = tk.Button(self,textvariable=self.button1_text,command=button1_clicked)
        self.button1.grid()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
