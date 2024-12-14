import praw
from datetime import datetime, timedelta, timezone
from collections import defaultdict

# Reddit API credentials
CLIENT_ID = 'Q47PMKXvw9mekQ32LshqtA'
CLIENT_SECRET = 'Y4sJhBDA9eYEHF3GGD_PcIl2G4VUAg'
USER_AGENT = 'SRho100 by u/SRho100'
USERNAME = 'SRho100'
PASSWORD = 'Richardho787'


# Initialize Reddit API
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT, 
                     username = USERNAME, 
                     password = PASSWORD)

def fetch_user_activity(username):
    """Fetch the activity (posts and comments) of a specific user."""
    try:
        user = reddit.redditor(username)
        posts = list(user.submissions.new(limit=50))
        comments = list(user.comments.new(limit=50))
        return posts, comments
    except Exception as e:
        print(f"Error fetching user activity: {e}")
        return None, None

def analyze_activity(posts, comments):
    """Analyze a user's activity for bot-like patterns."""
    now = datetime.now(timezone.utc)
    suspicious = False
    
    # Check number of posts and comments in a short timeframe
    post_times = [datetime.fromtimestamp(post.created_utc, tz=timezone.utc) for post in posts]
    comment_times = [datetime.fromtimestamp(comment.created_utc, tz=timezone.utc) for comment in comments]
    all_times = post_times + comment_times

    # Activity in the last 24 hours
    recent_activity = [time for time in all_times if (now - time) < timedelta(days=1)]
    if len(recent_activity) > 50:  # Adjust threshold based on analysis
        suspicious = True
        print(f"High activity detected: {len(recent_activity)} items in the last 24 hours.")
    
    # Check subreddit diversity
    subreddits = [post.subreddit.display_name for post in posts] + \
                 [comment.subreddit.display_name for comment in comments]
    unique_subreddits = set(subreddits)
    if len(unique_subreddits) > 10:  # Adjust threshold
        suspicious = True
        print(f"Unusual subreddit diversity: {len(unique_subreddits)} unique subreddits.")
    
    # Analyze karma
    post_karma = sum(post.score for post in posts)
    comment_karma = sum(comment.score for comment in comments)
    if post_karma < 0 or comment_karma < 0:
        suspicious = True
        print("Negative karma detected.")
    
    # Check repetitive content
    post_titles = [post.title for post in posts]
    if len(set(post_titles)) < len(post_titles) * 0.5:  # At least 50% are unique
        suspicious = True
        print("Repetitive content detected.")

    return suspicious

def detect_bot(username):
    """Detect if a user exhibits bot-like behavior."""
    try:
        posts, comments = fetch_user_activity(username)
        if not posts and not comments:
            print(f"No activity found for user '{username}'.")
            return False
        is_bot = analyze_activity(posts, comments)
        if is_bot:
            print(f"User '{username}' exhibits bot-like behavior.")
            return True
        else:
            print(f"User '{username}' seems like a human.")
            return False
    except Exception as e:
        print(f"Error analyzing user '{username}': {e}")
        return None

def crawl_subreddit(subreddit_name, limit=50):
    """Crawl a subreddit for active users and analyze their behavior."""
    print(f"Crawling subreddit: {subreddit_name}...")
    bots = []
    humans = []
    try:
        subreddit = reddit.subreddit(subreddit_name)
        user_activity = defaultdict(int)
        
        # Fetch posts
        for submission in subreddit.new(limit=limit):
            if submission.author:  # Check if the author is not deleted
                user_activity[submission.author.name] += 1
        
        # Fetch comments
        for comment in subreddit.comments(limit=limit):
            if comment.author:  # Check if the author is not deleted
                user_activity[comment.author.name] += 1

        print(f"Analyzing users in subreddit '{subreddit_name}'...")
        for user, activity_count in user_activity.items():
            print(f"Analyzing user: {user} (Activity count: {activity_count})")
            is_bot = detect_bot(user)
            if is_bot is True:
                bots.append(user)
            elif is_bot is False:
                humans.append(user)
        
        # Output results
        print(f"\nDetected {len(bots)} bots and {len(humans)} humans in subreddit '{subreddit_name}'.")
        print("\nBots Detected:")
        for bot in bots:
            print(f"  - {bot}")
        print("\nHumans Detected:")
        for human in humans:
            print(f"  - {human}")
    except Exception as e:
        print(f"Error while crawling subreddit: {e}")

    return bots, humans

# Example usage
subreddit_to_crawl = input("Enter the subreddit to crawl (e.g., politics): ").strip()
limit = int(input("Enter the number of posts/comments to fetch (e.g., 100): ").strip())
bots, humans = crawl_subreddit(subreddit_to_crawl, limit)
