from httpx import get
from selectolax.parser import HTMLParser


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

if __name__ == '__main__':
    img_nodes = get_img_tags_for('cars')
    all_img_urls = [get_high_res_img_url(i) for i in img_nodes]
    img_urls = [u for u in all_img_urls if u]

    print(img_urls)
    # img_urls = [i.attrs['src'] for i in img_nodes]
    # relevant_urls = [i for i in img_urls if img_filter_out(i, ['plus', 'premium', 'profile'])]

    # for u in relevant_urls:
    #     print(u)

    # print(len(relevant_urls))
