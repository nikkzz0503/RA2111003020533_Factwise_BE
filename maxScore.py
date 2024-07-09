def maxScore(cardPoint,k):
    n=len(cardPoints)
    window_sum=sum(cardPoints[:k])
    max_score=window_sum
    for i in range(k):
        window_sum=window_sum-cardPoints[k-1-i]+cardPoints[n-1-i]
        max_score=max(max_score,window_sum)
    return max_score
cardPoints= [1,2,3,4,5,6,1]
k=3
print(maxScore(cardPoints,k))