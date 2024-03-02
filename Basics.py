# # Find the count of each numbers in the list:
# #
# # def find_the_max_occurance_of_a_num(list):
# #     return max(list, key=list.count)
# #
# #
# # a = [1, 1, 5, 2, 2]
# # print(find_the_max_occurance_of_a_num(a))
#
#
# # Find the Index of the numbers that can add up to match the target
# # def sum_two_num(list, target):
# #     for i in range(len(list)):
# #         for j in range(i + 1, len(list)):
# #             if list[i] + list[j] == target:
# #                 return [list[i], list[j]]
# #
# #
# # list = [5, 8, 2, 4, 5, 6, 0]
# # target = 12
# # print(sum_two_num(list, target))
# #
# #
# # # dictionary where the keys are the unique characters from the string and the values are their frequencies in the string. The function should ignore case, so 'A' and 'a' should be counted as the same character.
# # # For example, given the string "Hello, World!", the function should return the following dictionary:
# #
# #
# # def convert_text_dict(string):
# #     s = string.lower()
# #     count_dict = {}
# #     for char in s:
# #         if char.isalpha():
# #             if char not in count_dict:
# #                 count_dict[char] = 1
# #             else:
# #                 count_dict[char] += 1
# #     return count_dict
# #
# #
# # s = 'Hello, World'
# # print(convert_text_dict(s))
# #
# #
# # # def find_pairs_with_sum(nums, target=10):
# # #     seen = set()  # Set to store numbers we've seen so far
# # #     pairs = set()  # Set to store unique pairs that sum to target
# # #     for num in nums:
# # #         complement = target - num
# # #         if complement in seen:
# # #             pairs.add(tuple(sorted((num, complement))))
# # #         else:
# # #             seen.add(num)
# # #         return list(pairs)
# # #
# # #
# # # # Test the function
# # # lst1 = [3, 4, 1, 6, 5, 7, -1, 6]
# # # print(find_pairs_with_sum(lst1))
# #
# #
# #
# #
# #
# # messi_goals = 30
# #
# # ronaldo_goals = 25
# #
# # neymar_goals = 15
# #
# #
# #
# # if (messi_goals > ronaldo_goals
# #     or ronaldo_goals > neymar_goals
# #     and messi_goals + neymar_goals < ronaldo_goals * 2):
# #     result = "Messi = GOAT"
# #
# # elif (neymar_goals + ronaldo_goals < messi_goals * 2
# #
# #       and messi_goals - ronaldo_goals < neymar_goals):
# #
# #     result = "Messi goat"
# # else:
# #     result = "Messi"
# #
# #
# # print(result)
# #
# #
# # def can_watch_two_movies(movie_durations, flight_duration):
# #     target_duration = flight_duration - 30  # exclude the 30-minute break for end credits
# #
# #     # Create a set to keep track of movies we've seen
# #     seen_movies = set()
# #
# #     for duration in movie_durations:
# #         # Calculate how much time is left after watching this movie
# #         remaining_time = target_duration - duration
# #
# #         # If the remaining_time exists in our set, it means we've found two movies
# #         # that can be watched entirely during the flight
# #         if remaining_time in seen_movies:
# #             return True
# #
# #         # Add the current movie duration to the set
# #         seen_movies.add(duration)
# #     return False
# #
# # # Test
# # movie_durations = [90, 130, 75, 60, 120, 150, 125]
# # flight_duration = 250
# # print(can_watch_two_movies(movie_durations, flight_duration))  # True
#
# #
#
#
# # def find_the_two_numbers_from_the_list_that_matches_the_target(lst, target):
# #     print(len(lst))
# #     for i in range(len(lst)):
# #         for j in range(i+1,len(lst)):
# #           if lst[i]+lst[j] == target:
# #            return lst[i],lst[j]
# #
# # list = [5, 8, 2, 4, 5, 6, 0]
# # target = 12
# # print(find_the_two_numbers_from_the_list_that_matches_the_target(list, target))
#
# def can_watch_two_movies(movie_durations, flight_duration):
#     movie_durations.sort()
#     target_duration = flight_duration - 30
#     left, right = 0, len(movie_durations) - 1
#
#     while left < right:
#         current_duration = movie_durations[left] + movie_durations[right]
#         if current_duration == target_duration:
#             return True
#         elif current_duration < target_duration:
#             left += 1
#         else:
#             right -= 1
#
#     return False
#
# # Test
# movie_durations = [90, 85, 75, 60, 120, 150, 125]
# flight_duration = 250
# print(can_watch_two_movies(movie_durations, flight_duration))  # True or False based on the movies list
