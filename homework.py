import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("500x400")
root.title("Tkinter Homeworks")

photo = tk.PhotoImage(file='bi.png')
photo1 = tk.PhotoImage(file='fib1.png')
photo2 = tk.PhotoImage(file='tower1.png')


def create_scrollable_frame(container):
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return scrollable_frame


def homework1_page():
    homework1_frame = create_scrollable_frame(main_frame)
    lb = tk.Label(homework1_frame, image=photo, width=1230, height=700)
    lb.pack()


def homework2_page():
    homework2_frame = create_scrollable_frame(main_frame)
    lb = tk.Label(homework2_frame, image=photo1, width=1230, height=700)
    lb.pack()


def homework3_page():
    homework3_frame = create_scrollable_frame(main_frame)
    lb = tk.Label(homework3_frame, image=photo2, width=1230, height=700)
    lb.pack()


def hide_indicators():
    home1_indicate.config(bg='#c3c3c3')
    home2_indicate.config(bg='#c3c3c3')
    home3_indicate.config(bg='#c3c3c3')


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def indicate(lb, page):
    hide_indicators()
    lb.config(bg='#158aff')
    delete_pages()
    page()


options_frame = tk.Frame(root, bg='#c3c3c3', highlightbackground='black',
                         highlightthickness=1)

home1_button = tk.Button(options_frame, text='HomeWork1', font=('Bold', 13),
                         fg='#158aff', bd=0, bg='#c3c3c3',
                         command=lambda: indicate(home1_indicate, homework1_page))

home1_button.place(x=13, y=20)

home1_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home1_indicate.place(x=3, y=20, width=5, height=29)

home2_button = tk.Button(options_frame, text='HomeWork2', font=('Bold', 13),
                         fg='#158aff', bd=0, bg='#c3c3c3',
                         command=lambda: indicate(home2_indicate, homework2_page))

home2_button.place(x=13, y=70)

home2_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home2_indicate.place(x=3, y=70, width=5, height=29)

home3_button = tk.Button(options_frame, text='HomeWork3', font=('Bold', 13),
                         fg='#158aff', bd=0, bg='#c3c3c3',
                         command=lambda: indicate(home3_indicate, homework3_page))

home3_button.place(x=13, y=120)

home3_indicate = tk.Label(options_frame, text='', bg='#c3c3c3')
home3_indicate.place(x=3, y=120, width=5, height=29)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=135, height=700)

main_frame = tk.Frame(root, highlightbackground='black',
                      highlightthickness=1)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=700, width=1230)

root.mainloop()
