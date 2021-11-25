while True:
     our= input('变量名: ')
     if our == 'exit':
         print('退出')
         break
     if our[0].isalpha() or our[0] == '_':
         for i in our[1:]:
             if not(i.isalnum() or i == '_'):
                 print('%s变量名不合法' %our)
                 break
         else:
             print('%s变量名合法' %our)
     else:
         print('%s变量名不合法' %our)
