character_gender = input("Please type a gender for your character. MALE or FEMALE: ")

if character_gender.lower() == "male":
    sig_other_pronoun_subject = "her"
    sig_other_pronoun_object = "she"
elif character_gender.lower() == "female":
    sig_other_pronoun_subject = "him"
    sig_other_pronoun_object = "he"
else:
    print("Invalid gender input. Please choose either Male or Female.")
    exit()

character_name = input("Please enter a name for your character: ")
response = input("You currently have your dream job, but you don't make much money. Another company offers you a job that pays triple what you make now, but it's not your dream job. Do you ACCEPT or REJECT the offer? Your choice: ")

if response.lower() == "accept":
    print(f"Congratulations {character_name}! You quit your dream job to accept a higher paying position. On your first day, you notice your boss is smuggling money from the business for himself. Do you REPORT HIM or LEAVE IT ALONE?")
    response = input("Your choice: ")
   
    if response.lower() == "report him":
        print("Your boss finds out you are in the process of reporting him, and he fires you. Your former boss does get convicted, and you serve as a witness. Good job! You are still unemployed. Do you GET A MASTER'S DEGREE or GET A NEW JOB? ")

        response = input("Your choice: ")
        if response.lower() == "get a master's degree":
            print(f"Congrats {character_name}! You have a master's degree! You have more job opportunities, but even more debt. Do you LIVE ON THE CHEAP or WORK TWO JOBS?")
            response = input("Your choice: ")
            if response.lower() == "live on the cheap":
                print(f"Congrats {character_name}! You lived cheaply, sure you ate a lot of boxed ramen noodles, but you have plenty saved up! What will you do with your newfound money? SAVE IT or TAKE A TRIP?")

                response = input("Your choice: ")
                if response.lower() == "save it":
                    print(f"Excellent choice {character_name}! You save up enough money to buy your dream home! You live a happy life, and you look forward to adventures in your life ahead!")
                elif response.lower() == "take a trip":
                    print("You have the time of your life! Good choice {character_name}! On your trip, you meet the love of your life. Two years later you are married and living your dream life!")
            elif response.lower() == "work two jobs":
                print("Now you have no time for your family, your friends, or dating. Life is pretty tough, and despite your best efforts, you can't pull the funds to pay your bills. What do you do? MOVE IN WITH YOUR PARENTS or CRASH ON YOUR FRIEND'S COUCH?")

                response = input("Your choice: ")
                if response.lower() == "move in with your parents":
                    print("You love living with your parents. In fact, you love it so much you never leave. You are now your parents' caregiver in their old age.")

                elif response.lower() == "crash on your friend's couch":
                    print("You crash on your friend's couch and you end up meeting the love of your life. Three years later you are married with a baby on the way... and you are not living on your friend's couch!")

        elif response.lower() == "get a new job":
            print("You find a new job, and it's not easy work. After some time your boss asks if you would be his replacement when he retires. Do tell him YES or NO?")
                
            response = input("Your choice: ")
            if response.lower() == "yes":
                print(f"Congratulations {character_name}! You make a lot more money, and a lot more work! You don't really have time to date, so you never get married, and never have a family. You retire fairly early though, at 45. So maybe there's still hope for you.")
                
            elif response.lower() == "no":
                print("You continue to work at that job for a while. You have time to spend with friends and family. You end up running into your high school sweetheart. A year later you are married and looking forward to your future!")

    elif response.lower() == "leave it alone":
        print("Your boss is eventually caught, and you are asked to act as a witness. Your boss' legal team directs you to protect your boss so you will be protected. Do you DEFEND YOUR BOSS or TELL THE TRUTH?")

        response = input("Your choice: ")
        if response.lower() == "defend your boss":
            print("That was a terrible idea. You are charged with lying under oath. You are sentenced to three years in prison with thousands of dollars in fines.")

        elif response.lower() == "tell the truth":
            print("You tell the truth, and your testimony is exactly what the jury and the judge need to know your boss is guilty. Unfortunately, your boss has some powerful friends, so you are blacklisted from jobs within your industry. You start your own business and live a successful life! And you can sleep at night knowing you did the right thing.")

elif response.lower() == "reject":
    print(f"You are happy with your choice! There is a new hire at work who has started flirting with you. Do you ASK {sig_other_pronoun_subject.upper()} TO HAVE LUNCH WITH YOU, ASK {sig_other_pronoun_subject.upper()} ON A DATE, or DO NOTHING?")

    response = input("Your choice: ")
    if response.lower() == f"ask {sig_other_pronoun_subject} to have lunch with you":
        print(f"You have a wonderful lunch and end up having lunch with {sig_other_pronoun_subject} every day.{sig_other_pronoun_object} asks you to go to dinner. Do you ACCEPT or REJECT the invitation?")

        response = input("Your choice: ")
        if response.lower() == "accept":
            print(f"You have a wonderful dinner and many more great dates. You are now in a pretty serious relationship. {sig_other_pronoun_object} brings up getting married. Do you RUN AWAY or SAY YES?")

            response = input("Your choice: ")
            if response.lower() == "run away":
                print(f"You really will regret that choice. You end up alone. {sig_other_pronoun_object} was your soulmate.")

            elif response.lower() == "say yes":
                print(f"Congratulations {character_name}! You have a beautiful wedding, buy a house & have two kids. You are living the dream, and you are very happy.")

    elif response.lower() == f"ask {sig_other_pronoun_subject} on a date":
        print(f"Your co-worker tells you that {sig_other_pronoun_object} doesn't date co-workers. Do you CHANGE DESKS so you don't have to see {sig_other_pronoun_subject} or do you STAY PUT?")

        response = input("Your choice: ")
        if response.lower() == "change desks":
            print(f"You change desks and avoid {sig_other_pronoun_subject}. One day someone in HR says there's been a complaint from your office admirer. They claim that you are being rude and trying to avoid them. Do you COMPLAIN THAT {sig_other_pronoun_object.upper()} WERE FLIRTING or TALK TO {sig_other_pronoun_object.upper()} DIRECTLY? ")
        
            response = input("Your choice: ")
            if response.lower() == "complain that they were flirting":
                print("The HR department doesn't believe you. Soon there are rumors going around that you are the one that is flirtatious with co-workers. You no longer have work friends and you are ostracized. It isn't fair.")
            elif response.lower() == f"talk to {sig_other_pronoun_object} directly":
                print(f"You talk to your flirtatious co-worker directly. {sig_other_pronoun_object} understands that you are not interested, and instead sets you up with another co-worker. You fall in love and get married soon after.")

        elif response.lower() == "stay put":
            print("Your co-worker continues to flirt with you. Another co-worker recognizes that you are uncomfortable and interferes. You become good friends with this co-worker. 2 years later you marry this co-worker. You are living your best life!")
    elif response.lower() == "do nothing":
        print("You still have a crush on your co-worker. You are really close friends! Your co-worker is now in a serious relationship. You co-worker is considering moving out of state along with {sig_other_pronoun_subject} significant other. And {sig_other_pronoun_object} asks you if that is a good idea, and if there is anything you want to tell {sig_other_pronoun_subject}. You CONFESS YOUR LOVE or TELL {sig_other_pronoun_subject.upper()} TO GO?")
        response = input ("Your choice: ")
        if response.lower() == "confess your love":
            print(f"Your co-worker is conflicted, but after some time {sig_other_pronoun_subject} confesses {sig_other_pronoun_object} for you. A year later you are married-- and all your co-workers attend the wedding. You are happy!")
        elif response.lower() == f"tell {sig_other_pronoun_subject} to go":
            print("You regret letting your co-worker go. And you are lonely. You regret that you let {sig_other_pronoun_object} go.")
else:
    print("You have not submitted a valid choice.")
