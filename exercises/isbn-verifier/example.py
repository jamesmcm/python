import string

def verify_isbn(isbn):
    handleX = lambda x: 10 if x == 'X' else x
    nums = [int(handleX(x)) for x in isbn if x in string.digits+'X']
    return(sum([x*(10-ind) for ind, x in enumerate(nums)]) % 11 == 0)

