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
            
        if flag:
            digits.insert(0, 1)
        else:
            return digits

        return digits
    

if __name__ == "__main__":
    digitList = [1, 2, 3, 4]
    plusOne(digitList)