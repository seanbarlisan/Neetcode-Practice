def plusOne(digits):
        digitsLength = len(digits) - 1
        flag = False
        while digitsLength > -1:
            if digits[digitsLength] == 9:
                digits[digitsLength] = 0
                flag = True
            elif digits[digitsLength] != 9:
                digits[digitsLength] += 1
                break
            
            digitsLength -= 1
            

        if flag: # the logic needs to be fixed here
            if digits[0] == 0:
                digits.insert(0, 1)
            else:
                return digits
        else:
            return digits
        # if flag:
        #     digits.insert(0, 1)
        # else:
        #     return digits

        # return digits
    

if __name__ == "__main__":
    digitList = [8, 9, 9, 9]
    plusOne(digitList)
    print(digitList)

# need to account for edge case of [8, 9, 9, 9] -> [9, 0, 0, 0]