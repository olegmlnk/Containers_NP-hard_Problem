import math

MAX_WEIGHT = 100
cargos_list = [
    [54, 73, 15, 6, 51, 64, 90, 63, 91, 72, 37, 37, 59, 28, 71, 80, 87, 56, 90, 41],
    [70, 52, 65, 11, 69, 17, 61, 83, 51, 12, 51, 6, 38, 67, 64, 89, 32, 54, 4, 75],
    [79, 41, 12, 38, 69, 36, 70, 56, 44, 60, 49, 14, 65, 14, 26, 86, 83, 39, 69, 35]
]

def NFA(cargos):
    containers = [MAX_WEIGHT]  # Початковий контейнер
    compares = 0
    
    for cargo in cargos:
        compares += 1
        # Спочатку перевіряємо останній контейнер
        if containers[-1] >= cargo:
            containers[-1] -= cargo
        else:
            # Якщо не вміщується, створюємо новий контейнер
            containers.append(MAX_WEIGHT - cargo)
    
    return len(containers), compares

def FFA(cargos):
    containers = [MAX_WEIGHT]  # Початковий контейнер
    compares = 0
    
    for cargo in cargos:
        placed = False
        compares += 1
        
        # Спочатку перевіряємо останній контейнер
        if containers[-1] >= cargo:
            containers[-1] -= cargo
            placed = True
        else:
            # Якщо не вміщується в останній, перевіряємо всі контейнери по черзі
            for i in range(len(containers) - 1):  # Виключаємо останній, бо вже перевірили
                compares += 1
                if containers[i] >= cargo:
                    containers[i] -= cargo
                    placed = True
                    break
        
        if not placed:
            # Якщо нікуди не вміщується, створюємо новий контейнер
            containers.append(MAX_WEIGHT - cargo)
    
    return len(containers), compares

def WFA(cargos):
    containers = [MAX_WEIGHT]
    compares = 0

    for cargo in cargos:
        compares += 1
        if containers[-1] >= cargo:
            containers[-1] -= cargo
            continue

        # Якщо в останній не влазить — шукаємо найгірший варіант
        worst_index = -1
        max_space = -1
        for i in range(len(containers) - 1):  # виключаємо останній
            compares += 1
            if containers[i] >= cargo and containers[i] > max_space:
                worst_index = i
                max_space = containers[i]

        if worst_index != -1:
            containers[worst_index] -= cargo
        else:
            containers.append(MAX_WEIGHT - cargo)

    return len(containers), compares


def BFA(cargos):
    containers = [MAX_WEIGHT]  # Початковий контейнер
    compares = 0
    
    for cargo in cargos:
        placed = False
        compares += 1
        
        # Спочатку перевіряємо останній контейнер
        if containers[-1] >= cargo:
            containers[-1] -= cargo
            placed = True
        else:
            # Шукаємо контейнер з мінімальним вільним місцем, але достатнім для вантажу
            best_index = -1
            min_space = float('inf')
            
            for i in range(len(containers) - 1):  # Виключаємо останній, бо вже перевірили
                compares += 1
                if containers[i] >= cargo and containers[i] - cargo < min_space:
                    best_index = i
                    min_space = containers[i] - cargo
            
            if best_index != -1:
                containers[best_index] -= cargo
                placed = True
            else:
                # Якщо нікуди не вміщується, створюємо новий контейнер
                containers.append(MAX_WEIGHT - cargo)
    
    return len(containers), compares

def run_packing_algorithms(cargos, row_number):
    print("-" * 30)
    print(f"Рядок {row_number} (Без впорядкування)")
    
    nfa_result = NFA(cargos)
    print(f"NFA: {nfa_result[0]} ; Обчислювальна складність: {nfa_result[1]}")
    
    ffa_result = FFA(cargos)
    print(f"FFA: {ffa_result[0]} ; Обчислювальна складність: {ffa_result[1]}")
    
    wfa_result = WFA(cargos)
    print(f"WFA: {wfa_result[0]} ; Обчислювальна складність: {wfa_result[1]}")
    
    bfa_result = BFA(cargos)
    print(f"BFA: {bfa_result[0]} ; Обчислювальна складність: {bfa_result[1]}")
    
    sorted_cargos = sorted(cargos, reverse=True)
    sorting_complexity = round(len(cargos) * math.log2(len(cargos)))
    
    print("-" * 30)
    print(f"Рядок {row_number} (З впорядкуванням)")
    
    nfa_sorted = NFA(sorted_cargos)
    print(f"NFA: {nfa_sorted[0]} ; Обчислювальна складність: {nfa_sorted[1] + sorting_complexity}")
    
    ffa_sorted = FFA(sorted_cargos)
    print(f"FFA: {ffa_sorted[0]} ; Обчислювальна складність: {ffa_sorted[1] + sorting_complexity}")
    
    wfa_sorted = WFA(sorted_cargos)
    print(f"WFA: {wfa_sorted[0]} ; Обчислювальна складність: {wfa_sorted[1] + sorting_complexity}")
    
    bfa_sorted = BFA(sorted_cargos)
    print(f"BFA: {bfa_sorted[0]} ; Обчислювальна складність: {bfa_sorted[1] + sorting_complexity}")

def main():
    for i, cargos in enumerate(cargos_list, start=1):
        run_packing_algorithms(cargos, i)
        print("=" * 40)  # Розділення між наборами

main()
