import json
import statistics
import sys
from itertools import chain

class Chatbot:
    def __init__(self, cookie_path=None):
        self.cookie_path = cookie_path

    def get_history(self, filename):
        """Lê dados JSON e retorna o histórico bruto em formato de dicionário."""
        try:
            if filename == "-":
                json_data = json.load(sys.stdin)
            else:
                with open(filename, "r") as json_file:
                    json_data = json.load(json_file)

            # Verifica se a chave 'dishGetHistory' está presente
            if 'dishGetHistory' not in json_data:
                raise KeyError("A chave 'dishGetHistory' não foi encontrada no JSON.")

            return json_data["dishGetHistory"]
        except FileNotFoundError:
            raise JsonError(f"O arquivo {filename} não foi encontrado.")
        except json.JSONDecodeError:
            raise JsonError("Falha ao decodificar o arquivo JSON.")
        except KeyError as e:
            raise JsonError(f"Erro de chave no JSON: {e}")

    def _compute_sample_range(self, history, parse_samples):
        current = int(history["current"])
        samples = len(history["popPingDropRate"])
        samples = min(samples, current)

        if parse_samples < 0 or samples < parse_samples:
            parse_samples = samples

        start = current - parse_samples
        if start == current:
            return range(0), 0, current

        end_offset = current % samples
        start_offset = start % samples

        if start_offset < end_offset:
            sample_range = range(start_offset, end_offset)
        else:
            sample_range = chain(range(start_offset, samples), range(0, end_offset))

        return sample_range, parse_samples, current

    def history_bulk_data(self, filename, parse_samples):
        """Busca dados de histórico para um intervalo de amostras."""
        try:
            history = self.get_history(filename)
        except JsonError as e:
            raise JsonError(f"Erro ao processar o arquivo: {e}")
        except Exception as e:
            raise JsonError(f"Erro inesperado: {e}")

        sample_range, parsed_samples, current = self._compute_sample_range(history, parse_samples)

        pop_ping_drop_rate = []
        pop_ping_latency_ms = []
        downlink_throughput_bps = []
        uplink_throughput_bps = []

        for i in sample_range:
            pop_ping_drop_rate.append(history["popPingDropRate"][i])
            pop_ping_latency_ms.append(history["popPingLatencyMs"][i] if history["popPingDropRate"][i] < 1 else None)
            downlink_throughput_bps.append(history["downlinkThroughputBps"][i])
            uplink_throughput_bps.append(history["uplinkThroughputBps"][i])

        return {
            "samples": parsed_samples,
            "end_counter": current,
        }, {
            "pop_ping_drop_rate": pop_ping_drop_rate,
            "pop_ping_latency_ms": pop_ping_latency_ms,
            "downlink_throughput_bps": downlink_throughput_bps,
            "uplink_throughput_bps": uplink_throughput_bps,
        }

    def history_stats(self, filename, parse_samples):
        """Busca, analisa e calcula estatísticas de ping e uso."""
        try:
            history = self.get_history(filename)
        except JsonError as e:
            raise JsonError(f"Erro ao processar o arquivo: {e}")
        except Exception as e:
            raise JsonError(f"Erro inesperado: {e}")

        sample_range, parsed_samples, current = self._compute_sample_range(history, parse_samples)

        total_ping_drop = 0.0
        count_full_drop = 0
        rtt_full = []

        for i in sample_range:
            d = history["popPingDropRate"][i]
            if d >= 1:
                d = 1
                count_full_drop += 1
            total_ping_drop += d

            rtt = history["popPingLatencyMs"][i]
            if d == 0.0:
                rtt_full.append(rtt)

        mean_full = statistics.mean(rtt_full) if rtt_full else None

        return {
            "samples": parsed_samples,
            "end_counter": current,
        }, {
            "total_ping_drop": total_ping_drop,
            "count_full_ping_drop": count_full_drop,
            "mean_full_ping_latency": mean_full,
        }


class JsonError(Exception):
    """Exceção personalizada para erros de JSON."""
    pass


if __name__ == "__main__":
    filename = "configure.json"  # Nome do arquivo JSON com os dados
    parse_samples = 100  # Número de amostras a serem analisadas
    chatbot = Chatbot(cookie_path="cookie.json")  # Instanciando o Chatbot
    try:
        stats, data = chatbot.history_stats(filename, parse_samples)
        print("Estatísticas de Histórico:", stats)
        print("Dados de Histórico:", data)
    except JsonError as e:
        print("Erro ao processar o histórico:", e)
    except Exception as e:
        print("Erro inesperado:", e)
