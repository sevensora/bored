from string import ascii_letters, digits

for i in ascii_letters + digits:
    for j in ascii_letters + digits:
        for k in ascii_letters + digits:
            for l in ascii_letters + digits:
                for m in ascii_letters + digits:
                    for n in ascii_letters + digits:
                        print(i, j, k, l, m, n)
