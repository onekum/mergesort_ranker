import sys

def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    left = arr[l:l+n1]
    right = arr[mid+1:mid+1+n2]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        print(f"Compare '{left[i]}' and '{right[j]}'.")
        print("Enter '1' for the first item, '2' for the second item, or '0' for equal:")
        preference = int(input())

        if preference == 1:
            arr[k] = left[i]
            i += 1
        elif preference == 2:
            arr[k] = right[j]
            j += 1
        else:  # if preference == 0 (equal)
            arr[k] = left[i]
            i += 1
            k += 1
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

def main():
    if len(sys.argv) < 2:
        print("Usage: python mergesort.py item1 item2 item3 ...")
        sys.exit(1)

    items = sys.argv[1:]
    merge_sort(items, 0, len(items) - 1)
    print("\nFinal ranking of items:")
    for item in items:
        print(item)

if __name__ == "__main__":
    main()
