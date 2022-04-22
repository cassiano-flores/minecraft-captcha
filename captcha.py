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

    if captcha >= (0, 39, 234) and captcha <= (71, 162, 257):  # azul
        optionCaptcha = (124, 144, 169)

    if captcha >= (241, 146, 0) and captcha <= (257, 190, 100):  # laranja
        optionCaptcha = (169, 134, 104)

    if captcha >= (250, 5, 0) and captcha <= (254, 76, 74):  # vermelho
        optionCaptcha = (144, 104, 104)

    if captcha >= (184, 0, 250) and captcha <= (234, 102, 254):  # roxo
        optionCaptcha = (154, 113, 169)

    if captcha >= (230, 230, 230) and captcha <= (252, 252, 252):  # branco
        optionCaptcha = (184, 184, 184)

    if captcha >= (250, 94, 205) and captcha <= (260, 183, 237):  # rosa
        optionCaptcha = (179, 134, 149)

    if captcha >= (238, 226, 19) and captcha <= (257, 256, 122):  # amarelo
        optionCaptcha = (174, 174, 104)

    if captcha >= (0, 250, 8) and captcha <= (138, 254, 106):  # verde
        optionCaptcha = (134, 164, 93)

    if captcha >= (0, 0, 0) and captcha <= (30, 30, 30):  # preto
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