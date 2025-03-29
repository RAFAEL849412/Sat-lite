import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import attcak
# Definindo a classe do manipulador de eventos
class MyHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.event_type == "created":
            print(f"Algo foi criado: {event.src_path}")
        elif event.event_type == "modified":
            print(f"Algo foi modificado: {event.src_path}")
        elif event.event_type == "deleted":
            print(f"Algo foi deletado: {event.src_path}")

# Definindo a classe que gerencia o monitoramento
class MyWatch:
    def __init__(self, path='./'):
        self.path = path
        self.observer = Observer()

    def run(self):
        handler = MyHandler()
        self.observer.schedule(handler, self.path, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            print("Monitoramento interrompido.")
            self.observer.stop()
        self.observer.join()

# Inicializando e rodando o monitoramento
if __name__ == "__main__":
    w = MyWatch() 
    w.run()
