import random
import string


Encryption_set = [
    {"char" : "A", "code": "7&Y"}, {"char" : "B", "code" : "8#R"}, {"char" : "C", "code" : "4@o"}, {"char" : "D", "code" : "6!h"},
    {"char" : "E", "code" : "5(x"}, {"char" : "F", "code" : "5:v"}, {"char" : "G", "code" : "1*S"}, {"char" : "H", "code" : "1+D"},
    {"char" : "I", "code" : "0`W"},{"char" : "J", "code" : "0$L"},{"char" : "K", "code" : "1^3"}, {"char" : "L", "code": "8:B"},
    {"char" : "M", "code" : "4;N"},{"char" : "N", "code" : "6$g"},{"char" : "O", "code": "5`M"},{"char" : "P", "code" :"7]V"},
    {"char" : "Q", "code":"9?i"}, {"char" : "R", "code":"9*j"},{"char" : "S", "code":"2[e"},{"char" : "T", "code":"9&c"},
    {"char" : "U", "code":"9!Y"}, {"char" : "V", "code":"7{K"},{"char" : "W", "code":"2~D"},{"char" : "X", "code" : "3*a"},
    {"char" : "Y", "code":"8}f"},{"char" : "Z", "code":"6+q"}, {"char" : " ", "code": "9#t"},
    {"char" : "a", "code": "A1&"}, {"char" : "b", "code" : "Z3~"}, {"char" : "c", "code" : "p0@"}, {"char" : "d", "code" : "O9#"},
    {"char" : "e", "code" : "x4!"}, {"char" : "f", "code" : "Y5#"}, {"char" : "g", "code" : "C7&"}, {"char" : "h", "code" : "c6~"},
    {"char" : "i", "code" : "V3$"},{"char" : "j", "code" : "v5$"},{"char" : "k", "code" : "L8;"}, {"char" : "l", "code": "u9;"},
    {"char" : "m", "code" : "Q2:"},{"char" : "n", "code" : "w1?"},{"char" : "o", "code": "W9?"},{"char" : "p", "code" :"q8="},
    {"char" : "q", "code":"a3+"}, {"char" : "r", "code":"n2}"},{"char" : "s", "code":"m2#"},{"char" : "t", "code":"M1]"},
    {"char" : "u", "code":"N8["}, {"char" : "v", "code":"C4*"},{"char" : "w", "code":"O5&"},{"char" : "x", "code" : "x7~"},
    {"char" : "y", "code":"X6@"},{"char" : "z", "code":"W8#"},
    {"char" : "!", "code":"#A4"}, {"char" : "?", "code":"?B2"},{"char" : "-", "code":"#C3"},{"char" : "*", "code" : "@D9"},
    {"char" : "&", "code":"#e8"},{"char" : "#", "code":"!f1"},{"char" : ".", "code":"$g7"},{"char" : "(", "code":"`#9"}


]


def main():
    text = input("Please enter your text. ")
    slicedText = letterSlicer(text)
    encrypt1 = FirstEncryption(slicedText)
    fragmentList = fragmenter(encrypt1)
    shuffled_list = JumboJumbler(fragmentList)
    sequence_code, data = antiSequencer(shuffled_list)
    segment_1 =""
    segment_2 =""
    if len(data) % 2 != 0:
        segment_1 = data[0: (len(data) - 1) // 2]
        segment_2 = data[((len(data) - 1) // 2) : ]
    else:
        segment_1 = data[0: (len(data)) // 2]
        segment_2 = data[((len(data)) // 2) : ] 
    
    char_1 = random.choice(string.ascii_letters)
    char_2 = str(random.randint(0,9))
    char_3 = str(random.randint(0,9))

    triplet_code = char_1 + char_2 + char_3

    final_passCode = sequence_code + "-" + triplet_code

    with open(f".././server/{triplet_code}.txt", "w") as file:
        file.write(segment_1) 
    with open(f".././client/{triplet_code}.txt", "w") as file:
        file.write(segment_2)

    print(f"Your Secret Key is {final_passCode}") 

def letterSlicer(str):
    sentence = str.strip()
    list_final = list(sentence)
    return list_final

def FirstEncryption(array):
    FinalCode = ""
    for char in array:
        for char1 in Encryption_set:
            if char == char1["char"]:
                FinalCode += char1["code"]
                break
            else:
                continue
    return FinalCode

def fragmenter(array):
    #deciding number of segments
    arrayLength = len(array)

    if arrayLength == 3:
        segNumber = 3
    elif 3 < arrayLength <= 9:
        segNumber = random.randint(4,9)
    elif 9 < arrayLength <= 100:
        segNumber = random.randint(6,10)
    else:
        segNumber = random.randint(10,20)
    
        
    
    #determination of main number
    length = (len(array) // segNumber)

    #creation of first list
    number_list = [0]

    i=0
    for _ in range(segNumber - 1):
        i = i + length
        number_list.append(i)

    #slicer function
    tuples_list = []
    j = 0 
    for _ in range(len(number_list) - 1):
        if number_list[j] == 0: 

            firstNumber = number_list[j]
        else:
            firstNumber = number_list[j] + 1
        nextNumber = number_list[j + 1] + 1
        preTemp = {"id": str(j + 1) , 
                   "fragment": array[firstNumber:nextNumber]
        }
        tuples_list.append(preTemp) 
        j += 1
    number123 = number_list[len(number_list) - 1] + 1
    preTemp2 = {"id" : str(j + 1) , 
                "fragment" :  array[number123 : ]
    }
    tuples_list.append(preTemp2)
    return tuples_list

def JumboJumbler(array):
    array1 = array
    random.shuffle(array1)
    random.shuffle(array1)
    return array1

def antiSequencer(array):
    number_sequence = ""
    finalCode = ""
    for dic in array:
        randSymbol = random.choice(["?","/","#","$","&"])
        number_sequence += (dic["id"] + randSymbol)
        finalCode += (dic["fragment"] + random.choice(["/","%","<",">"]))
    return number_sequence, finalCode

main()