from django.shortcuts import render, redirect
from messaging.models import Tweet, Hashtag
# Create your views here.


def home_view(request):

    tweets = Tweet.objects.order_by('-created_at')
    return render(request, "home.html", {"tweets": tweets})


def hashtags_view(request):
    tweets = Tweet.objects.order_by('-created_at')
    hashtags = Hashtag.objects.exclude(tagged_tweets=None)

    return render(request, "hashtags.html", {"tweets": tweets, "hashtags": hashtags})

def hashtags_filter(request, t_name):

    tweets = Tweet.objects.filter(tags=Hashtag.objects.get(name=t_name))
    hashtags = Hashtag.objects.exclude(tagged_tweets=None)

    return render(request, "filtered_hashtags.html", {"tweets": tweets, "hashtags": hashtags, "t_name": t_name})

def create_tweet(request):

    #parse hashtags here
    if request.method == "POST":
        newbody = request.POST["tweetBody"]
        auth = request.user
        n_tweet = Tweet.objects.create(body=newbody, author=auth)

        bodyText = str(newbody)
        indxs = [i for i, a in enumerate(bodyText) if (a == '#' or a == ' ')]
        numTags = bodyText.count('#')

        for i in range(len(indxs)):
            curr_idx = indxs[i]
            if bodyText[curr_idx] == '#':
                if i != len(indxs) - 1:
                    tag_name = bodyText[curr_idx: indxs[i+1]]
                else:
                    tag_name = bodyText[curr_idx:]
                tag_name = tag_name.replace('#', '')
                if Hashtag.objects.filter(name=tag_name).count() == 0:
                    n_hash = Hashtag(name=tag_name)
                    n_hash.save()
                    n_hash.tagged_tweets.add(n_tweet)
                else:
                    existing_hash = Hashtag.objects.get(name=tag_name)
                    existing_hash.tagged_tweets.add(n_tweet)

        return redirect("/myprofile")

    return render(request, "myprofile.html", {})


def delete_tweet(request):

    d_tweet = Tweet.objects.filter(id=request.GET.get('del_butt'))
    d_tweet.delete()
    return redirect("/myprofile")