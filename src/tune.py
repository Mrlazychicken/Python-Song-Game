# tune.py

import random
import os
import pygame
from time import sleep

# Set up pygame for playing music
pygame.init()


# Function to play a random song snippet
def play_random_song():
    # Add your song file paths here
    song_files = ["LifeOnMars.mp3"]
    random_song = random.choice(song_files)

    pygame.mixer.music.load(random_song)

    # Play a 15-second snippet of the song
    pygame.mixer.music.play(1, 0.0, 15)

    # Wait for the snippet to finish
    sleep(15)


# Function to get the player's guess
def get_player_guess():
    return input("Guess the song title: ")


# Function to check if the player's guess is correct
def check_guess(guess, correct_song):
    return guess.lower() == correct_song.lower()


def main():
    # Set up pygame mixer
    pygame.mixer.init()

    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to Name that Tune!")
    print("Listen to the song snippet and guess the song title.")

    play_random_song()

    # Replace these with the actual song titles
    correct_song_title = "Example Song"

    player_guess = get_player_guess()

    if check_guess(player_guess, correct_song_title):
        print("Congratulations! You guessed the correct song title.")
    else:
        print(f"Sorry, the correct song title was: {correct_song_title}")

    # Clean up pygame mixer
    pygame.mixer.quit()


if __name__ == "__main__":
    main()
