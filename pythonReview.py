def create_youtube_video(title,description):
	youtube_video = {"Title": title,"description": description, "likes" : 0 , "dislike" : 0 ,"comments" : {}}
	return youtube_video 
def like(youtube_video):
	if "likes" in youtube_video :
		youtube_video["likes"] += 1
	return youtube_video
def dislike(youtube_video):
	if "deslike" in youtube_video :
		youtube_video["deslike"] += 1
	return youtube_video
def comments(youtube_video,username,comment_text):
	youtube_video["comments"[username]] =  comment_text
	return youtube_video

video= create_youtube_video("lego","how to play lego")
print(video)



