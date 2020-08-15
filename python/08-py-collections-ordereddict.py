#!/bin/python3

from collections import OrderedDict


def main():
    n = int(input())
    items = OrderedDict()

    for i in range(n):
        args = input().split()
        item_name = ' '.join(args[:-1])
        net_price = int(args[-1])

        if item_name not in items:
            items[item_name] = net_price
        else:
            items[item_name] += net_price

    for item, price in items.items():
        print(item, price)


if __name__ == '__main__':
    main()
