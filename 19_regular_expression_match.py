# 面试题19：正则表达式匹配
def match(str, pattern):
    if not str or not pattern:
        return False
    # 开始递归
    return match_core(str, pattern)

def match_core(str, pattern):
    if not str and not pattern:
        return True

    if (str and not pattern) or (not str and pattern):
        return False

    if len(pattern) > 1 and pattern[1] == '*':
        if str[0] == pattern[0] or (pattern[0] == '.' and str):
            return match_core(str, pattern[2:]) or \
                   match_core(str[1:], pattern) or \
                   match_core(str[1:], pattern[2:])
        else:
            return match_core(str, pattern[2:])

    if str[0] == pattern[0] or (pattern[0] == '.' and str):
        return match_core(str[1:], pattern[1:])
    else:
        return False


if __name__ == '__main__':
    str = "aaba"
    pattern = "ab*a*c*a"
    print(match(str, pattern))