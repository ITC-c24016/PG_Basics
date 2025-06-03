file_path = "/mnt/c/Users/c24016/Desktop/a.txt"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
