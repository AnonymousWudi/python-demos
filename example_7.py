# coding=utf-8


def format_duration(seconds):
    temp_list = []
    temp_index = 0
    temp_deno = 60
    temp_text = ''
    while seconds != 0:
        temp_value = seconds % temp_deno
        seconds /= temp_deno
        if temp_value:
            temp_list.insert(0, str(temp_value))
            if temp_index == 0:
                temp_text = 'second'
            elif temp_index == 1:
                temp_text = 'minute'
            elif temp_index == 2:
                temp_text = 'hour'
            elif temp_index == 3:
                temp_text = 'day'
            elif temp_index == 4:
                temp_text = 'year'
            if temp_value > 1:
                temp_text += 's'
            temp_list.insert(1, temp_text)
        if seconds == 0:
            break
        if temp_index == 0:
            temp_deno = 60
        elif temp_index == 1:
            temp_deno = 24
        elif temp_index == 2:
            temp_deno = 365
        temp_index += 1
    result = ''
    if not temp_list:
        return 'now'
    if len(temp_list) == 2:
        return '%s %s' % (temp_list[0], temp_list[1])
    else:
        for i in range(len(temp_list)):
            if i == len(temp_list) - 3:
                result += temp_list[i] + ' and '
            elif i % 2 == 0:
                result += temp_list[i] + ' '
            elif i % 2 == 1 and i != len(temp_list) - 1:
                result += temp_list[i] + ', '
            else:
                result += temp_list[i]
    return result

if __name__ == '__main__':
    seconds = 0
    print format_duration(seconds)
