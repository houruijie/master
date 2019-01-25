# i = 0
# for line in open("domain.txt","r"):
#     i = i + 1
#     print(i)
#     domain = line.split(',')[0]
#     with open("domain.txt", 'a+') as f:
#         f.write(domain+"\n")



def txt_readlines():
    pass

def tex_readline():
    pass

def txt_write(target, line):
    with open(target, "a+") as fw:
        fw.write(line)

def txt_split(source, target, start, length):
    with open(source, 'r') as fr:
        lines = fr.readlines()
        lines = set(lines)
        for i, line in enumerate(lines):
            if i in range(start, start+length):
                txt_write(target,line)
            if i > start+length:
                return
def txt_count(source):
    with open(source,"r") as fr:
        lines = fr.readlines()
        return len(lines)


if __name__ == "__main__":
    source = "domain_1.txt"
    target = "domain_2.txt"
    start = 0
    length = 150000
    txt_split(source,target,start,length)
    # source = "domain_1.txt"
    # count = txt_count(source)
    # print(count)
