import multiprocessing
import pickle
import traceback
import time
from io import BytesIO
import requests

par_loaded_objs = []

class ParallelLoad:
    def __init__(self, loading_fun=None, url=None):
        self.model = None
        manager = multiprocessing.Manager()
        self.ret_dict = manager.dict()
        par_loaded_objs.append(self)

        if url is not None:
            self.url = url
            self.p = multiprocessing.Process(
                target=self.load_pickle_from_url,
                args=(self.url, self.ret_dict)
            )
        elif loading_fun is not None:
            self.p = multiprocessing.Process(
                target=lambda f, d: d.__setitem__(1, f()),
                args=(loading_fun, self.ret_dict)
            )
        else:
            raise ValueError("Você deve fornecer loading_fun ou url")

        self.p.start()

    @property
    def obj(self):
        if self.model is None:
            counter = 0
            while len(self.ret_dict) == 0:
                time.sleep(2)
                counter += 1
                if counter >= 50:
                    break

            if len(self.ret_dict) == 0:
                print("Erro: ParallelLoad não conseguiu carregar o objeto após 100 segundos")
                traceback.print_stack()
                raise AssertionError("ParallelLoad failed to load object after 100 seconds")

            self.model = self.ret_dict[1]
            self.p = None

        return self.model

    @staticmethod
    def load_pickle_from_url(url, ret_dict):
        try:
            print(f"Baixando pickle de {url} ...")
            start_time = time.time()
            response = requests.get(url)
            response.raise_for_status()
            bytes_io = BytesIO(response.content)
            retval = pickle.load(bytes_io)
        except Exception:
            traceback.print_exc()
            raise
        print(f"Download e carregamento do pickle concluído em {time.time() - start_time:.2f} segundos")
        ret_dict[1] = retval

    @staticmethod
    def wait_for_all_loads():
        print("Waiting for all loads...")
        for par_load in par_loaded_objs:
            _ = par_load.obj


if __name__ == "__main__":
    url = "https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan2/versions/1/files/stylegan2-afhqcat-512x512.pkl"
    loader = ParallelLoad(url=url)

    print("Fazendo outras coisas enquanto baixa e carrega pickle...")

    # Aguarda e acessa o objeto carregado
    obj = loader.obj
    print("Objeto carregado do URL:")
    print(type(obj))  # Normalmente é um dict ou objeto do pickle
