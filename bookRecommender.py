import requests
import random

API_KEY = "BcQIu47MTGC00fKzEbR5FFxBvZzymHBt"

list_name = []

# generating random number between 0 and 4 so as to get a random book name
random_book_pos = random.randint(0, 4)

# getting names from the overview api of NYT


def get_Name():
    requestUrl = "https://api.nytimes.com/svc/books/v3/lists/overview.json?api-key=" + API_KEY
    requestHeaders = {
        "Accept": "application/json"
    }

    request = requests.get(requestUrl, headers=requestHeaders)
    response_overView = request.json()

    # getting the size of lists json object so as to generate a random number between 0 n len-1
    looper_lists = len(response_overView["results"]["lists"])
    list_match = random.randint(0, looper_lists-1)

    # taking the random generated number for book data
    book_pos = random_book_pos

    # result array for storing all the variables that are to be returned for sending text message
    result = []

    book_title = response_overView["results"]["lists"][list_match]["books"][book_pos]["title"]
    book_author = response_overView["results"]["lists"][list_match]["books"][book_pos]["author"]
    book_image = response_overView["results"]["lists"][list_match]["books"][book_pos]["book_image"]
    book_desc = response_overView["results"]["lists"][list_match]["books"][book_pos]["description"]
    book_url = response_overView["results"]["lists"][list_match]["books"][book_pos]["amazon_product_url"]

    result.append(book_image)
    result.append(book_title)
    result.append(book_author)
    result.append(book_desc)
    result.append(book_url)
    # return {"book_title": book_title, "book_author": book_author, "book_image": book_image, "book_desc": book_desc, "book_url": book_url}
    # return book_title, book_author, book_image, book_desc, book_url
    return result

# for testing purposes
# if __name__ == "__main__":
#     results = get_Name()
#     print(results[0])
#     print(results[1])
#     print(results[2])
#     print(results[3])
#     print(results[4])
