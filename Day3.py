def sort_remove():
    sentense = sorted(set((input().split(' '))))
    print(' '.join(sentense))

sort_remove()