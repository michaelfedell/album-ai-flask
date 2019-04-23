# Album.ai

This project aims to leverage deep learning models to classify an album's genre of music based only on that album's cover art.

## Problem

Our group will address categorizing album genres based on the cover artwork of the album. Music streaming services, such as Spotify and Pandora, could benefit from this solution. Using deep learning to fill in missing album metadata can save these streaming services from having to spend employee time listening to music to classify it. Being able to correctly classify genres would allow these streaming services to add songs to playlists or to stations based on genre, without having to take the time to have a human listen to and classify the genre of an album.

## Available Data

The dataset leveraged for this project is obtained from Albumoftheyear.org and includes somewhere between 100 and 1000 albums for each of nearly 20 genres. This results in a combined set of some 15,000 albums for analysis. The data may be augmented via the Spotify developer API where needed. All data access is within the bounds of source websites' terms and conditions.

## Getting Started

To manage dependencies, this project will run in a conda environment which can be created from the included `environment.yml` file.

```shell
conda env create -f environment.yml
conda activate album-ai
```

Data will be kept in the `data/` folder, but ignored from git. If you are new to this project, you will first need to build the training data from the raw source data. This can be done automatically by running TODO: build scripts

TODO: This section will be updated once more progress has been made.

## References

- <http://www.dgp.toronto.edu/~libeks/Libeks_ArtistImage_IEEEMM11.pdf>
- <https://www.researchgate.net/publication/318987126_Album_Cover_Generation_from_Genre_Tags>

## Collaborators

_Note_: as collaborators will use a mix of windows/mac/linux environments, it is important to keep code system agnostic (e.g. `os.path.join(path, to, file)` instead of `path/to/file`)

- [Alex Burzinski](https://github.com/aburzinski)
- [Ted Carlson](https://github.com/tce9232)
- [Tony Colucci](https://github.com/tonycolucci)
- [JD Cook](https://github.com/josephd8)
- [James Fan](https://github.com/rfq4587)
- [Michael Fedell](https://github.com/michaelfedell)