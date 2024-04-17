class Solution:
    def calPoints(self, operations: List[str]) -> int:
        index = 0
        record_sum = 0
        records = []
        last = 0
        remove ='C'
        double = 'D'
        sum_of_records ='+'

        for index in range(len(operations)):
            if operations[index].isdigit() or (operations[index][0] == '-' and operations[index][1:].isdigit()):
                records.append(int(operations[index]))
            elif operations[index] == remove and len(records) >=1:
                records.pop()
            elif operations[index]==double and len(records) >=1:
                number = records[-1] * 2
                records.append(number)
            elif operations[index]== sum_of_records and len(records) >=2:
                last = records[len(records)-2] + records[len(records)-1]
                records.append(last)
        
            else:
                return 0

        return sum(records)