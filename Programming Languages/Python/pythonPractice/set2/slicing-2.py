'''
    🔥 Tricky Slicing Exercises

    Skip–Take Pattern
    From s = "abcdefghijklmnopqrstuvwxyz",
    get "acegikmoqsuwy" (every other letter).

    Chunk Out the Middle
    From nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],
    get [4, 5, 6].

    Reverse in Chunks
    From s = "abcdefghij",
    get "cba fed jih" (reverse every group of 3).
    (Hint: you’ll need slicing inside slicing.)

    Mirror Trick
    From word = "mirror",
    get "mirrorrim".

    Matrix Diagonal (Bonus 🔥)
    Given:

    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    Use slicing to get the diagonal [1, 5, 9].

    💡 The last one is a little sneaky because slicing isn’t always obvious in 2D — but you can pair it with range stepping or comprehension.
'''

def main():
    s = "abcdefghijklmnopqrstuvwxyz"
    print(s[::2])

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(nums[3:-3])

    s2 = "abcdefghij"
    print(" ".join(s2[i:i+3][::-1] for i in range(0, len(s2), 3)))

    # more simple way for the above
    print(f"{s2[0:3][::-1]} {s2[3:6][::-1]} {s2[6:9][::-1]} {s2[9:][::-1]}")

    word = "mirror"
    print(f"{word[0:5]}{word[0:4][::-1]}") # works only for mirror
    print(word + word[2::-1])

    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    middles = []

    for i,box in enumerate(mat):
        middles.append(box[i])

    print(middles)




if __name__ == "__main__":
    main()