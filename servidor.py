import socket
import threading
import re

# Configurações básicas [cite: 38, 39]
HOST = "127.0.0.1"
PORTA = 12340

# Listas para guardar os clientes e os dados para Engenharia Social [cite: 8, 28, 94]
todos_clientes = []
nomes_clientes = {}
dados_roubados = [] 

def verificar_gdpr(texto):
    """Procura emails e números de telefone na mensagem [cite: 17, 41, 60]"""
    tem_email = re.search(r'[a-zA-Z0-9.]+@[a-zA-Z0-9.]+', texto)
    tem_tel = re.search(r'\d{9}', texto)
    
    if tem_email or tem_tel:
        return True
    return False

def enviar_para_todos(mensagem, remetente_proprio):
    """Envia a mensagem para todos os utilizadores [cite: 8, 45, 59]"""
    for c in todos_clientes:
        if c != remetente_proprio:
            try:
                c.send(mensagem.encode('utf-8'))
            except:
                c.close()
                if c in todos_clientes: todos_clientes.remove(c)

def gerir_cliente(conn, addr):
    """Trata de cada utilizador que entra [cite: 7, 31, 58]"""
    try:
        conn.send("NOME_REQ".encode('utf-8'))
        nome = conn.recv(1024).decode('utf-8')
        nomes_clientes[conn] = nome
        todos_clientes.append(conn)
        
        print(f"[NOVO] {nome} ligou-se.") # [cite: 34, 62]
        enviar_para_todos(f"--- {nome} entrou no chat ---", conn) # [cite: 96]

        while True:
            msg = conn.recv(1024).decode('utf-8')
            if not msg or msg.lower() == "sair":
                break

            if verificar_gdpr(msg):
                conn.send("[AVISO] Mensagem bloqueada por conter dados pessoais.".encode('utf-8')) # [cite: 10, 15, 67]
                dados_roubados.append(f"User: {nome} | Conteúdo: {msg}") # [cite: 28, 94]
                print(f"[ALERTA GDPR] Bloqueada mensagem de {nome}") # [cite: 34]
            else:
                enviar_para_todos(f"{nome}: {msg}", conn) # [cite: 8, 45, 91]
    except:
        pass

    if conn in todos_clientes:
        todos_clientes.remove(conn)
    conn.close()
    enviar_para_todos(f"--- {nome} saiu do chat ---", conn) # [cite: 73, 96]
    print(f"[SAÍDA] {nome} desconectou-se.") # [cite: 62]

def iniciar():
    """Inicia o servidor [cite: 44, 57]"""
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # [cite: 39]
    servidor.bind((HOST, PORTA))
    servidor.listen()
    print(f"Servidor ligado na porta {PORTA}...")

    while True:
        canal, endereco = servidor.accept() # [cite: 7, 30, 58]
        tarefa = threading.Thread(target=gerir_cliente, args=(canal, endereco)) # [cite: 40, 97]
        tarefa.start()

if __name__ == "__main__":
    iniciar()