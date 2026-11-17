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
    songs = read_songs()
    print(f"{len(songs)} songs loaded")

    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "D":
            display_songs(songs)
        elif menu_choice == "R":
            recommended_song = recommend_song(songs)
            if recommended_song is not None:
                print(f"Let's learn... {recommended_song[0]} by {recommended_song[1]}")
            else:
                print("No songs to learn")
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


def read_songs():
    """Read songs from CSV into a nested list."""
    try:
        with open(FILENAME, 'r') as in_file:
            songs = []
            for line in in_file:
                title, artist, year, status = line.strip().split(",")
                songs.append([title, artist, int(year), status])
            sort_songs(songs)
        return songs
    except FileNotFoundError:
        print(f"ERROR: '{FILENAME}' not found")
        songs = []
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
    max_title_length, max_artist_length = get_display_widths(songs)
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
        return None
    else:
        random_unlearned_song = random.choice(unlearned_songs)
        return random_unlearned_song


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
    new_title, new_artist, new_year = get_valid_new_song_input()
    songs.append([new_title, new_artist, new_year, UNLEARNED])
    sort_songs(songs)
    print(f"{new_title} by {new_artist} ({new_year}) added to supply of songs")


def get_display_widths(songs: list[Any]) -> tuple[int, int]:
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


def get_unlearned_songs(songs) -> list[Any]:
    """Returns a list of unlearnt songs."""
    unlearned_songs = []
    for song in songs:
        if song[3] == UNLEARNED:
            unlearned_songs.append(song)
    return unlearned_songs


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


def get_valid_new_song_input() -> tuple[str, str, int]:
    """Collect nonblank, comma-free song details and a positive integer year."""
    while True:
        new_title = input("Title: ").strip()
        if "," in new_title:
            print("Song title can not contain commas")
        elif new_title != "":
            break
        else:
            print("Input can not be blank")
    while True:
        new_artist = input("Artist: ").strip()
        if "," in new_artist:
            print("Artist name can not contain commas")
        elif new_artist != "":
            break
        else:
            print("Input can not be blank")
    while True:
        try:
            new_year = int(input("Year: "))
            if new_year > 0:
                break
            else:
                print("Number must be > 0")
        except ValueError:
            print("Enter a valid integer")
    return new_title, new_artist, new_year


def save_songs(songs: list[Any]):
    with open(FILENAME, 'w') as out_file:
        for song in songs:
            print(f"{song[0]},{song[1]},{song[2]},{song[3]}", file=out_file)


if __name__ == '__main__':
    main()
