import PIL.ImageGrab
import pyautogui
import time

teste = True;
while (teste == True):

# seleciona o pixel do captcha e descobre qual cor eh desta vez
    
    time.sleep(10)
    captcha = PIL.ImageGrab.grab().load()[707, 261]
    optionCaptcha = (1, 1, 1)

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


    if PIL.ImageGrab.grab().load()[111, 388] == (15, 11, 7):    #caso desconecte, para
        teste = False

    time.sleep(600)                                             #repete de 10 em 10min



# opcao do captcha 1: (544, 303)
# opcao do captcha 2: (581, 303)
# opcao do captcha 3: (617, 303)
# opcao do captcha 4: (653, 303)
# opcao do captcha 5: (690, 303)
# opcao do captcha 6: (725, 303)
# opcao do captcha 7: (760, 303)
# opcao do captcha 8: (796, 303)
# opcao do captcha 9: (832, 303)