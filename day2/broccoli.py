def mini_replace_broccoli(broccoli):

    left_w = 0
    right_g = broccoli.count('G')

    # 左側の'W'の数と、右側の'G'の数の合計が最小置換回数
    mini_replace = left_w + right_g

    for i in range(len(broccoli)):
        if broccoli[i] == 'W':
            left_w += 1 # もし'W'だったら、境界線の左側の'W'を増やす
        else:
            right_g -= 1 # もし'G'だったら、境界線の右側の'G'を減らす
        mini_replace = min(mini_replace, left_w + right_g)
    return mini_replace

print(mini_replace_broccoli('GWGGWWGWGWGWGWGWWWWGWGWGW'))
print(mini_replace_broccoli('GWGGWWGWGG'))