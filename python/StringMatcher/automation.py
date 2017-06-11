
def compute_transition(pattern):
    res = []
    for index in range(len(pattern)):
        transition = {}
        for char in set(pattern[0:index + 1]):
            next = min(len(pattern), index)

            while 

def match(text, pattern):
    transition = compute_transition(pattern)