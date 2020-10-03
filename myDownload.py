import urllib.request
import click
import feedparser
import ssl
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(level= logging.INFO, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')



def get_links(search_word, jobs, titleasname):
    url_links = []

    # replace "search_query = all" to "search_query = _keyword_"
    query_URL = 'http://export.arxiv.org/api/query?search_query=all:{}&start=0&max_results={}'.format(search_word, jobs)
    logging.info('New URL is: %s' % query_URL)

    # search for targeted
    data = urllib.request.urlopen(query_URL).read()

    # parse the response using feedparser
    feed = feedparser.parse(data)

    # Run through each entry, and print out information
    # Source: https://static.arxiv.org/static/arxiv.marxdown/0.1/help/api/examples/python_arXiv_parsing_example.txt
    for entry in feed.entries:
        logging.info(entry.id)
        if titleasname:
            fileName = entry.title
        else:
            fileName = entry.id.split('/')[-1]

        logging.info('fileName: %s' % fileName)

        logging.info('Title:  %s' % entry.title)
        # feedparser v4.1 only grabs the first author
        logging.info('First Author:  %s' % entry.author)

        # Get PDF link from links
        for link in entry.links:
            if link.rel == 'alternate':
                logging.info('abs page link: %s' % link.href)
            elif link.title == 'pdf':
                logging.info('pdf link: %s' % link.href)
                url_links.append((link.href, fileName))

    return url_links


def download_single_pdf(URL, arXiv_ID, job_id):
    response = urllib.request.urlopen(URL)
    with open(arXiv_ID + ".pdf", 'wb') as file:
        file.write(response.read())
        logging.info("Download Successful")
    return job_id


def fetch_pdfs(url_links, num_workers):
    pooled_executor = ThreadPoolExecutor(max_workers = num_workers)
    logging.info("total_jobs:" + str(len(url_links)))
    all_tasks = []
    for i in range(len(url_links)):
        url_link = url_links[i][0]
        file_name = url_links[i][1]
        all_tasks.append(pooled_executor.submit(download_single_pdf, url_link, file_name, i))

    for future in as_completed(all_tasks):
        res = future.result()
        logging.info("job id: {} finished successfully".format(res))


# fetch link function
# Implement Click API to create a customize command line option --Search TEXT
# --Search TEXT allows the users to type in <1> keyword they want, and download <1> related article using arXiv API.
@click.command()
@click.option('--search', default = 'Ecomony', help='Only one word is allowed [Default = Economy] ')
@click.option('--thread', default = 3, help = 'Allow the user to input the max number of Threads [Optional][Default = 3')
@click.option('--jobs', default = 1, help = 'Allow the user to input the max number of Files [Optional][Default] = 3')
@click.option('--titleasname', default = False, type = bool, help = 'Use article title as file name[Optional][Default = False, use True to enable]')
def downloadFiles(search, thread, jobs, titleasname):
    logging.info('Looking for keyword: %s' %search)

    url_links = get_links(search, jobs, titleasname)
    fetch_pdfs(url_links, thread)


if __name__ == '__main__':
    downloadFiles()