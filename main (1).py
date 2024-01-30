class Node:
    def __init__(self, jogador, tipo_evento, tempo_jogo):
        self.jogador = jogador
        self.tipo_evento = tipo_evento
        self.tempo_jogo = tempo_jogo
        self.proximo = None

class ListaEventos:
    def __init__(self):
        self.inicio = None

    def adicionar_evento(self, jogador, tipo_evento, tempo_jogo):
        novo_evento = Node(jogador, tipo_evento, tempo_jogo)
        if not self.inicio:
            self.inicio = novo_evento
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_evento

    def exibir_eventos(self):
        atual = self.inicio
        while atual:
            print(f"Jogador: {atual.jogador}, Tipo de Evento: {atual.tipo_evento}, Tempo de Jogo: {atual.tempo_jogo}")
            atual = atual.proximo

class FilaSubstituicoes:
    def __init__(self):
        self.fila = []

    def solicitar_substituicao(self, jogador_entra, jogador_sai):
        self.fila.append((jogador_entra, jogador_sai))
        print(f"Solicitação de substituição: {jogador_entra} entra, {jogador_sai} sai.")

    def realizar_substituicao(self):
        if self.fila:
            jogador_entra, jogador_sai = self.fila.pop(0)
            print(f"Substituição realizada: {jogador_entra} entrou, {jogador_sai} saiu.")
        else:
            print("Não há substituições pendentes.")

    def exibir_fila(self):
        print("Fila de substituições:")
        for i, (jogador_entra, jogador_sai) in enumerate(self.fila, 1):
            print(f"{i}. {jogador_entra} entra, {jogador_sai} sai")
            
            
            
            
class PilhaEstatisticas:
    def __init__(self):
        self.pilha = []

    def registrar_estatistica(self, jogador, estatistica):
        self.pilha.append((jogador, estatistica))
        print(f"Estatística registrada: {jogador} - {estatistica}")

    def desfazer_ultima_estatistica(self):
        if self.pilha:
            jogador, estatistica = self.pilha.pop()
            print(f"Desfez última estatística: {jogador} - {estatistica}")
        else:
            print("Não há estatísticas para desfazer.")

    def exibir_pilha(self):
        print("Pilha de estatísticas:")
        for i, (jogador, estatistica) in enumerate(self.pilha, 1):
            print(f"{i}. {jogador} - {estatistica}")


# Exemplo de uso eventos:
lista_eventos = ListaEventos()
lista_eventos.adicionar_evento("Jogador1", "Cesta de 2 pontos", "10:30")
lista_eventos.adicionar_evento("Jogador2", "Falta", "08:45")
lista_eventos.adicionar_evento("Jogador1", "Assistência", "05:20")

lista_eventos.exibir_eventos()


#Exemplo de uso substituições
fila_substituicoes = FilaSubstituicoes()
fila_substituicoes.solicitar_substituicao("Jogador3", "Jogador1")
fila_substituicoes.solicitar_substituicao("Jogador5", "Jogador2")
fila_substituicoes.solicitar_substituicao("Jogador7", "Jogador4")

fila_substituicoes.exibir_fila()
fila_substituicoes.realizar_substituicao()
fila_substituicoes.exibir_fila()

# Exemplo de uso estatisticas:
pilha_estatisticas = PilhaEstatisticas()
pilha_estatisticas.registrar_estatistica("Jogador1", "Cesta de 2 pontos")
pilha_estatisticas.registrar_estatistica("Jogador2", "Falta")
pilha_estatisticas.registrar_estatistica("Jogador1", "Assistência")

pilha_estatisticas.exibir_pilha()
pilha_estatisticas.desfazer_ultima_estatistica()
pilha_estatisticas.exibir_pilha()
