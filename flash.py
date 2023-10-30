import tkinter as tk

# Function to create flashcard
def create_flashcard():
    question = question_entry.get()
    answer = answer_entry.get()

    flashcard = f"Question: {question}\nAnswer: {answer}"
    flashcard_label.config(text=flashcard)

    # Clear the entry fields
    question_entry.delete(0, tk.END)
    answer_entry.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Flashcard Creator")

# Create question label and entry field
question_label = tk.Label(window, text="Word:")
question_label.pack()
question_entry = tk.Entry(window)
question_entry.pack()

# Create answer label and entry field
answer_label = tk.Label(window, text="Meaning:")
answer_label.pack()
answer_entry = tk.Entry(window)
answer_entry.pack()

# Create button to create flashcard
create_button = tk.Button(window, text="Create Flashcard", command=create_flashcard)
create_button.pack()

# Create label to display flashcard
flashcard_label = tk.Label(window, text="")
flashcard_label.pack()

# Start the main loop
window.mainloop()
