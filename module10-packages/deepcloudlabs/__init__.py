print("deepcloudlabs module is loaded!")

from deepcloudlabs.dictionary import words

with open("deepcloudlabs/dictionary-tur.txt", mode="r") as afile:
    for word in afile.readlines():
        words.append(word.strip())
