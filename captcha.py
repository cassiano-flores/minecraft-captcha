import PIL.ImageGrab
import pyautogui
import time

# possiveis ranges, do fraco ao forte

azul_fraco = (0, 4, 219)
azul_forte = (86, 200, 272)
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
verde_forte = (170, 269, 121)
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

    if captcha[0] >= azul_fraco[0] and captcha[0] <= azul_forte[0] and captcha[1] >= azul_fraco[1] and captcha[1] <= azul_forte[1] and captcha[2] >= azul_fraco[2] and captcha[2] <= azul_forte[2]:
        optionCaptcha = (124, 144, 169) # azul

    if captcha[0] >= laranja_fraco[0] and captcha[0] <= laranja_forte[0] and captcha[1] >= laranja_fraco[1] and captcha[1] <= laranja_forte[1] and captcha[2] >= laranja_fraco[2] and captcha[2] <= laranja_forte[2]:  
        optionCaptcha = (169, 134, 104) # laranja

    if captcha[0] >= vermelho_fraco[0] and captcha[0] <= vermelho_forte[0] and captcha[1] >= vermelho_fraco[1] and captcha[1] <= vermelho_forte[1] and captcha[2] >= vermelho_fraco[2] and captcha[2] <= vermelho_forte[2]: 
        optionCaptcha = (144, 104, 104) # vermelho

    if captcha[0] >= roxo_fraco[0] and captcha[0] <= roxo_forte[0] and captcha[1] >= roxo_fraco[1] and captcha[1] <= roxo_forte[1] and captcha[2] >= roxo_fraco[2] and captcha[2] <= roxo_forte[2]:  
        optionCaptcha = (154, 113, 169) # roxo

    if captcha[0] >= branco_fraco[0] and captcha[0] <= branco_forte[0] and captcha[1] >= branco_fraco[1] and captcha[1] <= branco_forte[1] and captcha[2] >= branco_fraco[2] and captcha[2] <= branco_forte[2]:  
        optionCaptcha = (184, 184, 184) # branco

    if captcha[0] >= rosa_fraco[0] and captcha[0] <= rosa_forte[0] and captcha[1] >= rosa_fraco[1] and captcha[1] <= rosa_forte[1] and captcha[2] >= rosa_fraco[2] and captcha[2] <= rosa_forte[2]:  
        optionCaptcha = (179, 134, 149) # rosa

    if captcha[0] >= amarelo_fraco[0] and captcha[0] <= amarelo_forte[0] and captcha[1] >= amarelo_fraco[1] and captcha[1] <= amarelo_forte[1] and captcha[2] >= amarelo_fraco[2] and captcha[2] <= amarelo_forte[2]:  
        optionCaptcha = (174, 174, 104) # amarelo

    if captcha[0] >= verde_fraco[0] and captcha[0] <= verde_forte[0] and captcha[1] >= verde_fraco[1] and captcha[1] <= verde_forte[1] and captcha[2] >= verde_fraco[2] and captcha[2] <= verde_forte[2]:  
        optionCaptcha = (134, 164, 93) # verde

    if captcha[0] >= preto_fraco[0] and captcha[0] <= preto_forte[0] and captcha[1] >= preto_fraco[1] and captcha[1] <= preto_forte[1] and captcha[2] >= preto_fraco[2] and captcha[2] <= preto_forte[2]:  
        optionCaptcha = (93, 93, 93) # preto


    if PIL.ImageGrab.grab().load()[544, 303] == optionCaptcha: #opcao 1
        pyautogui.click(544, 303)
        time.sleep(2)
        pyautogui.click(544, 303)

    if PIL.ImageGrab.grab().load()[581, 303] == optionCaptcha: #opcao 2
        pyautogui.click(581, 303)
        time.sleep(2)
        pyautogui.click(581, 303)

    if PIL.ImageGrab.grab().load()[617, 303] == optionCaptcha: #opcao 3
        pyautogui.click(617, 303)
        time.sleep(2)
        pyautogui.click(617, 303)

    if PIL.ImageGrab.grab().load()[653, 303] == optionCaptcha: #opcao 4
        pyautogui.click(653, 303)
        time.sleep(2)
        pyautogui.click(653, 303)

    if PIL.ImageGrab.grab().load()[690, 303] == optionCaptcha: #opcao 5
        pyautogui.click(690, 303)
        time.sleep(2)
        pyautogui.click(690, 303)

    if PIL.ImageGrab.grab().load()[725, 303] == optionCaptcha: #opcao 6
        pyautogui.click(725, 303)
        time.sleep(2)
        pyautogui.click(725, 303)

    if PIL.ImageGrab.grab().load()[760, 303] == optionCaptcha: #opcao 7
        pyautogui.click(760, 303)
        time.sleep(2)
        pyautogui.click(760, 303)

    if PIL.ImageGrab.grab().load()[796, 303] == optionCaptcha: #opcao 8
        pyautogui.click(796, 303)
        time.sleep(2)
        pyautogui.click(796, 303)

    if PIL.ImageGrab.grab().load()[832, 303] == optionCaptcha: #opcao 9
        pyautogui.click(832, 303)
        time.sleep(2)
        pyautogui.click(832, 303)


    time.sleep(5)                                               



# opcao do captcha 1: (544, 303)
# opcao do captcha 2: (581, 303)
# opcao do captcha 3: (617, 303)
# opcao do captcha 4: (653, 303)
# opcao do captcha 5: (690, 303)
# opcao do captcha 6: (725, 303)
# opcao do captcha 7: (760, 303)
# opcao do captcha 8: (796, 303)
# opcao do captcha 9: (832, 303)