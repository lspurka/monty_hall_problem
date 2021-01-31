#!/usr/bin/python

import argparse

from monty_hall import run_simulation

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
