# coding=utf-8

if __name__ == '__main__':
    init_str = raw_input()
    chg_times = int(raw_input())
    str_list = list(init_str)
    for i in range(chg_times):
        p, l = raw_input().split()
        p, l = int(p), int(l)
        list_reverse = str_list[p:p+l]
        list_reverse.reverse()
        for j in range(p+l, p+l+l):
            str_list.insert(j, list_reverse[j - p - l])
    str_result = ''
    for s in str_list:
        str_result += s
    print str_result