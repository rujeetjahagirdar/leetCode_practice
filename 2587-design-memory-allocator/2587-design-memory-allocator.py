class Allocator:

    def __init__(self, n: int):
        self.memory = ["_"] * n  # Memory array
        self.free_blocks = [(0, n - 1)]  # List of free memory ranges as (start, end)
        self.allocated = {}

    def allocate(self, size: int, mID: int) -> int:
        for index, (start, end) in enumerate(self.free_blocks):
            if end - start + 1 >= size:
                # Allocate memory
                alloc_start = start
                alloc_end = start + size - 1
                self.memory[alloc_start:alloc_end + 1] = [mID] * size

                # Update free_blocks
                if alloc_end < end:
                    self.free_blocks[index] = (alloc_end + 1, end)
                else:
                    self.free_blocks.pop(index)

                # Update allocated
                if mID not in self.allocated:
                    self.allocated[mID] = []
                self.allocated[mID].append((alloc_start, alloc_end))

                return alloc_start
        return -1

    def freeMemory(self, mID: int) -> int:
        if mID not in self.allocated:
            return 0

        freed_units = 0
        for start, end in self.allocated[mID]:
            # Free memory and count freed units
            self.memory[start:end + 1] = ["_"] * (end - start + 1)
            freed_units += end - start + 1
            # Add the freed range back to free_blocks
            self.free_blocks.append((start, end))

        # Remove the entry for mID
        del self.allocated[mID]

        # Merge free blocks
        self.free_blocks.sort()  # Sort by start
        merged_blocks = []
        for start, end in self.free_blocks:
            if merged_blocks and merged_blocks[-1][1] + 1 >= start:
                # Merge overlapping or adjacent blocks
                merged_blocks[-1] = (merged_blocks[-1][0], max(merged_blocks[-1][1], end))
            else:
                merged_blocks.append((start, end))
        self.free_blocks = merged_blocks

        return freed_units        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)