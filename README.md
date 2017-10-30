# JDCrawler

JDCrawler is an efficient web crawler designed for crawling product information & details on JD.com. Its workflows can be decomposed into the following module:
1. crawl/Downloader: download web content
2. crawl/Parser: parse raw content into structured data
3. crawl/**Crawl: crawl specific information (item detail, price, comment, score, etc.
4. db/Loader: load crawled data into MySQL database
5. db/SQLHelper: specify table structure that stores data
6. util/myProxies: call to proxies pool.

Features of JDCrawler:
1. Multi-processing
2. Proxies pool
3. Real-time connection with MySQL

The proxies pool is digged and maintained under awesome open-source project /IPProxyPool.
