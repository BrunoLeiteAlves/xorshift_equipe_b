# Função Xorshift para gerar números pseudo-aleatórios
def xorshift(seed, bits):
    x = seed
    while True:  # Mantém o gerador em execução até que ele seja interrompido
        x ^= (x << 13) & 0xFFFFFFFF  # Aplicação do Xorshift com deslocamento e XOR
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        yield format(x & 0xFFFFFFFF, '032b')  # Gera 32 bits de cada vez

# Converter texto para binário usando ASCII
def texto_para_binario(texto):
    return ''.join(format(ord(c), '08b') for c in texto)

# Converter binário para texto ASCII
def binario_para_texto(binario):
    return ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))

# Função para gerar chave usando PRNG Xorshift
def gerar_chave_xorshift(tamanho, seed):
    prng = xorshift(seed, tamanho)
    chave_binaria = ''
    while len(chave_binaria) < tamanho:
        chave_binaria += next(prng)
    return chave_binaria[:tamanho]  # Cortar para o tamanho exato da mensagem

# Função XOR entre a mensagem e a chave
def encript_decript(mensagem_binario, chave_binario):
    return ''.join('1' if mensagem_binario[i] != chave_binario[i] else '0' for i in range(len(mensagem_binario)))

# Texto de entrada
mensagem = "Olá grupo A! Somos do grupo B."
# Converter mensagem para binário usando ASCII
mensagem_binario = texto_para_binario(mensagem)
#Tamanho
tamanho = len(mensagem_binario)
# Definir uma seed para o PRNG
seed = 123456789
# Gerar uma chave pseudo-aleatória do mesmo tamanho que a mensagem em binário usando Xorshift
chave_binario = gerar_chave_xorshift(len(mensagem_binario), seed)
# Aplicar XOR entre a mensagem e a chave para criptografar
mensagem_criptografada_binario = encript_decript(mensagem_binario, chave_binario)
# Descriptografar aplicando XOR novamente entre a mensagem criptografada e a chave
mensagem_descriptografada_binario = encript_decript(mensagem_criptografada_binario, chave_binario)
# Converter a mensagem decriptografada de volta para texto ASCII
mensagem_descriptografada_texto = binario_para_texto(mensagem_descriptografada_binario)

# Exibindo os resultados
print("Mensagem original: ", mensagem)
print("Mensagem em binário: ", mensagem_binario)
print("Tamanho da Mensagem em binário: ", tamanho)
print("Chave aleatória gerada pelo Xorshift: ", chave_binario)
print("Mensagem criptografada em binário: ", mensagem_criptografada_binario)
print("Mensagem decriptografada em binário: ", mensagem_descriptografada_binario)
print("Mensagem descriptografada (ASCII): ", mensagem_descriptografada_texto)