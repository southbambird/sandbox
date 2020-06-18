get_head = [1, 5, 6, 7, 8, 9, 15, 16, 19]
message = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = message.split(' ')
dic = {}
for i,word in enumerate(word_list):
    if i+1 in get_head:
        dic[i+1] = word[0]
    else:
        dic[i+1] = word[:2]

print(dic)