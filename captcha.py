import PIL.ImageGrab
import pyautogui
import time

azul_fraco = (0, 4, 219)
azul_forte = (86, 177, 272)
laranja_fraco = (226, 131, 0)
laranja_forte = (272, 205, 115)
vermelho_fraco = (235, 0, 0)
vermelho_forte = (269, 91, 89)
roxo_fraco = (169, 0, 235)
roxo_forte = (249, 117, 269)
branco_fraco = (215, 215, 215)
branco_forte = (267, 267, 267)
rosa_fraco = (235, 79, 190)
rosa_forte = (275, 198, 252)
amarelo_fraco = (223, 211, 4)
amarelo_forte = (272, 271, 137)
verde_fraco = (0, 235, 0)
verde_forte = (153, 269, 121)
preto_fraco = (0, 0, 0)
preto_forte = (45, 45, 45)


teste = True;
while (teste == True):

# seleciona o pixel do captcha e descobre qual cor eh desta vez
    
    time.sleep(10)
    captcha = PIL.ImageGrab.grab().load()[707, 261]
    optionCaptcha = (1, 1, 1)

# o captcha e suas alternativas nao possuem as cores identicas
# dependendo do rgb do captcha, armazena em optionCaptcha a cor que sera a resposta

    if captcha.index(0) >= azul_fraco.index(0) and captcha <= azul_forte.index(0) and captcha.index(1) >= azul_fraco.index(1) and captcha <= azul_forte.index(1) and captcha.index(2) >= azul_fraco.index(2) and captcha <= azul_forte.index(2):
        optionCaptcha = (124, 144, 169) # azul

    if captcha >= laranja_fraco and captcha <= laranja_forte:  
        optionCaptcha = (169, 134, 104) # laranja

    if captcha >= vermelho_fraco and captcha <= vermelho_forte: 
        optionCaptcha = (144, 104, 104) # vermelho

    if captcha >= roxo_fraco and captcha <= roxo_forte:  # roxo
        optionCaptcha = (154, 113, 169)

    if captcha >= branco_fraco and captcha <= branco_forte:  # branco
        optionCaptcha = (184, 184, 184)

    if captcha >= rosa_fraco and captcha <= rosa_forte:  # rosa
        optionCaptcha = (179, 134, 149)

    if captcha >= amarelo_fraco and captcha <= amarelo_forte:  # amarelo
        optionCaptcha = (174, 174, 104)

    if captcha >= verde_fraco and captcha <= verde_forte:  # verde
        optionCaptcha = (134, 164, 93)

    if captcha >= preto_fraco and captcha <= preto_forte:  # preto
        optionCaptcha = (93, 93, 93)


    if PIL.ImageGrab.grab().load()[544, 303] == optionCaptcha: #opcao 1
        pyautogui.click(544, 303)

    if PIL.ImageGrab.grab().load()[581, 303] == optionCaptcha: #opcao 2
        pyautogui.click(581, 303)

    if PIL.ImageGrab.grab().load()[617, 303] == optionCaptcha: #opcao 3
        pyautogui.click(617, 303)

    if PIL.ImageGrab.grab().load()[653, 303] == optionCaptcha: #opcao 4
        pyautogui.click(653, 303)

    if PIL.ImageGrab.grab().load()[690, 303] == optionCaptcha: #opcao 5
        pyautogui.click(690, 303)

    if PIL.ImageGrab.grab().load()[725, 303] == optionCaptcha: #opcao 6
        pyautogui.click(725, 303)

    if PIL.ImageGrab.grab().load()[760, 303] == optionCaptcha: #opcao 7
        pyautogui.click(760, 303)

    if PIL.ImageGrab.grab().load()[796, 303] == optionCaptcha: #opcao 8
        pyautogui.click(796, 303)

    if PIL.ImageGrab.grab().load()[832, 303] == optionCaptcha: #opcao 9
        pyautogui.click(832, 303)


    #if PIL.ImageGrab.grab().load()[111, 388] == (15, 11, 7):    #caso desconecte, para
    #    teste = False

    time.sleep(5)                                             #repete de 10 em 10min



# opcao do captcha 1: (544, 303)
# opcao do captcha 2: (581, 303)
# opcao do captcha 3: (617, 303)
# opcao do captcha 4: (653, 303)
# opcao do captcha 5: (690, 303)
# opcao do captcha 6: (725, 303)
# opcao do captcha 7: (760, 303)
# opcao do captcha 8: (796, 303)
# opcao do captcha 9: (832, 303)