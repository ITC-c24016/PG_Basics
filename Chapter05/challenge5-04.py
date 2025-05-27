dictionary = {"身長":172,"体重":61}

key = input("知りたい情報を入力してください")

if key in dictionary:
    print(f"{key}は{dictionary[key]}です。")
else:
    print("存在しません")
