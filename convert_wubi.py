

# tranditional : simple  chinese  table
# ts_dict = {}
# def mk_ts_dict():
#     global ts_dict
#     with open("./STCharacters.txt",encoding='utf-8') as f:
#         lines = f.readlines()
#         for line in lines:
#             tokens = line.split("\t")
#             print(len(tokens))
#             ts_dict[tokens[1].strip()] = tokens[0].strip()

# mk_ts_dict()
# print(ts_dict)


words = {}
with open("./wb_single_table.txt",encoding='utf-8') as f:
   lines = f.readlines()
   for line in lines:
       tokens = line.split(" ")
       for token in tokens[1:]:
           print(token.strip())
           target = token.strip()
           words[target]=tokens[0].strip()

with open("./shouxin_wubi_st.txt","w",encoding="utf-16") as f:
   for k,v in words.items():
       f.write(f"{k}={v[:1]}\n")



words = {}
#
# 只判断简体字
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
            else:
                print(target)
with open("./shouxin_wubi_s.txt", "w", encoding="utf-16") as f:
    for k, v in words.items():
        f.write(f"{k}={v[:1]}\n")

    with open("./user_defined.txt",encoding='utf-8') as f2:
        lines = f2.readlines()
        f.write("\n".join(lines))

        # 最好不要使用两个码判断，跟双拼冲突比较大，一个码足够了。
        # f.write(f"{k}={v[:2]}\n")
