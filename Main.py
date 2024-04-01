import praw

def is_toxic_comment(comment, toxic_words):
    for word in toxic_words:
        if word.lower() in comment.lower():
            return True
    return False


def scrape_and_identify_toxic_comments(url, reddit_client_id, reddit_client_secret, reddit_user_agent, toxic_words):

    reddit = praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent=reddit_user_agent)

    # Extract submission ID from the URL
    submission_id = url.split('/')[-3]

    # Fetch the submission (post) from Reddit
    submission = reddit.submission(id=submission_id)


    print("Title:", submission.title)

    print("\nComments:")
    # Iterate through top-level comments
    for comment in submission.comments:
        if isinstance(comment, praw.models.Comment):
            # Check if the comment is toxic
            if is_toxic_comment(comment.body, toxic_words):
                # Print the comment
                print("Comment:", comment.body)
                print("[TOXIC COMMENT]")


# id og secreet til din script app
reddit_client_id = 'r7-XJUTM28cDAGk6f53mBg'
reddit_client_secret = 'eWIpMS_s61XtDqfu9TPeVPzpxvpbGw'
reddit_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20200101 Firefox/100.0'

reddit_post_url = 'https://www.reddit.com/r/Brawlhalla/comments/1bqwvlb/why_do_noobs_think_they_are_good_when_they_use/'

toxic_words = ['noob', 'tilføj andre toxic ord her']

scrape_and_identify_toxic_comments(reddit_post_url, reddit_client_id, reddit_client_secret, reddit_user_agent, toxic_words)




