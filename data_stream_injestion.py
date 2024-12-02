class DataStream:
    def __init__(self):
        self.last_print_time = {}
    
    def should_output_data_str(self, timestamp: int, data_str: str) -> bool:
        if data_str in self.last_print_time:
            last_time = self.last_print_time[data_str]
            if timestamp - last_time < 5:
                return False
        
        self.last_print_time[data_str] = timestamp
        return True

data_stream = DataStream()

print(data_stream.should_output_data_str(timestamp=0, data_str="hello"))  
print(data_stream.should_output_data_str(timestamp=1, data_str="world"))  
print(data_stream.should_output_data_str(timestamp=6, data_str="hello"))  
print(data_stream.should_output_data_str(timestamp=7, data_str="hello"))  
print(data_stream.should_output_data_str(timestamp=8, data_str="world"))  
