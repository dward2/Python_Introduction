import tkinter as tk      # Importing standard tkinter as the "tk" alias
from tkinter import ttk   # Importing newer "themed" widgets as the "ttk" alias

from PIL import Image, ImageTk

from pid_calculations import generate_PID_plot


def main_window():

    def update_cmd():
        print("Clicked on Update Button")
        # Get information from GUI
        kp = kp_value.get()
        ki = ki_value.get()
        kd = kd_value.get()
        # Call another function to do work and receive answer
        plot_image = generate_PID_plot(kp, ki, kd)
        # Update the GUI with new information
        im_label.configure(image=plot_image)
        im_label.image = plot_image

    def close_cmd():
        root.destroy()

    # Define Root Window
    root = tk.Tk()
    root.title("PID Simulator")

    # Create Label Widgets
    title_label = tk.Label(root, text="PID Simulator")
    title_label.grid(column=0, row=0, columnspan=2)
    kp_label = ttk.Label(root, text="Kp =")
    kp_label.grid(column=0, row=1, sticky="e")
    ki_label = ttk.Label(root, text="Ki =")
    ki_label.grid(column=0, row=2, sticky="e")
    kd_label = ttk.Label(root, text="Kd =")
    kd_label.grid(column=0, row=3, sticky="e")

    # Create entry box widgets and variables to hold inputs
    kp_value = tk.IntVar()
    kp_entry = ttk.Entry(root, textvariable=kp_value, width=8)
    kp_entry.grid(column=1, row=1)
    ki_value = tk.IntVar()
    ki_entry = ttk.Entry(root, textvariable=ki_value, width=8)
    ki_entry.grid(column=1, row=2)
    kd_value = tk.IntVar()
    kd_entry = ttk.Entry(root, textvariable=kd_value, width=8)
    kd_entry.grid(column=1, row=3)

    # Create Button Widgets.
    # The commented out lines show how to use the "ttk" versions.
    # The uncommented out lines show how to use the "tk' versions and change
    #   their colors

    # update_btn = ttk.Button(root, text="Update", command=update_cmd)
    update_btn = tk.Button(root, text="Update", command=update_cmd,
                           background="blue", foreground="white")
    update_btn.grid(column=0, row=4, columnspan=2, sticky="ew", padx=5)

    # close_btn = ttk.Button(root, text="Close", command=close_cmd)
    close_btn = tk.Button(root, text="Close", command=close_cmd,
                           background="blue", foreground="white")
    close_btn.grid(column=0, row=5, columnspan=2, sticky="ew", padx=5)

    # Create image label widget
    image = Image.open("blank_plot.jpg")
    tk_image = ImageTk.PhotoImage(image)
    im_label = ttk.Label(root, image=tk_image)
    im_label.image = tk_image
    im_label.grid(column=2, row=1, rowspan=99)

    # Start GUI
    root.mainloop()


main_window()
