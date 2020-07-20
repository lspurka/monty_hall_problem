
#!/usr/bin/python

import matplotlib.pyplot as plt
import random
import seaborn as sns

def run_simulation(generate_plot=True, num_of_minigames=100, num_of_simulations=1000):
    """Run Monty Hall Simulation, either changing choosen door or not changing.
    :param generate_plot: bool, if True, will generate plot
    :param num_of_minigames: int, number of minigames within each simulation
    :param num_of_simulations: int, number of simulated minigames
    :return change_wins_list
    """

    # TODO update these variable names
    no_change_wins_list = []
    change_wins_list = []

    # TODO Double-check logic:
    for y in range(num_of_simulations):
        no_change_wins = 0.0
        change_wins = 0.0
        for x in range(num_of_minigames):
            random_list = random.sample(['C','G','G'], 3)
            random_choice = random.sample(range(3), 1)[0]
            # no change
            if random_list[random_choice] == 'C':
                no_change_wins += 1
            # change answer
            other_2_options = []
            for count, item in zip(range(3), random_list):
                if count != random_choice:
                    other_2_options.append(random_list[count])
            if 'C' in other_2_options:
                change_wins += 1  
        
        no_change_wins_list.append((no_change_wins / num_of_minigames))
        change_wins_list.append((change_wins / num_of_minigames))


    no_change_percent_right = round(100 * (no_change_wins / num_of_minigames), 2)
    change_percent_right = round(100 * (change_wins / num_of_minigames), 2)

    print(f"If you never change your answer in {num_of_minigames} tries, you'll win the car \
            {no_change_percent_right}% of the time.")

    print(f"If you always change your answer in {num_of_minigames} tries, you'll win the car {change_percent_right}% \ 
            of the time.")



# TODO make this into a function
# Make distribution of outcomes
sns.distplot(change_wins_list)
plt.title(f"Frequency of Wins if you always change your mind ({num_of_minigames} games of {total_num_of_tries} times\
         changing your mind within each game)")
plt.xlabel("Fraction of Wins in One Game")
plt.ylabel("Frequency of Game Wins")
plt.show()
plt.close()






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Monty Hall Simulation!")
    parser.add_argument("--plot", "-p", type=bool, dest="generate_plot", help="bool, if True, plot will be generated.")
    parser.add_argument("--num_of_minigames", "-m", type=int, dest="num_of_minigames", help="Number of minigames within each simulation, 100 as default.")
    parser.add_argument("--num_of_simulations", "-s", type=int, dest="num_of_simulations", help="Number of simulated minigames, 1000 as default.")
    args = parser.parse_args()
    generate_plot, num_of_minigames, num_of_simulations = args.generate_plot, args.num_of_minigames, 
            args.num_of_simulations
    run_simulation(generate_plot=generate_plot, num_of_minigames=num_of_minigames,      
            num_of_simulations=num_of_simulations)
