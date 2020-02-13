from text_cleaning import as_list_soup
from file_of_functions import counter_cosine_similarity
from gensim.test.utils import datapath
from gensim.models import KeyedVectors
import os.path
import csv
import time
from datetime import datetime 
import configparse

start_time = time.clock()
timestamp = datetime.now().strftime("%Y_%m_%d=%H:%M:%S")

w2v_model_300= KeyedVectors.load_word2vec_format("model300.bin", binary=True)
print("Model 300 loaded")

save_not_crawled = "path_to_save_not_crawled_urls"
csv_filename = "sample_file.csv"
counter = 0
with open("path_of_the_textfile_in_which-urls_were_saved", "r") as f:
            # spliting the urls from txt file line by line  and save to a variable
        temp_urls = (url.split() for url in f.readlines())
        for extract_list in temp_urls:
    # reading all the urls as  list from text file and extracting one by one in loop
            for each_url  in  extract_list:
                print(each_url)
                try:
                    corpus = as_list_soup(each_url)
                    #print(corpus)
                    if (len(corpus)<100) or ("This site can’t be reached" in corpus) or ("document not found" in corpus) or ("No document" in corpus) or ("page not found" in corpus) or ("under construction" in corpus):
                            print("Not enough content in",each_url," adding to not_crawled list.")
                          # if the content from url is Not enough then  add it  to not_crawled list
                        # saving all the urls that were not_crawled to a text file
                            with open(save_not_crawled, 'a') as filehandle:
                                #for listitem in not_crawled:
                                    filehandle.write('%s\n' % each_url + "Not enough content")
                    else:
                        config = configparser.ConfigParser() 
                        config.read('listnames_as_tuple.ini')
                        all_the_lists = config.items("lists")
                        for list_name, list_values in all_the_lists:
                            # print(list_name,list_values)
                            print(list_name)
                            cos_sim = counter_cosine_similarity(corpus,list_values)
                            print(url_item,"cosine_similarity = ",cos_sim)
                            sim_list_300=w2v_model_300.wmdistance(corpus,list_values)
                            print(url_item,"wmd_distance = ",sim_list_300)
                            wmsimilarity = 1/(1+sim_list_300)  # Similarity is the negative of the distance.
                            print(url_item,"wm_similarity = ",wmsimilarity)
                            endtime = time.clock()
                            time_taken = endtime - start_time 
                            # writing these results to a csv file                       
                            file_exists = os.path.isfile(csv_filename)
                            with open(csv_filename, 'a', newline='') as trail_csvFile:
                                column_names = ["url","List_Name","cos_sim","wmd_distance","wm_similarity","start_timestamp","time_taken"]
                                csv_writer = csv.DictWriter(trail_csvFile, fieldnames=column_names)
                                if not file_exists:
                                    csv_writer.writeheader()                            
                                csv_writer.writerow({'url':each_url,'List_Name':list_name,'cos_sim':cos_sim,'wmd_distance':sim_list_300,
                                'wm_similarity':wmsimilarity,'start_timestamp':start_time,'time_taken':endtime})  
                            
                except Exception as ex:                     
                        #execption_message= str(ex)
                        print ('url passed no corpus found for url  ',each_url,"Exception ERROR -1 " + str(ex))

                        with open(save_not_crawled, 'a') as filehandle:
                            filehandle.write('%s\n' % each_url + str(ex))
                            pass # skip
                print("done")
counter += 1

