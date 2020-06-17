moji1 = "パトカー"
moji2 = "タクシー"
moji_num = max(len(moji1),len(moji2))

concat = ""
for i in range(moji_num):
    concat = concat + moji1[i] + moji2[i]

print(concat)
