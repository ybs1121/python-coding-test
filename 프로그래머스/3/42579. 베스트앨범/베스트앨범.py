def solution(genres, plays):
    answer = []
    songs = {}
    type_dict = {}

    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre in songs:  # 장르가 이미 있을때
            song = songs[genre]
            song.append([play, index])
            song.sort(key=lambda x: (x[0], -x[1]), reverse=True)
            print(song)
            songs[genre] = song
            type_dict[genre] = type_dict[genre] + play
        else:  # 장르가 없을 때
            songs[genre] = [[play, index]]

            type_dict[genre] = play

    sorted_keys = [item[0] for item in sorted(type_dict.items(), key=lambda item: item[1], reverse=True)]

    for i in sorted_keys:
        gen_songs = songs[i]
        n = 0
        for j in range(len(gen_songs)):
            print(gen_songs[j])
            if n == 2:
                break
            answer.append(gen_songs[j][1])
            n = n + 1

    print(answer)
    return answer