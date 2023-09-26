import pyscreenshot as pshot
import pyautogui as pa
import time

# time.sleep(2)
# print(pa.position())

def pegaRefPosicao():
    refPosicao = pa.locateOnScreen('./imgs/referenciaPosicao.png',confidence=0.9)
    return refPosicao

def minhaPosicao():
    left, top, width, height = pegaRefPosicao()


    comprado =  pa.locateOnScreen('./imgs/comprado.png',confidence=0.8,region=(left,top,200,100))
    vendido =  pa.locateOnScreen('./imgs/vendido.png',confidence=0.8,region=(left,top,200,100))

    if comprado != None and vendido == None:
        return "comprado"
    elif comprado == None and vendido != None:
        return "vendido"
    elif comprado == None and vendido == None:
        return "zerado"
    else:
        return "problema"

def printSaldoCorretoras():
    referenciaSaldo = pa.locateOnScreen('./imgs/referenciaSaldo.png',confidence=0.8)
    left,top,width, height = referenciaSaldo
    corSaldo = pshot.grab(bbox=(left, top + 30, left + 20, top + 50))                       # 20x20
    corSaldo.save("./imgs/saldo.png")

    return corSaldo

def corSaldoCorretora(foto):
    sizeX, sizeY = foto.size
    contRed, contGreen, contBlue = 0, 0, 0

    for x in range(sizeX):
        for y in range(sizeY):
            pixel = foto.getpixel((x, y))
            # print(pixel)
            # Se vermelho maior que isso (200,100,100)
            if pixel[0] > 150 and pixel[1] < 100 and pixel[2] < 100:
                contRed = contRed + 1
            # Se Verde maior que isso (100,200,100)
            elif pixel[0] < 100 and pixel[1] > 150 and pixel[2] < 100:
                contGreen = contGreen + 1
            # Se Azul maior que isso (100,100,200)
            elif pixel[0] < 100 and pixel[1] < 100 and pixel[2] > 150:
                contBlue = contBlue + 1

    if contRed > 200:
        return "vermelho"
    elif contGreen > 200:
        return "verde"
    elif contBlue > 200:
        return "azul"
    else:
        return "branco"

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
    pa.leftClick(zerarEsq + 20, zerarTop + 7)

def moveProCentro():
    pa.moveTo(600, 600)

def entrarPosicao():
    posicao = minhaPosicao()
    fotoSaldo = printSaldoCorretoras()
    corSaldo = corSaldoCorretora(fotoSaldo)

    if posicao == "zerado" and corSaldo == 'verde':
        clicaCompra()
        moveProCentro()
    elif  posicao == "zerado" and corSaldo == 'vermelho':
        clicaVenda()
        moveProCentro()
    elif posicao == "comprado" and corSaldo == 'vermelho':
        clicaZerar()
        clicaVenda()
        moveProCentro()
    elif posicao == "vendido" and corSaldo == 'verde':
        clicaZerar()
        clicaCompra()
        moveProCentro()


def verificaComponetens():
    botaoComprar = pa.locateOnScreen("./imgs/botaoComprar.png", confidence=0.9)
    botaoVender = pa.locateOnScreen("./imgs/botaoVender.png", confidence=0.9)
    botaoZerar = pa.locateOnScreen("./imgs/botaoZerar.png", confidence=0.9)

    print(f" A referencia da posicao esta em: {pegaRefPosicao()}")
    print(f"A minha posicao é: {minhaPosicao()}")
    print(f"A cor do saldo é: {corSaldoCorretora(printSaldoCorretoras())}")
    print(f"O botao comprar esta em: {botaoComprar}")
    print(f"O botao vender esta em: {botaoVender}")
    print(f"O botao zerar esta em: {botaoZerar}")

entrarPosicao()