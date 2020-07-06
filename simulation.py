from matplotlib import pyplot as plt
import random
import numpy as np
import csv
import pandas as pd
days = 20
population = 1000
ppl_to_meet_every_day = 10
fine = 200
enforcement_rate = 0.01

class Player(object):
    def __init__(self, num, choice):
        self.number = num
        self.choice = choice
        self.people_met = []
        self.got_caught = False
        self.met_fined_person = False
        self.balance = 0
        self.yesterday_mask_rate = 0
        self.days_after_fine = 0
        self.days_after_talking_to_fined = 0
        self.score = 0

    def make_choice(self):

        self.choice = 'no mask'

        if self.balance <= -600:
            self.choice = 'mask'

        elif self.got_caught and self.days_after_fine < 7:
            self.choice = 'mask'

        elif self.met_fined_person and self.days_after_talking_to_fined < 3:
            chance_to_talk_to_fined = random.randint(0, 100)
            if chance_to_talk_to_fined > 20:
                self.choice = 'mask'

        elif self.yesterday_mask_rate < 0.6:
            self.choice = 'no mask'
        else:
            self.choice = 'mask'

    def show(self):
        print("player num:", self.number, "choice:", self.choice, "sickAfterDays:", self.sickAfterDays)

    def meet_people(self, people):
        self.people_met = people
        for p in people:
            if p.choice == "mask" and self.choice == "mask":
                p.score += 3
                self.score += 3
            elif p.choice == "no mask" and self.choice == "mask":
                p.score += 5
                self.score += 0
            elif p.choice == "mask" and self.choice == "no mask":
                p.score += 0
                self.score += 5
            else:
                p.score += 1
                self.score += 1

    def has_mask(self):
        return self.choice == 'mask'


Players = []


def fill_player(person_id):
    Players.append(Player(person_id, random.choice(['mask','no mask'])))


for person in range(population):
    fill_player(person)


def simulate_meetings( person ):

    #randomly choose 10 people to meet
    people_to_meet = random.choices(Players, k=ppl_to_meet_every_day)
    person.meet_people(people_to_meet)
    wearing_masks = list(map(lambda meet_person: meet_person.choice, people_to_meet))
    #print(wearing_masks)

    #calculate percent of mask wearing, save it on the current player
    mask_wearing_people = list(filter(lambda meet_person: meet_person == 'mask', wearing_masks))
    mask_wearing_percent = len(mask_wearing_people) / ppl_to_meet_every_day
    #print(mask_wearing_percent)
    person.yesterday_mask_rate = mask_wearing_percent

def simulate_enforcement ( person ):

    if not person.has_mask():
        # give fine if no mask
        person.balance -= fine
        person.got_caught = True
        person.days_after_fine = 0

        print('enforced')
        # all people he met - know he got a fine
        for other in person.people_met:
            other.met_fined_person = True
            other.days_after_talking_to_fined = 0

def do_enforcement():
    num_of_enforced = population * enforcement_rate

    enforced_people = random.sample(range(1, population), int(num_of_enforced))

    return enforced_people

mask_wearing_percent = []
for day in range(days):

    enforced_people = do_enforcement()

    for person in Players:

        if person.got_caught:
            person.days_after_fine += 1
        if person.met_fined_person:
            person.days_after_talking_to_fined += 1

        simulate_meetings(person)

        # only for enforced people
        if person.number in enforced_people:
            simulate_enforcement( person )

        #make decision for next day
        person.make_choice()

        #TODO: when people are encouraged to wear a mask?

    print('percentage of mask wearing today :')
    mask_wearing_percent.append(len(list(filter(lambda ppl: ppl.choice == 'mask', Players))) / population)
    print (mask_wearing_percent[day])


    t = np.arange(0, len(Players), 1)

    scores = sorted(list((p.score for p in Players)))
    x = range(0, len(Players))



    #plt.plot(x, scores)

    #plt.savefig("scores.png")
    #plt.show()


print('percentage of mask during the sampled period :')
print (len(list(filter(lambda ppl: ppl.choice == 'mask', Players))) / population)

scores = mask_wearing_percent
x = range(0, days)

plt.plot(x, scores)
plt.figure(figsize=(8, 5))
plt.savefig("scores.png")
plt.show()

