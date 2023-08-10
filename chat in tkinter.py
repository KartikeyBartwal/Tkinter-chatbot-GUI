import tkinter as tk

class ChatApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Personalised Metaverse Health Coach")
        self.master.configure(bg="#333333")
        self.master.resizable(False, False)
        
        self.conversation_history = tk.Text(master, state=tk.DISABLED, height=30, width=70,
                                     font=("Helvetica", 12), bg="#4F4F4F",
                                     fg="#FFFFFF", insertbackground="#FFFFFF",
                                     borderwidth=0, highlightthickness=0)
        self.conversation_history.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        
        self.message_entry = tk.Entry(master, width=50, font=("Helvetica", 12),
                                      bg="#4F4F4F", fg="#FFFFFF", insertbackground="#FFFFFF",
                                      borderwidth=0, highlightthickness=0)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10)
        self.message_entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(master, text="Send", command=self.send_message,
                                     font=("Helvetica", 12), bg="#1E88E5", fg="#FFFFFF",
                                     activebackground="#1565C0", activeforeground="#FFFFFF",
                                     borderwidth=0, highlightthickness=0)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.user1 = "You:"
        self.user2 = "Sandeep: "
        self.current_user = self.user1
        
    def send_message(self, event=None):
     message = self.message_entry.get()
     if message:
        self.conversation_history.config(state=tk.NORMAL)
        self.conversation_history.insert(tk.END, self.current_user)
        
        if self.current_user == self.user2:
            # animate text for user2
            for char in message:
                self.conversation_history.insert(tk.END, char)
                self.conversation_history.see(tk.END)
                self.master.update_idletasks()
                self.master.after(30)
        else:
            self.conversation_history.insert(tk.END, message)
            
        self.conversation_history.insert(tk.END, "\n \n")
        self.conversation_history.config(state=tk.DISABLED)
        self.message_entry.delete(0, tk.END)
        self.toggle_user()

    
    def toggle_user(self):
        if self.current_user == self.user1:
            self.current_user = self.user2
        else:
            self.current_user = self.user1

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("720x720")
    app = ChatApplication(root)
    root.mainloop()
