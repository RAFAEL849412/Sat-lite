class ModeloApp:
    def __init__(self, arquivo='app.h5'):
        self.modelo = None
        self.arquivo = arquivo
        self.carregado = False  # flag para controlar carregamento

    def radar_sdk(self):
        if self.carregado:
            print("Modelo já carregado, ignorando recarregamento.")
            return
        
        print(f"Carregando modelo {self.arquivo}...")
        self.modelo = tf.keras.models.load_model(self.arquivo)
        self.carregado = True
        print("Modelo carregado com sucesso.")
