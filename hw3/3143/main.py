import songlist

dct, plst = {}, []
while True:
    print("Input Song:")
    song = input().replace("Song ", "")
    if (song == "q"): break

    in_dct = songlist.query(dct, song)
    if in_dct:
        print("JJ has known this song writer: {}".format(in_dct))
    else:
        print("Writer is?")
        in_dct = input().replace("Singer ", "")
        dct = songlist.practice(dct, song, in_dct)
        plst.append(song)

print("JJ's song list:")
print(sorted(plst))
print("{} songs".format(len(plst)))

