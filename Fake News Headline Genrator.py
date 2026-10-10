  #import the random module
import random
# creat subjects
subjects = [
    "Sharukh khan",
    "Virat Kohli",
    "priya",
    "Rajat dallal",
    "Landypuchi"
    "Niramal Sitharman",
    "A delhi cat",
    "A group of monkeys",
    "Prime minister modi",
    "Auto Rickshaw Driver from delhi"
    "in a plane",
    "Osama bin laden",
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "decalares war on iran",
    "Orders",
    "celebrates",
    "study in",
    "Taking flight",
    "workind in",
    "giving perfect blowjob",
    "In america"
]

places = [
    "Red Fort",
    " In mumbai local train",
    "delhi protest",
    "during ipl match ",
    " a plate of samosa",
    " at ganga ghat",
    "at airport",
    "in the tajmahal",
    "Ducat in Noida sec 16"

]

# start the headlight genration loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f" BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break
#print good bye message
print("\nThanks for using the Fake News Headline Genrator. Have a fun day") 




