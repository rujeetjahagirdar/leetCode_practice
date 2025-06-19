class Router:

    def __init__(self, memoryLimit: int):
        self.limit= memoryLimit
        self.q = deque()
        self.uniq_packets = set()
        self.q_len = 0
        self.destination_time = defaultdict(list)
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if(packet in self.uniq_packets):
            return False
        else:
            if(self.q_len>=self.limit):
                t = self.q.popleft()
                self.uniq_packets.remove(t)
                self.q_len-=1
                self.destination_time[t[1]].remove(t[2])
            self.q.append(packet)
            self.uniq_packets.add(packet)
            self.q_len+=1
            bisect.insort(self.destination_time[destination], timestamp)
            return True

    def forwardPacket(self) -> List[int]:
        if(self.q):
            packet = self.q.popleft()
            self.uniq_packets.remove(packet)
            self.q_len-=1
            self.destination_time[packet[1]].remove(packet[2])
            return [packet[0], packet[1], packet[2]]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ans=0
        # print(self.q)
        # for p in self.q:
        #     if(p[1]==destination and (startTime<=p[2]<=endTime)):
        #         ans+=1
        # return ans

        left = bisect.bisect_left(self.destination_time[destination], startTime)
        right = bisect.bisect_right(self.destination_time[destination], endTime)
        
        return right - left

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)