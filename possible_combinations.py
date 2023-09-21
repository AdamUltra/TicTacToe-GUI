def possibilities(num):
    import random
    all_combs = []
    bad = 0
    while bad < 5000:
        UInp = str(num)
        while bad < 5000:
            new_comb = tuple(random.sample(UInp, k=3))
            sorted_num = sorted(new_comb)
            transition = ""
            for i in sorted_num:
                if i.isdigit():
                    transition += i

            sorted_num = int(transition)
            if sorted_num not in all_combs:
                all_combs.append(sorted_num)
                bad = 0

            else:
                bad += 1

    return all_combs
