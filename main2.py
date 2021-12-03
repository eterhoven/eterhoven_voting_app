import tkinter as tk

vote_on = True
while vote_on:
    root = tk.Tk()
    root.title('Voting App')
    root.geometry('1280x720')
    root.configure(background = '#FFFFFF')

    #root.state('zoomed')

    myLabel = tk.Label(root, text="CHOOSE YOUR PET WISELY!", font=('Verdana', 30))
    myLabel.place(relx=0.5, rely=0.1, anchor='center')


    def dog():
        dog_votes = 1
        cat_votes = 0
        hamster_votes = 0
        mybutton4 = tk.Button(root, text=dog_votes, font=('Verdana', 15), padx=70, pady=50, fg="white", bg="blue")
        mybutton5 = tk.Button(root, text=cat_votes, font=('Verdana', 15), padx=70, pady=50, fg="white", bg="red")
        mybutton6 = tk.Button(root, text=hamster_votes, font=('Verdana', 15), padx=70, pady=50, fg="white", bg="green")
        mybutton4.place(relx=0.5, rely=0.5, anchor='center')
        mybutton5.place(relx=0.25, rely=0.5, anchor='w')
        mybutton6.place(relx=0.75, rely=0.5, anchor='e')
        myresult = tk.Label(root, text="A WISE CHOICE", font=('Verdana', 25))
        myresult.place(relx=0.5, rely=0.3, anchor='center')

    def cat():
        dog_votes = 0
        cat_votes = 1
        hamster_votes = 0
        mybutton4 = tk.Button(root, text=dog_votes, font=('Verdana', 15), padx=70, pady=50, fg="white", bg="blue")
        mybutton5 = tk.Button(root, text=cat_votes, font=('Verdana', 15), padx=70, pady=50, fg="white", bg="red")
        mybutton6 = tk.Button(root, text=hamster_votes, font=('Verdana', 15), padx=70, pady=50, fg="white", bg="green")
        mybutton4.place(relx=0.5, rely=0.5, anchor='center')
        mybutton5.place(relx=0.25, rely=0.5, anchor='w')
        mybutton6.place(relx=0.75, rely=0.5, anchor='e')
        myresult = tk.Label(root, text="REALLY? CATS? AREN'T THEY EVIL?", font=('Verdana', 25))
        myresult.place(relx=0.5, rely=0.3, anchor='center')

    def hamster():
        dog_votes = 0
        cat_votes = 0
        hamster_votes = 1
        mybutton4 = tk.Button(root, text=dog_votes, font=('Verdana', 15), padx=70, pady=50, fg="white", bg="blue")
        mybutton5 = tk.Button(root, text=cat_votes, font=('Verdana', 15), padx=70, pady=50, fg="white", bg="red")
        mybutton6 = tk.Button(root, text=hamster_votes, font=('Verdana', 15), padx=70, pady=50, fg="white", bg="green")
        mybutton4.place(relx=0.5, rely=0.5, anchor='center')
        mybutton5.place(relx=0.25, rely=0.5, anchor='w')
        mybutton6.place(relx=0.75, rely=0.5, anchor='e')
        myresult = tk.Label(root, text="I'M NOT EVEN SURE A HAMSTER QUALIFIES AS A PET...", font=('Verdana', 25))
        myresult.place(relx=0.5, rely=0.3, anchor='center')
    

    mybutton1 = tk.Button(root, text="DOG", font=('Verdana', 15), padx=50, pady=50, command=dog, fg="white", bg="blue")
    mybutton2 = tk.Button(root, text="CAT", font=('Verdana', 15), padx=52, pady=50, command=cat, fg="white", bg="red")
    mybutton3 = tk.Button(root, text="HAMSTER", font=('Verdana', 15), padx=30, pady=50, command=hamster, fg="white", bg="green")


    mybutton1.place(relx=0.5, rely=0.5, anchor='center')
    mybutton2.place(relx=0.25, rely=0.5, anchor='w')
    mybutton3.place(relx=0.75, rely=0.5, anchor='e')
    
    vote_on = False

    root.mainloop()