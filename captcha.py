import PIL.ImageGrab

# seleciona o pixel do captcha e descobre qual cor eh desta vez
captcha = PIL.ImageGrab.grab().load()[707, 261]

# o captcha e suas alternativas nao possuem as cores identicas
# dependendo do rgb do captcha, armazena em optionCaptcha a cor que sera a resposta

if captcha == (5, 97, 242):  # azul
    optionCaptcha = (124, 144, 169)

if captcha == (249, 187, 90):  # laranja
    optionCaptcha = (169, 134, 104)

if captcha == (252, 37, 27):  # vermelho
    optionCaptcha = (144, 104, 104)

if captcha == (224, 11, 252):  # roxo
    optionCaptcha = (154, 113, 169)

if captcha == (249, 249, 249):  # branco
    optionCaptcha = (184, 184, 184)

if captcha == (252, 179, 229):  # rosa
    optionCaptcha = (179, 134, 149)

if captcha == (246, 250, 4):  # amarelo
    optionCaptcha = (174, 174, 104)

if captcha == (163, 252, 58):  # verde
    optionCaptcha = (134, 164, 93)

if captcha == (6, 6, 6):  # preto
    optionCaptcha = (93, 93, 93)


#proximo: num range de tanto (9 opcoes), se o rgb da opcao 1 for igual ao optionCaptcha, clique
#                                                    opcao 2, 3, ... 9

#proximo: espera 10 minutos (proximo captcha), e repete infinitamente


# opcao do captcha 1: (544, 303)
# opcao do captcha 2: (581, 303)
# opcao do captcha 3: (617, 303)
# opcao do captcha 4: (653, 303)
# opcao do captcha 5: (690, 303)
# opcao do captcha 6: (725, 303)
# opcao do captcha 7: (760, 303)
# opcao do captcha 8: (796, 303)
# opcao do captcha 9: (832, 303)
