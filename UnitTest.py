import unittest
import myDownload
import timeit


class TestmyDownloads(unittest.TestCase):

    def testZeroFiles(self):
        raised = False
        try:
            url_links = myDownload.get_links("cnn", 0)
            myDownload.fetch_pdfs(url_links, 10)
        except:
            raised = True
        self.assertFalse(raised, "Exception raised when number of file is 0")

    def testDownloadingTenFilesisSlowerthanDownloadingOneFile(self):
        start_oneFile = timeit.default_timer()
        url_links = myDownload.get_links("cnn", 1)
        myDownload.fetch_pdfs(url_links, 1)
        stop_oneFile = timeit.default_timer()
        time1 = stop_oneFile - start_oneFile
        print("Time for downloading 1 file: ", time1)

        start_TenFile = timeit.default_timer()
        url_links = myDownload.get_links("cnn", 10)
        myDownload.fetch_pdfs(url_links, 1)
        stop_TenFile = timeit.default_timer()
        time2 = stop_TenFile - start_TenFile
        print("Time for downloading 10 file: ", time2)
        self.assertGreater(time2, time1, "Error: Downloading one file is slower than that of downloading ten files")

    def testDownloadinginOneThreadisSlowerthanDownloadinginTenThread(self):
        start_oneThread = timeit.default_timer()
        url_links = myDownload.get_links("cnn", 10)
        myDownload.fetch_pdfs(url_links, 1)
        stop_oneThread = timeit.default_timer()
        time1 = stop_oneThread - start_oneThread
        print("Time for downloading in 1 thread: ", time1)

        start_tenThread = timeit.default_timer()
        url_links = myDownload.get_links("cnn", 10)
        myDownload.fetch_pdfs(url_links, 10)
        stop_tenThread = timeit.default_timer()
        time2 = stop_tenThread - start_tenThread
        print("Time for downloading in 10 threads: ", time2)
        self.assertGreater(time1, time2, "Error: Downloading in ten thread is slower than that of downloading in ten threads")

if __name__ == '__main__':
    unittest.main()

