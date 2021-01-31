import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

def run_simulation(generate_plot=True, num_of_minigames=100, num_of_simulations=1000):
    """Run Monty Hall Simulation, either changing the choosen door or not changing.
    Monty Hall Problem explained here: https://en.wikipedia.org/wiki/Monty_Hall_problem
    :param generate_plot: bool, if True, will generate plot
    :param num_of_minigames: int, number of minigames within each simulation
    :param num_of_simulations: int, number of simulated minigames
    :return None
    """

    no_change_wins_list = []
    change_wins_list = []

    for y in range(num_of_simulations):
        no_change_wins = 0.0
        change_wins = 0.0
        for x in range(num_of_minigames):
            selection_list = random.sample(["car", "goat", "goat"], 3)
            player_choice = random.sample(range(3), 1)[0]
            # no change
            if selection_list[player_choice] == "car":
                no_change_wins += 1
            # change answer
            # The following logic works out because one of the doors is opened, revealing a goat.  If the player changes
            # their choice, then there is just one door remaining.  We can essentially get rid of the player_choice and
            # if either remaining choice is the car, the player wins.
            selection_list.pop(player_choice)
            if "car" in selection_list:
                change_wins += 1  
        
        no_change_wins_list.append((no_change_wins / num_of_minigames))
        change_wins_list.append((change_wins / num_of_minigames))

    no_change_percent_right = round(100 * (np.array(no_change_wins_list).mean()), 2)
    change_percent_right = round(100 * (np.array(change_wins_list).mean()), 2)

    print(f"If you never change your choice in {num_of_minigames} games, you'll win the car about " \
            f"{no_change_percent_right}% of the time.")

    print(f"So if you always change your choice in {num_of_minigames} games, you'll win the car about " \
            f"{change_percent_right}% of the time.")

    if generate_plot:
        plot_histogram(wins_list=change_wins_list, num_of_minigames=num_of_minigames, 
                num_of_simulations=num_of_simulations)


def plot_histogram(wins_list, num_of_minigames, num_of_simulations):
    sns.histplot(wins_list)
    plt.title(f"Frequency of Wins if you always change your choice ({num_of_minigames} games of {num_of_simulations} " \
            "simulations)")
    plt.xlabel("Fraction of Wins in One Game")
    plt.ylabel("Frequency of Game Wins")
    plt.show()
    plt.close()
