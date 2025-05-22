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
