import re

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
    secretKey = input("Please Input your Secret Key.")
    fileCode = (file_key(secretKey)).strip("-")

    with open(f".././server/{fileCode}.txt", "r") as file:
        segment_1 = (file.readlines())[0]
    with open(f".././client/{fileCode}.txt", "r") as file:
        segment_2 = (file.readlines())[0]

    encoded_text = segment_1 + segment_2

    sequence_list = sequenceFinder(secretKey, fileCode)

    encode_list = codeLister(encoded_text)

    finalCode, count = finalEncodeSequencer(sequence_list, encode_list)

    Your_Text = Decoder(Converter(finalCode, count))

    print(f"DECODED MESSAGE : {Your_Text}")

#Extracts key for identification of file
def file_key(key):
    try:
        value = re.search((r"-[a-zA-Z]\d{2}"), key)
        return value.group(0)
    except:
        raise ValueError

#using the secret key, gets the sequence in which the fragments were jumbled, RETURNS LIST**        
def sequenceFinder(string,key):
    index = string.find(key)
    string = string[0:index - 1]
    string = string
    characters = "/?#&$"
    for char in characters:
        string = string.replace(char, "_")

    split_list = string.split("_")
    cleaned_list = [item for item in split_list if item] 
    return cleaned_list

#Extracts the fragments 
def codeLister(string):
    characters = "|%<>"
    for char in characters:
        string = string.replace(char, "_")

    split_list = string.split("_")
    cleaned_list = [item for item in split_list if item] 
    return cleaned_list

#Sequences the fragments into right order
def finalEncodeSequencer(sequence, crypt):
    master_list = []
    final_coded_text= ""

    for i in range(len(sequence)):
        temp = {"id": sequence[i-1] , 
        "fragment": crypt[i-1]
        }
        master_list.append(temp)

    sorted_list = []

    number_count = 1

    for _ in range(len(master_list)):

        for item in master_list:
            if number_count == int(item["id"]):
                sorted_list.append(item)
                number_count += 1
                break
            else:
                continue

    for data in sorted_list:
        final_coded_text += data["fragment"]

    count = len(final_coded_text)  

    return final_coded_text, count

#slices the whole into triplets for decoding
def Converter(code, count):
    count = (count // 3) 
    x = 0
    y = 3
    sliced_list = []

    for _ in range(count - 1):
        sliced_list.append(code[x:y])
        x += 3
        y += 3
    sliced_list.append(code[y-3:])
    return sliced_list

#Decodes using encryption key
def Decoder(code_list):
    final_text =""
    for triplet in code_list:
        for crypt in Encryption_set:
            if triplet == crypt["code"]:
                final_text += crypt["char"]
                break
            else:
                continue
    return final_text


main()