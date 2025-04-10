import string
import sys
#from students_code import words_in, lookup_word_count

#My code
class node:
    def __init__(self, word):
        self.data = word
        self.count = 1
class Hash:
    def __init__(self, size):
        self.lis = []*size
        self.size = size
        self.col = 0
        self.buc = size
        
    def lookup_word_count(self, word):
        y = 0
        lu = 0
        c = 0
        for char in word:
            if (65<= ord(char) <=90):
                char = chr(ord(char)+32)
            y = y + ord(char)
        y = y%self.size
        if (word == self.lis[y[0]]):
            lu = lu +1
            return (self.lis[y[0]].count, lu)
        else:
            x = 1
            find = False
            while (x < len(self.lis[y])):
                if (self.lis[y[x]] == word):
                    return (self.lis[y[0]].count, lu)
                x = x+1
                    
                
            
    def add(self, word):
        x=0
        y =0
        col = 0
        for char in word:
            if (65<= ord(char) <=90):
                char = chr(ord(char)+32)
            y = y + ord(char)
        y = y%self.size
        if (self.lis[y] == None):
            self.lis[y] = [word]
        elif (len(self.lis[y]) > 1):
            x =0
            while(x < len(self.lis[y])):
                if (self.lis[y[x]] == word):
                    x = x+1
                    self.lis[y].count = self.lis[y].count+1
        else: #thing there is diffrent
            new = node(word)
            z = self.lis[y] + [new]
            self.lis[y] = z
            self.buc = self.buc +1
            col = col +1
            
    def words_in(self, word_list):
        for item in word_list:
            add(word)
        return(self.buc, col)
            


# Read and process text file
def process_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Convert to lowercase and remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    
    return words

# Main function to run the simulation
def main():
    # Read and process the input file
    
    filename = input(Alice.txt)  # Change this to your text file name
    words_list = process_text_file(filename)
    x = len(words_list)
    if (x < 7000):
        new = Hash(x/3*2.8)
    else:
         new = Hash(7000)
    # Run students' words_in function
    # num_buckets, collisions = 
    new.words_in(words_list)
    num_buckets = new.buc
    collisions = new.col
    print(f"Number of Buckets Used: {num_buckets}")
    print(f"Collisions: {collisions}")

    # Convert list to a set for unique word lookups
    unique_words = set(words_list)

    # Run students' lookup_word_count function and track lookup score
    total_lookups = 0
    for word in unique_words:
        _, lookups = new.lookup_word_count(word)
        total_lookups += lookups

    # Calculate final score
    total_score = num_buckets + collisions + total_lookups

    # Print results
    print("\n--- Student's Hash Table Score ---")
    print(f"Buckets Used: {num_buckets}")
    print(f"Collisions: {collisions}")
    print(f"Total Lookups: {total_lookups}")
    print(f"Final Score: {total_score}")

if __name__ == "__main__":
    main()

