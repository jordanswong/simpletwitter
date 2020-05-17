#Assignment 6 Report

Name: Jordan Wong, PennKey: jswong, No Partner

##Routes
- '/' = Splash page of website

- 'login/' = Login page of website
- 'signup/' = Signup page of website
- 'logout/' = Logout path of website, no associated page
- 'myprofile/' = User profile page of website, shows users own tweets and allows for the creation and deletion of said tweets
- 'myprofile/tweet' = Tweet creation path from myprofile page
- 'myprofile/delete' = Tweet deletion path from myprofile page
- 'home/' = Page that shows all tweets from all users
- 'hashtags/' = Page that shows all tweets but with hashtag filters on the right hand side of the page that can filter by hashtags
- 'hashtags/<<str:t_name>>/' = Page that user gets to after clicking one of the hashtag filters on the hashtag page - shows only tweets that contain hashtag in URL

##Design Considerations

The biggest factor going into the design of the website was simplicity - I just tried to make everything look as clean and 
simple as possible (hence the website title of "simple twitter"). To do this, I tried to make the UX as simple as possible to
prevent screen clutter as well as make everything as nice to the eye as possible (e.g. dark mode). In the end, instead of viewing the low funtionality
of the app as a hinderance I tried to make it a feature by having the website match its featureset.

The tweets actually structure I tried to keep as close as possible to actual twitter, providing the username of the person who sent out the tweet,
the date and time, and the body right underneath - I could have made this closer to an actual tweet by adding account functionality for nicknames/ account headers, but
I didn't have the time to implement

Something that I could have done better was using djangos template inheritance, which I found out about when I was already done with the bulk of my
project. Many of the pages have a lot of the same boilerplate html code, so getting rid of a lot of that would have probably been good to keep
the frontend html looking a bit neater.

##How to start the server

1. Use cmd to cd into the root directory of the project, twitter_clone
2. run python manage.py runserver to get onto the server
3. Use admin account to see backend by either:
    - creating a superuser with python manage.py createsupepruser
    - using the admin account I have put in - user: admin, password: 123123 (I'm not sure if this option works)

With this you should be able to do whatever you want to see the server's frontend or backend

##Extra Credit

Didn't implement anything that was specifically listed as extra credit on the CIS 192 page, but hopefully you guys can give me some brownie points for putting this together
on my own ;) - haha jk... unless?
