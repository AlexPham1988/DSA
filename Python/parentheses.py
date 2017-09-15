import os

dict = {
    '(':')',
    '{':'}',
    '[':']',
}



def isValid(str):
    stack = []
    for i in str:
        if i in dict:
            stack.append(i)
        else:
            if not stack:
                return 0
            else:
                last = stack[-1]
                if (i == dict[last]):
                    stack.pop()
                else:
                    stack.append(i)
    if not stack:
        return 1
    else:
        return 0


def getMaxValidLength(str):
    stack = []
    stack_index = []
    stack_index.append(-1)
    max_len = 0
    max_from = 0
    max_to = 0
    for i in range (0,len(str)):
        if str[i] in dict:
            stack.append(str[i])
            stack_index.append(i)
        else:
            if stack:
                last = stack[-1]
                if last in dict:
                    if (str[i] == dict[last]):
                        stack.pop()
                        stack_index.pop()
                        current = stack_index[-1]
                        l = i - current
                        if(l > max_len):
                            max_len = l
                            max_from = current + 1
                            max_to = i
                    else:
                        stack.append(str[i])
                        stack_index.append(i)
                else:
                    stack.append(str[i])
                    stack_index.append(i)
            else:
                stack.append(str[i])
                stack_index.append(i)
    return [max_len,max_from,max_to]



# str = '(()[[]])'
# print isValid(str)



# str = '([()(()[])'
str = '][()[()()][()'

print getMaxValidLength(str)

# print dict[']']
