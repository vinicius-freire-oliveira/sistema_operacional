import platform  # Importa o módulo 'platform' que fornece informações sobre o sistema operacional

def obter_descricao_windows():
    # Função que obtém e retorna a descrição completa do sistema operacional Windows
    return platform.platform()

if __name__ == "__main__":
    # Verifica se o script está sendo executado diretamente (não importado como módulo)
    descricao_windows = obter_descricao_windows()  # Chama a função para obter a descrição do Windows
    print("Descrição completa do Windows:", descricao_windows)  # Imprime a descrição completa do Windows


