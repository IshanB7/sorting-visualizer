import pygame
from random import randint

screen = pygame.display.set_mode((1200,800))
array = [randint(1, 300) for i in range(300)]
XList = [[i, i+4] for i in range(0, 1200, 4)]

pygame.init()
pygame.font.init()

def bubbleSort(List):
    for i in range(len(List)-1):
        sorted = False
        for j in range(len(List)-i-1):
            if List[j] > List[j+1]:
                sorted = True
                List[j], List[j+1] = List[j+1], List[j]
                show(List)
        if not sorted:
            break

def selectSort(List):
    for i in range(len(List)-1):
        min = i
        for j in range(i+1, len(List)):
            if List[min] > List[j]:
                min = j
        List[min], List[i] = List[i], List[min]
        show(List)

def mergeSort(List, xList):

    if len(List) > 1:
        mid = len(List)//2
        left = List[:mid]
        lxList = xList[:mid]
        right = List[mid:]
        rxList = xList[mid:]

        mergeSort(left, lxList)
        List[:mid] = left

        mergeSort(right, rxList)
        List[mid:] = right

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                List[k] = left[i]
                i += 1
            else:
                List[k] = right[j]
                j += 1
            show(List, xList)
            k += 1
        
        while i < len(left):
            List[k] = left[i]
            i += 1; k += 1
            show(List, xList)
        
        while j < len(right):
            List[k] = right[j]
            j += 1; k += 1
            show(List, xList)

def part(List, xList):
    pivot = List[len(List)-1]
    index = -1

    for i in range(len(List)):
        if List[i] < pivot:
            index += 1
            List[index], List[i] = List[i], List[index]
            show(List, xList)
    List[index + 1], List[len(List)-1] = List[len(List)-1], List[index+1]
    return (index + 1)

def quickSort(List, xList):
    if len(List) > 1:
        pi = part(List, xList)
        left = List[:pi]
        lxList = xList[:pi]
        right = List[pi+1:]
        rxList = xList[pi+1:]
        quickSort(left, lxList)
        List[:pi] = left
        quickSort(right, rxList)
        List[pi+1:] = right
        show(List, xList)

def show(LIST, xLIST = XList):
    x1 = xLIST[0][0]
    x2 = xLIST[len(xLIST)-1][1]
    pygame.draw.rect(screen, (0,0,0), (x1, 0, x2-x1, 800))
    i = x1
    for each in LIST:
        pygame.draw.rect(screen, (0,255,0), (i+1, 800-(2.5*each), 2, (2.5*each)))
        i += 4

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.update()
    pygame.event.pump()
    pygame.time.Clock().tick(200)

def menu():
    color1 = (0,0,0)
    color2 = (255,255,255)

    Font = pygame.font.SysFont("Times New Roman", 70)
    bubbleText = Font.render("Bubble Sort", True, color1, color2)
    bubbleRect = bubbleText.get_rect(center = (300, 200))
    selectText = Font.render("Selection Sort", True, color1, color2)
    selectRect = selectText.get_rect(center = (900, 200))
    mergeText = Font.render("Merge Sort", True, color1, color2)
    mergeRect = mergeText.get_rect(center = (300, 600))
    quickText = Font.render("Quick Sort", True, color1, color2)
    quickRect = quickText.get_rect(center = (900, 600))

    yes = 1

    while yes:

        screen.fill((0, 0, 0))
        screen.blit(bubbleText, bubbleRect)
        screen.blit(selectText, selectRect)
        screen.blit(mergeText, mergeRect)
        screen.blit(quickText, quickRect)
        pygame.display.update()
        pygame.event.pump()

        while True:
            pressed = pygame.mouse.get_pressed()

            if pressed[0] or pressed[1]:
                x, y = pygame.mouse.get_pos()
                
                if bubbleRect.collidepoint(x, y):
                    show(array[:])
                    bubbleSort(array[:])
                    pygame.time.delay(2000)
                    break
                elif selectRect.collidepoint(x, y):
                    show(array[:])
                    selectSort(array[:])
                    pygame.time.delay(2000)
                    break
                elif mergeRect.collidepoint(x, y):
                    show(array[:])
                    mergeSort(array[:], XList)
                    pygame.time.delay(2000)
                    break
                elif quickRect.collidepoint(x, y):
                    show(array[:])
                    quickSort(array[:], XList)
                    pygame.time.delay(2000)
                    break
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

def main():
    menu()

main()