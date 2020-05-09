import Module.Queue as q


def ularNaga(nama, hitungan):
    gameQueue = q.createQueue()
    for namaAnak in nama:
        q.enqueue(gameQueue, namaAnak)
    print('Peserta Permainan=', gameQueue)
    while q.size(gameQueue) > 1:
        for i in range(hitungan):
            q.enqueue(gameQueue, q.dequeue(gameQueue))
            print('hitungan ke-', i+1, '=', gameQueue)
        q.dequeue(gameQueue)
        print('Peserta Permainan=', gameQueue)
    return gameQueue


ularNaga(['fatin', 'ajeng', 'sindy', 'shafa', 'indah', 'mala'], 2)

