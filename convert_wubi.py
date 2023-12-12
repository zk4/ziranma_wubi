

# tranditional : simple  chinese  table
ts_dict = {}
def mk_ts_dict():
    global ts_dict
    with open("./STCharacters.txt",encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            tokens = line.split("\t")
            print(len(tokens))
            ts_dict[tokens[1].strip()] = tokens[0].strip()

mk_ts_dict()
print(ts_dict)


words = {}
with open("./wb_single_table.txt",encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        tokens = line.split(" ")
        for token in tokens[1:]:
            print(token.strip())
            target = token.strip()
            # if token.strip() in ts_dict:
            #     target = ts_dict[token.strip()]
            words[target]=tokens[0].strip()

with open("./shouxin_wubi.txt","w",encoding="utf-16") as f:
    for k,v in words.items():
        f.write(f"{k}={v[:1]}\n")
        # f.write(f"{k}={v[:2]}\n")
