class Barco():
    
    tipo_dibujo = "x"
    tamanos_dict = {
        2: "S",
        3: "M",
        4: "L",
        5: "XL",
    }
    
    def extraer_orientacion(self, pos):
        if "v" in pos.lower():
            return "VERTICAL"
        elif "h" in pos.lower():
            return "HORIZONTAL"
        else:
            return "ERROR"

    def __init__(self, num_tamano, pos):
        self.num_tamano = num_tamano
        self.pos = pos
        self.tamano = self.tamanos_dict[num_tamano]
        self.orientacion = self.extraer_orientacion(pos)

grande = Barco(5, "3v4:8")
pequeño = Barco(2, "3h4:5")  