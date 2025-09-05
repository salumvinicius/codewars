def generate_hashtag(s):
    result = []
    for palavra in s.split(" "):
        result.append(palavra.capitalize())
    
    result = "#" + "".join(result)
    return result if 1 < len (result) <= 140 else False