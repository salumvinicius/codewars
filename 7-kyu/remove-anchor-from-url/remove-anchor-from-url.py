def remove_url_anchor(url):
    resultado = []
    for letra in url:
        if letra == "#":
            break
        resultado.append(letra)
    return "".join(resultado)