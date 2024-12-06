from django.shortcuts import render, redirect

def identificacao(request):
    return render(request, 'JOGO/identificacao.html')

from django.shortcuts import render

def intro(request):
    return render(request, 'JOGO/index.html')
def menu(request):
    return render(request, 'JOGO/menu.html')
def carregar_jogo(request):
    return render(request, 'JOGO/index.html')
def configuracoes(request):
    return render(request, 'JOGO/index.html')
def sair(request):
    return render(request, 'JOGO/index.html')




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
            "Você está em uma floresta escura, onde a lua parece ser a única testemunha do que está prestes a acontecer. "
            "O som de corujas e o farfalhar das folhas criam uma melodia inquietante. "
            "Há duas trilhas à sua frente: uma leva a uma caverna sombria, de onde ecoam sons perturbadores; "
            "a outra segue para um antigo vilarejo coberto de neblina, conhecido por seu passado trágico. "
            "O ar está pesado, como se a própria floresta quisesse impedir sua escolha."
        ),
        'imagem': 'floresta_escuridao.jpg',  # Imagem da floresta
        'escolhas': [
            {'texto': 'Seguir para a caverna', 'proximo': 'caverna_entrada'},
            {'texto': 'Ir ao vilarejo', 'proximo': 'vilarejo'}
        ]
    },
    'caverna_entrada': {
        'texto': (
            "A entrada da caverna parece a boca de uma criatura gigante, escura e faminta. O ar dentro é úmido, "
            "e um cheiro metálico mistura-se ao som de gotas ecoando. Ao observar mais atentamente, você percebe "
            "uma inscrição na parede, com palavras antigas que brilham fracamente: *'A coragem abre os caminhos do destino.'* "
            "Você sente calafrios. Dois caminhos surgem à frente: uma passagem estreita que parece sussurrar segredos e "
            "um túnel largo com pegadas pesadas que não inspiram confiança."
        ),
        'imagem': 'caverna_entrada.jpg',  # Imagem para a entrada da caverna
        'escolhas': [
            {'texto': 'Explorar a passagem estreita, apesar do risco', 'proximo': 'passagem_estreita'},
            {'texto': 'Seguir pelo túnel largo, mesmo com o perigo iminente', 'proximo': 'tunel_largo'}
        ]
    },
    'passagem_estreita': {
        'texto': (
            "Você se espreme pela passagem, sentindo o peso das paredes de pedra ao seu redor. Sua respiração "
            "fica difícil, e você percebe que cada movimento faz ecoar um som abafado, como se algo mais estivesse "
            "ali, ouvindo. No fim da passagem, há um baú antigo coberto de poeira. Antes de tocá-lo, você sente um "
            "ar gelado passar pelo seu pescoço, e uma risada fraca ecoa na escuridão. Está preparado?"
        ),
        'imagem': 'passagem_estreita.jpg',  # Imagem da passagem estreita
        'escolhas': [
            {'texto': 'Abrir o baú, enfrentando o medo', 'proximo': 'bau'},
            {'texto': 'Sair rapidamente e voltar para a entrada da caverna', 'proximo': 'caverna_entrada'}
        ]
    },
    'bau': {
        'texto': (
            "Você abre o baú lentamente, e um rangido ecoa como um grito distante. Dentro, encontra uma espada "
            "antiga, coberta de ferrugem, mas ainda reluzente em partes. Junto dela, há um pequeno diário com letras "
            "desgastadas que diz: *'O portador desta lâmina deve estar pronto para sacrificar tudo.'* O peso da escolha "
            "se torna real. Será que vale a pena arriscar?"
        ),
        'imagem': 'bau.jpg',  # Imagem do baú
        'escolhas': [
            {'texto': 'Pegar a espada e aceitar o risco', 'proximo': 'tunel_largo'},
            {'texto': 'Deixar a espada e retornar à entrada', 'proximo': 'caverna_entrada'}
        ]
    },
    'tunel_largo': {
        'texto': (
            "No túnel largo, o ar fica mais pesado a cada passo. Você sente uma vibração no chão e ouve uma respiração "
            "profunda e lenta à distância. Ao se aproximar, vê um dragão colossal adormecido. Ele guarda um brilho dourado "
            "que ilumina a caverna, revelando montanhas de tesouros. Seu coração bate rápido. Um espirro seu pode acordá-lo."
        ),
        'imagem': 'tunel_dragao.jpg',  # Imagem do túnel largo com o dragão
        'escolhas': [
            {'texto': 'Tentar roubar o tesouro silenciosamente', 'proximo': 'dragao_tesouro'},
            {'texto': 'Enfrentar o dragão com a espada, mesmo sendo quase suicídio', 'proximo': 'lutar_dragao'},
            {'texto': 'Desistir do tesouro e recuar', 'proximo': 'caverna_entrada'}
        ]
    },
    'dragao_tesouro': {
        'texto': (
            "Você se aproxima com passos leves, mas um pequeno deslize faz uma moeda cair. O som desperta o dragão, "
            "cujos olhos brilham como brasas. Ele rosna profundamente antes de lançar chamas em sua direção. Você tenta "
            "fugir, mas não há tempo. O dragão é implacável. Você é consumido pelas chamas.\n\nFim do jogo."
        ),
        'imagem': 'dragao_furioso.jpg',  # Imagem do dragão acordado
        'escolhas': [
            {'texto': 'FIM', 'proximo': 'creditos'}
        ]
    },
    'lutar_dragao': {
        'texto': (
            "Com a espada enferrujada em mãos, você avança contra o dragão. O calor do seu sopro parece derreter sua "
            "determinação, mas você não desiste. A batalha é feroz e dolorosa, e, no fim, a lâmina quebra. No entanto, "
            "um golpe certeiro faz o dragão rugir e fugir, deixando o tesouro para trás. Você venceu, mas está gravemente ferido.\n\n"
            "Parabéns, você sobreviveu, mas a que custo?"
        ),
        'imagem': 'batalha_dragao.jpg',  # Imagem da batalha
        'escolhas': [
            {'texto': 'FIM', 'proximo': 'creditos'}
        ]
    },
    'vilarejo': {
        'texto': (
            "Ao chegar ao vilarejo, uma sensação inquietante toma conta de você. As ruas estão desertas, mas há sinais de vida: "
            "uma lamparina ainda acesa balança ao vento em frente à taberna, e o sino da igreja toca sozinho, ecoando como um chamado distante. "
            "Há rumores de que o vilarejo está amaldiçoado, mas ninguém sabe ao certo o que aconteceu com seus moradores.\n\n"
            "Você precisa decidir para onde ir. No céu, corvos se empoleiram nas casas, observando seus passos como juízes silenciosos."
        ),
        'imagem': 'vilarejo_assombrado.jpg',  # Imagem do vilarejo deserto
        'escolhas': [
            {'texto': 'Explorar a taberna e enfrentar os rumores de assombrações', 'proximo': 'taberna'},
            {'texto': 'Seguir para a igreja e investigar o mistério do sino solitário', 'proximo': 'igreja'}
        ]
    },
    'taberna': {
        'texto': (
            "A taberna parece abandonada há anos. Mesas e cadeiras estão tombadas, copos quebrados espalhados pelo chão. "
            "Ao entrar, você sente um cheiro estranho, uma mistura de bebida fermentada e algo pútrido. "
            "Atrás do balcão, há um diário coberto de poeira, com a capa gravada em letras: *'Segredos da Noite.'* "
            "Antes que possa pegar o livro, uma risada fantasmagórica ecoa, seguida de um som de passos no andar de cima."
        ),
        'imagem': 'taberna_abandonada.jpg',  # Imagem da taberna abandonada
        'escolhas': [
            {'texto': 'Ler o diário, mesmo com os passos assustadores', 'proximo': 'ler_diario'},
            {'texto': 'Investigar o andar de cima, enfrentando o medo', 'proximo': 'andar_de_cima'},
            {'texto': 'Sair da taberna e explorar outra parte do vilarejo', 'proximo': 'vilarejo'}
        ]
    },
    'ler_diario': {
        'texto': (
            "Você abre o diário com cuidado, e as páginas parecem grudar nos seus dedos. Ele descreve avistamentos de uma criatura "
            "que aparece apenas à noite, atraída por sons e cheiros humanos. *'Ela é rápida, mas teme a luz,'* diz a última página. "
            "De repente, uma sombra se move pelo salão, e você sente que não está sozinho."
        ),
        'imagem': 'diario_segredos.jpg',  # Imagem do diário
        'escolhas': [
            {'texto': 'Fugir da taberna antes que seja tarde demais', 'proximo': 'vilarejo'},
            {'texto': 'Enfrentar a sombra e tentar descobrir o que está acontecendo', 'proximo': 'sombra_taberna'}
        ]
    },
    'andar_de_cima': {
        'texto': (
            "Você sobe as escadas lentamente, cada degrau rangendo sob seus pés. O andar de cima está tomado por teias de aranha "
            "e poeira, mas você ouve murmúrios vindos de um quarto no final do corredor. Ao abrir a porta, você encontra um espelho antigo, "
            "e nele, uma versão de você mesmo que começa a rir de forma maníaca. O que você faz?"
        ),
        'imagem': 'espelho_sombrio.jpg',  # Imagem do espelho sombrio
        'escolhas': [
            {'texto': 'Destruir o espelho e quebrar o feitiço', 'proximo': 'espelho_quebrado'},
            {'texto': 'Fugir do quarto e voltar para a entrada', 'proximo': 'taberna'}
        ]
    },
    'espelho_quebrado': {
        'texto': (
            "Ao quebrar o espelho, um grito agudo ecoa pela taberna, e a figura dentro dele desaparece. "
            "Você encontra um amuleto brilhante entre os cacos de vidro. Ele parece ter um propósito, mas você não sabe qual ainda. "
            "O ambiente ao seu redor fica mais leve, como se algo tivesse sido libertado."
        ),
        'imagem': 'amuleto_brilhante.jpg',  # Imagem do amuleto
        'escolhas': [
            {'texto': 'Levar o amuleto com você e continuar explorando', 'proximo': 'vilarejo'}
        ]
    },
    'igreja': {
        'texto': (
            "A igreja é majestosa, mesmo em sua decadência. O sino para de tocar assim que você cruza os portões. "
            "No altar, há um sacerdote idoso, que parece aliviado ao vê-lo. Ele explica que o vilarejo foi amaldiçoado "
            "devido à ganância de seus antigos líderes, e que apenas um ritual perigoso pode quebrar a maldição.\n\n"
            "No entanto, você percebe que algo está errado: a sombra do sacerdote não combina com seus movimentos."
        ),
        'imagem': 'igreja_sombra.jpg',  # Imagem da igreja
        'escolhas': [
            {'texto': 'Confiar no sacerdote e ajudar no ritual', 'proximo': 'ritual_maldicao'},
            {'texto': 'Confrontar o sacerdote sobre sua sombra estranha', 'proximo': 'sacerdote_sombra'},
            {'texto': 'Fugir da igreja e buscar outra solução', 'proximo': 'vilarejo'}
        ]
    },
    'sacerdote_sombra': {
        'texto': (
            "Você aponta para a sombra, e o sacerdote hesita antes de começar a rir. Ele revela ser o espírito de um "
            "dos líderes gananciosos, preso à igreja até que a maldição seja quebrada. Ele implora que você o ajude, "
            "mas avisa: *'A maldição é faminta. Sempre haverá um preço a pagar.'*"
        ),
        'imagem': 'sacerdote_sombra_revelada.jpg',  # Imagem do sacerdote revelado
        'escolhas': [
            {'texto': 'Aceitar ajudar no ritual, apesar do risco', 'proximo': 'ritual_maldicao'},
            {'texto': 'Recusar e continuar explorando', 'proximo': 'vilarejo'}
        ]
    },
    'ritual_maldicao': {
        'texto': (
            "O sacerdote começa o ritual, entoando palavras em uma língua antiga. O ambiente ao redor escurece, "
            "e sombras começam a dançar nas paredes. Você sente algo pesado em seu peito, como se a maldição tentasse te consumir. "
            "De repente, a criatura do vilarejo aparece, interrompendo o ritual. Você precisa decidir rápido."
        ),
        'imagem': 'ritual_interrompido.jpg',  # Imagem do ritual sendo interrompido
        'escolhas': [
            {'texto': 'Proteger o sacerdote para completar o ritual', 'proximo': 'ritual_sucesso'},
            {'texto': 'Lutar contra a criatura para salvar a si mesmo', 'proximo': 'criatura_combate'}
        ]
    },
    'ritual_sucesso': {
        'texto': (
            "Você defende o sacerdote enquanto ele completa o ritual. A criatura grita de dor enquanto é consumida pela luz, "
            "e a maldição finalmente é quebrada. O vilarejo começa a recuperar sua antiga beleza, mas o sacerdote desaparece, "
            "deixando para trás apenas uma frase no ar: *'Você será lembrado.'* Você venceu, mas sente que perdeu algo importante."
        ),
        'imagem': 'ritual_completo.jpg',  # Imagem do ritual concluído
        'escolhas': [
            {'texto': 'FIM', 'proximo': 'creditos'}
        ]
    },
    'criatura_combate': {
        'texto': (
            "Você enfrenta a criatura com tudo que tem, mas ela é ágil e implacável. Após uma luta intensa, "
            "você consegue feri-la, mas também sai gravemente machucado. O ritual é interrompido, e a maldição permanece.\n\n"
            "Fim do jogo."
        ),
        'imagem': 'luta_criatura.jpg',  # Imagem da luta contra a criatura
        'escolhas': [
            {'texto': 'FIM', 'proximo': 'creditos'}
        ]
    }

}

def creditos(request):
    return render(request, 'JOGO/creditos.html')
