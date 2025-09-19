def main():
    m = int(input())
    n = int(input())
    k = int(input())  # количество кусков
    
    # Для k кусков нужно k-1 разрез
    max_cuts = k - 1
    
    left, right = 1, m * n
    
    def possible(max_size):
        # Проверяем, можно ли разрезать m×n на куски не больше max_size
        # используя не более max_cuts разрезов
        for h_cuts in range(0, m):  # количество горизонтальных разрезов
            # Высота каждого куска после h_cuts разрезов
            h_piece = m // (h_cuts + 1)
            if h_piece == 0:
                continue
                
            # Максимальная ширина куска при данной высоте
            max_w = max_size // h_piece
            if max_w == 0:
                continue
                
            # Количество вертикальных разрезов needed
            w_pieces = (n + max_w - 1) // max_w
            w_cuts = max(0, w_pieces - 1)
            
            total_cuts = h_cuts + w_cuts
            if total_cuts <= max_cuts:
                return True
        return False
    
    while left < right:
        mid = (left + right) // 2
        if possible(mid):
            right = mid
        else:
            left = mid + 1
            
    print(left)

if __name__ == "__main__":
    main()
