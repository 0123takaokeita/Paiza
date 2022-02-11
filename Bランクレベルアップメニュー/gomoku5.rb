#  五目並べ斜め判定


result = 'D'
input = []
x = 0
o = 0
rx = 0
ro = 0
# 結果を配列に変換
5.times do |i|
    input.push(gets.chomp)
end

# 配列の値の添字を一つ追加して出力

input.each_with_index do |i,index|
    # 昇順のななめ
    x += 1 if i[index] == 'X'
    o += 1 if i[index] == 'O'
    
    # 降順のななめ
    rx += 1 if i[4 - index] == 'X'
    ro += 1 if i[4 - index] == 'O'
    
    # リザルトに代入して答えを出力
    if x == 5 || rx == 5
        result 'X'
    elsif o == 5 || ro == 5
        result = 'O'
    end
            
end
    puts result


