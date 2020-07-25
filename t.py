from video_data import  videos_with_their_tag_lst
from collections import OrderedDict 
from collections import Counter
import random


def tagger(slcted_cntr_video_dct, central_group_tags_dct ): 
		all_tags_of_one_group = []

		#[*dct] = key list of dict
		#zdes sobiraem vse tegi iz vidosov prenadlejashey dannoy gruppe
		for i , j in zip([*slcted_cntr_video_dct], [*central_group_tags_dct]):
			for k in slcted_cntr_video_dct[i]:
				all_tags_of_one_group.append(list(videos_with_their_tag_lst[k]))

			#making 1 big lst from list of lists. i.e [[1,2],[3]]->[1,2,3]
			all_tags_of_one_group = [x for sub_lst in all_tags_of_one_group for x in sub_lst]
		
			tags_with_their_repetition_count_dct = dict(Counter(all_tags_of_one_group))
			central_group_tags_dct[j] = tags_with_their_repetition_count_dct
			all_tags_of_one_group = []
		
		return central_group_tags_dct


def main():
	k_clusters = 12
	n_videos = 20
	n_itter = 2
	max_ccg_score = 0

	for y in range(0, n_itter):
		
		slcted_cntr_video_indx_lst = random.sample(range(1, n_videos), k_clusters)
		slcted_cntr_video_indx_lst.sort()

		slcted_cntr_video_lst = []
		#[*dct] = key list of dict
		video_name_lst = [*videos_with_their_tag_lst]

		for i in slcted_cntr_video_indx_lst:
			slcted_cntr_video_lst.append(video_name_lst[i])

		slcted_cntr_video_dct = {}
		for i in slcted_cntr_video_lst:
			slcted_cntr_video_dct[i] = []

		
		'''Step 1: Groupiing by centroid video. u mena est vibrannie vidosi, da?.
		teper ya smotru na vse vidosi, sravnivayu tegi vidosov s centralnimi 
		vidosami(skajem nazivaniyami grup), i dealyu append etot vidos(kotoriy 
		ya rassmatrivayu shas) k gruppe k kotoroy on tonostitsa'''
		max_matched_tags = -1
		for i in video_name_lst:

			for j in slcted_cntr_video_lst:
				common_tags = videos_with_their_tag_lst[i].intersection(videos_with_their_tag_lst[j])
				if len(common_tags) > max_matched_tags:
					max_matched_tags = len(common_tags)
					video_belongs_to = j
			
			slcted_cntr_video_dct[video_belongs_to].append(i)
			# dla sledushey itteracii nado obnulit max_matched_tags
			max_matched_tags = -1
		

		


		''' Step 2  Building 1st tag conglamerats: teper kogda u mena est 
		opredelnnie gruppi, ya teper poluchu tegi etix vsex grupp.
		T.e ya xochu poluchit dictinoray keys kotorogo budut nazvaniya
		vidosov(skajem nazvaniya grup), a values budut listi tegov ot vidosov
		kororie v svoyu oceredotnosatsa k etoy je gruppe'''
		# central_group_tags_dct = {'ct1':[], 'ct2': [],'ct3': [],'ct4': [],'ct5': [],'ct6': [], 'ct7': [],'ct8': [], 'ct9': [],'ct10': [],'ct11': [],'ct12': []}
		cntr_name_lst = [0]*k_clusters
		for j in range (1, k_clusters+1):
			cntr_name_lst[j-1] = "ct"+str(j)
		# central_groups_dct = {'ct1':[], 'ct2': [],'ct3': [],'ct4': [],'ct5': [],'ct6': [], 'ct7': [],'ct8': [], 'ct9': [],'ct10': [],'ct11': [],'ct12': []}
		central_groups_dct  = dict.fromkeys(cntr_name_lst , [])

		central_group_tags_dct = dict.fromkeys(cntr_name_lst , [])
		central_group_tags_dct = tagger(slcted_cntr_video_dct, central_group_tags_dct)


		# Step 3 going throug congamerats
		#!!!Problema : ya sam est tut, mne bali dobavlayusa a te kto prishel so stroni ne portat kartinu kak v knn euclidian

		counter = 0
		converged = 0
		central_groups_dct_coppy = {}
		
		while converged == 0:
			if(counter == 0):
				for i, j in zip(list(central_groups_dct.keys()), list(slcted_cntr_video_dct.keys()) ):
					central_groups_dct_coppy[i] = slcted_cntr_video_dct[j]
			else:
				for i, j in zip(list(central_groups_dct.keys()), list(slcted_cntr_video_dct.keys()) ):
					central_groups_dct_coppy[i] = central_groups_dct[j]

			central_groups_dct_init = central_groups_dct
		
			for j in range (1, k_clusters+1):
				cntr_name_lst[j-1] = "ct"+str(j)
			central_groups_dct  = dict.fromkeys(cntr_name_lst , [])

			central_groups_dct =  {'ct1':[], 'ct2': [],'ct3': [],'ct4': [],'ct5': [],'ct6': [], 'ct7': [],'ct8': [], 'ct9': [],'ct10': [],'ct11': [],'ct12': []  }

			video_score = 0
			max_score = -1
			video_belongs_to_conglrmt = 10

			for i in video_name_lst:
				for j in [*central_group_tags_dct]:
					for k in videos_with_their_tag_lst[i]:
						video_score = video_score + float(central_group_tags_dct[j].get(k,0))/float(len(central_groups_dct_coppy[j]))

					if video_score > max_score:
						max_score = video_score
						video_belongs_to_conglrmt = j
		
					video_score = 0

				max_score = 0
			
				central_groups_dct[video_belongs_to_conglrmt].append(i)


			if central_groups_dct == central_groups_dct_init:
				converged = 1

		video_score = 0
		for ccg,cct in zip(central_groups_dct.keys(), central_group_tags_dct.keys()):
			for video in central_groups_dct[ccg]:
				for tag in videos_with_their_tag_lst[video]:	
					video_score = video_score + float(central_group_tags_dct[ccg].get(tag, 0))/float(len(central_groups_dct[cct]))
					
		if video_score > max_ccg_score:
			max_ccg_score = video_score
			central_groups_dct_best = central_groups_dct

		# max_ccg_score = 0

	print ("!!max score:", max_ccg_score,"\n")
	# print ("!! best group with this score:", central_groups_dct_best)
		
main()