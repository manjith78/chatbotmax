import tkinter as tk
import random
import time

def get_greeting():
    greetings = ["Hello!", "Hi there!", "Hey!"]
    return random.choice(greetings)

def respond_to_user(input_message):
    i=1
    l1=[]
    for item in input_message.split(" "):
      l1.append(item) 
    l2=["hi","hello","hey","yo"]
    l3=["what","name"]
    l4=["clock" ,"time"]
    l5=["where", "you","from"]
    l6=["old","age"]
    l7=["job","hobby","activity"]
    l8=["python","language"]
    l9=["help","coding"]
    l10=["improve"]
    l11=["bye","tata","goodbye"]
    l12=["calculate","compute","add","subtract","multiply","divide"]
    l13= [
            "The Lazy Song  by Bruno Mars",
            "Vaseegara song by Bombay Jayashri",
            "Bullet Song Song by Silambarasan TR",
            "The Life of Ram Song by Govind Vasantha and Pradeep Kumar",
            "Shape of You Song by Ed Sheeran"
          ]
    l14= [
            "Little Do You Know Song by Alex & Sierra",
            "ava enna enna thedi vantha anjala song by Harris Jayaraj, Karthik, &  Prassanna",
            "vida chollam song by Anu Pravin & Kranthi",
            "Chinnanjiru Nilave Song by A. R. Rahman, Haricharan, and Ilango Krishna",
            "HEARTBREAK ANNIVERSARY Song by Giveon"
          ]
    l15= [
            "Wait a Minute! Song by Willow Smith",
            "Naaka Mukka Song by Vijay Antony",
            "Kudukku Song by Manu Manjith, Shaan Rahman, and Vineeth Sreenivasan",
            "Maamadura Song by Dhee and Santhosh Narayanan",
            "Surround Sound Song by JID"
          ],
    l16= [
            "The Lazy Song  by Bruno Mars",
            "Innum Konjam Naeram Song by A. R. Rahman, Shweta Mohan, and Vijay Prakash",
            "Athmave Poo Song by Sushin Shyam",
            "Kadhal Sadugudu Song by A. R. Rahman and S. P. Charan",
            "Hymn for the Weekend Song by Coldplay"
          ]
    l17= ["xo","ox","game","bored","tictactoe"]
    l20=[
            "treat you better",
            "monster",
            "nights",
            "sugarcrush",
            "perfect","senjittalae","wasted","kavaalaa","lolitaa","mundhinam","azhagae","kadhaipoma","2002","blindinglights"]
        
    def start_tic_tac_toe():
      from tkinter import messagebox

      class TicTacToe:
          def __init__(self, master):
            self.master = master
            self.master.title("Tic-Tac-Toe")
            self.current_player = "X"
            self.board = [""] * 9

            self.buttons = []
            for i in range(3):
              row = []
              for j in range(3):
                btn = tk.Button(self.master, text="", width=10, height=4,
                                command=lambda i=i, j=j: self.on_click(i, j))
                btn.grid(row=i, column=j)
                row.append(btn)
              self.buttons.append(row)

          def on_click(self, row, col):
              index = 3 * row + col
              if self.board[index] == "":
                  self.board[index] = self.current_player
                  self.buttons[row][col].config(text=self.current_player)
                  if self.check_winner():
                     messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                     self.reset_board()
                  elif "" not in self.board:
                    messagebox.showinfo("Tie", "It's a tie!")
                    self.reset_board()
                  else:
                    self.current_player = "O" if self.current_player == "X" else "X"

          def check_winner(self):
              winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                             (0, 3, 6), (1, 4, 7), (2, 5, 8),
                             (0, 4, 8), (2, 4, 6)]
              for pos in winning_positions:
                if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != "":
                   return True
              return False

          def reset_board(self):
           self.current_player = "X"
           self.board = [""] * 9
           for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

      if __name__ == "__main__":
        root = tk.Tk()
        game = TicTacToe(root)
        root.mainloop()

    n=len(l1)
    for element in l1:
      if element in l2:
        return "hello..!\nhow can i help you..?"
      elif element in l3:
        return "I'm chatbot. You can call me max!"
      elif element in l4:
        current_time = time.strftime('%H:%M:%S')
        return current_time
      elif element in l5:
        return "I'm from heaven,just to help you..!"
      elif element in l6:
        return "I don't have an age. I'm always up to date!"
      elif element in l7:
        return "I love chatting with users like you!"
      elif element in l8:
        return "I know Python! It's a great language for beginners."
      elif element in l9:
        return "Sure, I can help with basic programming questions!"
      elif element in l10:
       return "Feel free to provide feedback or suggestions for improvement!"
      elif element in l11:
       return "bye...\nsee ya soon..!"
      elif element in l12:
            try:
                calculation = " ".join(l1[n-i:])
                result = eval(calculation)
                return f"The result is {result}"
            except Exception as e:
                return "Error: Invalid calculation"  
      elif element=="happy":
           return random.choice(l13)
      elif element=="sad":
           return random.choice(l14)
      elif element=="energetic":
           return random.choice(l15)
      elif element=="relaxed":
           return random.choice(l16)
      elif element in l17:
         start_tic_tac_toe()
      elif element=="randomsong":
          return random.choice(l20)
      else:
        continue

def send_message():
    user_input = entry_field.get()
    chat_log.config(state=tk.NORMAL)
    if user_input.lower() == "exit":
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        chat_log.insert(tk.END, "Chatbot: Goodbye! Exiting the chatbot.\n")
        entry_field.delete(0, tk.END)
        entry_field.config(state=tk.DISABLED)
        send_button.config(state=tk.DISABLED)
    else:
        chat_log.insert(tk.END, "You: " + user_input + "\n")
        response = respond_to_user(user_input)
        chat_log.insert(tk.END, "Chatbot: " + response + "\n")
        entry_field.delete(0, tk.END)
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
import tkinter as tk

window = tk.Tk()
window.title("Chatbot max")
window.geometry("900x900")
window.configure(bg="black")

# Create and place chat log
chat_log = tk.Text(window, width=50, height=15, state=tk.DISABLED, bg="pink", fg="black")
chat_log.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Center-aligned

# Create and place entry field
entry_field = tk.Entry(window, width=50, bg="#333333", fg="white")
entry_field.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Center-aligned

# Create and place send button
send_button = tk.Button(window, text="Chat", width=10, command=send_message, bg="#333333", fg="white")
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")  # Center-aligned

# Configure row and column weights to center-align the widgets
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

# Insert greeting message
chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "Chatbot: " + get_greeting() + "\n")
chat_log.config(state=tk.DISABLED)

window.mainloop()


