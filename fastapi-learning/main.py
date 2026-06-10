from fastapi import FastAPI

#Create FastAPI object
app = FastAPI() #Creates web application


#Route Decorator
@app.get("/") #When a GET request is sent to "/", the below home() func is run

#Return Dictionary 
def home():
    return {"message": "Home Page"} #FastAPI automatically converts Python dicts into JSON.

@app.get("/about")
def about():
    return {"message" : "About Page"}

@app.get("/profile")
def profile():
    return {"Name" : "Vishal",
            "learning" : "FastAPI"}

#Path Parameter
@app.get("/users/{user_id}/posts/{post_id}") #using a placeholder {}
def get_user(user_id: int, post_id: int): #FastAPI extracts the value from the URL.
    return {
        "user_id" : user_id,
        "post_id" : post_id
    }

@app.get("/users/me")
def get_me():
    return {"user" : "current user"}

@app.get("/products/{product_id}/reviews/{review_id}")
def products(product_id: int, review_id: int):
    return {"product_id" : product_id,
            "review_id" : review_id }

'''Path Parameters identify a resource
    Query Parameters filter or modify the result
    
    Example: Think of a URL''' 

# def get_posts(limit: int = 10,published : bool = True):
#     return {"limit" : limit,
#             "published" : published}

# @app.get("/posts") #Query Parameter - using "limit"
#Simulating a Database - Fake data
posts = [
    {"id" : 1, "title" : "FastAPI"},
    {"id" : 2, "title" : "Python"},
    {"id" : 3, "title" : "Docker"},
    {"id" : 4, "title" : "Linux"}
]
# @app.get("/posts") #Query Parameter - using "limit"
# def get_posts(limit: int = 10):
#     return posts[:limit]

#Searching
@app.get("/posts") #Query Parameter - using "limit"
def get_posts(limit: int = 10, search: str = ""):
    filtered_posts = []

    for post in posts: #here 'posts' refers to the above created list
        if search.lower() in post["title"].lower():
            filtered_posts.append(post)
    return filtered_posts[:limit]

