
def list_sum_basic(num_list):
    result = 0

    for item in num_list:
        result = result + item

    return result


def list_sum_recursion(num_list):
    if len(num_list) <= 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursion(num_list[1:])


def main():
    print "list_sum_basic:", list_sum_basic([1,3,5,7,9])
    print "lcist_sum_recursion:", list_sum_recursion([1,3,5,7,9])

if __name__ == '__main__':
    main()