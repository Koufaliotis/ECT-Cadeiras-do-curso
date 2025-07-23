import time
import psutil
#import psutil #####need to do at home
#https://www.geeksforgeeks.org/psutil-module-in-python/

#print(psutil.cpu_percent(interval = 5))

#print(time.time())
#psutil.net_io_counters()


print("Registrando estatísticas do sistema por 60 segundos...\n")
print("{:<10} {:<20} {:<20} {:<10}".format("Tempo(s)", "Octetos Enviados", "Octetos Recebidos", "CPU (%)"))
print("-" * 60)

start_time = time.time()
duration = 60  # Executa por 60 segundos

while True:
    # Calcula o tempo decorrido
    elapsed_time = int(time.time() - start_time)

    # Captura estatísticas da CPU e da rede
    cpu_usage = psutil.cpu_percent(interval=1)
    net_stats = psutil.net_io_counters()
    bytes_sent = net_stats.bytes_sent
    bytes_received = net_stats.bytes_recv

    # Exibe os valores coletados
    print("{:<10} {:<20} {:<20} {:<10}".format(elapsed_time, bytes_sent, bytes_received, cpu_usage))

    # Interrompe após 60 segundos
    if elapsed_time >= duration:
        break