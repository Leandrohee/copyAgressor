import pyscreenshot as pshot
import pyautogui as pa
import time

# time.sleep(2)
# print(pa.position())

saldoRegiao = pa.locateOnScreen("./imgs/ref.png",confidence=0.9)
regiaoEsq,regiaoSup,larg,alt = saldoRegiao

def printaCorSaldo():
    corSaldo = pshot.grab(bbox=(regiaoEsq, regiaoSup + 30, regiaoEsq + 20, regiaoSup + 50))
    corSaldo.save("./imgs/saldo.png")
    return corSaldo                     # Retorna o print da cor do Saldo

def printaCorPorc():
    corPorc = pshot.grab(bbox=(regiaoEsq + 200, regiaoSup + 30, regiaoEsq + 220, regiaoSup + 50))
    corPorc.save("./imgs/porc.png")
    return corPorc                     # Retorna o print da cor da Porc

def verificaCor(foto):
    sizeX, sizeY = foto.size
    contRed,contGreen,contBlue = 0,0,0
    #print(sizeX,sizeY)

    for x in range(sizeX):
        for y in range(sizeY):
            pixel = foto.getpixel((x, y))
            #print(pixel)
            #Se vermelho maior que isso (200,100,100)
            if pixel[0] > 150 and pixel[1] < 100 and pixel[2] < 100:
                contRed = contRed + 1
            #Se Verde maior que isso (100,200,100)
            elif pixel[0] < 100 and pixel[1] > 150 and pixel[2] < 100:
                contGreen = contGreen + 1
            #Se Azul maior que isso (100,100,200)
            elif pixel[0] < 100 and pixel[1] < 100 and pixel[2] > 150:
                contBlue = contBlue + 1

    if contRed > 200:
        return "vermelho"
    elif contGreen > 200:
        return  "verde"
    elif contBlue > 200:
        return  "azul"
    else:
        return "branco"

    #print(f"Red: {contRed}, Green: {contGreen}, Blue: {contBlue}")

def verificaPosicao():
    comprado = pa.locateOnScreen("./imgs/comprado.png",confidence=0.9)
    vendido = pa.locateOnScreen("./imgs/vendido.png",confidence=0.9)

    #print(f"comprado: {comprado}")
    #print(f"vendido: {vendido}")

    if (comprado != None and vendido == None):
        return "comprado"
    elif (vendido != None and comprado == None):
        return "vendido"
    elif (comprado == None and vendido == None):
        return "zerado"
    else:
        return "problema"

def clicaCompra():
    botaoComprar = pa.locateOnScreen("./imgs/botaoComprar.png",confidence=0.9)
    comprarEsq, comprarTop,comprarLarg, comprarAlt = botaoComprar
    pa.leftClick(comprarEsq+20,comprarTop+7)

def clicaVenda():
    botaoVender = pa.locateOnScreen("./imgs/botaoVender.png", confidence=0.9)
    venderEsq,venderTop, venderLarg, venderAlt = botaoVender
    pa.leftClick(venderEsq + 20, venderTop + 7)

def clicaZerar():
    botaoZerar = pa.locateOnScreen("./imgs/botaoZerar.png", confidence=0.9)
    zerarEsq, zerarTop, zerarLarg, zerarAlt = botaoZerar
    pa.moveTo(zerarEsq + 20, zerarTop + 7)

def moveProCentro():
    pa.moveTo(600, 600)

def entraPosicao():
    while True:
        posicao = verificaPosicao()
        fotoSaldo = printaCorSaldo()
        fotoPorc = printaCorPorc()
        corSaldo =  verificaCor(fotoSaldo)
        corPorc = verificaCor(fotoPorc)

        print(f"posicao: {posicao}, corSaldo: {corSaldo}, corPorc: {corPorc}")

        if (posicao == "zerado" and corSaldo == "verde" and corPorc == "azul"):
            clicaCompra()
            moveProCentro()
        elif (posicao == "zerado" and corSaldo == "vermelho" and corPorc == "azul"):
            clicaVenda()
            moveProCentro()
        elif (posicao == "comprado" and corSaldo == "vermelho" and corPorc == "azul"):
            clicaZerar()
            clicaVenda()
            moveProCentro()
        elif (posicao == "vendido" and corSaldo == "verde" and corPorc == "azul"):
            clicaZerar()
            clicaCompra()
            moveProCentro()

entraPosicao()