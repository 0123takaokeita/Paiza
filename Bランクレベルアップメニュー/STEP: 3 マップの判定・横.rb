# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_snake_map_step3

num = gets.split(' ').map(&:to_i)
tate = num[0]
yoko = num[1]
array = []
tate.times {array << gets.chomp}

array.each_with_index do |str,int|
  
  yoko.times do |i|
      ans = int.to_s + ' ' + i.to_s
      right = str[i+1] == '#'
      left = str[i-1] == '#'
      
    if left && right
        puts ans
    elsif i == 0 && right
        puts ans
    elsif i == yoko-1 && left
        puts ans
    end
  end
end