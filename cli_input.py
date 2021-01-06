def get_video_url():
    user_input = input("Input YouTube link: ")
    
    if check_if_youtube_link(user_input):
        print("YouTube link was accepted")
        return user_input
    else:
        print("Not recognized as a YouTube link, please try again.")
        get_link()
        return

def check_if_youtube_link(user_input):
    # add: check if this is a working link with youtube
    # add: check if video is age restricted
    start = user_input.find("https://www.youtube.com/watch?v=")
    if start == 0:
        return True
    else:
        return False

get_video_url()