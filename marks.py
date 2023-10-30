import tkinter as tk

def calculate_grade():
    name = entry_name.get()
    roll_no = entry_roll_no.get()
    python_marks = int(entry_python_marks.get())
    ds_marks = int(entry_ds_marks.get())
    maths_marks = int(entry_maths_marks.get())
    os_marks = int(entry_os_marks.get())
    cn_marks = int(entry_cn_marks.get())

    total_marks = python_marks + ds_marks + maths_marks+os_marks+cn_marks
    average_marks = total_marks / 5

    grade = ''
    if average_marks >= 90:
        grade = 'A+'
    elif average_marks >= 80:
        grade = 'A'
    elif average_marks >= 70:
        grade = 'B'
    elif average_marks >= 60:
        grade = 'C'
    else:
        grade = 'F'

    label_name.config(text=f"Name: {name}")
    label_roll_no.config(text=f"Roll No: {roll_no}")
    label_total_marks.config(text=f"Total Marks: {total_marks}")
    label_average_marks.config(text=f"Average Marks: {average_marks}")
    label_grade.config(text=f"Grade: {grade}")

root = tk.Tk()
root.title("Marksheet")
root.geometry("350x300")

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, sticky=tk.E)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_roll_no = tk.Label(root, text="Roll No:")
label_roll_no.grid(row=1, sticky=tk.E)

entry_roll_no = tk.Entry(root)
entry_roll_no.grid(row=1, column=1)

label_python_marks = tk.Label(root, text="Python Marks:")
label_python_marks.grid(row=2, sticky=tk.E)

entry_python_marks = tk.Entry(root)
entry_python_marks.grid(row=2, column=1)

label_ds_marks = tk.Label(root, text="DS Marks:")
label_ds_marks.grid(row=3, sticky=tk.E)

entry_ds_marks = tk.Entry(root)
entry_ds_marks.grid(row=3, column=1)

label_maths_marks = tk.Label(root, text="Maths Marks:")
label_maths_marks.grid(row=4, sticky=tk.E)

entry_maths_marks = tk.Entry(root)
entry_maths_marks.grid(row=4, column=1)

label_os_marks = tk.Label(root, text="OS Marks:")
label_os_marks.grid(row=5, sticky=tk.E)

entry_os_marks = tk.Entry(root)
entry_os_marks.grid(row=5, column=1)

label_cn_marks = tk.Label(root, text="CN Marks:")
label_cn_marks.grid(row=6, sticky=tk.E)

entry_cn_marks = tk.Entry(root)
entry_cn_marks.grid(row=6, column=1)

button_calculate = tk.Button(root, text="Calculate", command=calculate_grade)
button_calculate.grid(row=7, columnspan=2)

label_total_marks = tk.Label(root, text="")
label_total_marks.grid(row=8, columnspan=2)

label_average_marks = tk.Label(root, text="")
label_average_marks.grid(row=9, columnspan=2)

label_grade = tk.Label(root, text="")
label_grade.grid(row=10, columnspan=2)

root.mainloop()
