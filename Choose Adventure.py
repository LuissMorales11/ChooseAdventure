# Choose.py
# by [Marcos,William,Justin,Luis]
# Description: starter code for the Choose Your
# Own Adventure Project
#asdlf;j
# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

# Luis functions # 
def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "\nHello, you are a high schooler from Luisito High School. " + \
                        "You want to try out to a professional soccer club form Oregon like Timbers. Alright? ")
    choice = simpledialog.askinteger("Choose wisely",
                                   "Would you like to try out? (When 1 is 'yes' and 2 is 'no'). ")
    if choice == 1:
        tryout()
    elif choice == 2:
        noTryout()
    else:
        intro()

def noTryout():
    choice = messagebox.showinfo("Bye Bye",
                                     "You will regret it!!!!! You go back to your normal life.")

def tryout():
    choice = simpledialog.askinteger("Choose wisely",
                                      "Eat appropriate food before training day? Now choose either 1(yes) or 2(no).")
    if (choice == 1):
        messagebox.showinfo("Yes",
                            "Training goes very well and you got offered a spot on the team!")
        offer()
        
    elif (choice == 2):
        messagebox.showinfo("No",
                            "Training goes bad and you head home disappointed.")
        sad()
        
    if tryout == 1:
        offer()
    elif tryout == 2:
        sad()
    else:
        intro()

def offer():
    choice = simpledialog.askinteger("Team offer",
                                     "You want to accept the spot on the team or no? Yes(2) or No(1)")
    if (choice == 2):
        messagebox.showinfo("Deal is done",
                            "offer you a deal for $2,000!")
        messagebox.showinfo("But wait",
                            "At the same time, a division 1 university offers you a scholarship to play soccer.")
        decision()
                            
    elif (choice == 1):
        messagebox.showinfo("Denied deal",
                            "You didnt accept the deal and you go back to your normal life.")
        end()

# Justin Function # 
def end():
    messagebox.showinfo( "End",
                         "Good luck with your life.")
def decision():
    choice = simpledialog.askinteger("Decision",
                                     "Do you want to accept the deal and take the $2,000(1) OR take the scholarship(2)?")
    if (choice == 1):
        messagebox.showinfo("Taking the deal",
                            "You have accept the deal and taken the $2,000")
        messagebox.showinfo("But wait",
                            "But wait, they think about the deal again and increase your deal to $10,000 since you're a decent player!")
        dream()
        
    elif (choice == 2):
        messagebox.showinfo("Denied deal",
                            "They ask you if you're sure if you don't want to accept")
        scholarship()
        
    
    if decision == 1:
        dream()
    elif decision == 2:
        scholarship()
    else:
        intro()

def dream():
    messagebox.showinfo("First match",
                        "Weeks later after you accept your deal, you have scored your first goal on your first match on the team!")
    messagebox.showinfo("Dream come true",
                        "You're living the dream! Congrats of being a professional soccer player!")
                        
def scholarship():
    choice = simpledialog.askinteger("Scholarship",
                                   "You dont want the scholarship(1) OR think about it(2).?")
    if (choice == 1):
        messagebox.showinfo("Denied",
                            "You go back home, continue high school.")
                        
        college()

    elif (choice == 2):
        messagebox.showinfo("scholarship",
                            "Give you 2 weeks to think about your decision.")
                        
        denied()

    if scholarship == 1:
        college()
    elif scholarship == 2:
        denied()
    else:
        intro()

def college():
    messagebox.showinfo("College",
                        "During your senior year, you have received an offer to a college scholarship to play soccer")
    choice = simpledialog.askinteger("Yeah or nah?",
                                     "Accept the scholarship(1) OR Deny it(2)")
    if (choice == 1):
        messagebox.showinfo("Scholarship",
                            "You have accept to play for a college for 4 years and hope you get drafted to the MLS to be a professinal soccer player.")
        drafted()
                        
    elif (choice == 2):
        messagebox.showinfo("Denied",
                            "You have denied the offer and went on to a dream college of yours to learn a new career.")
        end()
                        
    if college == 1:
        drafted()
    elif college == 2:
        end()
    else:
        intro()

# Willy Function #
    
def drafted():
    messagebox.showinfo("Draft",
                        "Good news, after all those hard work you have put in during those 4 years, you have been drafted to the Seattle Sounders and sign a contract with them with a great deal! You're living the dream!")
    end()                    

def denied():
    messagebox.showinfo("Denied",
                        "They have found another good player which they think he is better than you. So you just got replace.")
    messagebox.showinfo("Denied",
                        "So, you took too long to decide whether to take the offer or not. So you have to find another backup career to learn so you can go to college and become whatever you want. Last words for ya...")
    end()

def sad():
    messagebox.showinfo("Wondering",
                        "Now you're thinking if you still want to continue with your soccer dream OR start learning about something and become whatever you just learned.")
    choice = simpledialog.askinteger("Think",
                                     "Start improving by going back to your high school team until something good happens(1) OR quit soccer and find an another career(2).")
    if (choice == 1):
        college()
    elif (choice == 2):
        career()
    else:
        intro()

def career():
    messagebox.showinfo("Career",
                        "You found a career that you're interested in. But someone from the academy team motivates you to do better and put in 100% to acheive your dream of being a professional soccer player.")
    choice = simpledialog.askinteger("Career",
                                     "Stick with the career you were learning about(1) OR you are willing to take another chance of being a professional soccer player(2).")
    if (choice == 1):
        career2()
    elif (choice == 2):
        tryout2()
    else:
        intro()

# Marcos Function #
def career2():
    messagebox.showinfo("Denied Soccer",
                        "You chose to learn more about the career you were learning about.")
    messagebox.showinfo("Career",
                        "Later, you finally graduate and getting close to what you're learning and becoming what you want. Got last words for you though...")

    end()

def tryout2():
    messagebox.showinfo("Tryouts",
                        "The teammate who motivated you, talked to the coach and decided to give you another chance of making the team.")
    messagebox.showinfo("Tryouts",
                        "2 hrs later, the coach liked your performance and gave you a offer of $2,000 and a spot in the team.")
    choice = simpledialog.askinteger("Choose",
                                   "Take the offer(1) or walk away and find some other career to learn about(2).")
    if (choice == 1):
        messagebox.showinfo("Accept offer",
                            "You take the offer and now you're offically on the team! You're starting to live the dream, congrats!")
        end()

    elif (choice == 2):
        messagebox.showinfo("New Career",
                            "The coach wanted to give you one more chance to think about it. You have 3 days to decide.")
        decide()
                    
    if tryout2 == 1:
        end()
    elif tryout2 == 2:
        decide()
    else:
        intro()

def decide():
    messagebox.showinfo("Decide",
                        "Have you decide yet? Whats it going to be.?")
    choice = simpledialog.askinteger("Decide",
                                     "I'll take the offer(1) or naaaahhhhhhh Im good(2)")
    if (choice == 1):
        lucky()
    elif (choice == 2):
        messagebox.showinfo("Denied",
                            "You have denied the offer and you're going to find another career to become as for your future but most importantly..")
        end()
        
def lucky():
    messagebox.showinfo("You have given another chance to be in the team and you have earned it. GREAT JOB!! You are now offically a professional soccer player. Well done.! Now....")
    
        
################ Main #####################
intro()


root.destroy()

