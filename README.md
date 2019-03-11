# Emoji-Kmeans-Clustering
The goal of this project was to use Kmeans Clustering on a dataset of emojis in order to group them;

# The Data
There are 2 data files. One is a lookup file, which has emoji names across from their corresponding emojis, stored in tsv format. The other file contains 300 dimesional vectors corresponding to each emoji (what they represent is unkown to me).

# K-means algorithm
The first step of kmeans is to generate some number of random points. For this project, I chose 15. The next step is to compare each of the data points to the random points. I created a dictionary in which each data point was matched with its closest random point, which was found using the distance formula (a.k.a the pythagorean theorem and some common sense). Next, the random points will be moved. I took the average position of all points that were closest to each random point, then moved that point there. Once all of those proceses are set up, one must iterate over all of them. The three steps are repeated until the random points do not move. At this point, there should be 15 different groups of emoji lables. These lables were printed as emojis by printing their corresponding emoji in the reference set.

Made while working with Hello World Studio
