# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_snake_move_step1

num = gets.split(' ').map(&:to_i)
y = num[0]
x = num[1]
array = []

y.times {array << gets.chomp}

array.each_with_index do |str,int|
    str.length.times do |i|
        if str[i] == '#'
            y = int
            x = i
        end
    end
end