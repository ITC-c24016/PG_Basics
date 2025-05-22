def a(c):
    """
    引数cをfloat型に変換して返す関数。
    変換できない場合は "hogehoge" を表示する。

    引数:
        c (str): 数値に変換可能な文字列

    戻り値:
        float or None: 変換成功時はfloat、失敗時はNone
    """
    try:
        return float(c)
    except ValueError:
        print("hogehoge")

b = a("43.0")
print(b)
