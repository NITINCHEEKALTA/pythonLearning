def main():

    rotate()



def rotate():

    arr = [1,2,3,4,5,6,7]

    k =3
    length = len(arr)
    k = k % length

    rotated_arr = [0] * length

    for i in range(length):

        rotated_arr[(i + k) % length] = arr[i]  

    

    print(rotated_arr)


if __name__ == "__main__":
    main()

