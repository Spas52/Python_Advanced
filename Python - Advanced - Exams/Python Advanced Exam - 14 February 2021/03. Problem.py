from collections import deque


def stock_availability(flavours, action, *args):
    flavours = deque(flavours)
    if action == "delivery":
        for item in args:
            flavours.append(item)
    elif action == "sell":
        if args:
            for par in args:
                if isinstance(par, int):
                    for rem in range(par):
                        flavours.popleft()
                elif isinstance(par, str):
                    if par in flavours:
                        count = flavours.count(par)
                        if count > 1:
                            flavours = set(flavours)
                            flavours = list(flavours)
                        flavours.remove(par)
        else:
            flavours.popleft()
    return list(flavours)


print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


