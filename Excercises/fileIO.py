def main():
  print("Starting Script....")
  f = open('test.txt')
  print(f.read())
  f.close()
  
  try:
    with open('test.txt', mode='a+')as  file:
        text = file.write('hey  it\'s me!!')
        text = file.write('\n')
        print(file.read())
  except FileNotFoundError as e:
    print("File does not exist")
    raise(e)

  except IOError as e:
    print("IO Error")
    raise(e)


if __name__ == '__main__':
  main()
