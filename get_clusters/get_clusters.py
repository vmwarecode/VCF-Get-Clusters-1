#Get all Clusters
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint

class GetClusters:
    def __init__(self):
        print('Get Clusters')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]

    def get_clusters(self):
        get_clusters_url = 'https://'+self.hostname+'/v1/clusters/'
        pprint.pprint(self.utils.get_request(get_clusters_url))

if __name__== "__main__":
    GetClusters().get_clusters()
