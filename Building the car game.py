command = ('')
while command != 'quit':
   command = input ('>').lower()
   if command == 'start':
       print('car started')
   elif command =='stop':
          print('Car stopped')
   elif command == 'help':
          print('''
start-to start
stop-to stop
quit-to quit''')
   elif command == "quit" :
       break
   else:
    print("I don't understand")

