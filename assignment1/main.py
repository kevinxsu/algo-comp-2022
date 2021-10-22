#!usr/bin/env python3
import json
import sys
import os

INPUT_FILE = 'testdata.json' # Constant variables are usually in ALL CAPS

class User:
    def __init__(self, name, gender, preferences, grad_year, responses):
        self.name = name
        self.gender = gender
        self.preferences = preferences
        self.grad_year = grad_year
        self.responses = responses


# Takes in two user objects and outputs a float denoting compatibility
def compute_score(user1, user2):
    # YOUR CODE HERE
    return gender_score(user1, user2) * responses_score(user1.responses, user2.responses)
    #return 0

def gender_score(user1, user2):
    return 1 if (user2.gender in user1.preferences) and (user1.gender in user2.preferences) else 0

# returns a score between two user responses
def responses_score(lst1, lst2):
    max_score = 4 * len(lst1)
    return sum(compatibility_list(lst1, lst2)) / max_score

 # returns a list based on compatibility
def compatibility_list(lst1, lst2):
     return [compatibility_score(x, y) for x, y in zip(lst1, lst2)]

def compatibility_score(resp1, resp2):
    return 4 - abs(resp1 - resp2)
    

if __name__ == '__main__':
    # Make sure input file is valid
    if not os.path.exists(INPUT_FILE):
        print('Input file not found')
        sys.exit(0)

    users = []
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
        for user_obj in data['users']:
            new_user = User(user_obj['name'], user_obj['gender'],
                            user_obj['preferences'], user_obj['gradYear'],
                            user_obj['responses'])
            users.append(new_user)

    for i in range(len(users)-1):
        for j in range(i+1, len(users)):
            user1 = users[i]
            user2 = users[j]
            score = compute_score(user1, user2)
            print('Compatibility between {} and {}: {}'.format(user1.name, user2.name, score))
