#this program is a food log to track food introductions for Rusty and any physical reactions he may have to them
#he has been on a hypoallergenic diet for almost 3 months now and I want to keep track of what he eats and how he reacts to it
import datetime

#class to log food and reactions
class FoodLog:
    def __init__(self):
        self.log = []
        self.filename = 'rustyfoodlog.txt'

#adding entry to log
    def add_entry(self, food, reaction, stoolquality, note):
        entry = {'date': datetime.datetime.now(), 'food': food, 'reaction': reaction, 'stoolquality': stoolquality, 'note': note}
        self.log.append(entry)

#saving log to file
    def save_log(self):
        with open(logentry.filename, 'a') as file:
            for entry in logentry.log:
                file.write(str(entry['date']) + '\n')
                file.write('Food: ' + entry['food'] + '\n')
                file.write('Reaction: ' + entry['reaction'] + '\n')
                file.write('Stool Quality: ' + entry['stoolquality'] + '\n')
                file.write('Note: ' + entry['note'] + '\n')
                file.write('\n')

#creating instance of FoodLog class
logentry = FoodLog()

#gets entry from user
food = input("What food did Rusty eat? ")
reaction = input("What was Rusty's reaction? ")
stoolquality = input("What was Rusty's stool quality? ")
note = input("Any additional notes? ")

#adds entry to log and saves it
logentry.add_entry(food, reaction, stoolquality, note)
logentry.save_log()
print("Entry saved to log.")

