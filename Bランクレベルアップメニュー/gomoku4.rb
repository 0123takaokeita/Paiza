# 五目並べ縦列の判定


board = []
result = 'D'
# 盤面の初期化
(1..5).each { board.push(gets.chomp.split('')) }

(0..4).each do |i|
  o = 0
  x = 0
  board.each do |row|
    if row[i] == 'O'
      o = o +1 
    elsif row[i] == 'X'
      x = x + 1
    end
  end
  if o == 5
    result = 'O'
    break
  elsif x == 5
    result = 'X'
    break
  end
end

puts result

