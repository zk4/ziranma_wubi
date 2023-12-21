words = {}

def is_simplified(char):
    try:
        char.encode('gb2312')
        return True
    except UnicodeEncodeError:
        return False

with open("./wb_single_table.txt", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        tokens = line.split(" ")
        for token in tokens[1:]:
            target = token.strip()

            # Check if the character is simplified
            if is_simplified(target):
                words[target] = tokens[0].strip()

with open("./shouxin_wubi_s_word.txt", "w",encoding="utf-16") as fw:
    with open("./现代汉语常用词表.txt", "r") as f:
        for line in f.readlines():
            word  = line.split("\t")[0]
            if len(word) == 2:
                if word[0] in words:
                    try:
                        o=word+"="+words[word[0]][0]+words[word[0]][1]+words[word[1]][0]+words[word[1]][1]
                        print(o)
                        fw.write(o+"\n")
                    except:
                        pass


