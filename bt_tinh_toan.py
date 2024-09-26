import tkinter as tk
from tkinter import ttk

# Tạo lớp Calculator để thực hiện các phép tính
class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0

    def set_values(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Không thể chia cho 0"

# Tạo đối tượng Calculator
calc = Calculator()

# Hàm để lấy giá trị nhập và tính toán dựa trên thao tác
def calculate(operation):
    a_value = a_input.get()
    b_value = b_input.get()
    
    # Đặt các giá trị cho calculator
    calc.set_values(a_value, b_value)
    
    # Xử lý phép tính dựa trên thao tác
    if operation == "add":
        result = calc.addition()
    elif operation == "subtract":
        result = calc.subtraction()
    elif operation == "multiply":
        result = calc.multiplication()
    elif operation == "divide":
        result = calc.division()
    
    # Hiển thị kết quả
    kq_input.set(f"{result}")

# Tạo cửa sổ chính
win = tk.Tk()

# Nhãn và ô nhập cho 'a'
a_label = ttk.Label(win, text="a: ")
a_label.grid(column=0, row=0)
a_input = tk.StringVar()
a_in = ttk.Entry(win, width=12, textvariable=a_input)
a_in.grid(column=1, row=0)

# Nhãn và ô nhập cho 'b'
b_label = ttk.Label(win, text="b: ")
b_label.grid(column=0, row=1)
b_input = tk.StringVar()
b_in = ttk.Entry(win, width=12, textvariable=b_input)
b_in.grid(column=1, row=1)

# Nút để thực hiện các phép tính
btn_add = ttk.Button(win, text="Cộng", command=lambda: calculate("add"))
btn_add.grid(column=2, row=0)

btn_subtract = ttk.Button(win, text="Trừ", command=lambda: calculate("subtract"))
btn_subtract.grid(column=2, row=1)

btn_multiply = ttk.Button(win, text="Nhân", command=lambda: calculate("multiply"))
btn_multiply.grid(column=2, row=2)

btn_divide = ttk.Button(win, text="Chia", command=lambda: calculate("divide"))
btn_divide.grid(column=2, row=3)

# Nhãn và ô nhập cho kết quả
kq_label = ttk.Label(win, text="Kết quả: ")
kq_label.grid(column=0, row=4)
kq_input = tk.StringVar()
kq_in = ttk.Entry(win, width=12, textvariable=kq_input)
kq_in.grid(column=1, row=4)

# Đặt tiêu đề cho cửa sổ
win.title("Tính Toán OOP")
win.mainloop()
