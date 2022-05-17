# Problem: create a dictionary associating
# search  functionality to take an author name

books = {
    "":[""],
    "":[""],
    "":[""],
};

author_name = input("Enter author to search");
book_results = books.get(author_name, ["None"]);
print(f"Books by {author_name}: ", ', '.join(sorted(book_results)));
