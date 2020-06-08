class Operation:
    @staticmethod
    def delimiter(A, symbol):
        ClearB = []
        for i in symbol:
            A = A.replace(i, '♫')

        B = A.split("♫ ")
        for i in range(0, len(B)):
            if str(B[i]) != ' ' and str(B[i]) != '♫' and str(B[i]) != '':
                ClearB.append(B[i].replace('♫', ''))
        return ClearB

    @staticmethod
    def calculate(A, B):
        Line = ""
        i = 1
        while i < 600:
            for j in B:
                if str(i) == str(j):
                    K = B.index(int(j))
                    Line += A[K] + ". "
                    del(A[K])
                    del(B[K])
                    i -= 1
            i += 1
        return Line




class TextObr:
    def __init__(self, text):
        self.symbol1 = [".", "!", "?"]
        TextObr.allchar1 = []
        TextObr.sentence1 = Operation.delimiter(text, self.symbol1)
        TextObr.mas1count = []
        SentenceObr(TextObr.sentence1)
        CharObr(TextObr.allchar1)
        print(TextObr.mas1count)


class SentenceObr:
    def __init__(self, sentence):
        print(sentence)
        for i in sentence:
            self.sword1 = i.split(" ")
            SentenceObr.char1insentence = []
            SentenceObr.char1countinsentence = 0
            SwordObr(self.sword1)
            TextObr.mas1count.append(SentenceObr.char1countinsentence)


class SwordObr():
    def __init__(self, sword):
        print(sword)
        for i in sword:
            for j in range(0, len(i)):
                if i[j] != ' ':
                    SentenceObr.char1insentence.append(i[j])
                    SentenceObr.char1countinsentence += 1
                    TextObr.allchar1.append(i[j])


class CharObr:
    def __init__(self, char):
        print(char)


class Main:
    TextObr(input("Write text\n"))
    print("Output\n" + str(Operation.calculate(TextObr.sentence1, TextObr.mas1count)))
