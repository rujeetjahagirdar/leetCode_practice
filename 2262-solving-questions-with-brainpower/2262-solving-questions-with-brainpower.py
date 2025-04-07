class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """For each question we have two choices, solve this question of skip this question.
        If we solve this question, we can earn, current question point + point of question after skipping
        If we skip this question, then we will consider next question and maximum points we could earn by skipping this question will be equal to the solving this next question."""
        dp = [0] * (len(questions)+1)

        for i in reversed(range(len(questions))):
            t = questions[i][0]

            if(i+questions[i][1]+1 < len(questions)):
                t+=dp[i+questions[i][1]+1]
            
            #skip

            dp[i] = max(t, dp[i+1])
        
        print(dp)
        return dp[0]