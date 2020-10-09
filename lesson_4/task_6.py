from itertools import count
from itertools import islice
from itertools import cycle

try:
    low_bound = int(input("Enter low bound:"))
    top_bound = int(input("Enter top bound:"))
    if low_bound <= 0 or top_bound <= 0 or top_bound <= low_bound:
        raise Exception('Wrong parameters! Bounds must be > 0 and the Low must be less than the Top!')
    # Variant 1.
    print("Variant 1")
    el = count(low_bound)
    while str(el) != "count(" + str(top_bound + 1) + ")":
        print(str(el.__next__()))

    # Variant 2.
    print("Variant 2")
    for el in islice(count(low_bound), top_bound - low_bound + 1):
        print(el)

    pr_lang = ["python", "java", "perl", "javascript"]
    cur_iter = cycle(pr_lang)

    for i in range(low_bound, top_bound + 1):
        print(next(cur_iter))

except Exception as e:
    print(f"Error: ", str(e))
