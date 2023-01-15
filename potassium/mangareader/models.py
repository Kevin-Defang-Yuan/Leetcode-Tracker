from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['complete']
    
    def __str__(self):
        return self.description

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=100)
    difficulty_level = models.IntegerField()
    complete = models.BooleanField(default=False)
    link = models.URLField(max_length=200)

    class Meta:
        ordering = ['topic', 'difficulty_level', 'name']

    def __str__(self):
        output = self.name + ' - ' + self.topic + ' - ' + self.difficulty
        return output

class Collection(models.Model):
    # null=True, can have blank collections
    # blank=True, forms can accepts blanks
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    questions = models.ManyToManyField(Question) 
    custom = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_question_count(self):
        count = 0
        for question in self.questions.all():
            count += 1
        return count

    def get_question_completed(self):
        count = 0
        for question in self.questions.all():
            if question.complete == True:
                count += 1
        return count
    
    def initialize_topics(self):
        topics = []
        for question in self.questions.all():
            if question.topic not in topics:
                topics.append(question.topic)
        return topics
    
    def populate_topic(self, topic):
        topic_question_list = []
        for question in self.questions.all().order_by('difficulty_level'):
            if topic == question.topic:
                topic_question_list.append(question)
        return topic_question_list
    
    def get_topic_questions_complete(self, topic):
        count = 0
        for question in self.questions.all():
            if question.complete == True and question.topic == topic:
                count += 1
        return count
    
    def get_topic_questions_total(self, topic):
        count = 0
        for question in self.questions.all():
            if question.topic == topic:
                count += 1
        return count

    






@receiver(post_save, sender=User)
def init_new_user(instance, created, raw, **kwargs):
    if created and not raw:
        contains_duplicate = Question.objects.create(
            name="Contains Duplicate",
            user=instance,
            topic="Arrays & Hashing",
            difficulty="Easy",
            difficulty_level = 1,
            complete=False,
            link='https://leetcode.com/problems/contains-duplicate/'
        )
        two_sum = Question.objects.create(
            name="Two Sum",
            user=instance,
            topic="Arrays & Hashing",
            difficulty="Easy",
            difficulty_level = 1,
            complete=False,
            link='https://leetcode.com/problems/two-sum/'
        )
        group_anagrams = Question.objects.create(
            name="Group Anagrams",
            user=instance,
            topic="Arrays & Hashing",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/group-anagrams/'
        )
        sort_colors = Question.objects.create(
            name="Sort Colors",
            user=instance,
            topic="Arrays & Hashing",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/sort-colors/'
        )
        first_missing_positive = Question.objects.create(
            name="First Missing Positive",
            user=instance,
            topic="Arrays & Hashing",
            difficulty="Hard",
            difficulty_level = 3,
            complete=False,
            link='https://leetcode.com/problems/first-missing-positive/'
        )
        valid_palindrome = Question.objects.create(
            name="Valid Palindrome",
            user=instance,
            topic="Two Pointers",
            difficulty="Easy",
            difficulty_level = 1,
            complete=False,
            link='https://leetcode.com/problems/valid-palindrome/'
        )
        move_zeroes = Question.objects.create(
            name="Move Zeroes",
            user=instance,
            topic="Two Pointers",
            difficulty="Easy",
            difficulty_level = 1,
            complete=False,
            link='https://leetcode.com/problems/move-zeroes/'
        )
        three_sum = Question.objects.create(
            name="3Sum",
            user=instance,
            topic="Two Pointers",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/3sum/'
        )
        container_with_most_water = Question.objects.create(
            name="Container With Most Water",
            user=instance,
            topic="Two Pointers",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/container-with-most-water/'
        )
        trapping_rain_water = Question.objects.create(
            name="Trapping Rain Water",
            user=instance,
            topic="Two Pointers",
            difficulty="Hard",
            difficulty_level = 3,
            complete=False,
            link='https://leetcode.com/problems/trapping-rain-water/'
        )

        search_in_rotated_sorted_array = Question.objects.create(
            name="Search In Rotated Sorted Array",
            user=instance,
            topic="Binary Search",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/search-in-rotated-sorted-array/'
        )

        koko_eating_bananas = Question.objects.create(
            name="Koko Eating Bananas",
            user=instance,
            topic="Binary Search",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/koko-eating-bananas/'
        )

        binary_search = Question.objects.create(
            name="Binary Search",
            user=instance,
            topic="Binary Search",
            difficulty="Easy",
            difficulty_level = 1,
            complete=False,
            link='https://leetcode.com/problems/binary-search/'
        )
        split_array_largest_sum = Question.objects.create(
            name="Split Array Largeset Sum",
            user=instance,
            topic="Binary Search",
            difficulty="Hard",
            difficulty_level = 3,
            complete=False,
            link='https://leetcode.com/problems/split-array-largest-sum/'
        )
        invert_binary_tree = Question.objects.create(
            name="Invert Binary Tree",
            user=instance,
            topic="Trees",
            difficulty="Easy",
            difficulty_level = 1,
            complete=False,
            link='https://leetcode.com/problems/invert-binary-tree/'
        )
        diameter_of_binary_tree = Question.objects.create(
            name="Diameter of Binary Tree",
            user=instance,
            topic="Trees",
            difficulty="Easy",
            difficulty_level = 1,
            complete=False,
            link='https://leetcode.com/problems/diameter-of-binary-tree/'
        )
        binary_tree_level_order_traversal = Question.objects.create(
            name="Binary Tree Level Order Traversal",
            user=instance,
            topic="Trees",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/binary-tree-level-order-traversal/'
        )
        validate_binary_search_tree = Question.objects.create(
            name="Validate Binary Search Tree",
            user=instance,
            topic="Trees",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/validate-binary-search-tree/'
        )
        binary_tree_maximum_path_sum = Question.objects.create(
            name="Binary Tree Maximum Path Sum",
            user=instance,
            topic="Trees",
            difficulty="Hard",
            difficulty_level = 3,
            complete=False,
            link='https://leetcode.com/problems/binary-tree-maximum-path-sum/'
        )
        convert_bst_to_greater_tree = Question.objects.create(
            name="Convert Bst to Greater Tree",
            user=instance,
            topic="Trees",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/convert-bst-to-greater-tree/'
        )
        reverse_linked_list = Question.objects.create(
            name="Reverse Linked List",
            user=instance,
            topic="Linked List",
            difficulty="Easy",
            difficulty_level = 1,
            complete=False,
            link='https://leetcode.com/problems/reverse-linked-list/'
        )
        palindrome_linked_list = Question.objects.create(
            name="Palindrome Linked List",
            user=instance,
            topic="Linked List",
            difficulty="Easy",
            difficulty_level = 1,
            complete=False,
            link='https://leetcode.com/problems/palindrome-linked-list/'
        )
        reorder_list = Question.objects.create(
            name="Reorder List",
            user=instance,
            topic="Linked List",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/reorder-list/'
        )
        add_two_numbers = Question.objects.create(
            name="Add Two Numbers",
            user=instance,
            topic="Linked List",
            difficulty="Medium",
            difficulty_level = 2,
            complete=False,
            link='https://leetcode.com/problems/add-two-numbers/'
        )
        merge_k_sorted_lists = Question.objects.create(
            name="Merge K Sorted Lists",
            user=instance,
            topic="Linked List",
            difficulty="Hard",
            difficulty_level = 3,
            complete=False,
            link='https://leetcode.com/problems/merge-k-sorted-lists/'
        )
        reverse_nodes_in_k_group = Question.objects.create(
            name="Reverse Nodes in K Group",
            user=instance,
            topic="Linked List",
            difficulty="Hard",
            difficulty_level = 3,
            complete=False,
            link='https://leetcode.com/problems/reverse-nodes-in-k-group/'
        )
        

        




        blind75 = Collection.objects.create(
            name="Blind 75", 
            user=instance,
        )
        neetcode150 = Collection.objects.create(
            name="NeetCode 150", 
            user=instance,
        )
        neetcodeall = Collection.objects.create(
            name="NeetCode All",
            user=instance
        )
        blind75.questions.add(
            contains_duplicate, two_sum, group_anagrams, valid_palindrome, three_sum, container_with_most_water,
            search_in_rotated_sorted_array, invert_binary_tree, binary_tree_level_order_traversal, validate_binary_search_tree,
            binary_tree_maximum_path_sum, reverse_linked_list, reorder_list, merge_k_sorted_lists
        )
        neetcode150.questions.add(
            contains_duplicate, two_sum, group_anagrams, valid_palindrome, three_sum, container_with_most_water,
            search_in_rotated_sorted_array, koko_eating_bananas, binary_search, invert_binary_tree, diameter_of_binary_tree,
            binary_tree_level_order_traversal, validate_binary_search_tree, binary_tree_maximum_path_sum,
            reverse_linked_list, reorder_list, add_two_numbers, merge_k_sorted_lists, reverse_nodes_in_k_group
        )
        neetcodeall.questions.add(
            contains_duplicate, two_sum, group_anagrams, sort_colors, first_missing_positive, valid_palindrome, move_zeroes, three_sum,
            container_with_most_water, trapping_rain_water, search_in_rotated_sorted_array, koko_eating_bananas, binary_search,
            split_array_largest_sum, invert_binary_tree, diameter_of_binary_tree, binary_tree_level_order_traversal, validate_binary_search_tree,
            binary_tree_maximum_path_sum, convert_bst_to_greater_tree, reverse_linked_list, palindrome_linked_list,
            reorder_list, add_two_numbers, merge_k_sorted_lists, reverse_nodes_in_k_group
        )


