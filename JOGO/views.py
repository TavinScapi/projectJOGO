from django.shortcuts import render, redirect

def identificacao(request):
    return render(request, 'JOGO/identificacao.html')

from django.shortcuts import render

def intro(request):
    return render(request, 'JOGO/index.html')
def menu(request):
    return render(request, 'JOGO/menu.html')
def cameras(request):
    return render(request, 'JOGO/cameras.html')
def bestiario(request):
    return render(request, 'JOGO/bestiario.html')
def configuracoes(request):
    return render(request, 'JOGO/index.html')
def sair(request):
    return render(request, 'JOGO/index.html')
def cutscene(request):
    return render(request, 'JOGO/cutscene.html')
def splash_screen(request):
    return render(request, 'JOGO/splash_screen.html')
def room(request):
    return render(request, 'JOGO/room.html')




def JOGO(request, parte='inicio'):
    if parte == 'creditos':
        return redirect('creditos')  # Redireciona para a view de créditos

    historia_parte = historia.get(parte)
    if not historia_parte:
        return redirect('JOGO', parte='inicio')

    return render(request, 'JOGO/jogo.html', {'historia': historia_parte})

historia = {
    'inicio': {
        'texto': (
            "Você se encontra em uma instalação subterrânea de pesquisa, cheia de corredores frios e desolados. "
            "As luzes flickerem acima, jogando sombras ameaçadoras contra as paredes brancas. À sua frente, há duas portas: "
            "uma leva a uma sala de contenção SCP, de onde vem um murmúrio grave e incomum; a outra leva a uma área de pesquisa antiga, "
            "coberta de poeira e arquivos abandonados. O ar é carregado de tensão, como se algo estivesse escondido nas sombras."
        ),
        'imagem': 'instalacao_scientifica.jpg',  # Imagem da instalação SCP
        'escolhas': [
            {'texto': 'Seguir para a sala de contenção SCP', 'proximo': 'sala_construcao'},
            {'texto': 'Explorar a área de pesquisa antiga', 'proximo': 'pesquisa_antiga'}
        ]
    },
    'sala_construcao': {
        'texto': (
            "Ao entrar na sala de contenção SCP, você encontra uma série de câmeras de segurança espalhadas por todo o local. "
            "Na frente, há uma máquina de contenção com luzes piscando e um painel de controle que mostra vários SCPs classificados como 'Altamente Perigosos'. "
            "Uma voz eletrônica ecoa do sistema de som, avisando sobre uma brecha de segurança em algum lugar do complexo. Você percebe que há duas saídas: "
            "uma que leva a uma sala de emergência, onde pode encontrar suprimentos, e outra que leva a um corredor escuro, onde a segurança parece mais intensa."
        ),
        'imagem': 'sala_construcao.jpg',  # Imagem da sala de contenção
        'escolhas': [
            {'texto': 'Procurar na sala de emergência por suprimentos', 'proximo': 'sala_emergencia'},
            {'texto': 'Seguir pelo corredor escuro, mesmo com a segurança alta', 'proximo': 'corredor_seguro'}
        ]
    },
    'pesquisa_antiga': {
        'texto': (
            "Ao explorar a área de pesquisa antiga, você encontra arquivos e documentos amarelados. Um dos documentos destaca-se, descrevendo um SCP que "
            "é capaz de alterar a percepção do tempo de quem o observa. O ar no local parece pesado, e você escuta passos discretos atrás de você. "
            "Há duas opções: uma leva a uma sala de observação, onde você pode tentar aprender mais sobre o SCP, e a outra leva a uma sala de segurança, "
            "aparentemente trancada, mas com uma janela que revela algo inquietante lá dentro."
        ),
        'imagem': 'pesquisa_antiga.jpg',  # Imagem da área de pesquisa antiga
        'escolhas': [
            {'texto': 'Entrar na sala de observação', 'proximo': 'sala_observacao'},
            {'texto': 'Tentar abrir a sala de segurança', 'proximo': 'sala_seguranca'}
        ]
    },
    'sala_emergencia': {
        'texto': (
            "Na sala de emergência, você encontra uma máscara de gás e um kit de primeiros socorros. Enquanto os pega, uma mensagem aparece em um monitor: "
            "'Atenção, brecha de segurança detectada em SCP-096. A evacuação imediata é recomendada.' Você percebe que há um caminho para a superfície, "
            "mas uma porta com luz vermelha barrando o caminho, e outra que leva a um laboratório ao lado, aparentemente inutilizado."
        ),
        'imagem': 'sala_emergencia.jpg',  # Imagem da sala de emergência
        'escolhas': [
            {'texto': 'Seguir para a superfície pela porta barrada', 'proximo': 'superficie'},
            {'texto': 'Explorar o laboratório ao lado', 'proximo': 'laboratorio'}
        ]
    },
    'corredor_seguro': {
        'texto': (
            "O corredor escuro é silencioso e cheio de umidade. Ao longe, você ouve o som de algo que se move. Seguindo em frente, você encontra um SCP-173 preso em uma gaiola. "
            "Ele te observa sem piscar, sua presença é inquietante. Há uma porta que leva a um laboratório mais iluminado, e outra que parece dar para a área externa, "
            "com uma pequena janela quebrada por onde se vê a noite lá fora."
        ),
        'imagem': 'corredor_seguro.jpg',  # Imagem do corredor com SCP-173
        'escolhas': [
            {'texto': 'Entrar no laboratório iluminado', 'proximo': 'laboratorio'},
            {'texto': 'Sair pela área externa', 'proximo': 'area_externa'}
        ]
    },
    'sala_observacao': {
        'texto': (
            "Na sala de observação, você encontra um SCP-106 preso em uma caixa de contenção. O ar ao redor está gelado e a caixa emite um brilho fraco. "
            "Há um monitor mostrando imagens de pessoas desaparecendo em ambientes diferentes. Uma voz eletrônica avisa: 'Atenção, SCP-106 em movimento.' "
            "Duas saídas surgem: uma para o corredor de contenção e outra para uma sala de segurança.",
        ),
        'imagem': 'sala_observacao.jpg',  # Imagem da sala de observação
        'escolhas': [
            {'texto': 'Seguir para o corredor de contenção', 'proximo': 'corredor_construcao'},
            {'texto': 'Ir para a sala de segurança', 'proximo': 'sala_seguranca'}
        ]
    },
    'sala_seguranca': {
        'texto': (
            "Na sala de segurança, você encontra um computador com várias câmeras de segurança. Um alarme soa, e um aviso aparece: 'Atenção, brecha de segurança no SCP-682. "
            "A contenção foi rompida.' Há uma única saída, mas leva a um corredor escuro e fechado. A outra porta está trancada com código de segurança.",
        ),
        'imagem': 'sala_seguranca.jpg',  # Imagem da sala de segurança
        'escolhas': [
            {'texto': 'Tentar acessar o código de segurança', 'proximo': 'codigo_seguranca'},
            {'texto': 'Seguir pelo corredor escuro', 'proximo': 'corredor_escuro'}
        ]
    },
    'laboratorio': {
        'texto': (
            "O laboratório está vazio, mas você encontra um caderno de notas com experimentos antigos sobre SCP-049. As anotações indicam que ele é uma entidade que pode curar doenças, "
            "mas também transforma pessoas em 'infectados'. Você ouve passos atrás de você e uma voz fraca sussurra: 'Fuja, antes que seja tarde.'"
        ),
        'imagem': 'laboratorio.jpg',  # Imagem do laboratório
        'escolhas': [
            {'texto': 'Procurar por suprimentos no laboratório', 'proximo': 'procurar_suprimentos'},
            {'texto': 'Sair do laboratório e voltar para o corredor', 'proximo': 'corredor_seguro'}
        ]
    },
    'codigo_seguranca': {
        'texto': (
            "Você tenta desbloquear a porta com o código de segurança. A senha correta é um anagrama de 'contained', mas você está correndo contra o tempo. A cada erro, o alarme soa mais alto. "
            "Finalmente, você consegue abrir a porta, mas o corredor está preenchido por SCP-682, um crocodilo humanoide, rugindo e avançando na sua direção."
        ),
        'imagem': 'codigo_seguranca.jpg',  # Imagem do código de segurança
        'escolhas': [
            {'texto': 'Tentar lutar contra SCP-682', 'proximo': 'luta'},
            {'texto': 'Fugir pela porta aberta', 'proximo': 'superficie'}
        ]
    },
    'procurar_suprimentos': {
        'texto': (
            "Enquanto procura por suprimentos, você encontra uma máscara de gás e uma pistola velha. O som de passos vem do corredor. "
            "Você percebe que SCP-049 está vindo em sua direção. Sua única saída é lutar ou correr.",
        ),
        'imagem': 'procurar_suprimentos.jpg',  # Imagem dos suprimentos
        'escolhas': [
            {'texto': 'Usar a pistola para enfrentar SCP-049', 'proximo': 'luta_scp049'},
            {'texto': 'Fugir rapidamente pela porta', 'proximo': 'superficie'}
        ]
    },
    'luta': {
        'texto': (
            "Você enfrenta SCP-682 em uma batalha intensa. Sua resistência é extraordinária, mas você acaba ferido. No fim, ou ele ou você."
            "\n\nFim do jogo."
        ),
        'imagem': 'luta_final.jpg',  # Imagem da luta contra SCP-682
        'escolhas': [
            {'texto': 'FIM', 'proximo': 'creditos'}
        ]
    },
    'luta_scp049': {
        'texto': (
            "Você tenta lutar contra SCP-049, mas ele é rápido e ágil. Seus ataques causam ferimentos graves. Sem saída, você decide usar a máscara de gás. "
            "O SCP-049 parece enfraquecer e recuar, permitindo sua fuga."
            "\n\nFim do jogo."
        ),
        'imagem': 'luta_final.jpg',  # Imagem da luta contra SCP-049
        'escolhas': [
            {'texto': 'FIM', 'proximo': 'creditos'}
        ]
    },
    'superficie': {
        'texto': (
            "Finalmente, você consegue alcançar a superfície. A noite está fria e o céu estrelado parece uma dádiva, depois de tudo o que enfrentou. "
            "Você respira fundo e, com um sorriso fraco, sabe que fez o que pôde. Talvez seja hora de sair da instalação... ou de voltar e encarar a próxima ameaça."
            "\n\nFim do jogo."
        ),
        'imagem': 'superficie.jpg',  # Imagem da saída para a superfície
        'escolhas': [
            {'texto': 'FIM', 'proximo': 'creditos'}
        ]
    }
}

def creditos(request):
    return render(request, 'JOGO/creditos.html')
