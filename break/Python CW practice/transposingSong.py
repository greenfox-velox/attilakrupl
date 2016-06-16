listOfSharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
listOfFlats = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']


def transpose(song, interval):
    newSong = []
    position = 0
    for note in song:
        if note in listOfSharps:
            position = listOfSharps.index(note)
        else:
            position = listOfFlats.index(note)
        newSong.append(listOfSharps[position+(interval%12)])
    return newSong
    

print (transpose(['Bb', 'C#', 'E'], -4))