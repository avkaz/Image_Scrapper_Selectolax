# Unsplash Image Scraper

The Unsplash Image Scraper is a versatile Python project designed for searching, retrieving, and downloading high-resolution images from Unsplash, a popular source of quality images. The project offers two distinct approaches, each tailored to different user needs. Both scripts incorporate customization options and logging for a seamless user experience.

## `main.py` (Scraping via selectolax Library)

The `main.py` script leverages the `selectolax` library to scrape Unsplash's website. Key features of this script include:

- **Customized Search:** The script enables users to specify a search term, such as "dolphins," and retrieves relevant images.

- **High-Quality Image Filtering:** It filters the search results to exclude images with specified keywords (e.g., "plus," "premium," and "profile"), ensuring that only desired, high-quality images are considered.

- **Efficient Downloading:** The script downloads the high-resolution images and saves them to a local directory, offering control over the number of images downloaded and organizing them according to user-defined tags.

## `main_api.py` (Scraping via API Requests with Pagination Support)

The `main_api.py` script takes a different approach, utilizing Unsplash's API and performing API requests for more efficient image retrieval. Key features of this script include:

- **Customized Search and Retrieval:** Users can specify a search term and the desired number of images to retrieve.

- **Pagination Support:** The script handles pagination by making multiple API requests to acquire the requested number of images, even when only 20 images are available on one page.

- **Filtering for Quality:** Like `main.py`, this script also filters out premium images and focuses on freely available, high-quality images.

- **Efficient Downloading:** It downloads and saves images to the local directory, efficiently managing downloads while maintaining organization.

Both scripts offer efficient ways to collect images from Unsplash based on user-defined search terms and requirements, with the choice of the web scraping approach (using `selectolax`) or the API request approach (via Unsplash's API). Users can customize the behavior of these scripts to suit their specific needs for image retrieval.




