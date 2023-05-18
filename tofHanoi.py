def towerofHanoi(n: int, src: str,helper: str,dest: str):
    if n == 1 :
        print(f"transfer disk {n} from {src} to {dest}")
        return

    towerofHanoi(n-1, src, dest, helper)
    print(f"transfer disk {n} from {src} to {dest}")
    towerofHanoi(n-1, helper, src, dest)

n = 3
towerofHanoi(n, "S", "H", "D")
