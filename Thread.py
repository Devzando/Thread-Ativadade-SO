import threading
import datetime

# Função para escrever nos arquivos de registro
def write_to_file(file, thread_name, run_number, program_name):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"{run_number} {program_name} {thread_name} {now}\n"
    with open(file, "a") as f:
        f.write(message)

# Função que será executada pelas threads
def thread_function(file1, file2, run_count, program_name):
    thread_name = threading.current_thread().name
    for i in range(run_count):
        write_to_file(file1, thread_name, i+1, program_name)
        write_to_file(file2, thread_name, i+1, program_name)

# Entrada do usuário
run_count = int(input("Digite a quantidade de vezes que cada thread deve rodar: "))

# Criação das threads
thread1 = threading.Thread(target=thread_function, args=("registro1.txt", "registro2.txt", run_count, "programa1"), name="Thread1")
thread2 = threading.Thread(target=thread_function, args=("registro1.txt", "registro2.txt", run_count, "programa1"), name="Thread2")
thread3 = threading.Thread(target=thread_function, args=("registro1.txt", "registro2.txt", run_count, "programa1"), name="Thread3")

thread4 = threading.Thread(target=thread_function, args=("registro1.txt", "registro2.txt", run_count, "programa2"), name="Thread4")
thread5 = threading.Thread(target=thread_function, args=("registro1.txt", "registro2.txt", run_count, "programa2"), name="Thread5")
thread6 = threading.Thread(target=thread_function, args=("registro1.txt", "registro2.txt", run_count, "programa2"), name="Thread6")

# Início da execução das threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
