import contractions
import spacy
from gensim.parsing.preprocessing import STOPWORDS
from wordcloud import STOPWORDS as wordcloud_STOPWORDS

from util.utilities import Utilities
util = Utilities()

import nltk
nltk.data.path.append(util.nltk_data_path)
from nltk.corpus import stopwords, words

class CustomStopWords:
    def __init__(self,
                 domain_specific_stops: list[str]|None=None):
        self.nlp = spacy.load('en_core_web_lg',disable=['parser','ner'])

        english_custom_stops = list(
            {
                'i','me','my','myself',
                'we','our','ours','ourselves','us',
                'they','them','their','theirs','themselves',
                'you','your','yours','yourself','yourselves',
                'he','him','his','himself',
                'she','her','hers','herself',
                'it','its','itself',
                'what','which','who','whom',
                'this','that','these','those',
                'am','is','are','was','were','be','been','being','will','would',
                'have','has','had','having',
                'do','does','did','doing',
                'a','an','the','and',
                'but', 'if', 'or', 'because','as','until',
                'while','of','at','by','for','with','about','against',
                'between','into','through','during','before','after',
                'above','below','to','from','up','down',
                'in','out','on','off','over','under',
                'again','further','then','once','here','there',
                'when','where','why','how',
                'all','any','both','each','few','more','most','other','some','such',
                'no','nor','not','only','own','same','so','than',
                'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
                'should', 'now', 'upon', 'too', 'very',
                'd','ll','m','o','re','ve','y',
                'ain','aren','couldn','didn','doesn','hadn','hasn','haven','isn',
                'ma','mightn','mustn','needn','shan','shouldn','wasn','weren','won','wouldn',
                'yet','among','onto','shall','twice','thrice','thus','unto',
            }
        )

        # Additional stopwords
        alphabets = ['a','b','c','d','e','f','g','h','i','j',
                     'k','l','m','n','o','p','q','r','s','t',
                     'u','v','w','x','y','z']
        prepositions = list(
            {
                'about','above','across','after','afterwards','against',
                'along','alongside','behind','beside','besides',
                'among','around','at','before','behind','below','between',
                'by','down','during','each','for','from','into','of','on','in',
                'inside','into','near','of','off','on','once','onward','onwards',
                'out','over','through','to','toward','towards','under','underneath',
                'up','upward','upwards','with'
            }
        )
        prepositions_less_common = list(
            {
                'aboard','around','at','along','amid','as','beneath','beyond','but',
                'considering','despite','except','following','like','minus','onto',
                'outside','per','plus','regarding','right','round','since','than','till',
                'underneath','unlike','until','upon','versus','via','within','without'
            }
        )
        coordinating_conjunctions = list(
            {
                'and','but','for','nor','or','so','yet'
            }
        )
        correlative_conjunctions = list(
            {
                'both','and','either','or','neither','nor',
                'not','only','but','also','as','whether',
                'rather','than','if','then'
            }
        )
        subordinating_conjunctions = list(
            {
                'after','although','as','because','before','if','lest','once','only',
                'since','so','supposing','that','than','though','till','unless','until',
                'when','whenever','whereas','wherever','while'
            }
        )
        pronouns = list(
            {
                "i", "you", "he", "she", "it", "we", "they",
                "me", "you", "him", "her", "it", "us", "them",
                "my", "your", "his", "her", "its", "our", "their",
                "mine", "yours", "his", "hers", "its", "ours", "theirs",
                "myself", "yourself", "himself", "herself", "itself", "oneself",
                "ourselves", "yourselves", "themselves","themself",
                "this", "that", "these", "those",
                "who", "whom", "whose", "what", "which", "that",
                "all", "another", "any", "anybody", "anyone", "anything", "both", "each",
                "either", "enough", "everybody", "everyone", "everything", "few", "fewer",
                "least", "less", "little", "many", "most", "much", "neither", "no one",
                "nobody", "none", "nothing", "one", "other", "others", "several", "some",
                "somebody", "someone", "something", "such", "whole",
                "each other", "one another","each", "either", "neither", "any", "none",
                "you", "one", "we", "they"
            }
        )
        misc = list(
            {
                'hi', 'hello', 'hey', 'll','a','an','the','of','in','on',
                'or','so','at','for','with','by','from','into','to',
                'before','after','above','below','up','down','once',
                'here','there','when','where','why','how','all','any','both',
                'each','few','other','some','own','same','so','can','will','and','or',
                'but','if','while','as','because','i','me','my','myself',
                'we','our','ourselves','ours','their','theirs',
                'your','yourself','yourselves','you','yours',
                'he','him','his','himself','she','her','hers','herself',
                'it','its','itself','they','them','their','theirs','themselves',
                'what','which','who','whom','when','where','why','whose',
                'this','that','these','those','as','is','am','are','was','were',
                'be','been','being','has','have','had','having',
                'do','does','did','doing','done'
            }
        )

        '''
        pronouns = {
            "personal": {
                "subjective": ["i", "you", "he", "she", "it", "we", "they"],
                "objective": ["me", "you", "him", "her", "it", "us", "them"]
            },
            "possessive": {
                "dependent_determiner": ["my", "your", "his", "her", "its", "our", "their"],
                "independent": ["mine", "yours", "his", "hers", "its", "ours", "theirs"]
            },
            "reflexive_and_intensive": {
                "singular": ["myself", "yourself", "himself", "herself", "itself", "oneself"],
                "plural": ["ourselves", "yourselves", "themselves"],
                "gender-neutral": ["themself"]
            },
            "demonstrative": ["this", "that", "these", "those"],
            "interrogative": ["who", "whom", "whose", "what", "which"],
            "relative": ["who", "whom", "whose", "what", "which", "that"],
            "indefinite": [
                "all", "another", "any", "anybody", "anyone", "anything", "both", "each",
                "either", "enough", "everybody", "everyone", "everything", "few", "fewer",
                "least", "less", "little", "many", "most", "much", "neither", "no one",
                "nobody", "none", "nothing", "one", "other", "others", "several", "some",
                "somebody", "someone", "something", "such", "whole"
            ],
            "reciprocal": ["each other", "one another"],
            "distributive": ["each", "either", "neither", "any", "none"],
            "impersonal_inclusive": ["you", "one", "we", "they"],
            "neopronouns": {
                "subjective": ["ey", "xe", "ze", "fae", "thon", "co"],
                "objective": ["em", "xem", "hir", "faer", "thon", "co"],
                "possessive_determiner": ["eir", "xyr", "hir", "faer", "thons", "cos"],
                "possessive_independent": ["eirs", "xyrs", "hirs", "faers", "thons", "cos"],
                "reflexive": ["emself", "xemself", "hirself", "faerself", "thonself", "coself"]
            }
        }
        '''

        additional_stops = (alphabets +
                            pronouns +
                            prepositions +
                            prepositions_less_common +
                            coordinating_conjunctions +
                            correlative_conjunctions +
                            subordinating_conjunctions +
                            misc)

        self.sentiment_custom_stops = alphabets + misc

        english_stops_raw = [word.lower() for word in list(set(
            stopwords.words('english')+
            list(STOPWORDS)+
            list(wordcloud_STOPWORDS)+
            english_custom_stops+
            additional_stops))]
        self.english_stops = self.get_final_list(english_stops_raw)

        domain_specific_stops_raw = [word.lower() for word in list(set(domain_specific_stops))] if domain_specific_stops is not None else []
        self.domain_specific_stops = self.get_final_list(domain_specific_stops_raw)

        self.words_lower = [word.lower for word in words.words()]

    def get_final_list(self,
                       raw_list):
        if len(raw_list) <= 0:
            return []

        stops_expanded = contractions.fix(' '.join(raw_list))
        stops_expanded_lemmatized = ' '.join([token.lemma_ for token in self.nlp(stops_expanded)])
        final_stops = list(set(nltk.word_tokenize(stops_expanded_lemmatized)))

        return final_stops