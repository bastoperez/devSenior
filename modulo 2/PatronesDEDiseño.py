class Config:
    _instance = None  # Atributo de clase para la instancia única

    def __new__(cls):  # Se sobrescribe __new__
        if cls._instance is None:  # Si no hay instancia, se crea
            cls._instance = super().__new__(cls)
            cls._instance.settings = {"theme": "dark", "language": "es"}  # Diccionario de configuración
        return cls._instance  # Siempre devuelve la misma instancia

# Creación de instancias
config1 = Config()  # Se crea la instancia
config2 = Config()  # Se intenta crear otra, pero se reutiliza la misma

config1.settings["theme"] = "light"  # Modificamos la configuración desde config1

print(config2.settings["theme"])  # 'light' -> config2 es la misma instancia que config1
