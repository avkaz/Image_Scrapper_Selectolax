from httpx import get
from selectolax.parser import HTMLParser
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def get_img_tags_for(term =None):
    if not term:
        raise Exception('No search term provided')
    url = f'https://unsplash.com/s/photos/{term}'
    resp = get(url)

    if resp.status_code != 200:
        raise Exception('Error getting response')
    
    tree = tree = HTMLParser(resp.text)
    images = tree.css('figure a img')
    return images


def img_filter_out (url, keywords):
    return not any(x in url for x in keywords)



def get_high_res_img_url(img_node):
    if "srcset" in img_node.attrs:
        srcset = img_node.attrs["srcset"]
        srcset_list = srcset.split(', ')
        url_res = [src.split(" ") for src in srcset_list if img_filter_out(src, ['plus', 'premium', 'profile'])]
        
        if not url_res:
            return None
        return url_res[0][0].split("?")[0]
    
def save_images(img_urls, dest_dir="images", tag=""):
    for url in img_urls:
        resp = get(url)
        logging.info(f"Downloading {url}...")

        file_name = url.split("/")[-1]

        # Create the destination directory if it doesn't exist
        os.makedirs(os.path.join(dest_dir, tag), exist_ok=True)


        with open(f"{dest_dir}/{tag}/{tag}{file_name}.jpeg", "wb") as f:
            f.write(resp.content)
            logging.info(f"Saved {file_name}, with size {round(len(resp.content)/1024/1024,2)} MB.")

if __name__ == '__main__':
    search_tag = 'dolphins'
    img_nodes = get_img_tags_for(search_tag)
    all_img_urls = [get_high_res_img_url(i) for i in img_nodes]
    img_urls = [u for u in all_img_urls if u]

    save_images(img_urls[:3], 'images', search_tag)
    # img_urls = [i.attrs['src'] for i in img_nodes]
    # relevant_urls = [i for i in img_urls if img_filter_out(i, ['plus', 'premium', 'profile'])]

    # for u in relevant_urls:
    #     print(u)

    # print(len(relevant_urls))
