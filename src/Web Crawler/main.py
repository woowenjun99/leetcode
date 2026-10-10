from collections import deque
from typing import List

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """

class Solution:
    def __get_hostname(self, url: str) -> str:
        hostname = list("http://")
        for i in range(7, len(url)):
            if url[i] == "/": break
            hostname.append(url[i])
        return "".join(hostname)
        
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        answer = set([startUrl])
        queue = deque([startUrl])
        hostname = self.__get_hostname(startUrl)
        while queue:
            front = queue.popleft()
            urls = htmlParser.getUrls(front)
            for url in urls:
                if url in answer: continue
                if self.__get_hostname(url) == hostname:
                    queue.append(url)
                    answer.add(url)
        return list(answer)
        