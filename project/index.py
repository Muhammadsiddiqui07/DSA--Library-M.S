class Node:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    #Insertion in Linked list    
    def insert_at_end(self, title, author):
        new_node = Node(title, author)
        if self.start is None:
            self.start = new_node
            return
        ptr = self.start
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = new_node

    # Traversing
    def traverse(self):
        if self.start is None:
            print("List is empty")
            return
        ptr = self.start
        while ptr is not None:
            print("Title:", ptr.title, "Author:", ptr.author)
            ptr = ptr.next


    # Linear Search
    def linear_search(self, title):
        if self.start is None:
            print("List is Empty")
            return
        ptr = self.start
        while ptr is not None:
            if ptr.title == title:
                print(f" Title {ptr.title}, Author {ptr.author}")
                return
            ptr = ptr.next
        print(f"Value {title} Not found in List")
    
    
    #  Deletion
    def delete_from_position(self, position):
        if self.start is None:
            print("List is Already Empty")
            return
        if position == 1:
            self.start = self.start.next
            return
        current = self.start
        for i in range(1, position - 1):
            if current is None or current.next is None:
                print("Position Not Found")
                return
            current = current.next
        if current.next is not None:
            current.next = current.next.next
        else:
            print("Position Not Found")
      
    
    
# find mid for binary search
    def find_middle(self, start, end):
        slow = start
        fast = start.next
        while fast != end:
            fast = fast.next
            if fast != end:
                slow = slow.next
                fast = fast.next
        return slow

    # Binary search function to find mid point or know the position
    def binary_search_util(self, start, end, title):
        if start == end:
            return None

        mid = self.find_middle(start, end)
        if mid is None:
            return None

        if mid.title == title:
            return mid
        elif mid.title < title:
            return self.binary_search_util(mid.next, end, title)
        else:
            return self.binary_search_util(start, mid, title)
    
    # Binary search main function
    def binary_search(self, title):
        result = self.binary_search_util(self.start, None, title)
        if result:
            print(f" Title {result.title}, Author {result.author}")
        else:
            print(f"Value {title} Not found in List")
            
            
    # Count function
    def count(self):
        count = 0
        current = self.start
        while current:
            count += 1
            current = current.next
        return count
    
    
    
    # Insertion Sort
    def sorted_book(self):
        if self.start is None:
            return
        current = self.start.next
        while current is not None:
            title = current.title
            author = current.author
            prev = self.start

            while prev != current and prev.title < title:
                prev = prev.next

            if prev == self.start:
                new_node = Node(title, author)
                new_node.next = self.start
                self.start = new_node
            else:
                new_node = Node(title, author)
                new_node.next = prev.next
                prev.next = new_node

            current = current.next

    # Bubble Sort
    def bubSort(self):
        if self.start is None:
            return

        if self.start.next is None:
            return
        end = None
        while end != self.start:
            ptr1 = self.start
            while ptr1.next != end:
                ptr2 = ptr1.next
                if ptr1.title > ptr2.title:
                    ptr1.title, ptr2.title = ptr2.title, ptr1.title
                    ptr1.author, ptr2.author = ptr2.author, ptr1.author
                ptr1 = ptr1.next
            end = ptr1


    # Update Function
    def update_book(self, old_title, new_title, new_author):
        if self.start is None:
            print("List is Empty")
            return
        ptr = self.start
        while ptr is not None:
            if ptr.title == old_title:
                ptr.title = new_title
                ptr.author = new_author
                print(f"Book updated: Title {ptr.title}, Author {ptr.author}")
                return
            ptr = ptr.next
        print(f"Book with title {old_title} not found in list")

    #Save file Function 
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            current = self.start
            while current is not None:
                file.write(f"{current.title},{current.author}\n")
                current = current.next
        print(f"\033[92mBook Data saved to {filename} successfully!\033[0m")

    # Load employee data from a text file
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(',')
                    self.insert_at_end(data[0], data[1])
            print("\033[92mEmployee data loaded from", filename, "successfully!\033[0m")
        except FileNotFoundError:
            print("\033[91mFile not found. Please make sure the file name is correct.\033[0m")

my_list = LinkedList()


def intro():
    print("------------------------------------Welcome to Library Management System-------------------------------")
    print("----------------------------We Have Following Features So, Select Accordingly--------------------------")
    print(
        "--Press 1 For Add Book.------------------ " + '\n' +
        "--Press 2 For Search Book.--------------- " + '\n' +
        "--Press 3 For Delete Book.--------------- " + '\n' +
        "--Press 4 For Show All Books.------------ " + '\n' +
        "--Press 5 For Update Your Data------------" + '\n' +
        "--Press 6 For Sorting The Data------------" + '\n' +
        "--Press 7 For Filing The Data Of Library--" + '\n' +
        "--Press 8 For Read File-------------------" 
        
    )
    a = int(input())

    if a == 1:
        print("---------------------------------------------------------------------------------------------------")
        print("Add Function in here")
        print("Enter your Title.--- ")
        title = input()
        print("Enter Your Author Name.--- ")
        author = input()
        my_list.insert_at_end(title, author)

        print("-------------------------------------Book Added Successfully!--------------------------------------")
        my_list.traverse()
        print("---------------------------------------------------------------------------------------------------")
        intro()

    elif a == 2:
        print("---------------------------------------------------------------------------------------------------")
        print("Search Function in here")
        print("Press 1 for Linear Search")
        print("Press 2 for Binary Search")
        ts = int(input())
        print("Enter Title For Searching.--- ")
        title = input()
        print("----------------------------------------Here's The Result------------------------------------------")
        if ts == 1:
            my_list.linear_search(title)
        elif ts == 2:
            my_list.binary_search(title)
        print("---------------------------------------------------------------------------------------------------")
        intro()

    elif a == 3:
        print("---------------------------------------------------------------------------------------------------")
        print("Delete Function in here")
        print("If You Know the position of your Book then press a.--- ")
        print("And if you don't know the position then Press b.--- ")
        res = input()
        if res == 'a':
            print("-----------------------------------------------------------------------------------------------")
            print("Enter the position of your Book.--- ")
            pos = int(input())
            my_list.delete_from_position(pos)
            print("-------------------------------------Book Deleted Successfully!--------------------------------")
            print("-----------------------------------------------------------------------------------------------")
            intro()

        elif res == 'b':
            print("------------------------------------------------------------------------------------------------")
            print("Enter your Book Title to know the position.--- ")
            title = input()
            my_list.linear_search(title)
            print("Enter the position of your Book.--- ")
            pos = int(input())
            my_list.delete_from_position(pos)
            print("-------------------------------------Book Deleted Successfully!--------------------------------")
            print("-----------------------------------------------------------------------------------------------")
            intro()
        else:
            intro()

    elif a == 4:
        print("---------------------------------------------------------------------------------------------------")
        print("Following Are The Books That Are Enrolled In Our Library")
        my_list.traverse()
        print("---------------------------------------------------------------------------------------------------")
        intro()

    elif a == 5:
        print("---------------------------------------------------------------------------------------------------")
        print("Enter The Title Name Which You Can Update")
        Oldtit = input()
        print("Enter New Title Name")
        newTit = input()
        print("Enter New Author Name")
        newAut = input()
        my_list.update_book(Oldtit, newTit, newAut)
        print("-------------------------------------Book Updated Successfully!------------------------------------")
        intro()

    elif a == 6:
        print("---------------------------------------------------------------------------------------------------")
        print("Press 1 for Bubble Sort")
        print("Press 2 for insertion sort")
        srt = int(input())
        if srt == 1:
            my_list.bubSort()
            print('Bubble Sort in Completed')
            print("-----------------------------------------------------------------------------------------------")
            intro()
        elif srt == 2:
            my_list.sorted_book()
            print('Insertion Sort in Completed')
            print("-----------------------------------------------------------------------------------------------")
            intro()
            
    elif a == 7:
        filename = input("Enter the filename to save: ")
        my_list.save_to_file(filename)


    elif a == 8:
        print("---------------------------------------------------------------------------------------------------")
        print("Enter File Name to Load")
        a = input()
        my_list.load_from_file(a)
        print("-----------------------------------------------------------------------------------------------")
        intro()
        
        
intro()