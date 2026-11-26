"""
Name: Pavel Habermann
Date started: 21/10/2026
GitHub URL: https://github.com/cp1404students/cp1404-2026-tr3-a1-song-supply-pjhabermann/tree/main
"""

import random
from operator import itemgetter
from typing import Any

LEARNED = "l"
UNLEARNED = "u"
CLASSIC_CUTOFF = 1975
FILENAME = "songs.csv"
MENU = """D - Display Songs
R - Recommend a random song
A - Add a new song
C - Complete a song
Q - Quit"""


def main():
    """Run the Song Supply program and manage the main menu.

    It loads songs from the CSV file at the start and only saves them back once the user selects Q.
    It holds a list of songs in RAM while the user is navigating the menu.
    """
    print("Song Supply 1.0 - by Pavel Habermann")
    songs = load_songs()
    print(f"{len(songs)} songs loaded")
    print(MENU)
    menu_choice = input(">>> ").upper()

    while menu_choice != "Q":
        if menu_choice == "D":
            display_songs(songs)
        elif menu_choice == "R":
            recommended_song = recommend_song(songs)
        elif menu_choice == "A":
            add_song(songs)
        elif menu_choice == "C":
            complete_song(songs)
        else:
            print("Invalid menu choice")
        print(MENU)
        menu_choice = input(">>> ").upper()

    save_songs(songs)
    print(f"{len(songs)} songs saved to {FILENAME}")
    print("Enjoy the music!")


def load_songs():
    """Read songs from CSV into a nested list."""
    songs = []
    try:
        with open(FILENAME, 'r') as in_file:
            for line in in_file:
                title, artist, year, status = line.strip().split(",")
                songs.append([title, artist, int(year), status])
            sort_songs(songs)
    except FileNotFoundError:
        print(f"ERROR: '{FILENAME}' not found")
    return songs


def sort_songs(songs: list[Any]):
    """Sort the original song list in place based on year then name."""
    songs.sort(key=itemgetter(2, 0))


def display_songs(songs: list[Any]):
    """Displays an ordered songs list with learning markers and classic labels."""
    if not songs:
        print("No songs")
        return

    learned_count = 0
    max_title_length, max_artist_length = determine_display_widths(songs)
    for index, song in enumerate(songs, start=1):
        if song[3] == LEARNED:
            marker = ""
            learned_count += 1
        else:
            marker = "*"

        if is_classic(song):
            classic_status = "(classic)"
        else:
            classic_status = ""

        print(
            f"{index:>2}.{marker:>2} "
            f"{song[0]:<{max_title_length + 2}}- "
            f"{song[1]:<{max_artist_length}} "
            f"{song[2]:>4} {classic_status}"
        )

    print(f"{learned_count} songs learned, {len(songs) - learned_count} songs still to learn")


def recommend_song(songs) -> list | None:
    """Returns a randomly selected unlearned song or None if none remains."""
    unlearned_songs = get_unlearned_songs(songs)
    if not unlearned_songs:
        print("No songs to learn")
    else:
        random_unlearned_song = random.choice(unlearned_songs)
        print(f"Let's learn... {random_unlearned_song[0]} by {random_unlearned_song[1]}")


def get_unlearned_songs(songs) -> list[Any]:
    """Creates a list of all the current unlearned songs"""
    unlearned_songs = [song for song in songs if song[3] == UNLEARNED]
    return unlearned_songs


def complete_song(songs: list[Any]):
    """Changes a selected unlearnt song to learnt if there are unlearnt songs left."""
    unlearned_songs = get_unlearned_songs(songs)
    if not unlearned_songs:
        print("No songs to learn")
    else:
        print("Enter the number of a song to mark as learned")
        song_choice = get_valid_song_choice(songs)
        song = songs[song_choice - 1]
        if song[3] == UNLEARNED:
            song[3] = LEARNED
            print(f"{song[0]} by {song[1]} learned")
        else:
            print("You have already learnt this song!")


def add_song(songs: list[Any]):
    """Add validated new songs to list and maintains ordering criteria."""
    print("Enter details for a new song.")
    song = get_song()
    songs.append(song)
    sort_songs(songs)
    print(f"{song[0]} by {song[1]} ({song[2]}) added to supply of songs")


def determine_display_widths(songs: list[Any]) -> tuple[int, int]:
    """Return the maximum title and artist lengths for aligning display columns."""
    max_title_length = 0
    max_artist_length = 0
    for song in songs:
        if max_title_length < len(song[0]):
            max_title_length = len(song[0])

        if max_artist_length < len(song[1]):
            max_artist_length = len(song[1])
    return max_title_length, max_artist_length


def is_classic(song) -> bool:
    return song[2] <= CLASSIC_CUTOFF


def get_valid_song_choice(songs: list[Any]) -> int:
    """Returns a valid song choice from the display list."""
    while True:
        try:
            song_choice = int(input(">>> "))
            if 0 < song_choice <= len(songs):
                break
            elif song_choice > len(songs):
                print("Invalid song number")
            else:
                print("Number must be > 0")
        except ValueError:
            print("Enter a valid integer")
    return song_choice


def get_song() -> list[str | int]:
    """Collect nonblank song details and a positive integer year and returns them"""
    new_title = get_valid_string("Title: ")
    new_artist = get_valid_string("Artist: ")
    while True:
        try:
            new_year = int(input("Year: "))
            if new_year > 0:
                break
            else:
                print("Number must be > 0")
        except ValueError:
            print("Enter a valid integer")
    return [new_title, new_artist, new_year, UNLEARNED]


def get_valid_string(prompt: str) -> str:
    """Checks string inputs aren't empty"""
    string = input(prompt)
    while string == "":
        print("Input can not be blank")
        string = input(prompt)
    return string


def save_songs(songs: list[Any]):
    """Saves sorted song list to CSV file"""
    with open(FILENAME, 'w') as out_file:
        for song in songs:
            print(f"{song[0]},{song[1]},{song[2]},{song[3]}", file=out_file)


if __name__ == '__main__':
    main()
