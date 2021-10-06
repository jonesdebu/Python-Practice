from translate import Translator

def main():
  with open('translator.py', 'r') as file:
    text = file.read()
    translator = Translator(to_lang='ja')
    translation = translator.translate(text)
    print(translation)
    
    with open('./translation.txt', mode='w') as file:
      file.write(translation)



if __name__ == '__main__':
  main()