class Solution:

    def characterReplacement(self, s: str, k: int) -> int:

        # Initialize the frequency counter for the 26 letters of the alphabet

        frequency_counter = [0] * 26

        # Initialize pointers for the sliding window

        left = right = 0

        # Variable to keep track of the count of the most frequent character

        max_frequency = 0


        # Iterate over the characters in the string

        while right < len(s):

            # Update the frequency of the current character

            frequency_counter[ord(s[right]) - ord('A')] += 1

            # Find the maximum frequency count so far

            max_frequency = max(max_frequency, frequency_counter[ord(s[right]) - ord('A')])

          

            # Calculate the window size and compare it with the maximum frequency count and allowed replacements (k)

            if (right - left + 1) > max_frequency + k:

                # If the condition is true, decrement the frequency of the leftmost character 

                # as it will be excluded from the current window

                frequency_counter[ord(s[left]) - ord('A')] -= 1

                # Shrink the window by moving the left pointer forward

                left += 1

          

            # Move the right pointer forward to expand the window

            right += 1

      

        # Return the maximum length of the window

        return right - left