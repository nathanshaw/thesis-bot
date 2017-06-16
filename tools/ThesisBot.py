import os

class ThesisBot:
    """
    Collection of NLTK processing and other tools for
    having fun with my thesis
    """
    stop_chars = ["-", '"', "'", "/n"]
    allowed_chars = [
    'a', 'A', 'b', 'B', 'c', 'C',
    'd', 'D', 'e', 'E', 'f', 'F',
    'g', 'G', 'h', 'H', 'i', 'I',
    'j', 'J', 'k', 'K', 'l', 'L',
    'm', 'M', 'n', 'N', 'o', 'O',
    'p', 'P', 'q', 'Q', 'r', 'R',
    's', 'S', 't', 'T', 'u', 'U',
    'v', 'V', 'w', 'W', 'x', 'X',
    'y', 'Y', 'z', 'Z']

    allowed_numbers = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]

    allowed_punc = [',','.', ' ']

    def readLastThesisVersion(self):
        """
        Looks in the thesis-drafts folder and
        runs the readTxtFile function on
        the last file in the folder
        """
        file_names = os.listdir("../thesis-drafts")
        return readTxtFile(file_names[-1])

    def readTxtFile(self, filePath):
        """
        Reads in a file, provides brute force preprocessing,
        and returns a string of the file
        """
        text = ""
        finalText = ""
        with open(filePath, "r") as f:
            text = f.read().replace('\n', ', ')
        for char in text:
            if char in self.allowed_chars or char in self.allowed_punc:
                finalText += char
            if char in self.stop_chars:
                finalText += " "
        return finalText

    def writeTxtFile(self, filePath, contents):
        """
        Writes contents to filePath
        """
        with open(filePath, "w") as f:
            f.write(contents)

    def sayWords(self, thesis, voice="Tessa"):
        command = "say -v " + voice + " " + str(thesis[:10000])
        os.system(command)

    def tokenize(self, longString):
        # make sure we only tokenize letters
        processed_string = ""
        for char in longString:
            if char in self.allowed_chars or char == " ":
                processed_string += char
        tokens = nltk.word_tokenize(processed_string)
        token_list = []
        for token in tokens:
            token_list.append(token)
        return token_list

    def returnBigramFreqs(self, tokens):
        bgs = nltk.bigrams(tokens)
        fdist = nltk.FreqDist(bgs)
        bigram_freqs = []
        for k, v in fdist.items():
            bigram_freqs.append([v, k[0] + " " + k[1]])
        bigram_freqs.sort(key=lambda x: x[0])
        return bigram_freqs

    def returnBigrams(self, tokens):
        bgs = nltk.bigrams(tokens)
        return bgs

    def returnTrigrams(self, tokens):
        tgs = nltk.trigrams(tokens)
        return tgs

    def returnTrigramFreqs(self, tokens):
        tgs = nltk.trigrams(tokens)
        fdist = nltk.FreqDist(tgs)
        trigram_freqs = []
        for k, v in fdist.items():
            trigram_freqs.append([k[0] + " " + k[1] + " " + k[2], v])
        trigram_freqs.sort(key=lambda x: x[1])
        return trigram_freqs

    def returnNGrams(self, tokens, n):
        n_grams = nltk.ngrams(tokens, n)
        return n_grams;

    def sayRandomPhrase(self, listOfStrings, times):
        if type(listOfStrings) == list:
            sayWords(listOfStrings[random.randint(0, len(listOfStrings))])
        else:
            words = []
            for word in listOfStrings:
                words.append(word)

            result = ""
            i = 0
            while(i < times):
                to_say = words[random.randint(0, len(words))]
                for to_say_word in to_say:
                    result += to_say_word
                    result += " "
                i += 1
            print(result)
            sayWords(result + ".")
