#!/usr/bin/env python3

# class Gamer():      #? class creation 
#     pass

# gamer1 = Gamer()    #?   Object creation for class

# #?  Assigning attributes to the object

# gamer1.id = 1
# gamer1.username = "Logan"
# gamer1.rank = "Rank 20"
# gamer1.progress = 10

# print(gamer1.progress)




class Players:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.rank = 0
        self.progress = 0
        self.followers = 0
        self.following = 0
        self.view = 0
        self.viewed = 0

    
    def follow(self, player):
        player.followers += 1
        self.following += 1
    

    def status_view(self, player):
        self.view += 1
        player.viewed += 1

player1 = Players(1,"Logan")
player2 = Players(2,"Adele")

player1.follow(player2)
player2.follow(player1)
player1.status_view(player2)

# print(player1.followers)
# print(player1.following)
# print(player2.followers)
# print(player2.following)
# print(player1.view)
# print(player2.view)
# print(player1.viewed)
# print(player2.viewed)



class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.friends = 0
        self.new_friend = 0

    def friend(self, colleague):
        self.friends += 1
        colleague.new_friend +=1

account1 = User("Adele", 1)
account2 = User("Logan", 2)

account1.friend(account2)

print(account1.friends)
print(account1.new_friend)
print(account2.friends)
print(account2.new_friend)

