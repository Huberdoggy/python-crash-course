from functions import make_album

# Init this variable as falsey
store_songs = None
song_list = []

while True:
    print(f"\nYou will be prompted to enter the name of an artist,"
          " an album title,\nand optionally, the number of songs in the specified album.")
    print("Enter 'q' at any time to quit")

    a_name = input("Their name? => ")
    if a_name == 'q':
        break
    album_t = input("The album title? => ")
    if album_t == 'q':
        break
    ask_songs = input("Include number of songs? (y/n) => ")
    if ask_songs == 'y':
        store_songs = input("How many? => ")
    else:
        print("Okay, skipping that...'songs' is optional.")

    if store_songs:
        formatted_album = make_album(a_name, album_t, store_songs)
    else:
        formatted_album = make_album(a_name, album_t)
    # Reassign store_songs to a falsey value so that the next iteration
    # won't reuse whatever global value is stored in it if the user chose 'yes' include songs on the previous run
    store_songs = None
    print('-' * 70)
    print(f"Here's your selection: \n\t{formatted_album}")
    song_list.append(formatted_album)

print(f"\nAnd here's all the stored song data from today's input:\n\n\t*****SONGS IN THE LIST*****")
for info in song_list:
    print(f"\n\t{info}")