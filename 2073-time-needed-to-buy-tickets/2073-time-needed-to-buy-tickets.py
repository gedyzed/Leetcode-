class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
            totalTickets = sum(tickets)
    
            for i in range(len(tickets)):
                if tickets[i] < tickets[k] or k == i:
                    continue
                elif tickets[i] == tickets[k] and k < i:
                    totalTickets -= 1  
                elif tickets[i] > tickets[k] and k < i:
                    totalTickets += tickets[k]-tickets[i]-1
                else:  
                    totalTickets += tickets[k]-tickets[i]
                        
            return totalTickets 


        