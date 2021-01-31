
#!/usr/bin/python

import matplotlib.pyplot as plt
import argparse
import random
import seaborn as sns

def run_simulation(generate_plot=True, num_of_minigames=100, num_of_simulations=1000):
    """Run Monty Hall Simulation, either changing choosen door or not changing.
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
            random_list = random.sample(["C","G","G"], 3)
            random_choice = random.sample(range(3), 1)[0]
            # no change
            if random_list[random_choice] == 'C':
                no_change_wins += 1
            # change answer
            random_list.pop(random_choice)
            if "C" in random_list:
                change_wins += 1  
        
        no_change_wins_list.append((no_change_wins / num_of_minigames))
        change_wins_list.append((change_wins / num_of_minigames))


    no_change_percent_right = round(100 * (no_change_wins / num_of_minigames), 2)
    change_percent_right = round(100 * (change_wins / num_of_minigames), 2)

    print(f"If you never change your answer in {num_of_minigames} tries, you'll win the car about " \
            f"{no_change_percent_right}% of the time.")

    print(f"So if you always change your answer in {num_of_minigames} tries, you'll win the car about " \
            f"{change_percent_right}% of the time.")

    if generate_plot:
        plot_histogram(wins_list=change_wins_list, num_of_minigames=num_of_minigames, 
                num_of_simulations=num_of_simulations)


def plot_histogram(wins_list, num_of_minigames, num_of_simulations):
    sns.histplot(wins_list)
    plt.title(f"Frequency of Wins if you always change your mind ({num_of_minigames} games of {num_of_simulations} " \
            "simulations)")
    plt.xlabel("Fraction of Wins in One Game")
    plt.ylabel("Frequency of Game Wins")
    plt.show()
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Monty Hall Simulation!")
    parser.add_argument("--plot", "-p", type=bool, dest="generate_plot", help="bool, if True, plot will be generated."  
            , default=True)
    parser.add_argument("--num_of_minigames", "-m", type=int, dest="num_of_minigames", help="Number of minigames " \
            "within each simulation, 100 as default.", default=100)
    parser.add_argument("--num_of_simulations", "-s", type=int, dest="num_of_simulations", help="Number of simulated " \
            "minigames, 1000 as default.", default=1000)
    args = parser.parse_args()
    generate_plot, num_of_minigames, num_of_simulations = args.generate_plot, args.num_of_minigames, args.num_of_simulations
    run_simulation(generate_plot=generate_plot, num_of_minigames=num_of_minigames, num_of_simulations=num_of_simulations)
