import json
from urllib.request import urlopen
def MOVIE_JSON():
    print("Enter the movie name to be searched??")
    movie_name = input()
    url = "http://www.omdbapi.com/?t="+movie_name+"&y=&plot=short&r=json"
    my_info = urlopen(url).read().decode('utf8')
    print(my_info)
    my_ip = json.loads(my_info)
    st = input()
    print(st +' : '+my_ip.get(str(st)))
if __name__ == "__main__":
    print("Enter the number of Movies you want to search")
    N = int(input())
    for j in range(N):
        MOVIE_JSON()