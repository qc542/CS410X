from word_vector import *

entire_vector = load_vector("/Users/qilei/Downloads/wiki-news-300d-1M.vec")
# Path to vector file on macOS

#entire_vector = load_vector(r"C:\Users\qilei\Downloads\wiki-news-300d-1M.vec")
# Path to vector file on Windows

professions = ["professor", "boss", "student", "engineer", "doctor",
               "dentist", "manager", "journalist"]
venues = ["hospital", "pharmacy", "mall", "salon", "restaurant"]
companies = ["Amazon", "Google", "Facebook", "Apple", "Nasdaq", \
        "Walmart", "Nintendo", "Microsoft", "eBay", "Samsung", \
        "Uber", "Lyft", "Target", "Sony", "Volkswagen"]

professions_words = construct_word_list(professions, entire_vector)
venues_words = construct_word_list(venues, entire_vector)
company_names = construct_word_list(companies, entire_vector)

print("""Base word: surgeon\n""")
show_similarity_ranking(professions_words, lookup_vector("surgeon",
                                                            entire_vector))

print("""Base word: eatery\n""")
show_similarity_ranking(venues_words, lookup_vector("eatery", entire_vector))

print("""Base word: LinkedIn\n""")
show_similarity_ranking(company_names, lookup_vector("LinkedIn", entire_vector))

print("""Base word: Uber\n""")
show_similarity_ranking(company_names, lookup_vector("Uber", entire_vector))

print("""Base word: Amazon\n""")
show_similarity_ranking(company_names, lookup_vector("Amazon", entire_vector))

print("""Base word: Tesla\n""")
show_similarity_ranking(company_names, lookup_vector("Tesla", entire_vector))
