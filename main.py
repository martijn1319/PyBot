import random
import pyautogui, sys
import operations
import time
import tkinter as tk

import operations.keyboard_operations
import operations.mouse_operations

print('Press Ctrl-C to quit.')
#operations.volume.set_volume(100)
def countdown(n):
    while n >= 1:
        print(f"Time remaining: {n} second(s)")
        time.sleep(1)
        n -= 1
    start_program()

def start_program():
    print("Starting up...")

    points = {}

    def on_key_press(event):
        # The event object contains information about the key press
        if event.keysym == "Control_R":
            x, y = pyautogui.position()
            points[x] = y
            print(f"{str(x)}, {str(y)}")

    # Create the main application window
    root = tk.Tk()
    root.title("PyBot")

    # Set the size of the window
    root.geometry("400x300")

    # Create a header label
    header = tk.Label(root, text="PyBot", font=("Arial", 16))
    header.pack(pady=10)

    # Create labels to display the mouse coordinates
    mouse_label_x = tk.Label(root, text="X: ", font=("Arial", 12))
    mouse_label_y = tk.Label(root, text="Y: ", font=("Arial", 12))

    # Define button click functions
    def start():
        header.config(text="Started")
        if len(points) > 0:
            for x, y in points.items():
                operations.mouse_operations.move(x=x, y=y)
                time.sleep(2)
        else:
            print("no values")

    def stop():
        root.quit()  # Properly close the Tkinter window and exit

    def info():
        mouse_label_x.pack(pady=5)
        mouse_label_y.pack(pady=5)
        update_mouse_positions()  # Start updating the mouse position

    def update_mouse_positions():
        # Get the current mouse position
        x, y = pyautogui.position()
        if mouse_label_x.winfo_ismapped():
            mouse_label_x.config(text="X: " + str(x))
        if mouse_label_y.winfo_ismapped():
            mouse_label_y.config(text="Y: " + str(y))

        # Schedule the next update after 100 milliseconds
        root.after(100, update_mouse_positions)

    # Create Start button
    start_button = tk.Button(root, text="Start", command=start)
    start_button.pack(pady=5)

    # Create Info button
    info_button = tk.Button(root, text="Info", command=info)
    info_button.pack(pady=5)

    # Create Stop button
    stop_button = tk.Button(root, text="Stop", command=stop)
    stop_button.pack(pady=5)

    root.bind("<KeyPress>", on_key_press)

    # Start the Tkinter event loop
    root.mainloop()


# Start the countdown from 
start_program()