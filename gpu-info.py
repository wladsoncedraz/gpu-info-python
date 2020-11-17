# Para executar este script voce deve instalar as seguintes dependencias:
# pip install gputil
# pip install tabulate
# Creditos: python_genius

import GPUtil
from tabulate import tabulate

print("=" * 40, "GPU Details", "=" * 40)

# Detectando as GPUs disponiveis
gpus = GPUtil.getGPUs()
list_gpus = []

# Percorre as gpus identificadas extraindo suas informacoes e alocando numa lista
for gpu in gpus:
    gpu_id = gpu.id
    gpu_name = gpu.name
    gpu_load = f"{gpu.load * 100}%"
    gpu_free_memory = f"{gpu.memoryFree}MB"
    gpu_used_memory = f"{gpu.memoryUsed}MB"
    gpu_total_memory = f"{gpu.memoryTotal}MB"
    gpu_temperature = f"{gpu.temperature} °C"
    gpu_uuid = gpu.uuid
    list_gpus.append((
        gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory,
        gpu_temperature, gpu_uuid
    ))

# Exibe as informacoes das GPUs identificadas
print(tabulate(list_gpus, headers=("ID", "Name", "Load", "Free Memory", "Used Memory", 
    "Total Memory", "Temperature", "UUID")))