# 値の変数化
doc = []
hash = {}
peple = gets.to_i
# 配列の作成
peple.times do |i|
  doc << gets.chomp.split(' ') 
end

# 連想配列の作成
doc.each do |i|
  
  puts i[0] + ' ' + i[1]
end