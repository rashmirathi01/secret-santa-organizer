from email_sender import EmailService
from user import User
import copy
import random


def shuffle(santa, child_list):
    if(len(child_list) == 1):
        return None if (santa.name == child_list[0].name) else child_list[0]
    child = random.choice(child_list)
    while(santa.name == child.name):
        shuffle(santa, child_list)
        break
    return child

def reset_child(santa_list):
    for santa in santa_list:
        santa.child = None

def assign_santa(user_list):
    child_list = copy.deepcopy(user_list)
    for santa in user_list:
        child = shuffle(santa, child_list)
        if(child != None):
            santa.secret_child = child.name
            child_list.remove(child)
        else:
            reassign_santa(user_list)
            break


def reassign_santa(user_list):
    print("Assignment failed.. reassigning..")
    print_arrangement(user_list)
    reset_child(user_list)
    assign_santa(user_list)


def print_arrangement(user_list):
    print(".... Its a secret arrangement ....")
    #for user in user_list:
    #    print("Secret Santa:", user.name, ", Secret Child:", user.secret_child)

def validate_santa(user_list):
    for user in user_list:
        if(user.name == user.secret_child):
            return False
    return True

def send_invite(user_list):
    for user in user_list:
        EmailService(user).send_mail()


if __name__ == "__main__":
    user_list = [User('Priyank B', 'priyank.b@gmail.com'), User('Saif A', 'saif.a@gmail.com'), User('Anu P', 'anu.p@gmail.com'),
    User('Arun M', 'arun.m@gmail.com'), User('Hardik V', 'hardik.v@gmail.com'), User('Mahesh K', 'mahesh.k@gmail.com'),
    User('Narayana M', 'narayana.m@gmail.com'), User('Roshni R', 'roshni.r@gmail.com')]
    assign_santa(user_list)
    while(not validate_santa(user_list)):
        assign_santa(user_list)
    send_invite(user_list)
    print_arrangement(user_list)
