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
