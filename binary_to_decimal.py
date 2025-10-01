class BinaryToDecimal():
    def __init__(self, binary_number: str):
        self.binary_number: str = binary_number
        self._binary_holder: list[str] = [] # Stores each individual binary number
        self._true_binary_nums: list[str] = []
        self._binary_nums_with_place_value: list[str] = [] # Stores each binary number (Right to Left), with its corresponding place value Ex: "0 = 1", "1 = 2", "1 = 4"
        self._binary_place_values: list[str] = []
        
    def binary_to_decimal(self) -> None:
        place_value: int = 1
        total_place_value_sum: int = 0
        for binary_number in self.binary_number:
            self._binary_holder.append(binary_number) # Adds each individual value to a list, seperated.
        
        for binary_number in self._binary_holder:
            if binary_number == "1" or binary_number == "0": 
                self._true_binary_nums.append(binary_number)
            else:
                print(f"{binary_number} is not a binary number | It must be only 1's and 0's")
                print(f"Removing {binary_number}...\n")
                
        print(self._true_binary_nums)                            
        for binary_number in range(0, len(self._true_binary_nums)): # Counts backwards (Right to Left instead of Left to Right)
            print("hi")
            place_value *= 2
            if self._true_binary_nums[0] != "11" or self._true_binary_nums != "01": # If it does not have a place value of "1", which it never will, then it will add the 1
                if self._true_binary_nums[0] == "1":
                    self._true_binary_nums[0].replace("1", "11")
                elif self._true_binary_nums[0] == "0":
                    self._true_binary_nums[0].replace("0", "01")                 
                
            self._binary_nums_with_place_value.append(str(self._true_binary_nums[binary_number] + str(place_value))) # Ex: ["01", "12", "14", "08"]
            
        print(self._binary_nums_with_place_value)    
                
        for index in range(0, len(self._binary_nums_with_place_value)):
            if self._binary_nums_with_place_value[index][0].__contains__("1"):
                self._binary_nums_with_place_value[index][0].replace("1", "")
                self._binary_place_values.append(self._binary_nums_with_place_value[index])

                             
            else: # This varation runs if every number in the string is a binary number (1 or 0)
                for binary_number in range(0, len(self._binary_holder), -1): # Counts backwards (Right to Left instead of Left to Right)
                        multiply_place_value: int = place_value * 2
                        # self._binary_nums_with_place_value.append(str(self._binary_holder[binary_number] + str(multiply_place_value))) # Ex: ["01", "12", "14", "08"]
                        self._binary_nums_with_place_value.append("hi")
                for index in range(0, len(self._binary_nums_with_place_value)):
                    if self._binary_nums_with_place_value[index][0] == "1": # Checks if the first value of that index is a 1, if it is, then it removes it and just keeps int place_value, appending it to a seperate list for calucation
                        self._binary_nums_with_place_value[index][0].replace("1", "")
                        self._binary_place_values.append(self._binary_nums_with_place_value[index])
                    else:
                        pass                
                                                        
            for number in self._binary_place_values: # Takes all the values in the list, and adds them up, effectively getting total sum of all the place values for all the 1's in the binary number
                total_place_value_sum += int(number)                           
                                                    
   
        
         

number = BinaryToDecimal("1011023456789")  # Should equal 22
number.binary_to_decimal()  

      