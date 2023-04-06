#6.2[32]: �������� ������� print_operation_table(operation, num_rows=6, num_columns=6), 
#   ������� ��������� � �������� ��������� �������, ����������� ������� �� ������ ������ � �������, 
#   �.�. ������� ���� ����������. ��������� num_rows � num_columns ��������� ����� ����� � �������� �������, 
#   ������� ������ ���� �����������. ��������� ����� � �������� ���� � �������.
#�������/�����:
#print_operation_table(lambda x,y: x**y,4,4)
#1   1   1   1
#2   4   8  16
#3   9  27  81
#4  16  64 256

#print_operation_table(lambda x,y: x*y)
#1   2   3   4   5   6
#2   4   6   8  10  12
#3   6   9  12  15  18
#4   8  12  16  20  24
#5  10  15  20  25  30
#6  12  18  24  30  36
#(*) ����������. ����������� ��������������� ����� � �������� ����� � ��������

#�������/�����:
#print_operation_table(lambda x,y: x**y,4,4)
#       1   2   3   4
#    ----------------
#1 |    1   1   1   1
#2 |    2   4   8  16
#3 |    3   9  27  81
#4 |    4  16  64 256

#print_operation_table(lambda x,y: x*y)
#       1   2   3   4   5   6
#    ------------------------
#1 |    1   2   3   4   5   6
#2 |    2   4   6   8  10  12
#3 |    3   6   9  12  15  18
#4 |    4   8  12  16  20  24
#5 |    5  10  15  20  25  30
#6 |    6  12  18  24  30  36

from pydoc import stripid


def print_operation_table(operation, num_rows=6, num_columns=6):
    if operation(1,1) == 2:
        print (1, end = '\t')

    for i in range(1, num_rows+1):


        for j in range (1,num_columns+1):
            if operation(1,1) == 2:
                j = j - 1
            print(operation(i,j), end = '\t')
        print()


print (print_operation_table(lambda x,y: x**y,4,4))
