import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        root.bind('<Return>', lambda event: self.check_guess())
        self.root = root
        self.root.title("🎲 Number Guessing Game")
        self.root.geometry("500x540")
        self.root.config(bg="#e3e6f3")

        self.secret_number = None
        self.attempts_allowed = None
        self.attempts = 0
        self.score = 100

        self.main_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=440, height=540)

        self.title_label = tk.Label(self.main_frame, text="🎲 Number Guessing Game 🎲", font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#2d2d6e")
        self.title_label.pack(pady=(18, 10))

        self.diff_label = tk.Label(self.main_frame, text="Choose difficulty:", font=("Segoe UI", 12, "bold"), bg="#ffffff", fg="#4a4a4a")
        self.diff_label.pack(pady=(0, 2))

        self.diff_var = tk.StringVar(value="2")
        diff_frame = tk.Frame(self.main_frame, bg="#ffffff")
        diff_frame.pack(pady=(0, 10))
        tk.Radiobutton(diff_frame, text="Easy (1-50, 10 attempts)", variable=self.diff_var, value="1", bg="#ffffff", fg="#388e3c", font=("Segoe UI", 10), anchor="w", width=32, justify="left").pack(fill="x", pady=2)
        tk.Radiobutton(diff_frame, text="Medium (1-100, 7 attempts)", variable=self.diff_var, value="2", bg="#ffffff", fg="#1976d2", font=("Segoe UI", 10), anchor="w", width=32, justify="left").pack(fill="x", pady=2)
        tk.Radiobutton(diff_frame, text="Hard (1-500, 5 attempts)", variable=self.diff_var, value="3", bg="#ffffff", fg="#d32f2f", font=("Segoe UI", 10), anchor="w", width=32, justify="left").pack(fill="x", pady=2)

        self.start_button = tk.Button(self.main_frame, text="Start Game", command=self.start_game, bg="#4CAF50", fg="white", font=("Segoe UI", 12, "bold"), activebackground="#388e3c", activeforeground="white", bd=0, relief="ridge", cursor="hand2")
        self.start_button.pack(pady=8, ipadx=10, ipady=2)

        self.info_label = tk.Label(self.main_frame, text="", font=("Segoe UI", 12), bg="#ffffff", fg="#333333")
        self.info_label.pack(pady=7)

        entry_frame = tk.Frame(self.main_frame, bg="#ffffff")
        entry_frame.pack(pady=2)
        self.entry = tk.Entry(entry_frame, font=("Segoe UI", 14), width=10, justify="center", bd=2, relief="solid", fg="#2d2d6e")
        self.entry.pack(side="left", padx=(0, 8))
        self.submit_button = tk.Button(entry_frame, text="Submit Guess", command=self.check_guess, bg="#2196F3", fg="white", font=("Segoe UI", 11, "bold"), activebackground="#1565c0", activeforeground="white", bd=0, relief="ridge", cursor="hand2")
        self.submit_button.pack(side="left", ipadx=6, ipady=1)

        self.result_label = tk.Label(self.main_frame, text="", font=("Segoe UI", 13, "bold"), bg="#ffffff")
        self.result_label.pack(pady=14)

        self.score_label = tk.Label(self.main_frame, text="", font=("Segoe UI", 12), bg="#ffffff", fg="#ff9800")
        self.score_label.pack(pady=2)

        self.reset_button = tk.Button(self.main_frame, text="Play Again", command=self.start_game, state="disabled", bg="#FF9800", fg="white", font=("Segoe UI", 12, "bold"), activebackground="#e65100", activeforeground="white", bd=0, relief="ridge", cursor="hand2")
        self.reset_button.pack(pady=12, ipadx=10, ipady=2)

    def start_game(self):
        choice = self.diff_var.get()
        if choice == "1":
            self.secret_number = random.randint(1, 50)
            self.attempts_allowed = 10
            self.range_text = "1 to 50"
        elif choice == "2":
            self.secret_number = random.randint(1, 100)
            self.attempts_allowed = 7
            self.range_text = "1 to 100"
        else:
            self.secret_number = random.randint(1, 500)
            self.attempts_allowed = 5
            self.range_text = "1 to 500"

        self.attempts = 0
        self.score = 100
        self.info_label.config(text=f"Guess a number between {self.range_text}. Attempts: {self.attempts_allowed}")
        self.result_label.config(text="")
        self.score_label.config(text=f"⭐ Score: {self.score}")
        self.reset_button.config(state="disabled")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="⚠️ Please enter a valid number!", fg="red")
            return

        # Determine range based on difficulty
        if self.diff_var.get() == "1":
            min_val, max_val = 1, 50
        elif self.diff_var.get() == "2":
            min_val, max_val = 1, 100
        else:
            min_val, max_val = 1, 500

        if not (min_val <= guess <= max_val):
            self.result_label.config(text=f"❌ Number out of range! Enter between {min_val} and {max_val}.", fg="red")
            return

        self.attempts += 1
        diff = abs(self.secret_number - guess)

        if guess == self.secret_number:
            self.result_label.config(text=f"🎉 Correct! The number was {self.secret_number}.", fg="green")
            self.score_label.config(text=f"🏆 Final Score: {self.score}")
            self.reset_button.config(state="normal")
        elif diff <= 5:
            self.result_label.config(text="🔥 Very close!", fg="orange")
            self.score -= 5
        elif diff <= 10:
            self.result_label.config(text="🙂 Almost close!", fg="blue")
            self.score -= 10
        elif guess < self.secret_number:
            self.result_label.config(text="📉 Too low!", fg="purple")
            self.score -= 15
        else:
            self.result_label.config(text="📈 Too high!", fg="purple")
            self.score -= 15

        self.score_label.config(text=f"⭐ Score: {self.score}")

        if self.attempts >= self.attempts_allowed and guess != self.secret_number:
            self.result_label.config(text=f"😢 Out of attempts! The number was {self.secret_number}.", fg="red")
            self.score_label.config(text="Final Score: 0")
            self.reset_button.config(state="normal")

# Run the game
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
