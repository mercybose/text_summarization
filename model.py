from transformers import pipeline

example_txt = "There are broadly two types of extractive summarization tasks depending on what the summarization " \
              "program focuses on. The first is generic summarization, which focuses on obtaining a generic " \
              "summary or abstract of the collection (whether documents, or sets of images, or videos, " \
              "news stories etc.). The second is query relevant summarization, sometimes called query-based " \
              "summarization, which summarizes objects specific to a query. Summarization systems are able to " \
              "create both query relevant text summaries and generic machine-generated summaries depending on " \
              "what the user needs. An example of a summarization problem is document summarization, " \
              "which attempts to automatically produce an abstract from a given document. Sometimes one might be " \
              "interested in generating a summary from a single source document, while others can use multiple " \
              "source documents (for example, a cluster of articles on the same topic). This problem is called " \
              "multi-document summarization. A related application is summarizing news articles. Imagine a " \
              "system, which automatically pulls together news articles on a given topic (from the web), " \
              "and concisely represents the latest news as a summary.Image collection summarization is another " \
              "application example of automatic summarization. It consists in selecting a representative set of " \
              "images from a larger set of images.[5] A summary in this context is useful to show the most " \
              "representative images of results in an image collection exploration system. Video summarization " \
              "is a related domain, where the system automatically creates a trailer of a long video. This also " \
              "has applications in consumer or personal videos, where one might want to skip the boring or " \
              "repetitive actions. Similarly, in surveillance videos, one would want to extract important and " \
              "suspicious activity, while ignoring all the boring and redundant frames captured.At a very high " \
              "level, summarization algorithms try to find subsets of objects (like set of sentences, " \
              "or a set of images), which cover information of the entire set. This is also called the core-set. " \
              "These algorithms model notions like diversity, coverage, information and representativeness of " \
              "the summary. Query based summarization techniques, additionally model for relevance of the " \
              "summary with the query. Some techniques and algorithms which naturally model summarization " \
              "problems are TextRank and PageRank, Submodular set function, Determinantal point process, " \
              "maximal marginal relevance (MMR) etc. "


def build_summarizer():
    """
      Creates the pipeline object for summarization
      :return: None
      """
    summarizer = pipeline("summarization")

    return summarizer


def get_summarized_val(txt_to_summarize):
    """
      Get summary of text using summarization tranformer
      :param txt_to_summarize: text that must be summarized
      :return: summarized text
      """
    summarizer = build_summarizer()
    sum_text = summarizer(txt_to_summarize, min_length=30, max_length=150)

    return sum_text[0]['summary_text']


if __name__ == "__main__":
    print(get_summarized_val(example_txt))
