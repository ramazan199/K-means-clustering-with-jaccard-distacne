from video_data import  *
from collections import OrderedDict 
import random



listVT = [VideosTags1, VideosTags2, VideosTags3, VideosTags4, VideosTags5, VideosTags6,
 VideosTags7, VideosTags8, VideosTags9, VideosTags10, VideosTags11, VideosTags12, VideosTags13,
 VideosTags14, VideosTags15, VideosTags16, VideosTags17, VideosTags18, VideosTags19, VideosTags20]

listVT2 = [i.lower().replace('(','').replace(")","").replace("\n"," ").split(" ") for i in listVT]
listVT3 = [set(i) for i in listVT2]

	
V_t = {'Eminem LY' : listVT3[0], 'Eminem NOt afraid': listVT3[1], 'Twenty21 on ride': listVT3[2], 'Twenty21 bla bla': listVT3[3], 
'Four black cats meow': listVT3[4],
'Mother cat meow and hisses at me' : listVT3[5], 
'6IX9INE- GOOBA (Official Music Video)': listVT3[6],
'Future - Life Is Good (Official Music Video) ft. Drake': listVT3[7],
'SNOWRUNNER Gameplay Walkthrough Part 30 - FREE DERRY LONGHORN & CHAIN TIRES': listVT3[8],
'SnowRunner Top Twitch Funny Moments Compilation | SnowRunner GAMEPLAY Trucking Simulator Games': listVT3[9],
'Coolio - Gangstas Paradise (feat. L.V.) [Official Music Video]': listVT3[10],
'Gorillaz - Clint Eastwood (Official Video)': listVT3[11],
'Gorillaz - Feel Good Inc. (Official Video)': listVT3[12],
'Gorillaz - On Melancholy Hill (Official Video)': listVT3[13],
'2pac feat Dr.Dre - California Love HD' : listVT3[14],
'2Pac - Hit Em Up (Dirty) (Official Video) HD': listVT3[15],
'a Cat - "Mooo!" ': listVT3[16],
'CS:GOs Grenade Blast Update': listVT3[17], 
'Making a Jacobs Ladder to Celebrate a Million Subs': listVT3[18],
'How NOT to Make an Electric Guitar (The Hazards of Electricity)': listVT3[19]}


k_clusters = 12
n_videos = 20
n_itter = 2

# random.seed(9000)

max_ccg_score = 0

for g in range(0, n_itter):
	
	st = []
	t = random.sample(range(1,n_videos), k_clusters)
	t.sort()

	

	for i in t:
		st.append(list(V_t.keys())[i])
	print(st)
	centroids = st
	#vidosi ontosashiesa v1 i v3
	centr_groups = {}
	for i in centroids:
		centr_groups[i] = []
	distance = 0
	max_matched_tags = -1
	# group_lst = list(range(1, k_clusters+1))
	# center_conglomerats_groups  = dict.fromkeys(group_lst , [])
	group_lst3 = [0]*k_clusters
	for j3 in range (1, k_clusters+1):
		group_lst3[j3-1] = "ct"+str(j3)
	# group_lst.reverse()
	center_conglomerats_groups  = dict.fromkeys(group_lst3 , [])
	# center_conglomerats_groups = {'ct1':[], 'ct2': [],'ct3': [],'ct4': [],'ct5': [],'ct6': [], 'ct7': [],'ct8': [], 'ct9': [],'ct10': [],'ct11': [],'ct12': []  }

	# order_of_keys = group_lst
	# list_of_tuples = [(key, center_conglomerats_groups[key]) for key in order_of_keys]
	# center_conglomerats_groups = OrderedDict(list_of_tuples)
	# if center_conglomerats_groups == center_conglomerats_groups2:
	# 	print "elaa"
		# break
	#Step 1 Groupiing by centroid video

	for i in V_t.keys():
	# for i , cct in zip(V_t.keys(), center_conglomerats_groups.keys()):
		for j in centroids:
			common_tags = V_t[i].intersection(V_t[j])
			if len(common_tags) > max_matched_tags:
				max_matched_tags = len(common_tags)
			
				video_belongs_to = j
			# print i
			# print len(common_tags)
			# print "yessssssssss"
		centr_groups[video_belongs_to].append(i)
		# center_conglomerats_groups[cct] = centr_groups[video_belongs_to]

		max_matched_tags = -1
		# ini_dict['akash'] = ini_dict.pop('akshat') 
	print(centr_groups)
	

	# print("!!!!!!!!!!!!!!!!!!!!!")


	print ("==============")
	print (center_conglomerats_groups)
	print ("==============")


	#Step 2  Building 1st tag conglamerats
	from collections import Counter


	center_conglomerats_tags =  {'ct1':[], 'ct2': [],'ct3': [],'ct4': [],'ct5': [],'ct6': [], 'ct7': [],'ct8': [], 'ct9': [],'ct10': [],'ct11': [],'ct12': []  }
	# group_lst = list(range(1, k_clusters+1))
	# center_conglomerats_tags  = dict.fromkeys(group_lst , [])
	group_lst1 = [0]*k_clusters
	for j1 in range (1, k_clusters+1):
		group_lst1[j1-1] = "ct"+str(j1)
		group_lst1.reverse()	

	# group_lst.reverse()		
	center_conglomerats_tags = dict.fromkeys(group_lst1 , [])
	print ("ssdsd", center_conglomerats_tags)
	
	center_conglomerats_tags =  {'ct1':[], 'ct2': [],'ct3': [],'ct4': [],'ct5': [],'ct6': [], 'ct7': [],'ct8': [], 'ct9': [],'ct10': [],'ct11': [],'ct12': []  }
	# if center_conglomerats_tags2 == center_conglomerats_tags:
	# 	print "ddddddd"
	# 	break

	# if center_conglomerats_tags2 == center_conglomerats_tags:
	# 	print "elaa"
		# break
	# order_of_keys = group_lst1

	# list_of_tuples = [(key, center_conglomerats_tags[key]) for key in order_of_keys]
	# center_conglomerats_tags = OrderedDict(list_of_tuples)

	def tagger(centr_groups, center_conglomerats_tags ): 

		all_tags_of_1_conglmrt = []

		for i , cct in zip(centr_groups.keys(), center_conglomerats_tags.keys()):
			for j in centr_groups[i]:
				all_tags_of_1_conglmrt.append(list(V_t[j]))

			# print all_tags_of_1_conglmrt
			# print all_tags_of_1_conglmrt
			all_tags_of_1_conglmrt = [j for sub in all_tags_of_1_conglmrt for j in sub]
			tags_with_repetition_count = dict(Counter(all_tags_of_1_conglmrt))
			center_conglomerats_tags[cct] = tags_with_repetition_count
			all_tags_of_1_conglmrt = []

	tagger(centr_groups, center_conglomerats_tags)
	# print "ZZZZZZZZZZZZZZ"
	# print center_conglomerats_groups
	# print 'ZZZZZZZZZZZZZZs'

	# print(center_conglomerats_tags)



	# Step 3 going throug congamerats

	#!!!!!!Problema : ya sam est tut, mne bali dobavlayusa a te kto prishel so stroni ne portat kartinu kak v knn euclidian

	counter = 0
	converged = 0
	center_conglomerats_groups_coppy = {}
	while converged == 0:
		if(counter == 0):
			for i, j in zip(center_conglomerats_groups.keys(), centr_groups.keys() ):
				center_conglomerats_groups_coppy[i] = centr_groups[j]
		else:
			for i, j in zip(center_conglomerats_groups.keys(), centr_groups.keys() ):
				center_conglomerats_groups_coppy[i] = center_conglomerats_groups[j]

		center_conglomerats_groups_init = center_conglomerats_groups
		center_conglomerats_group =  {'ct1':[], 'ct2': [],'ct3': [],'ct4': [],'ct5': [],'ct6': [], 'ct7': [],'ct8': [], 'ct9': [],'ct10': [],'ct11': [],'ct12': []  }
		# group_lst = list(range(1, k_clusters+1))
		
		group_lst2 = [0]*k_clusters
		for j2 in range (1, k_clusters+1):
			group_lst2[j2-1] = "ct"+str(j2)
		# group_lst.reverse()
		print (group_lst2)
		center_conglomerats_groups  = dict.fromkeys(group_lst2 , [])
		# center_conglomerats_groups =  {'ct1':[], 'ct2': [],'ct3': [],'ct4': [],'ct5': [],'ct6': [], 'ct7': [],'ct8': [], 'ct9': [],'ct10': [],'ct11': [],'ct12': []  }
		# center_conglomerats_groups =  {'ct12':[], 'ct1': [],'ct3': [],'ct4': [],'ct5': [],'ct6': [], 'ct7': [],'ct8': [], 'ct9': [],'ct10': [],'ct11': [],'ct2': []  }

		if center_conglomerats_groups == center_conglomerats_groups:
			print("qwqwqewqe")
			print(center_conglomerats_groups)
			print(center_conglomerats_groups)
			print("qwqwqewqe")
			# break


		# order_of_keys = group_lst
		# list_of_tuples = [(key, center_conglomerats_groups[key]) for key in order_of_keys]
		# center_conglomerats_groups = OrderedDict(list_of_tuples)


		print("ggggggggggggg ", center_conglomerats_groups)
		video_score = 0
		max_score = -1
		video_belongs_to_conglrmt = 10

		for i in V_t.keys():
			for j in center_conglomerats_tags.keys():
				for k in V_t[i]:
					# if k in center_conglomerats_tags[j].keys:
					# 	video_score = video_score + center_conglomerats_tags[j][k]
					# print center_conglomerats_groups[j]
					video_score = video_score + float(center_conglomerats_tags[j].get(k, 0))/float(len(center_conglomerats_groups_coppy[j]))
				# print video_score
				# print "vidddeooo"
				if video_score > max_score:
					max_score = video_score
					# print max_score
					# print "maxxxxxxxxx"
					video_belongs_to_conglrmt = j

				# print(video_score)		
				video_score = 0

			max_score = 0
			# print "ZZZZZZZZZZZZZZ"
			# print center_conglomerats_groups
			# print 'ZZZZZZZZZZZZZZs'
			# new_center_conglomerats_groups
			center_conglomerats_groups[video_belongs_to_conglrmt].append(i)

			# print("!!!!!!")

		# print("Do Taggera:")
		# print ("----------------")
		# print (center_conglomerats_tags)
		# print ("----------------")

		
		# tagger(center_conglomerats_groups, center_conglomerats_tags)
		# print("Posle Taggera:")
		# print ("+++++++++++++++++++")
		# print (center_conglomerats_tags)
		# print ("+++++++++++++++++++")

		if center_conglomerats_groups == center_conglomerats_groups_init:
			converged = 1
		print ("----------------")
		print (center_conglomerats_groups)
	print ("!!!final video scores:")

	video_score = 0
	for ccg,cct in zip(center_conglomerats_groups.keys(), center_conglomerats_tags.keys()):
		for video in center_conglomerats_groups[ccg]:
			print (video)
			# ccg.key()
			for tag in V_t[video]:

				video_score = video_score + float(center_conglomerats_tags[ccg].get(tag, 0))/float(len(center_conglomerats_groups[cct]))
			# print video_score

	print (video_score)
	print ("\n")

	if video_score > max_ccg_score:
		max_ccg_score = video_score
		center_conglomerats_groups_best = center_conglomerats_groups

	# max_ccg_score = 0

print ("!!max score:", max_ccg_score)
print ("!! best group with this score:", center_conglomerats_groups_best)
	