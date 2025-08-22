def score(dice):
    total_points = 0
    contagem_1 = dice.count(1)
    contagem_2 = dice.count(2)
    contagem_3 = dice.count(3)
    contagem_4 = dice.count(4)
    contagem_5 = dice.count(5)
    contagem_6 = dice.count(6)
    total_points += (contagem_1 // 3) * 1000
    total_points += (contagem_1 % 3) * 100
    total_points += (contagem_2 // 3) * 200
    total_points += (contagem_3 // 3) * 300
    total_points += (contagem_4 // 3) * 400
    total_points += (contagem_5 // 3) * 500
    total_points += (contagem_5 % 3) * 50
    total_points += (contagem_6 // 3) * 600
    
    return total_points