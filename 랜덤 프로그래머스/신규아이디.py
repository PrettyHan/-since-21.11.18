def solution(new_id):
    answer = ''
    pd2 = ""
    pd1 = new_id.lower()
    for pd_word in pd1:
        if pd_word.isalnum() or pd_word == "-" or pd_word == "_" or pd_word == ".":
            pd2 += pd_word
    for pd2_word in pd2:
        if pd2.find("..") != -1:
            pd2 = pd2.replace("..", ".")
    pd3 = pd2.strip(".")
    if pd3 == "":
        pd3 = "a"
    if len(pd3) >= 15:
        pd3 = pd3[0:15]
    pd3 = pd3.strip(".")
    while len(pd3) <= 2:
        pd3 += pd3[-1]
        
    print(pd3)
    
    return pd3