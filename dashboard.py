import os
import json
from collections import Counter

RESULTS_DIR = "allure-results"

def generate_dashboard():
    results = []
    if not os.path.exists(RESULTS_DIR):
        print(f"Diretório '{RESULTS_DIR}' não encontrado. Execute os testes com '--alluredir' primeiro.")
        return

    for filename in os.listdir(RESULTS_DIR):
        if filename.endswith("-result.json"):
            with open(os.path.join(RESULTS_DIR, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                results.append({
                    "name": data.get("name", "Nome não encontrado"),
                    "status": data.get("status", "desconhecido"),
                    "duration_ms": data.get("time", {}).get("duration", 0)
                })

    if not results:
        print("Nenhum resultado de teste encontrado.")
        return

    # Cálculos
    total_tests = len(results)
    status_counts = Counter(result["status"] for result in results)
    total_duration_s = sum(result["duration_ms"] for result in results) / 1000

    # Imprimir Dashboard
    print("\n" + "="*50)
    print(" " * 15 + "DASHBOARD DE TESTES")
    print("="*50)
    print(f"Total de Testes Executados: {total_tests}")
    print(f"Tempo Total de Execução: {total_duration_s:.2f} segundos")
    print("\n--- Resultados por Status ---")
    for status, count in status_counts.items():
        print(f"  - {status.capitalize()}: {count}")
        
    print("\n--- Detalhes por Teste ---")
    for result in sorted(results, key=lambda x: x["duration_ms"], reverse=True):
        duration_s = result["duration_ms"] / 1000
        print(f"  - [{result['status'].upper()}] {result['name']} ({duration_s:.2f}s)")
    print("="*50)

if __name__ == "__main__":
    generate_dashboard()