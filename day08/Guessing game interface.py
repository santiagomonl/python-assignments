import tkinter as tk
from tkinter import messagebox
import random



class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("Guessing Game")

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close w/o question", command=exit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help dialogue", command=self.help_dialogue)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="Cheats and shortcuts", command=self.cheating_shortcuts)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.root.config(menu=self.menubar)




        self.label = tk.Label(self.root, text="Guess a number between 1 and 20", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox.bind("<KeyPress>", self.shortcut_enter)
        self.textbox.pack(padx=10, pady=10)

        self.check_state= tk.IntVar()

        self.check_button = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 12), variable=self.check_state)
        self.check_button.pack(padx=10, pady=10)

        self.button= tk.Button(self.root, text="Start Game", font=("Arial", 16), command=self.start_game)
        self.button.pack(padx=10, pady=10)

        #self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        #self.reset_button.pack(padx=10, pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.clearbtn= tk.Button(self.root, text="Clear", font=("Arial", 16), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.number_of_trials = 0

        self.random_number = random.randint(1, 20)

    
        self.root.mainloop()

    # def show_message(self):
    #     if self.check_state.get() == 0:
    #         print(self.textbox.get(1.0, tk.END))
    #     else:
    #         messagebox.showinfo("Message", self.textbox.get(1.0, tk.END))

    def start_game(self):
        if self.check_state.get()==0:
            #User guess and cheats
            user_guess = input("Guess a number between 1 and 20: ")
            while user_guess != str(self.random_number):
                try:
                    user_guess = int(user_guess)
                    self.number_of_trials = self.number_of_trials + 1
                    if user_guess < self.random_number:
                        print("Too small")
                    else:
                        print("Too high!")
                    user_guess = input("Guess again: ")
                except ValueError:
                    self.number_of_trials = self.number_of_trials +1
                    if user_guess == "s":
                        print("The number is:", self.random_number)
                        user_guess = int(input("Guess again: "))
                        if user_guess == self.random_number:
                            print("Congratulations! You guessed it right.")
                            print("Number of trials:", self.number_of_trials)
                            start_botton=input("Do you want to play again? (yes/no): ")
                            if start_botton == "no":
                                exit()
                            break
                        elif user_guess < self.random_number:
                            print("Too small")
                        else:
                            print("Too high!")
                    elif user_guess == "x":
                        exit()
                    elif user_guess == "n":
                        start_botton=input("Do you want to play again? (yes/no): ")
                        break

            if user_guess == str(self.random_number):    
                print("Congratulations! You guessed it right.")
                print("Number of trials:", self.number_of_trials)
                start_botton=input("Do you want to play again? (yes/no): ")
        else:
            #User guess and cheats
            user_guess = str(self.textbox.get(1.0, tk.END)).strip()
            while user_guess != str(self.random_number):
                try:
                    user_guess = int(user_guess)
                    self.number_of_trials = self.number_of_trials + 1
                    if user_guess < self.random_number:
                        messagebox.showinfo("Too Small!", (self.textbox.get(1.0, tk.END), "is too small, guess again"))
                        break
                    else:
                        messagebox.showinfo("Too High!", (self.textbox.get(1.0, tk.END), "is too high, guess again"))
                        break
                except ValueError:
                    self.number_of_trials = self.number_of_trials +1
                    if user_guess == "s":
                        print("The number is:", self.random_number)
                        messagebox.showinfo("Cheat Code!", ("The number is:", self.random_number))
                        break
                    elif user_guess == "x":
                        exit()
                    elif user_guess == "n":
                        if messagebox.askyesno("Quit?", "Do you want to play again?"):
                            continue
                        else:
                            self.root.destroy()
                        break

            if user_guess == str(self.random_number):    
                print("Congratulations! You guessed it right.")
                messagebox.showinfo("Winner!", ("Congratulations! You guessed it right.\nNumber of trials:",self.number_of_trials))
                #start_botton=input("Do you want to play again? (yes/no): ")

    def help_dialogue(self):
        messagebox.showinfo("Help, Instructions", "1) Guess a number between 1 and 20\n2) Do not press Enter as it will create a second line\n3) You can press Ctrl+Enter to start the game\n4) If you want to see the pop-up window message check the box by clicking it\n5) If you want to input from the terminal or coding environment simply uncheck the checkbox")
    
    def cheating_shortcuts(self):
        messagebox.showinfo("Cheating and Shortcuts", "First make sure that the checkbox is checked!\n1) If you type x in the textbox and press Start Game, it will close the program\n2) If you type n in the textbox and press Start Game, it will restart the game\n3) If you type s in the textbox and press Start Game, it will show the number you want to guess")

    def shortcut_enter(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.start_game()

    def on_closing(self):
        if messagebox.askyesno("Quit?", "Do you want to quit?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete(1.0, tk.END)

my_gui = MyGUI()