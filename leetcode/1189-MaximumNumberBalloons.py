class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        my_dict = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        
        for let in text:
            
            if let in my_dict:
                my_dict[let] += 1
        
        total = 0
        
        while my_dict["b"] >= 1:
            valid = True
            
            for key, value in my_dict.items():
                
                if key == "b" or key == "a" or key == "n":
                    if value < 1:
                        valid = False
                        break
                    else:
                        my_dict[key] -= 1
                    
                elif key == "l" or key == "o":
                    if value < 2:
                        valid = False
                        break
                    else:
                        my_dict[key] -= 2
            
            if valid:
                total += 1
        
        return total