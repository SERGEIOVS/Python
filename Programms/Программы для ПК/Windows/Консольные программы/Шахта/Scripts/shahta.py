import statistics 
import pandas as pd

my_file = open('кол-во детонаторов.txt', 'w')

dets = 18

det_number   = []

for i in range(dets):
  i+=1
  det_number.append(i)

det_quantity = [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  2 ,  1 ,  1]

camera_V = 60

print()

print()

run = True

while run:

            print('-' * 50)

            Total_need = int(input('Cколько кубов требуется добыть? '))

            #12640 кубов

            Camers_count = Total_need / camera_V

            print('',int(Camers_count),'камер нужно')

            print()

            print('|','-' * 50)

            for i in range(len(det_quantity)):

                print('|','детонаторов серии',det_number[i],'нужно:',det_quantity[i] *int(Camers_count),'|')

                print('-' * 50)

                vsego = [det_number[i],det_quantity[i] * int(camera_V)]
            
                my_file.write(str(vsego)+'\n')

                df = pd.DataFrame({

                                    'Тип'    : det_number,

                                    'Кол-во' :  det_quantity

                                  })
                
            df.to_excel('./расчет.xlsx')

            my_file.close()

            
            print(df)


