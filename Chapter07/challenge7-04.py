number = [1, 3, 5, 7, 9]

while True:
    answer = input("数字を入力してください。終わるにはQを押してください")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("終了するには数字またはqを入力してください")
    if answer in number:
        print("正解")
    else:
        print("不正解")

