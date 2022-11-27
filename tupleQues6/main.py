'''Ques 6
Consider a tupleQues6 t1 = {1,2,5,7,9,2,4,6,8,10}.
Write a program to perform following operations:
  (a) Print another tupleQues6 whose values are even numbers in the given tupleQues6.
  (b) Concatenate a tupleQues6 t2 = {11,13,15} with t1.
  (c) Return maximum and minimum value from this tupleQues6.
'''


def main():
    # Given
    t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
    t2 = (11, 13, 15)

    even_tuple = ()
    concatenated_tuple = ()
    max_value = 0
    min_value = 0

    print('Original Tuple:', t1)

    # Another Tuple with Even Numbers in t1
    for i in t1:
        if i % 2 == 0:
            even_tuple += (i,)
    print('Even Tuple:', even_tuple)

    # Concatenate t2
    concatenated_tuple = t1 + t2
    print('Concatenated Table: ', concatenated_tuple)

    # Max and Min Values in concatenated tupleQues6
    print('Max Value:', max(concatenated_tuple))
    print('Min Value:', min(concatenated_tuple))


if __name__ == '__main__':
    main()
