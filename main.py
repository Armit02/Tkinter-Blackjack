import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
import blackjackv3 as game
import time

# Create the main window and set it to fullscreen
window = tk.Tk()
window.title("Blackjack")
window_width = 1800
window_height = 900
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_pos = (screen_width // 12) - (window_width // 12)
y_pos = (screen_height // 12) - (window_height // 12)
window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

# Create the title label with a custom font
title_font = Font(family="Terminal", size=48, weight="bold")
title_label = ttk.Label(window, text="Blackjack", font=title_font)
title_label.place(relx=0.5, rely=0.5, anchor="center")

widgets = []

# Create a frame to hold the buttons
button_frame = ttk.Frame(window)
button_frame.pack(side=tk.BOTTOM, pady=50)

# Create a custom font for the buttons
button_font = Font(family="Terminal", size=24, weight="bold")
game_font = Font(family="Terminal", size=12)

# Define the hover effect for the buttons
def button_hover(e):
    e.widget.configure(bg="grey", fg="white")

def button_unhover(e):
    e.widget.configure(bg="white", fg="black")


# Create the start button and bind it to a function that changes the window content
def start_game():
    # Remove the title label and the buttons
    title_label.place_forget()
    start_button.destroy()
    for i in widgets:
        i.destroy()
    #exit_button.place_forget()

    # Create a frame for the text
    game_frame = tk.Frame(window)
    game_frame.pack(side=tk.TOP, padx=8, pady=12)
    
    # Create a new label for the game content
    game_label = tk.Label(window, text="Blackjack", font=game_font)
    game_label.pack(expand=True)

    try:
        exit_button.destroy()
    except UnboundLocalError:
        pass

        # Create the Exit button
    exit_button = tk.Button(button_frame, text="Exit", font=button_font, width=10, height=2, command=window.quit)
    exit_button.pack(side=tk.LEFT, padx=20)
    exit_button.bind("<Enter>", button_hover)
    exit_button.bind("<Leave>", button_unhover)
    
    game.main(window, game_font)

def back():
    for i in widgets:
        i.forget()

    title_label = ttk.Label(window, text="Blackjack", font=title_font)
    title_label.place(relx=0.5, rely=0.5, anchor="center")  

    start_button = tk.Button(button_frame, text="Start", font=button_font, width=10, height=2, command=start_game)
    start_button.pack(side="left", padx=20, pady=20)
    start_button.bind("<Enter>", button_hover)
    start_button.bind("<Leave>", button_unhover)

    leader_button = tk.Button(button_frame, text="Leaderboard", font=button_font, width=15, height=2, command=leaderboard)
    leader_button.pack(side="left", padx=20, pady=20)
    leader_button.bind("<Enter>", button_hover)
    leader_button.bind("<Leave>", button_unhover)

    # Create the Exit button
    exit_button = tk.Button(button_frame, text="Exit", font=button_font, width=10, height=2, command=window.quit)
    exit_button.pack(side=tk.LEFT, padx=20)
    exit_button.bind("<Enter>", button_hover)
    exit_button.bind("<Leave>", button_unhover)

    widgets.append(start_button)
    widgets.append(title_label)
    widgets.append(leader_button)
    widgets.append(exit_button)
def leaderboard():
    # Remove the title label and the buttons
    title_label.place_forget()
    start_button.forget()
    exit_button.forget()
    leader_button.forget()

    leader_frame = tk.Frame(window)
    leader_frame.pack(side=tk.TOP, padx=8, pady=12)
    
    # Create a new label for the game content
    leader_label = tk.Label(window, text="Top Scorers!", font=game_font)
    leader_label.pack(expand=True)
    
    leader = game.Leaderboard(window, game_font)
    leader.findRanks()

    back_button = tk.Button(button_frame, font=button_font, text="Back to Menu",command=back)
    back_button.pack(side=tk.RIGHT, padx=20)
    back_button.bind("<Enter>", button_hover)
    back_button.bind("<Leave>", button_unhover)

    widgets.append(back_button)
    widgets.append(leader_label)
    for i in leader.leaderboard_widgets:
        widgets.append(i)

start_button = tk.Button(button_frame, text="Start", font=button_font, width=10, height=2, command=start_game)
start_button.pack(side="left", padx=20, pady=20)
start_button.bind("<Enter>", button_hover)
start_button.bind("<Leave>", button_unhover)

leader_button = tk.Button(button_frame, text="Leaderboard", font=button_font, width=15, height=2, command=leaderboard)
leader_button.pack(side="left", padx=20, pady=20)
leader_button.bind("<Enter>", button_hover)
leader_button.bind("<Leave>", button_unhover)

# Create the Exit button
exit_button = tk.Button(button_frame, text="Exit", font=button_font, width=10, height=2, command=window.quit)
exit_button.pack(side=tk.LEFT, padx=20)
exit_button.bind("<Enter>", button_hover)
exit_button.bind("<Leave>", button_unhover)

# Start the main loop
window.mainloop()







