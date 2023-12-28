class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []
        sum_of_previous = 0

        for op in operations:
            if op == '+':
                sum_of_previous = record [-1] + record[-2]
            
                record.append(sum_of_previous)

            elif op == 'D':
                record.append(record[-1]*2)
            
            elif op =='C':
                record.pop()

            else:
                record.append(int(op))
            
        return sum(record)
