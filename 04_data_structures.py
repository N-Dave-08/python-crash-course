#1
movies = ["The Matrix", "The Dark Knight", "The Lord of the Rings", "The Hobbit"]
print(movies[1])

#2
birthday = {"Year": 2002, "Month": "September"}
print(birthday)

#3
colors = ["red", "blue", "green"]
colors.append("yellow")
print(colors)

#4
dictionary = {"title": "48 Laws of Power", "Author": "Robert Greene", "Year": "2006"}
print(dictionary)


#use case
sentence = "hello motherfucker goodbye goodbye"
words = sentence.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)