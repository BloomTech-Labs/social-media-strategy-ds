# So-Me

You can find the project at [https://www.so-me.net/](https://www.so-me.net/login).

## Contributors
|                                       [Andrew Lowe](https://github.com/AndrewSLowe)                                        |                                       [Sarah Xu](https://github.com/sarahxu087)                                        |                                       [Jud Taylor](https://github.com/gptix)                                        |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
|                      [<img src="https://avatars2.githubusercontent.com/u/54857972?s=460&u=521c79c3b34a1742ca8c1e6d97f530622f5c24cd&v=4" width = "200" />](https://github.com/)                       |                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-UNTKB89HQ-5ce141a9cadf-512" width = "200" />](https://github.com/)                       |                      [<img src="https://avatars3.githubusercontent.com/u/21339224?s=400&v=4" width = "200" />](https://github.com/)                       |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-female.png" width = "200" />](https://github.com/)                       |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/AndrewSLowe)                       |
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/AndrewSLowe)                 |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/sarahxu087)             |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/gptix)            |          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/NandoTheessen)           |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/wvandolah)             |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/andrew-lowe-5b581714a/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/sarahx/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) |



🚫 5️⃣ Optional examples of using images with links for your tech stack, make sure to change these to fit your project

![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Typescript](https://img.shields.io/npm/types/typescript.svg?style=flat)
[![Netlify Status](https://api.netlify.com/api/v1/badges/b5c4db1c-b10d-42c3-b157-3746edd9e81d/deploy-status)](netlify link goes in these parenthesis)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

🚫 more info on using badges [here](https://github.com/badges/shields)

## Project Overview

[Trello Board](https://trello.com/b/tn4nvK97/labs-22-social-media-strategy)

[Product Canvas](https://www.notion.so/Social-Media-Strategy-9d1840703db34c5cb44d0f4a0cc45543)

So-Me is a social media management tool for small businesses. Users of So-Me will be able to post to any of their company's major social media platforms (LinkedIn, Instagram, Facebook, Twitter) from the app, supported by a simple to use drag and drop design. Our app will give user's time recommendation's for posting and feedback on their proposed post using their follower's engagement data.

In it's current state, the app only supports Twitter. However, the user still gets benefit from using our app rather than posting directly on Twitter. We give the user a personalized time recommendation based on their follower's engagement data, and will soon give feedback on their text with their follower's data as well.  

[Deployed Front End](https://www.so-me.net/)

### Tech Stack

🚫 List all of the languages, frameworks, services, etc used here.

### Predictions

We have workshopped several models that will give our user's feedback. Utilizing a predictive model, we can predict the number of retweets, likes and comments a post will get; using topic modeling, we can see groupings of terms their followers typically engage with; and using sentiment analysis, we can predict the attitudes of texts their followers engage with.

### 2️⃣ Explanatory Variables

-   Explanatory Variable 1
-   Explanatory Variable 2
-   Explanatory Variable 3
-   Explanatory Variable 4
-   Explanatory Variable 5

### Data Sources
🚫  Add to or delete souce links as needed for your project


-   [Source 1] (🚫add link to python notebook here)
-   [Source 2] (🚫add link to python notebook here)
-   [Source 3] (🚫add link to python notebook here)
-   [Source 4] (🚫add link to python notebook here)
-   [Source 5] (🚫add link to python notebook here)

### Python Notebooks

🚫  Add to or delete python notebook links as needed for your project

[Python Notebook 1](🚫add link to python notebook here)

[Python Notebook 2](🚫add link to python notebook here)

[Python Notebook 3](🚫add link to python notebook here)

### How to connect to the web API

Connection to the web API is built into the flask_app/routes.py file. The backend makes a POST request to our flask app with the user's twitter handle and we return a PUT request with the optimal time for posting. The connection is possible with the backend token (stored in a hidden file) that can be received by sending a specific password and username to the backend URL with a GET request.

### How to connect to the data API

The only data API we have built into the app at this point is the Twitter Developer API. We accessed this with http requests, using our unique tokens for authentification.

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](_link to your backend readme here_) for details on the backend of our project.

See [Front End Documentation](_link to your front end readme here_) for details on the front end of our project.

