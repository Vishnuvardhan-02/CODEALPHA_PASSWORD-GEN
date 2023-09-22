import random #random module imported


def password_gen(len): #created a function to generate password
    list_of_combination = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

    generated_pass = random.sample(list_of_combination,len)

    pass_data = "".join(generated_pass)

    return pass_data


if __name__ == "__main__": # =main function that gets input from user for number of characters
    len = int(input("Enter number of characters needed?"))

    pass_data = password_gen(len)

    print("The Password is ", pass_data) #final outcome
