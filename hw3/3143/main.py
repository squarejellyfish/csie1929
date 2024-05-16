import songlist

dct, plst = {}, []
while True:
    print("Input Song:")
    song = input().replace("Song ", "")
    if (song == "q"): break

    writer = songlist.query(dct, song)
    if (writer):
        print("JJ has known this song writer: {}".format(writer))
    else:
        print("Writer is?")
        writer = input().replace("Singer ", "")
        dct = songlist.practice(dct, song, writer)
        plst.append(song)

print("JJ's song list:")
print(sorted(plst))
print("{} songs".format(len(plst)))
