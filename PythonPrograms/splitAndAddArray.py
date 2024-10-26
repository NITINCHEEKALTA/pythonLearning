import array


def main():
        
        print(splitAndAdd())

def splitAndAdd():
    
        arr = array.array('i',[1,2,3,4,5,6,7,8,9,10])
        n = len(arr)
        k = 3
        new_arr = [0] * n


        if k <= 0 or k >= n:
                return arr
        
        split_arr1 = arr[:k]
        spit_arr2 = arr[k:]

        new_arr = spit_arr2 + split_arr1

        return new_arr

if __name__ == "__main__":
        main()            