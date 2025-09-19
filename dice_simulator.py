"""
Dice Simulator
Author: Your Name
Description: Simulate rolling two dice multiple times, calculate probabilities, 
and plot a histogram of results.
"""

import random
import matplotlib.pyplot as plt

def roll_dice(sides=6):
    """Simulate rolling two dice with 'sides' sides each and return their sum."""
    die1 = random.randint(1, sides)
    die2 = random.randint(1, sides)
    return die1 + die2

def simulate_rolls(n_rolls, sides=6):
    """Simulate rolling dice n_rolls times and return a dictionary of frequencies."""
    min_sum = 2
    max_sum = sides * 2
    results = {total: 0 for total in range(min_sum, max_sum + 1)}

    for _ in range(n_rolls):
        total = roll_dice(sides)
        results[total] += 1

    return results

def display_results(results, n_rolls):
    """Print frequencies and probabilities of each sum."""
    print("\nSum | Frequency | Probability")
    print("-" * 30)
    for total in sorted(results.keys()):
        freq = results[total]
        prob = freq / n_rolls
        print(f"{total:>3} | {freq:>9} | {prob:.3f}")

def plot_histogram(results):
    """Plot a histogram of dice roll results."""
    sums = list(results.keys())
    frequencies = list(results.values())

    plt.bar(sums, frequencies, color='skyblue')
    plt.xlabel('Dice Sum')
    plt.ylabel('Frequency')
    plt.title('Dice Roll Simulation Results')
    plt.xticks(sums)
    plt.show()

def calculate_expected_value(results, n_rolls):
    """Calculate and return the expected value of the dice sum."""
    return sum(total * freq for total, freq in results.items()) / n_rolls

if __name__ == "__main__":
    print("Welcome to the Dice Simulator!")
    n_rolls = int(input("How many times do you want to roll the dice? "))
    sides = int(input("How many sides should each die have? (default 6) "))

    results = simulate_rolls(n_rolls, sides)
    display_results(results, n_rolls)

    expected_value = calculate_expected_value(results, n_rolls)
    print(f"\nExpected value of dice sum: {expected_value:.2f}")

    plot_histogram(results)

