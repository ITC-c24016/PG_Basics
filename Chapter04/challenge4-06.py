def a(x):
    """
    引数xを2乗して返す関数。
    引数:x (int or float): 数値
    戻り値:int or float: xの2乗
    """
    return x ** 2

print(a(2))



def a(string):
    """
    渡された文字列をそのまま出力する関数
    引数:string:表示したい文字列
    """
    print(string)
a("a,b,c.")



def a(a,b,c,x=100,y=100):
     """
    3つの数値と2つのオプション引数を使って計算結果を返す関数。

    引数:a (int or float): 足し算に使う値
         b (int or float): 足し算に使う値
         c (int or float): 掛け算に使う値
         x (int, optional): 掛け算に使う値（デフォルト100）
         y (int, optional): 使用されていない（デフォルト100）

    戻り値:int or float: 計算結果（a + b + c * x * x）
    return a + b + c * x * x
    """
result = a(1,2,3)
print(result)



def a(x):
    """
    引数xを2で割った値を返す関数。

    引数:
        x (int or float): 数値

    戻り値:
        float: xを2で割った
    """
    return x / 2



def b(x):
    """
    引数xに4を掛けた値を返す関数。

    引数:
        x (int or float): 数値

    戻り値:
        int or float: xに4を掛けた値
    """
    return x * 4

y = a(8)
z = b(y)

print(z)




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
