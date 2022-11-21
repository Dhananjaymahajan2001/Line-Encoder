import matplotlib.pyplot as plot
import numpy as np
import random

# Decoder Function


def dec_NRZL(data_nrzl):
    data = []
    for i in range(1, len(data_nrzl)):
        if data_nrzl[i] == -1:
            data.append(0)
        elif data_nrzl[i] == 1:
            data.append(1)
    return data


def dec_NRZI(data_nrzi):
    data = []
    if data_nrzi[1] == 1:
        data.append(1)
    else:
        data.append(0)
    for i in range(2, len(data_nrzi)):
        if data_nrzi[i] == data_nrzi[i - 1]:
            data.append(0)
        else:
            data.append(1)
    return data


def dec_Manchester(data_manc):
    data = []
    if data_manc[1] == 1:
        data.append(1)
    else:
        data.append(0)
    for i in range(3, len(data_manc), 2):
        if data_manc[i] == 1:
            data.append(1)
        else:
            data.append(0)
    return data


def dec_DManchester(data_dmanc):
    data = []
    if data_dmanc[1] == 1:
        data.append(1)
    else:
        data.append(0)
    for i in range(3, len(data_dmanc), 2):
        if data_dmanc[i] == data_dmanc[i - 2]:
            data.append(0)
        else:
            data.append(1)
    return data


def dec_AMI(data_ami):
    data = []
    for i in range(1, len(data_ami)):
        if data_ami[i] == 0:
            data.append(0)
        else:
            data.append(1)
    return data


def dec_B8ZS(data_b8zs):
    data = []
    prev = -1
    i = 1
    while i in range(len(data_b8zs)):
        if data_b8zs[i] == 0:
            data.append(0)
        elif data_b8zs[i] == -prev:
            data.append(1)
            prev = -prev
        else:
            for x in range(5):
                data.append(0)
            i = i + 4
        i = i + 1
    return data


def dec_HDB3(data_hdb3):
    data = []
    prev = -1
    i = 1
    while i in range(len(data_hdb3)):
        if data_hdb3[i] == 0:
            data.append(0)
        elif data_hdb3[i] == -prev:
            data.append(1)
            prev = -prev
        else:
            data.append(0)
            data[i - 4] = 0
        i = i + 1
    return data


# Palindrome

# Manacher Algorithm O(n)

# src leetcode


def longestPalindrome(str_list):
    s = ''.join(str(i) for i in str_list)
    print(s)
    max_len = 1
    start = 0
    for i in range(len(s)):
        if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
            start = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
            start = i - max_len
            max_len += 1
    return s[start:start + max_len]


# Encoder

# scrambling using sliding window algorithm

def B8ZS(data):
    prev = -1
    count = 0
    s = 1
    e = 1
    n = len(data)
    data_b8zs = [0]
    while s <= n and e <= n:
        if data[e - 1] == 0:
            data_b8zs.append(0)
            count = count + 1
            if count == 8:
                data_b8zs[s + 3] = prev
                data_b8zs[s + 4] = -prev
                data_b8zs[s + 6] = -prev
                data_b8zs[s + 7] = prev
                count = 0
                s = e + 1
        else:
            prev = -prev
            data_b8zs.append(prev)
            s = e + 1
            count = 0
        e = e + 1
    return data_b8zs


def HDB3(data):
    prev = -1
    count = 0
    f = 0
    s = 1
    e = 1
    n = len(data)
    data_hdb3 = [0]
    while s <= n and e <= n:
        if data[e - 1] == 0:
            data_hdb3.append(0)
            count = count + 1
            if count == 4:
                if f == 0:
                    data_hdb3[s] = -prev
                    data_hdb3[e] = -prev
                    prev = -prev
                    count = 0
                    s = e + 1
                else:
                    data_hdb3[e] = prev
                    f = 0
                count = 0
                s = e + 1
        else:
            prev = -prev
            if f == 0:
                f = 1
            else:
                f = 0
            data_hdb3.append(prev)
            s = e + 1
            count = 0
        e = e + 1
    return data_hdb3


def NRZ_L(data):
    data_nrzl = [0]
    for i in range(len(data)):
        if data[i] == 0:
            data_nrzl.append(-1)
        elif data[i] == 1:
            data_nrzl.append(1)
    return data_nrzl


def NRZ_I(data):
    data_nrzi = [0]
    if data[0] == 0:
        data_nrzi.append(-1)
    else:
        data_nrzi.append(1)
    for i in range(1, len(data)):
        if data[i] == 0:
            if data_nrzi[i] == -1:
                data_nrzi.append(-1)
            else:
                data_nrzi.append(1)
        elif data[i] == 1:
            if data_nrzi[i] == -1:
                data_nrzi.append(1)
            else:
                data_nrzi.append(-1)
    return data_nrzi


def Manchester(data):
    data_man = [0]
    for i in range(len(data)):
        if data[i] == 0:
            data_man.append(-1)
            data_man.append(1)
        elif data[i] == 1:
            data_man.append(1)
            data_man.append(-1)
    return data_man


def Diff_Manchester(data):
    data_mand = [0]
    x = 1
    for i in range(len(data)):
        if data[i] == 0:
            data_mand.append(-x)
            data_mand.append(x)
        else:
            data_mand.append(x)
            data_mand.append(-x)
            x = -x
    return data_mand


def AMI(data):
    data_ami = [0]
    prev = -1
    for i in range(len(data)):
        if data[i] == 0:
            data_ami.append(0)
        elif data[i] == 1:
            data_ami.append(-prev)
            prev = -prev
    return data_ami


# main function
a1 = 1
while a1:
    a1 = 0
    option1 = int(input("No of bits to be encoded "))
    if option1 > 0:
        option2 = int(input("Press 0 for random or 1 with fixed 0 sequence or 2 for fixed sequence "))
        if option2 == 0 or option2 == 1 or option2 == 2:
            data = []
            xpoints = np.linspace(0, option1, num=option1 + 1)

            # Random Generating Bits

            if option2 == 0:
                for i in range(option1):
                    data.append(random.getrandbits(1))
            elif option2 == 1:
                option3 = int(input("No of 0 Bits 4 or 8 "))
                if option3 == 4 or option3 == 8:
                    option4 = option1 - option3
                    if option4 > 0:
                        for i in range(option4):
                            data.append(random.getrandbits(1))
                        for i in range(option3):
                            data.append(0)
            elif option2 == 2:
                for i in range(option1):
                    data.append(input())

            print(f"Longest Palindromic sequence is {longestPalindrome(data)}")

            # choice of Encoding
            option5 = int(input("Enter your choice of encoding :\n1-NRZ-L\n2-NRZ-I\n3-Manchester\n4-Diff Manchester\n5-AMI\n"))
            if option5 == 5:
                option6 = int(input("Press 1 for scrambling else 0 "))
                if option6 == 1:
                    option7 = int(input("Press 0 for B8ZS or 1 for HDB3 "))
                    if option7 == 0:
                        ans = B8ZS(data)
                        lab = "AMI-B8ZS"
                    elif option7 == 1:
                        ans = HDB3(data)
                        lab = "AMI-HDB3"
                    else:
                        print("Please enter from one of the options")
                else:
                    ans = AMI(data)
                    lab = "AMI"
            elif option5 == 1:
                ans = NRZ_L(data)
                lab = "NRZ_L"
            elif option5 == 2:
                ans = NRZ_I(data)
                lab = "NRZ_I"
            elif option5 == 3:
                ans = Manchester(data)
                lab = "Machester"
                xpoints = np.linspace(0.0, option1, num=option1 * 2 + 1)  # To make x-axis points according to data
            elif option5 == 4:
                ans = Diff_Manchester(data)
                lab = "Diff_Manchester"
                xpoints = np.linspace(0.0, option1, num=option1 * 2 + 1)  # To make x-axis points according to data
            else:
                print("Please enter from one of the options")

            # plot

            plot.title("Line Encoder")
            plot.ylabel(lab)
            plot.plot(xpoints, ans, color='blue', drawstyle='steps-pre', marker='o')
            plot.show()

            # Decoder

            b1 = int(input(f"IF you want to decode Press 0 : "))
            if b1 == 0:
                print("OUTPUT AFTER DECODING")
                if option5 == 1:
                    print(dec_NRZL(ans))
                elif option5 == 2:
                    print(dec_NRZI(ans))
                elif option5 == 3:
                    print(dec_Manchester(ans))
                elif option5 == 4:
                    print(dec_DManchester(ans))
                elif option5 == 5:
                    if option6 == 0:
                        print(dec_AMI(ans))
                    else:
                        if option7 == 0:
                            print(dec_B8ZS(ans))
                        else:
                            print(dec_HDB3(ans))
                else:
                    print("Bits entered are less than the fixed sequence entered")
            else:
                print("Please enter from one of the options")
        else:
            print("Please enter from one of the options")
    else:
        print("Please enter a positive number")
    a1 = int(input(f"If you want to continue press 1 and 0 for exit: "))
