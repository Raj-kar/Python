playlist = {
    'title': 'Dil Bechara',
    'author': 'Raj kar',
    'songs': [
        {'title': 'song1', 'artist': ['A.singh'], 'duration':2.53},
        {'title': 'song2', 'artist': ['A.singh',
            'Shreya Ghoshal'], 'duration':3.25},
        {'title': 'song3', 'artist': ['A.R. Rahaman'], 'duration':3.13}
    ]
}

totalTime = 0.0;

for song in playlist['songs']:
	totalTime +=  song['duration']
	
print(totalTime)
