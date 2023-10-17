def solution(numbers):
    answer = []
    
    for i in range(0,len(numbers)-1):
        for j in range(1,len(numbers)): # range(1,len(numbers)-1)에서 -1을 뺏더니 잘 굴러간다!
            if i+j <= len(numbers)-1:
                answer.append(numbers[i]+numbers[i+j])
            else:
                pass
    
    
    return sorted(list(set(answer)))