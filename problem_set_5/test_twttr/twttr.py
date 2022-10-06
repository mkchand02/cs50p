"""
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""


def main():
    inp_str = input("Input: ")
    out_str = shorten(inp_str)
    print(out_str)


def shorten(word):
    """expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted"""
    out_list = []
    vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    for ch in word:
        if ch not in vowel_set:
            out_list.append(ch)

    out_str = "".join(out_list)
    return out_str


if __name__ == "__main__":
    main()
