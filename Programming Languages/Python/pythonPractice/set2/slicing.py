'''
    Try to write the slicing expressions for these:

    Given nums = [10, 20, 30, 40, 50, 60] → get [30, 40, 50]

    From "racecar" → get "aceca" (the middle section).

    From [1, 2, 3, 4, 5, 6] → get [6, 4, 2] (reverse every other element).

    From "python" → reverse it into "nohtyp".
'''

def main():
    nums = [10, 20, 30, 40, 50, 60]
    print(nums[2:5])
    print(nums[2:-1])


    s = "racecar"
    print(s[1:-1])
    print(s[1:6])

    nums2 = [1, 2, 3, 4, 5, 6]
    print(nums2[::-2])

    s2 = "python"
    print(s2[::-1])





if __name__ == "__main__":
    main()