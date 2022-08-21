
def reverse_string(string):
    if (len(string)==1):
        return string
    else:
        return reverse_string(string[1:])+string[0] #takes out the first letter of the string "1" then adds the letter
                                                                               #to the end  "0"  and sends the new modified string back through the function

def main():
    in_str=input("Enter a string: ")
    result= reverse_string(in_str)
    print(result)



main()

