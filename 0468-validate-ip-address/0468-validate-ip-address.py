class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def checkipv4(ip):
            if('.' not in ip):
                return False
            nums = ip.split('.')
            
            if(len(nums)!=4):
                return False
            
            for n in nums:
                if(len(n)<1 or len(n)>3):
                    return False
                if(n[0]=='0' and len(n)>1):
                    return False
                if(not n.isnumeric()):
                    return False
                if(int(n)<0 or int(n)>255):
                    return False
            
            return True

        
        def checkipv6(ip):
            if(":" not in ip):
                return False
            
            nums = ip.split(":")

            if(len(nums)!=8):
                return False

            for n in nums:
                if(len(n)<1 or len(n)>4):
                    return False
                
                for c in n:
                    if(c not in '0123456789abcdefABCDEF'):
                        return False
            
            return True
        
        if(checkipv4(queryIP)):
            return "IPv4"
        if(checkipv6(queryIP)):
            return "IPv6"
        
        return "Neither"