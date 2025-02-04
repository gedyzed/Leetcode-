class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        count_paired = defaultdict(int)
        for cpdomain in cpdomains:
            rep, domain = cpdomain.split()
        
            sub = domain.split(".")
            if len(sub) == 3:
                count_paired[f"{sub[0]}.{sub[1]}.{sub[2]}"] += int(rep)
                count_paired[f"{sub[1]}.{sub[2]}"] += int(rep)      
            else:          
                count_paired[f"{sub[0]}.{sub[1]}"] += int(rep)
            count_paired[sub[-1]] += int(rep)
   
        return [f"{count} {domain}" for domain, count in count_paired.items()]       



            
        