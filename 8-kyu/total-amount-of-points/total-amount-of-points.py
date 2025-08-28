def points(games):
    resultado = 0
    for placar in games:
        placar = placar.split(':')
        placar_x = int(placar[0])
        placar_y = int(placar[1])
        if placar_x > placar_y:
            resultado += 3
        if placar_x == placar_y:
            resultado += 1
    
    return resultado