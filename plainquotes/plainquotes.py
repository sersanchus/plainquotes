def plain_quotes(value, quote_char="'"):
    """ Auto plain nested quotes in a string. """

    QUOTES = ['"', "'"]

    stack = []
    quotes_and_levels = []
    pos = 0
    level = -1
    size = len(value)
    while pos < size:
        best_beg = None
        for ch in QUOTES:
            beg = value.find(ch, pos)
            if beg != -1 and (best_beg is None or beg < best_beg[0]):
                best_beg = (beg, ch)
        if best_beg:
            if len(stack) > 0 and best_beg[1] == stack[-1][1]:
                quotes_and_levels.append((stack[-1][0], best_beg[1], level))
                quotes_and_levels.append((best_beg[0], best_beg[1], level))
                level-=1
                stack.pop()
            else:
                level+=1
                stack.append(best_beg)
            pos = best_beg[0] + 1
        else:
            break

    quotes_and_levels = sorted(quotes_and_levels, key=lambda x: x[0], reverse=True)

    value_list = list(value)
    for quote in quotes_and_levels:
        quote_pos = quote[0]
        if quote[2] > 0:
            value_list[quote_pos] = '\\' * pow(2, quote[2] - 1) + quote_char
        elif value_list[quote_pos] != quote_char:
            value_list[quote_pos] = quote_char
    value = ''.join(value_list)

    return value
