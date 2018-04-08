try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
from pathlib import Path
#import os
import deepcut

class ThaiDeepcut():

    def __init__(self,sentense):
        self.__sentense = sentense
        
    def sentese(self):
        return self.__sentense

    def start_deepcut(self):
        wordchannels = deepcut.tokenize(self.__sentense)
        print(wordchannels)

class ReadOCR():

    def __init__(self,path_to_tesseract,path_to_image):
        filepath = Path(path_to_tesseract).resolve()
        pytesseract.pytesseract.tesseract_cmd = str(filepath)
        self.__tpath = str(Path(path_to_tesseract).resolve())
        self.__ipath = Path(path_to_image).resolve()

    def tesseract_path(self):
        return self.__tpath

    def image_path(self):
        return self.__ipath

    def reader(self,read_lang):
        pytesseract.pytesseract.tesseract_cmd = self.__tpath
        words = pytesseract.image_to_string(Image.open(str(self.__ipath)), lang=read_lang)
        print('reader = ' + words)
        return words

if __name__ == '__main__':
    # mockup path for tesseract
    # 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    # mockup path for image
    # 'C:\\Python\\reader\\TH02.png'
    ocr = ReadOCR('C:/Program Files (x86)/Tesseract-OCR/tesseract.exe','C:\\Python\\reader\\TH03.png')
    channels = ocr.reader('tha')
    thdeepcut = ThaiDeepcut(channels)
    thdeepcut.start_deepcut()