def make_readable(seconds):
    hora = seconds // 3600
    segundos_restantes = seconds % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    
    return f'{hora:02d}:{minutos:02d}:{segundos:02d}'
    