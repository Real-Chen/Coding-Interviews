# 20：表示数值的字符串
def scan_integer(num_str, i):
    if i < len(num_str) and (num_str[i] == "+" or num_str[i] == "-"):
        return scan_unsigned_integer(num_str, i + 1)
    return scan_unsigned_integer(num_str, i)

def scan_unsigned_integer(num_str, i):
    raw_pos = i
    while i < len(num_str) and num_str[i] >= '0' and num_str[i] <= '9':
        i += 1
    return (raw_pos < i), i

def is_numeric(num_str):
    if not num_str:
        return False
    if_num, i = scan_integer(num_str, 0)
    if i < len(num_str) and num_str[i] == '.':
        if_decimal, i = scan_unsigned_integer(num_str, i+1)
        if_num = if_num or if_decimal
    if i < len(num_str) and (num_str[i] == 'E' or num_str[i] == 'e'):
        if_exponent, i = scan_integer(num_str, i+1)
        if_num = if_num and if_exponent
    return if_num and i == len(num_str)


if __name__ == '__main__':
    num_strs = ["+100", "5e2", "-123", "3.1416", "-1E-16",
                "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4", ".", "e", ""]
    for str in num_strs:
        print(str, is_numeric(str))