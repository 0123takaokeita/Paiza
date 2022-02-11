# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_snake_map_step2

num = gets.split(' ').map(&:to_i)
tate = num[0]
yoko = num[1]
inst_num = num[2]

array = []
tate.times { array << gets.chomp}

# 書き換え
inst_num.times do |i|
  inst = gets.split(' ').map(&:to_i)
  array[inst[0]][inst[1]] = '#'
end

# 答えの出力
array.each {|i| puts i }