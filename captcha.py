import PIL.ImageGrab

# seleciona o pixel do captcha e descobre qual cor eh desta vez
rgb = PIL.ImageGrab.grab().load()[712, 269]
print(rgb)

# o captcha e suas alternativas nao possuem as cores identicas
# dependendo do rgb do captcha, armazena em colorOption a cor que sera a resposta

if rgb == (252, 163, 228):  # rosa
    colorOption = (179, 133, 149)

if rgb == (252, 163, 228):  # rosa
    colorOption = (179, 133, 149)


# opcao do captcha 1: (x, y)
# opcao do captcha 2: (x, y)
# opcao do captcha 3: (x, y)
# opcao do captcha 4: (x, y)
# opcao do captcha 5: (x, y)
# opcao do captcha 6: (x, y)
# opcao do captcha 7: (x, y)
# opcao do captcha 8: (x, y)
# opcao do captcha 9: (x, y)
