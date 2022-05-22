from operator import le


def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    min = 0 #探索範囲の左端のインデックスに対する初期条件。
    max = len(sorted_array)-1   #探索範囲の右端のインデックスに対する初期条件
    
    while min <= max:   #探索が終わるまで繰り返す。
        center = (min+max)//2   #探索範囲の中央のインデックスを取得
        
        if sorted_array[center]==target_number: #探索中央と探索対象が位置するとインデックスを返す。
            return center
        elif sorted_array[center]<target_number:    #探索中央の方が探索対象より小さいと探索範囲を狭める。
            min = center + 1
        elif sorted_array[center]>target_number:    #探索中央の方が探索対象より大きいと探索範囲を狭める。
            max = center - 1

    # ここまで記述


    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()