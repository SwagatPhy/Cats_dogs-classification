import matplotlib.pyplot as plt
import requests
import os
import shutil

def create_dir(filename=None):

  dataset_dir = '/Users/swagat98/Proj_1/datasets/cats_dogs'
  dataset_dir = f'{dataset_dir}/{filename}'

  if not os.path.exists(f'{dataset_dir}'):
    print(f"Creating directory")
    os.mkdir(dataset_dir)

    return dataset_dir

  else:
    print(f"Directory already exists")

    return dataset_dir


# def get_url(url, header):
#   r = requests.get(url, headers=header)
#   return r.text

def get_unsplash_url(num_images=None, width=None, height=None,labels=None, url=None):


  application_id = '868915'
  access_key = 'q7XhJQcxpEU1rMrqUxjccOrnhjcmx1bAxVpPawKelHg'
  secret_key = 'fFEvYh23_NG_lBDqquDUsSBnYVRJM-3r_RJ2Xa2T47w'


  # url = f'https://unsplash.com/s/photos/{query}'
  browser_header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}
  http_authorization_header = {'Authorization': f'Client-ID {access_key}'}
  print('Authorization: ',http_authorization_header)


  re = requests.get(url, headers=http_authorization_header)
  data = re.json()
  # print(f"Data: {data}")

  unsplash_results = []
  unsplash_urls_small  = []
  unsplash_urls_medium = []
  unsplash_urls_large  = []
  for i in range(len(data['results'])):
    results = data['results'][i]
    small_urls = data['results'][i]['urls']['small']
    medium_urls = data['results'][i]['urls']['regular']
    large_urls =data['results'][i]['urls']['full']
    unsplash_results.append(results)
    unsplash_urls_small.append(small_urls)
    unsplash_urls_medium.append(medium_urls)
    unsplash_urls_large.append(large_urls)

  return unsplash_urls_small
  # ask user what kind of images does the user want

def download_image_from_url(url_list, num_images, output_path = None, labels = None, num = None): # either input or upload a list of urls after converting to string list

  dummy_download_files = []
  for i in range(len(url_list)):
    url = url_list[i]
    # dummy_download_files.append(url)

    # return dummy_download_files

    result = requests.get(url)
    with open(f'{output_path}/{labels}_{num}_{i}.jpg','wb') as file:
      file.write(result.content)



# input the name of another class, and add their directory

cat_output_path = create_dir('cats')
dog_output_path = create_dir('dogs')

labels = {'cats':cat_output_path,'dogs':dog_output_path}
page_nums = 3

for labs, outpaths in labels.items():
  for current_page in range(1,page_nums + 1):
    print(f'Current page: ',current_page)

    query = labs
    query = '+'.join(query.split(' '))
    num_images = int(input(f"Input the number of images to download: "))
    width = 500
    height = 500

    url = f'https://api.unsplash.com/search/photos?query={query}&per_page={num_images}&width={width}&height={height}&page={current_page}'
    print(url)



    urls_t = get_unsplash_url(num_images=num_images, height=height, width=width,labels=labs, url = url)
    download_image_from_url(urls_t, num_images, output_path = outpaths,labels = labs, num = current_page)



#makeing training and testing directories and files

cat_train_output_path = create_dir('cats_train')
cat_test_output_path  = create_dir('cats_test')
dog_train_output_path = create_dir('dogs_train')
dog_test_output_path  = create_dir('dogs_test')

train_len = 9375
test_len = 3124


# for i in range(0,train_len):
#   copy_cat_train_cmd = f'cp -r {cat_output_path}/* {cat_train_output_path}'

cat_imagelist = [files for files in os.listdir(cat_output_path) if not files.startswith('.')] # searches the directory
dog_imagelist = [files for files in os.listdir(dog_output_path) if not files.startswith('.')] # searches the directory

# for first 40 train next test

for i in range(0,train_len):
  #copy cat train
  shutil.copy(f'{cat_output_path}/{ cat_imagelist[i]}',cat_train_output_path)
  #copy dog train
  shutil.copy(f'{dog_output_path}/{ dog_imagelist[i]}',dog_train_output_path)

for j in range(train_len,train_len + test_len):
  #copy cat train
  shutil.copy(f'{cat_output_path}/{ cat_imagelist[j]}',cat_test_output_path)
  #copy dog train
  shutil.copy(f'{dog_output_path}/{ dog_imagelist[j]}',dog_test_output_path)


