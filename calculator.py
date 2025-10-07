while True:
        print("----------CALCULATOR----------")
        a = int(input("Write first number:")) #kullanıcın girdiği ilk sayıyı bir değişkene tanımla.
        b = int(input("Write second number:"))#kullanıcın girdiği ikinci sayıyı bir değişkene tanımla.
        islem = input("Select the action you want to perform.(+,-,*,/)")#kullanıcının yapaçağı işlemi bir değişkene tanımla.
        if islem == "+": #eğer + yazarsa a ve b değişkenini toplayıp yaz.
            print("result:",a + b)
        elif islem == "-": #eğer - yazarsa a ve b değişkenini toplayıp yaz.
            print("result:",a - b)
        elif islem == "*": #eğer * yazarsa a ve b değişkenini toplayıp yaz.
            print("result:",a * b)
        elif islem == "/": #eğer / yazarsa a ve b değişkenini toplayıp yaz.
            print("result:",a / b)
        else:  #eğer bu dürdünden başka birşey yazarsa gerekli komutu yazdır.
            print("invalid transaction")
        print("action completed.") #işlemin tamamlandığına dair çıktı
