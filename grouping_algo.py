# from video_data import  videos_with_their_tags_dct
from data_generation import fake_data_generation
from collections import OrderedDict 
from collections import Counter
from plotting import plotting
import random

N_ITTER = 100
K_CLUSTERS = 4
N_VIDEOS = 10
MAX_N_TAGS_OF_ONE_VIDEO = 5
TOTAL_N_TAGS = 7

videos_with_their_tags_dct = fake_data_generation(N_VIDEOS,MAX_N_TAGS_OF_ONE_VIDEO, TOTAL_N_TAGS)
print("\n","videos with their tags:","\n", videos_with_their_tags_dct, "\n")

def tagger(slcted_cntr_video_dct, central_group_tags_dct ): 
		all_tags_of_one_group = []

		#[*dct] means list keys of dict
		#zdes sobiraem vse tegi iz vidosov prenadlejashey dannoy gruppe
		for i , j in zip([*slcted_cntr_video_dct], [*central_group_tags_dct]):
			for k in slcted_cntr_video_dct[i]:
				all_tags_of_one_group.append(list(videos_with_their_tags_dct[k]))

			#making 1 big lst from list of lists. i.e [[1,2],[3]]->[1,2,3]
			all_tags_of_one_group = [x for sub_lst in all_tags_of_one_group for x in sub_lst]
		
			tags_with_their_repetition_count_dct = dict(Counter(all_tags_of_one_group))
			central_group_tags_dct[j] = tags_with_their_repetition_count_dct
			all_tags_of_one_group = []
		
		return central_group_tags_dct


def main():
	max_ccg_score = 0

	for _ in range(0, N_ITTER):
		
		
		'''randomno vibiraem k clusterov. t.e eto nash initial dict, keys
		kotorogo randomno budut vibrani(v kolicestve K_CLUSTERS) 
		iz naznvaniya vidosov'''
		slcted_cntr_video_indx_lst = random.sample(range(1, N_VIDEOS), K_CLUSTERS)
		slcted_cntr_video_indx_lst.sort()
		slcted_cntr_video_lst = []
		#[*dct] means key list of dict
		video_name_lst = [*videos_with_their_tags_dct]

		for i in slcted_cntr_video_indx_lst:
			slcted_cntr_video_lst.append(video_name_lst[i])
		slcted_cntr_video_dct = {key:[] for key in slcted_cntr_video_lst}

		
		'''Step 1: Groupiing by centroid video. u mena est vibrannie vidosi, da?.
		teper ya smotru na vse vidosi, sravnivayu tegi vidosov s centralnimi 
		vidosami(skajem nazivaniyami grup), i dealyu append etot vidos(kotoriy 
		ya rassmatrivayu shas) k gruppe k kotoroy on tonostitsa'''
		max_matched_tags = -1
		for i in video_name_lst:

			for j in slcted_cntr_video_lst:
				common_tags = videos_with_their_tags_dct[i].intersection(videos_with_their_tags_dct[j])
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
		cntr_name_lst = [0]*K_CLUSTERS
		for j in range (1, K_CLUSTERS+1):
			cntr_name_lst[j-1] = "ct"+str(j)
		central_groups_dct  = {key:[] for key in cntr_name_lst}

		central_group_tags_dct = {key:[] for key in cntr_name_lst}
		central_group_tags_dct = tagger(slcted_cntr_video_dct, central_group_tags_dct)


		'''Step 3 going throug congamerats
		!!!Problema : ya sam est tut, mne bali dobavlayusa
		 a te kto prishel so stroni ne portat kartinu kak v knn euclidian'''
		converged = False
		central_groups_dct_coppy = {key:[] for key in cntr_name_lst}
		counter = 0
		central_groups_dct_init = {}
		
		while converged == False:
			central_groups_dct_2_itr_ago = central_groups_dct_init
			if counter == 0:
				for i, j in zip(list(central_groups_dct_coppy.keys()), list(slcted_cntr_video_dct.keys()) ):
					central_groups_dct_coppy[i] = slcted_cntr_video_dct[j]
			else:
				central_groups_dct_coppy = central_groups_dct
			counter = counter + 1

			central_groups_dct_init = central_groups_dct
			central_groups_dct  =  {key:[] for key in cntr_name_lst}
			
			'''proxoju cherez kajdiy vidos, smotra na ego tegi, sravnivayu ego tegi
			s tegami central_group_tags_dct. t.e s gruppoy i s ego vsego tegami.
			i.e eto s dct keys kotoreogo nazvanie gruppi(naprimer ct1) a values list
			vsex tegov kotroie otnosatsa k etoy gruppe. V kakoy gruppe etot vidos
			naberet bolshe score(koliceswtvo sovpadeniy tegov) k toy gruppe i dobavlu ego'''
			video_score = 0
			max_score = -1
			for i in video_name_lst:
				for j in [*central_group_tags_dct]:
					for k in videos_with_their_tags_dct[i]:

						N_VIDEOS_in_group = len(central_groups_dct_coppy[j])\
							if len(central_groups_dct_coppy[j]) > 0 else 1
						video_score = video_score + float(central_group_tags_dct[j].get(k,0))\
							/float(N_VIDEOS_in_group)
					
					if video_score > max_score:
						max_score = video_score
						video_belongs_to_conglrmt = j
				
					# nujno obnulit video_score i max_score dla sledushey 
					# itteracii(t.e sled vidosa)
					video_score = 0
				max_score = 0
				central_groups_dct[video_belongs_to_conglrmt].append(i)

			# esli posle etogo processsa central_groups_dct ne pomenalsa. 
			# znacit process nado ostanovit tak bolshe progrssa ne budet 
			if central_groups_dct == central_groups_dct_init or\
				central_groups_dct == central_groups_dct_2_itr_ago:
				converged = True
		

		'''now we need to choose best results from n itrerations'''
		video_score = 0
		for group_name in [*central_groups_dct]:
			for video in central_groups_dct[group_name]:
				for tag in videos_with_their_tags_dct[video]:

					video_score = video_score + \
						float(central_group_tags_dct[group_name].get(tag, 0))/ \
						float(len(central_groups_dct[group_name]))
					
		if video_score > max_ccg_score:
			max_ccg_score = video_score
			central_groups_dct_best = central_groups_dct

		# max_ccg_score = 0

	print ("max score:", max_ccg_score, "\n")
	print ("best group with this score:", "\n", central_groups_dct_best, "\n")

	plotting(central_groups_dct_best, videos_with_their_tags_dct)
	
	
		
main()