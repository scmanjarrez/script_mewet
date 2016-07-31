from selenium import webdriver
import time
import sys

usuarios = []
pines = []
claves = []


def parser():
    try:
        with open('cuentas.txt', 'r') as fich1:
            count = 0
            for line in fich1:
                if (count == 0 and line != '\n'):
                    usuarios.append(line)
                    count += 1
                elif (count == 1 and line != '\n'):
                    claves.append(line)
                    count += 1
                elif (count == 2 and line != '\n'):
                    pines.append(line)
                    count += 1
                elif (count == 3 and line == '\n'):
                    count = 0
                else:
                    print('Error al parsear el fichero cuentas.txt')
                    sys.exit(1)
    except:
        print("No se ha podido encontrar el fichero cuentas.txt")


def insert_pin(driver, pin1):
    pin=int(pin1)
    p1 = pin // 1000
    click_button(driver, p1)
    tmp = pin % 1000

    p2 = tmp // 100
    click_button(driver, p2)
    tmp = tmp % 100

    p3 = tmp // 10
    click_button(driver, p3)

    p4 = tmp % 10
    click_button(driver, p4)


def click_button(driver, n):
    if (n == 0):
        driver.find_element_by_id('numpadButton0').click()
    elif (n == 1):
        driver.find_element_by_id('numpadButton1').click()
    elif (n == 2):
        driver.find_element_by_id('numpadButton2').click()
    elif (n == 3):
        driver.find_element_by_id('numpadButton3').click()
    elif (n == 4):
        driver.find_element_by_id('numpadButton4').click()
    elif (n == 5):
        driver.find_element_by_id('numpadButton5').click()
    elif (n == 6):
        driver.find_element_by_id('numpadButton6').click()
    elif (n == 7):
        driver.find_element_by_id('numpadButton7').click()
    elif (n == 8):
        driver.find_element_by_id('numpadButton8').click()
    elif (n == 9):
        driver.find_element_by_id('numpadButton9').click()


def main():
    for pos in range(len(usuarios)):
        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)

        # open URL
        driver.get("http://www.mewet.es/")

        driver.find_element_by_id('loginnick').send_keys(usuarios[pos])
        driver.find_element_by_id('loginpass').send_keys(claves[pos])
        driver.find_element_by_id('loginpin').send_keys("")
        insert_pin(driver, pines[pos])

        driver.find_element_by_id('loginsubmit').click()
        time.sleep(3)

        # print and source code
        if(driver.current_url != 'http://www.mewet.es/news.php'):
            print('Error al logear con la cuenta \"{0}\"'.format(usuarios[pos].replace("\n","")))
        else:
            print('Se ha logeado correctamente con la cuenta \"{0}\"'.format(usuarios[pos].replace("\n","")))
        driver.close()
        driver.quit()


if __name__ == '__main__':
    parser()
    assert len(usuarios)==len(pines)==len(claves), "Error en fichero cuentas.txt"
    main()
