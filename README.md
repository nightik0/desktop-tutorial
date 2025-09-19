def main():
    m = int(input())
    n = int(input())
    k = int(input())  # k - количество КУСКОВ
    
    total_cuts_allowed = k - 1  # количество РАЗРЕЗОВ
    
    left, right = 1, m * n
    
    def can_divide(size):
        for h_cuts in range(1, m + 1):
            # Максимальная ширина куска при h_cuts горизонтальных разрезах
            max_width = size // h_cuts
            if max_width <= 0:
                continue
                
            if max_width >= n:
                # Нужны только горизонтальные разрезы
                if (h_cuts - 1) <= total_cuts_allowed:
                    return True
            else:
                # Нужны и горизонтальные и вертикальные разрезы
                v_pieces = (n + max_width - 1) // max_width
                v_cuts = v_pieces - 1
                total_cuts = (h_cuts - 1) + v_cuts
                if total_cuts <= total_cuts_allowed:
                    return True
        return False
    
    while left < right:
        mid = (left + right) // 2
        if can_divide(mid):
            right = mid
        else:
            left = mid + 1
            
    print(left)

if __name__ == "__main__":
    main()
