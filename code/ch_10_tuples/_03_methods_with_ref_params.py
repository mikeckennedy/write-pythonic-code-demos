import math


def main():
    args = list()
    out_params_bad(7, args)
    print(f"Return values (bad):   {args[0]} & {args[1]:.2f}")

    # can we do better?
    v1, v2 = out_params(7)
    print(f"Return values (good):  {v1} & {v2:.2f}")


# pythonic!
def out_params(base: float):
    r1 = base * base
    r2 = math.sqrt(base * base * base)

    return r1, r2


# non-pythonic!
def out_params_bad(base: float, args: list):
    if len(args) == 0:
        args.append(0)
        args.append(0)

    if len(args) != 2:
        raise Exception("Need to return values")

    args[0] = base * base
    args[1] = math.sqrt(base * base * base)


if __name__ == '__main__':
    main()
