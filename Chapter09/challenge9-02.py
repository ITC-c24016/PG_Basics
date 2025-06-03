answer = input("得意なプログラムはなんですか？")
with open("pro.txt","w") as f:
    f.write(answer)
