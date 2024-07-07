import random
import time
import csv
import tkinter as tk
from tkinter.font import Font


def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Adjust the delay time to your preference
    print()  # Add a new line at the end
def replace_array(array_of_arrays, new_array):
    for i, sub_array in enumerate(array_of_arrays):
        if sub_array[0] == new_array[0]:
            array_of_arrays[i] = new_array
            break
            

class Leaderboard:
    def __init__(self, window, font):
        self.leaderboard_widgets = []
        self.window = window
        self.font = font
    def clearBoard(self):
        for i in self.leaderboard_widgets:
            i.forget()
        import main
    def findRanks(self):
        ranking = []
        with open("players.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader: 
                if row != []:
                    print(row)
                    for j in ranking:
                        if j[0] == row[0]:
                            j = row
                    ranking.append(row)
                else: 
                    pass 
            sorted_ranking = sorted(ranking, key=lambda x: int(x[1]), reverse=True)
            for i in range (1,4):
                print(i)
                print(sorted_ranking[i-1])
                leaderboard = tk.Label(self.window, font=self.font, text=str(i) + ": " + str(sorted_ranking[i-1]))
                leaderboard.pack()
                self.leaderboard_widgets.append(leaderboard)
    

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.widgets = []

    def checkBalance(self, window, font):
        balance = tk.Label(window, font=font,
                           text="Your balance is: $" + self.balance)
        balance.pack()
        self.widgets.append(balance)
        if int(self.balance) < 0:
            balance1 = tk.Label(window, font=font,
                                text="Whoa, look's like you're in debt!!")
            balance1.pack()
            self.widgets.append(balance1)
        elif self.balance == 0:
            balance1 = tk.Label(window, font=font,
                                text="You've run out of cash!!")
            balance1.pack()
            self.widgets.append(balance1)
        else:
            balance1 = tk.Label(window, font=font,
                                text="Look's like you're good to go!")
            balance1.pack()
            self.widgets.append(balance1)

    def editBalance(self, winnings):
        self.balance = int(self.balance) + int(winnings)
        array = [self.name, self.balance]
        with open("players.csv", 'a') as file:
            writer = csv.writer(file)
            writer.writerow(array)
        file.close()


class Game:

    def __init__(self, window, font, player):
        self.hand = []
        self.hand_sum = 0
        self.dealer = []
        self.dealer_sum = 0
        self.cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.turn = 1
        self.game = 0
        self.bet = 0
        self.total = 0
        self.window = window
        self.font = font
        self.widgets = []
        self.player = player

    def replay(self):
        #replay = input("Would you like to play again?").lower()
        def replay():
            for i in self.widgets:
                i.destroy()
            self.hand = []
            self.hand_sum = 0
            self.dealer = []
            self.dealer_sum = 0
            self.turn = 1
            self.startGame()
        def end():
            for i in self.widgets:
                i.destroy()
            #print_slow("I hope you've enjoyed Blackjack! Goodbye")
            end_label = tk.Label(self.window, font=self.font, text="I hope you've enjoyed Blackjack! Goodbye!!")
            end_label.pack()
            #print("Your total winnings are: " + str(self.total))
            final_winnings = tk.Label(self.window, font=self.font, text="Your total winnings are: $" + str(self.total))
            final_winnings.pack()
            self.player.editBalance(self.total)
        replay_label = tk.Label(self.window, font=self.font, text="Would you like to play again?")
        replay_label.pack()
        self.widgets.append(replay_label)

        yes_button = tk.Button(self.window, font=self.font, text="Yes", command=replay)
        yes_button.pack()
        self.widgets.append(yes_button)

        no_button = tk.Button(self.window, font=self.font, text="No", command=end)
        no_button.pack()
        self.widgets.append(no_button)

    def checkHand(self):
        self.hand_sum = 0
        for i in self.hand:
            if type(i) != int:
                if i == 'A':
                    self.hand_sum += 11
                    if self.hand_sum > 21:
                        self.hand_sum = self.hand_sum - 10
                else:
                    self.hand_sum += 10
            else:
                self.hand_sum += i
        #print_slow("Here's your hand: ")
        player_hand_label = tk.Label(self.window, font=self.font, text="Here's your hand: ")
        player_hand_label.pack()
        self.widgets.append(player_hand_label)
        #print(self.hand)
        player_hand = tk.Label(self.window, font=self.font, text=str(self.hand))
        player_hand.pack(expand=True)
        self.widgets.append(player_hand)
        #print_slow("Total: ")
        hand_sum_label = tk.Label(self.window, font=self.font, text="Total: ")
        hand_sum_label.pack()
        self.widgets.append(hand_sum_label)
        #print(self.hand_sum)
        hand_sum = tk.Label(self.window, font=self.font, text=self.hand_sum)
        hand_sum.pack()
        self.widgets.append(hand_sum)

        self.dealer_sum = 0
        for i in self.dealer:
            if type(i) != int:
                if i == 'A':
                    self.dealer_sum += 11
                    if self.dealer_sum > 21:
                        self.dealer_sum = self.dealer_sum - 10
                else:
                    self.dealer_sum += 10
            else:
                self.dealer_sum += i
        time.sleep(0.5)
        #print_slow("Here's the dealer's hand: ")
        dealer_hand_label = tk.Label(self.window, font=self.font, text="Here's the Dealer's hand")
        dealer_hand_label.pack()
        self.widgets.append(dealer_hand_label)
        #print(self.dealer)
        dealer_hand = tk.Label(self.window, font=self.font, text=str(self.dealer))
        dealer_hand.pack(expand=True)
        self.widgets.append(dealer_hand)
        if self.turn == 0:
            dealer_sum = tk.Label(self.window, font=self.font, text="Total: " + str(self.dealer_sum))
            dealer_sum.pack
            self.widgets.append(dealer_sum)
        if self.dealer_sum > 21:
            win_label = tk.Label(self.window, font=self.font, text="Dealer is Bust! You won: $" + str(self.bet))
            win_label.pack()
            self.widgets.append(win_label)
            self.player.editBalance(int(self.bet))
            self.total += int(self.bet)
            self.turn = 1
            self.game = 1
            self.replay()

    def startGame(self):
        time.sleep(0.25)

        print("this works")
        # self.bet = int(input("Place your bets: $"))
        balance = tk.Label(self.window, font=self.font, text="Your balance is currently: " + str(self.player.balance))
        balance.pack()
        self.widgets.append(balance)
        bet_in = tk.Label(self.window, font=self.font,
                          text="Place your bets here: ")
        bet_in.pack()

        bet_in_entry = tk.Entry(self.window, font=self.font)
        bet_in_entry.pack()

        def submit():
            self.bet = int(bet_in_entry.get())
            bet_in_submit.destroy()
            bet_in.config(text="Your bet: " + str(self.bet))
            bet_in_entry.forget()
            self.widgets.append(bet_in)
            if type(self.bet) == int:
                bet_in.config(text="Your bet: " + str(self.bet))
                if int(self.bet) > 1000000:
                    err2_label = tk.Label(self.window, font=self.font, text="I'm sorry, you can't bet that high! Try something smaller!")
                    err2_label.pack()
                    for i in self.widgets:
                        i.forget()
                    self.widgets.append(err2_label)
                    self.startGame()
                    return 0
                elif int(self.bet) <= 0:
                    err2_label = tk.Label(self.window, font=self.font, text="I'm sorry, you need to bet a positive amount!!")
                    err2_label.pack()
                    for i in self.widgets:
                        i.forget()
                    self.widgets.append(err2_label)
                    self.startGame()
                    return 0
            else: 
                bet_in.config(text="You must only input a valid postive integer")
            print("Test 5")
            for i in self.player.widgets:
                i.forget()
            bet_out = tk.Label(self.window, font=self.font,
                            text="All bets are in, lets play!")
            
            bet_out.pack(side=tk.TOP, pady=100)
            self.widgets.append(bet_out)
            for i in range(2):
                self.hand.append(random.choice(self.cards))
            self.dealer.append(random.choice(self.cards))
            self.dealer.append('?')
            self.checkHand()
            self.playGame()
        bet_in_submit = tk.Button(
            self.window, font=self.font, text="Submit", command=submit)
        bet_in_submit.pack()

    def playGame(self):
        print("Test 7")
        if self.turn == 1:
            print("Test 8")
            try:
                def hit():
                    for i in self.widgets:
                        i.forget()
                    hit_label.config(text="Hit!")
                    self.hand.append(random.choice(self.cards))
                    self.widgets.append(hit_label)
                    self.checkHand()
                    if self.hand_sum > 21:
                        print_slow("Bust!")
                        bust_notice = tk.Label(self.window, font=self.font, text="Bust!! \n You lost $" + str(self.bet))
                        bust_notice.pack()
                        self.player.editBalance(-(int(self.bet)))
                        self.widgets.append(bust_notice)
                        self.total = self.total - int(self.bet)
                        self.replay()
                    else:
                        self.playGame()
                def stand():
                    print("Test 10")
                    for i in self.widgets:
                        i.forget()
                    hit_label.config(text="You stand at: " + str(self.hand_sum))
                    self.widgets.append(hit_label)
                    self.turn = 0
                    self.playGame()
                #hit = input("Hit or stand?: ").lower()
                print("Test 9")
                hit_label = tk.Label(
                    self.window, font=self.font, text="Hit or stand?")
                hit_label.pack()

                hit_button = tk.Button(self.window, font=self.font, text="Hit", command=hit)
                hit_button.pack()
                self.widgets.append(hit_button)

                stand_button = tk.Button(
                    self.window, font=self.font, text="Stand", command=stand)
                stand_button.pack()
                self.widgets.append(stand_button)
            except ValueError:
                print_slow("Must indicate either 'hit' or 'stand' only")
                self.playGame()

        elif self.turn == 0:
            print("Test 11")
            self.game = 0
            for j in range(len(self.dealer)):
                if self.dealer[j] == '?':
                    self.dealer[j] = random.choice(self.cards)

            basic_stratergy_table = {
                (4, 5, 6, 7, 8, 9, 10, 11): "hit",
                (12, 13, 14): "hit_low",
                (15, 16): "hit_med",
                (17, 18, 19, 20, 21): "stand"
            }
            if self.dealer_sum > 21:
                win_label = tk.Label(self.window, font=self.font, text="Dealer Bust, You Win! You won: $" + str(self.bet))
                win_label.pack()
                self.player.editBalance(int(self.bet))
                self.widgets.append(win_label)
                self.total += self.bet
                self.replay()
            else:
                print("Dealer not bust")
                while self.game != 1:
                    for key in basic_stratergy_table:
                        #print("Next test")
                        if self.dealer_sum in key:
                            print("Test 12")
                            action = basic_stratergy_table[key]
                            if 'hit' in action:
                                self.dealer.append(random.choice(self.cards))
                                print("Dealer hit")
                                self.checkHand()
                            elif 'hit_low' in action:
                                if self.hand_sum < 13:
                                    dealer_action = tk.Label(self.window, font=self.font, text="Dealer stands at: " + str(self.dealer_sum))
                                    dealer_action.pack()
                                    self.widgets.append(dealer_action)
                                    print("Dealer Stands at: " +
                                          self.dealer_sum)
                                    if self.dealer_sum > self.hand_sum:
                                        win_label = tk.Label(self.window, font=self.font, text="Dealer Wins! You lost: $" + str(self.bet))
                                        win_label.pack()
                                        self.player.editBalance(-(str(self.bet)))
                                        self.widgets.append(win_label)
                                        self.game = 1
                                        self.replay()
                                        break
                                    else:
                                        win_label = tk.Label(self.window, font=self.font, text="You Win! You won: $" + str(self.bet))
                                        win_label.pack()
                                        self.player.editBalance((int(self.bet)))
                                        self.widgets.append(win_label)
                                        self.game = 1
                                        self.replay()
                                        break
                                else:
                                    print("Dealer hit low")
                                    self.dealer.append(
                                        random.choice(self.cards))
                                    self.checkHand()
                                    break
                            elif 'hit_med' in action:
                                print("Dealer hit med")
                                self.dealer.append(random.choice(self.cards))
                                self.checkHand()
                                break
                            elif 'stand' in action:
                                print("Dealer stand")
                                dealer_action = tk.Label(self.window, font=self.font, text="Dealer stands at: " + str(self.dealer_sum))
                                dealer_action.pack()
                                self.widgets.append(dealer_action)
                                if self.dealer_sum > self.hand_sum:
                                    win_label = tk.Label(self.window, font=self.font, text="Dealer Wins! You lost: $" + str(self.bet))
                                    win_label.pack()
                                    self.player.editBalance(-(int(self.bet)))
                                    self.widgets.append(win_label)
                                    self.total = self.total - int(self.bet)
                                    self.game = 1
                                    self.replay()
                                    break
                                elif self.dealer_sum == self.hand_sum:
                                    win_label = tk.Label(self.window, font=self.font, text="Its a draw! All bets are pushed")
                                    win_label.pack()
                                    self.widgets.append(win_label)
                                    self.game = 1
                                    self.replay()
                                    break
                                else:
                                    win_label = tk.Label(self.window, font=self.font, text="You Win! You won: $" + str(self.bet))
                                    win_label.pack()
                                    self.player.editBalance(int(self.bet))
                                    self.widgets.append(win_label)
                                    self.total += int(self.bet)
                                    self.game = 1
                                    self.replay()
                                    break
                            else:
                                break
                        else: 
                            pass
                    
            self.turn = 1
        else:
            exit()

def main(window, font):

    start_label = tk.Label(window, font=font, text="What's your name?")
    start_label.pack(expand=True)

    name_entry = tk.Entry(window, font=font)
    name_entry.pack()

    def submit_name(event):
        name = name_entry.get()
        start_label.destroy()
        name_entry.destroy()
        if name != "":
            readFile(name)
        else:
            pass

    name_entry.bind("<Return>", submit_name)

    def readFile(name):
        widgets = []
        with open("players.csv", 'r') as file:
            reader = csv.reader(file)
            exists = False
            print(exists)
            print("Test 1")
            for row in reader:
                print("Checking row")
                if name in row:
                    print("Test 2")
                    exists = True
                    active_row = row
                    # Write the new balance to file
                    # player.editBalance(newGame.total)
                else:
                    pass
            if exists == True:
                player = Player(active_row[0], active_row[1])
                player.checkBalance(window, font)
                newGame = Game(window, font, player)
                newGame.startGame()
                #Write the new balance to file
                player.editBalance(newGame.total)
            if exists == False:
                print("Test 4")
                start_label.destroy()
                err1_label = tk.Label(window, font=font, text=(
                    "Welcome " + str(name) + " to Blackjack! \n\nSince you're new, We'll start you off with $1000"))
                err1_label.pack()
                widgets.append(err1_label)
                balance = 1000
                if balance != "":
                    if type(balance) == int:
                        player = Player(name, balance)
                        with open("players.csv", 'a') as file:
                            writer = csv.writer(file)
                            array = [player.name, player.balance]
                            writer.writerow(array)
                        file.close()
                        newGame = Game(window, font, player)
                        for i in widgets:
                            i.forget()
                        newGame.startGame()
                    else: 
                        pass
                else:
                    pass
        file.close()
