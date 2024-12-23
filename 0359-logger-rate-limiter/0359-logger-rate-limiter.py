class Logger:

    def __init__(self):
        self.msg_timestamp_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if(message not in self.msg_timestamp_map):
            self.msg_timestamp_map[message] = timestamp 
            return True
        else:
            if(timestamp<self.msg_timestamp_map[message]+10):
                return False
            else:
                self.msg_timestamp_map[message] = timestamp
                return True
        # return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)