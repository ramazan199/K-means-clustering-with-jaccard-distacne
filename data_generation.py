import random

def fake_data_generation(n_videos, max_n_tags_of_one_video, total_n_tags):
	N_VIDEOS = n_videos
	MAX_N_TAGS_OF_ONE_VIDEO = max_n_tags_of_one_video
	TOTAL_N_TAGS = total_n_tags

	video_lst = list(range(1, N_VIDEOS+1))
	tag_number_lst = [random.randint(1, MAX_N_TAGS_OF_ONE_VIDEO) for x in range(1, N_VIDEOS+1)]
	# print ("number of tags for each video:", "\n", tag_number_lst, "\n")

	# Create a zip object from two lists
	zipbObj = zip(video_lst, tag_number_lst)
	# Create a dictionary from zip object
	vid_and_tag_number_dct = dict(zipbObj)
	# print ("dictionary of videos with their tag number:", "\n",vid_and_tag_number_dct, "\n")

	for i in vid_and_tag_number_dct.keys():
		vid_and_tag_number_dct[i] = set(random.sample(range(1,TOTAL_N_TAGS), vid_and_tag_number_dct[i]))
	videos_with_their_tags_dct = vid_and_tag_number_dct
	
	for i in [*videos_with_their_tags_dct]:
		videos_with_their_tags_dct["video_n_"+str(i)] = videos_with_their_tags_dct.pop(i)
	# print ("dictornary of videos with their tags:", "\n", videos_with_their_tags_dct,"\n""\n")

	return videos_with_their_tags_dct


