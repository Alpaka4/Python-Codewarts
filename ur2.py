###Integer1◦ Дано расстояние L в сантиметрах. Используя операцию деления нацело, найти количество полных метров в нем (1 метр = 100 см).
##print("введите расстояние")
##L=int(input())
##M=L//100
##print("M=",M)
###Integer2 Дана масса M в килограммах. Используя операцию деления нацело,найти количество полных тонн в ней (1 тонна = 1000 кг).
##print("введите массу")
##M=int(input())
##T=M//1000
##print("T=",T)
###Integer3 Дан размер файла в байтах. Используя операцию деления нацело,найти количество полных килобайтов, которые занимает данный файл(1 килобайт = 1024 байта)
##print("введите размер файла(в байтах)")
##P=int(input())
##K=P//1024
##print("K=",K)
###Integer4 Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B(без наложений). Используя операцию деления нацело, найти количество
###отрезков B, размещенных на отрезке A
##print("введите два целых положительных числа(A>B)")
##A=int(input())
##B=int(input())
##R=A//B
##print("R=",R)
###Integer5◦Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). Используя операцию взятия остатка от деления нацело, найти
###длину незанятой части отрезка A.
##print("введите два целых положительных числа(A>B)")
##A=int(input())
##B=int(input())
##R=A%B
##print("R=",R)
###Integer6◦Дано двузначное число. Вывести вначале его левую цифру (десятки), а затем — его правую цифру (единицы). Для нахождения десятков использовать операцию деления нацело, для нахождения единиц — операцию взятия остатка от деления
##print("введите двузначное число")
##A=int(input())
##D=A//10
##print("D=",D)
##E=A%10
##print("E=",E)
###Integer7◦Дано двузначное число. Найти сумму и произведение его цифр
##print("введите двузначное число")
##A=int(input())
##D=A//10
##E=A%10
##S=D+E
##print("S=",S)
##P=D*E
##print("P=",P)
###Integer8◦Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
##print("введите двузначное число")
##A=int(input())
##D=A//10
##E=A%10
##P=E*10+D
##print("P=",P)
###Integer9◦Дано трехзначное число. Используя одну операцию деления нацело,вывести первую цифру данного числа (сотни).
##print("введите трёхзначное число")
##A=int(input())
##S=A//100
##print("S=",S)
#Integer10◦Дано трехзначное число. Вывести вначале его последнюю цифру(единицы), а затем — его среднюю цифру (десятки).
##print("введите трёхзначное число")
##A=int(input())
##D=(A%100)//10
##print("D=",D)
##E=A%10
##print("E=",E)
###Integer11◦Дано трехзначное число. Найти сумму и произведение его цифр.
##print("введите трёхзначное число")
##A=int(input())
##S=A//100
##D=(A%100)//10
##E=A%10
##C=S+D+S
##print("C=",C)
##P=S*D*C
##print("P=",P)
###Integer12◦Дано трехзначное число. Вывести число, полученное при прочтении исходного числа справа налево.
##print("введите трёхзначное число")
##A=int(input())
##S=A//100
##D=(A%100)//10
##E=A%10
##C=(E*100)+(D*10)+S
##print("C=",C)
###Integer13◦Дано трехзначное число. В нем зачеркнули первую слева цифру иприписали ее справа. Вывести полученное число.
##print("введите трёхзначное число")
##A=int(input())
##S=A//100
##D=(A%100)//10
##E=A%10
##C=(D*100)+(E*10)+S
##print("C=",C)
###Integer14◦Дано трехзначное число. В нем зачеркнули первую справа цифруи приписали ее слева. Вывести полученное число
##print("введите трёхзначное число")
##A=int(input())
##S=A//100
##D=(A%100)//10
##E=A%10
##C=(E*100)+(S*10)+D
##print("C=",C)
###Integer15◦Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков исходного числа (например, 123 перейдет в 213).
##print("введите трёхзначное число")
##A=int(input())
##S=A//100
##D=(A%100)//10
##E=A%10
##C=(D*100)+(S*10)+E
##print("C=",C)
###Integer16 Дано трехзначное число. Вывести число, полученное при перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132).
##print("введите трёхзначное число")
##A=int(input())
##S=A//100
##D=(A%100)//10
##E=A%10
##C=(S*100)+(E*10)+D
##print("C=",C)
###Integer17◦Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию взятия остатка от деления, найти цифру,соответствующую разряду сотен в записи этого числа
##print("введите число(A>999)")
##A=int(input())
##O=A%1000
##C=O//100
##print("C=",C)
###Integer18 Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию взятия остатка от деления, найти цифру,соответствующую разряду тысяч в записи этого числа.
##print("введите число(A>999)")
##A=int(input())
##O=A%10000
##C=O//1000
##print("C=",C)
###Integer19◦С начала суток прошло N секунд (N — целое). Найти количество полных минут, прошедших с начала суток
##print("введите кличество секунд прошедшее с начала дня")
##S=int(input())
##M=S//60
##print("M=",M)
###Integer20◦С начала суток прошло N секунд (N — целое). Найти количествополных часов, прошедших с начала суток.
##print("введите кличество секунд прошедшее с начала дня")
##S=int(input())
##M=S//3600
##print("M=",M)
###Integer21 С начала суток прошло N секунд (N — целое). Найти количество секунд, прошедших с начала последней минуты.
##print("введите кличество секунд прошедшее с начала дня")
##S=int(input())
##M=S%60
##print("M=",M)
###Integer22◦С начала суток прошло N секунд (N — целое). Найти количество секунд, прошедших с начала последнего часа
##print("введите кличество секунд прошедшее с начала дня")
##S=int(input())
##M=S%3600
##print("M=",M)
###Integer23◦С начала суток прошло N секунд (N — целое). Найти количество полных минут, прошедших с начала последнего часа.
##print("введите кличество секунд прошедшее с начала дня")
##S=int(input())
##M=S%3600
##Ch=M//60
##print("Ch=",Ch)
###Integer29◦Даны целые положительные числа A, B, C. На прямоугольнике размера A × B размещено максимально возможное количество квадратов со стороной C (без наложений). Найти количество квадратов, размещенных
###на прямоугольнике, а также площадь незанятой части прямоугольника
##print("введите три положительных целых числа")
##A=int(input())
##B=int(input())
##C=int(input())
##Pr=A*B
##K=Pr//C
##print("K=",K)
##S=Pr%C
##print("S=",S)
###Integer30◦Дан номер некоторого года (целое положительное число). Определить соответствующий ему номер столетия, учитывая, что, к примеру,началом 20 столетия был 1901 год
##print("введите любой год")
##G=int(input())
##S=(G//100)+1
##print("S=",S)






