import os 
import cv2
 
videos_src_path = '/Users/Samuel/Documents/iCloud/Desktop/ArtificialIntelligence/AICase/videos/video'
videos_save_path = '/Users/Samuel/Documents/iCloud/Desktop/ArtificialIntelligence/AICase/videos/images'
 
videos = os.listdir(videos_src_path)

 
i = 1
 
for each_video in videos:
	if not os.path.exists(videos_save_path + '/' + str(i)):
		os.mkdir(videos_save_path + '/' + str(i))
	each_video_save_full_path = os.path.join(videos_save_path,str(i))+'/'
	each_video_full_path = os.path.join(videos_src_path,each_video)
	cap = cv2.VideoCapture(each_video_full_path)
	frame_count = 1
	success = True
	
	while(success):
		success,frame = cap.read()
		if success==True:
			cv2.imwrite(each_video_save_full_path + "%d.jpg" % frame_count,
		frame)
		frame_count = frame_count + 1
	i = i + 1
	
	cap.release()