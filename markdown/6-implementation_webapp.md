Cyber Matters

## 6. Building a web application

#### Disclaimer:

This post will get into the guts of how I've built a prototype of the application I've been talking about for the last several posts. If you're not interested in hearing about how Python, Flask, and Vue.js work, it might be best to skim this and move on to the next post as quickly as possible.

#### The Guts:

I mentioned earlier that this application was going to be a client-server app. What does that look like in practice? Well, it starts about as simply as possible, with two folders named `client` and `server` (and one more called `venv` which I encourage you to read about [here](https://docs.python.org/3/library/venv.html)).

![](C:\Users\lwpul\Projects\cyber_capstone\markdown\photos\client-server-structure.png)

What does this really mean, though? Under the hood, the client and the server are just processes running on some computer (ideally on separate computers, but since I only have one, I'll be running them both on my machine). So really, the client and server folders just contain code to run two processes which interact with each other. 

##### Server File Structure

![](C:\Users\lwpul\Projects\cyber_capstone\markdown\photos\server.png)

As you can see, this is really a pretty simple architecture. There are some [Python](https://www.python.org/) files (with suffix .py) which process voter data from the `data/` folder and some others which interact with the Twitter API. The crux of it all is the `app.py` file, a snippet of which I've included below. That file defines the *routes* of the server. That is, if the server can be found at `https://server.com`, the app.py file determines what happens when you navigate to `https://server.com/example_route`. 

```python
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# ... Obviously there's more to this than what I've included here

if __name__ == '__main__':
    app.run()
```

Of course, this isn't the full file and there's a lot more logic to it, but if you look at the section labeled "`ping_pong`," you'll see an example of the general structure of this server. When the user navigates to a certain route (like `server/ping`), the server displays some data (in this case, just the word "pong!"). The data is returned in JSON format, which is just a simple and easy-to-parse format which you can read about [here](https://www.json.org/json-en.html). 

![Pong](C:\Users\lwpul\Projects\cyber_capstone\markdown\photos\pong.png)

Like so!

##### Client File Structure

![image-20191213111156307](C:\Users\lwpul\Projects\cyber_capstone\markdown\photos\client.png)

This is a little bit harder to understand than the Python, but it's the same general idea. The `main.js` file creates the `App.vue`, which is the main visual piece of the client application, as well as the `router.js`, which fulfills the same route-creation function I described above. The `components` and `views` pieces define the smaller sections of the complete application (like menus, toolbars, and layout files), while the `assets` folder contains necessary data for the application (like sound files or images). The client then simply makes requests to the server for the data it needs to display. I am indebted to [this tutorial](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/) by [Michael Herman](https://testdriven.io/authors/herman/) for helping me understand the Vue side of this, and I recommend it to anyone looking to understand this more fully. 

##### Why Both?

It may seem like overkill to run two applications with very similar structures, but as I mentioned earlier, there are compelling security and engineering reasons to use this kind of paradigm. The most powerful reason, though, is simply that different programming languages and frameworks have different strengths. Vue.js is a fantastic framework for visual displays in the browser, while Python is far more versatile for querying APIs and processing data. Using both allows each to focus on what it excels at. Enough of this, though – let's see it in action! 

#### App Demo

https://youtu.be/2LfmW7Y2L_I